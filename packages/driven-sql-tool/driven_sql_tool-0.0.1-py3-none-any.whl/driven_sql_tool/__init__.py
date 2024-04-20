from typing import Any, Generator, ClassVar, overload

import logging
logger = logging.getLogger(__name__)

import io
import re

import multiprocessing as mp
import pandas as pd

from collections.abc import Mapping
from dataclasses import dataclass, field

from turbodbc.connection import Connection
from turbodbc.cursor import Cursor
from turbodbc import connect, make_options, Megabytes
from turbodbc.exceptions import InterfaceError
from turbodbc_intern import Options




def with_kwargs(func):
    """
    Decorator for functions with no **kwargs.
    Truncates **kwargs entries that are not defined in function scope.
    """
    def modify(**kwargs):
        ars = func.__code__.co_varnames[:func.__code__.co_argcount]
        kwargs = {kwarg: kwargs[kwarg] for kwarg in kwargs if kwarg in ars}
        return func(**kwargs)
    return modify


class Mixin():
    """
    Helper mixin class
    """
    
    def __repr__(self):
        return self.__dict__.__str__()

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)


    def __getitem__(self, __name: str) -> Any:
        return self.__dict__[__name]

    def __setitem__(self, __item: str, __value: Any) -> None:
        self.__dict__[__item] = __value
    

    def __getattr__(self, __name: str) -> Any:
        try:
            return self.__dict__[__name]
        except KeyError:
            raise AttributeError(__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = __value


@dataclass
class SQLConfig(Mixin, Mapping):
    """
    Collection of configuration options for SQL connection.

    ---
    NOTE 

    Some arguments of `turbodbc_intern.Options` cannot be pickled in mp.
    Such arguments should be set on class-level to hide from instance's __dict__.
    Ex: `read_buffer_size` : ClassVar[Megabytes] = Megabytes(42)

    """

    server: str = r''
    database: str = r''

    driver: str = r'SQL Server'
    # driver: str = r'ODBC Driver 17 for SQL Server' # optional alternative
    
    trusted_connection: bool = True

    autocommit: bool = True
    use_async_io: bool = True
    prefer_unicode: bool = True

    read_buffer_size: ClassVar[Megabytes] = Megabytes(42)


    @classmethod
    def _get_class_lvl_attrs(cls):
        return {class_attr for class_attr in cls.__dict__ if not(class_attr.startswith('_') or class_attr.endswith('_'))}
    
    def _get_inst_lvl_attrs(self) -> set[str]:
        return {inst_attr for inst_attr in self.__dict__}


    def _all(self):
        set1 = self._get_class_lvl_attrs()
        set2 = self._get_inst_lvl_attrs()
        full_set = set1 | set2
        return {attr: getattr(self, attr) for attr in full_set}
    
    def pre_connect(self) -> None:
        """
        Actions that precede connection creation.
        """
        pass

    
    def get_connection(self) -> Connection:
        self.pre_connect()

        turbo_options: Options = with_kwargs(make_options)(**self._all())
        
        return connect(**self, turbodbc_options=turbo_options)

    def get_cursor(self) -> Cursor:
        connection = self.get_connection()
        return connection.cursor()

@dataclass
class Query:
    """
    Single Query object.

    ---
    Attributes:  

    `stmt` :  query statement (alternatively can be a file path, see `__post_init__`)  

    `data` :  input/output data (contextual)

    `conf` :  connection configuration

    `complete` : completion flag

    ---
    NOTE
    
    Running multi-statement transactions with turbodbc can be a challenging task.
    
    To name a few examples: 
        - MARS Transactions, see `Query().update_stmt()`
        - 'USE %DB%;' statement is ignored by 'turbodbc'. I believe, is due to Multi-Transaction nature of the query (GO)
    """

    stmt: str = '' 
    data: pd.DataFrame | None = None
    conf: SQLConfig = field(default_factory=SQLConfig)
    complete: bool = False

    def __post_init__(self):

        try:
            with io.open(self.stmt, 'r') as file:
                self.stmt = file.read()
            # logger.debug('Statement is a file path')
        # except FileNotFoundError:
        #     # logger.exception(f'File not found: {self.stmt}', exc_info=error)
        #     raise
        except OSError:
            # logger.debug('Statement is a string')
            pass
        # remove inline comments
        self.stmt = re.sub(r'--.*?\n', '', self.stmt)
        # logger.debug(f"cleaned up statement:\n{self.stmt}")

        # self.placeholders = re.findall(r'\?', self.stmt)
        # logger.debug(f"placeholders:\n{self.placeholders}")
    
    # Overloads to avoid type checker linting warnings
    @overload
    def execute(self, cursor: Cursor | None = None) -> pd.DataFrame:
        ...
    @overload
    def execute(self, cursor: Cursor | None = None) -> None:
        ...
    
    def execute(self, cursor: Cursor | None = None) -> pd.DataFrame | None:
        """
        Main wrapper to execute `Query` statement.
        """

        if not cursor:
            cursor = self.conf.get_cursor()

        match self.data:
            case pd.DataFrame():
                
                # to correctly convert missing values to SQL NULLs
                if self.data.isna().any(axis=None):
                    self.data = self.data.astype('object').where(self.data.notna(), None)
                
                # dt_cols = self.data.select_dtypes(include='datetime64[ns]').columns
                # if not dt_cols.empty:
                #     self.data[dt_cols] = self.data[dt_cols].stack().dt.strftime('%Y-%m-%d %H:%M:%S').unstack()
                
                cursor.executemany(self.stmt, self.data.itertuples(index=False))
            case None:
                cursor.execute(self.stmt)
            case _:
                raise TypeError
        
        try:
            result = cursor.fetchallnumpy()
            self.data = pd.DataFrame.from_dict(result)
            return self.data
        except InterfaceError:
            # This error only raised after statement was executed
            # Thus assume it only happens when no result is returned
            return None
        finally:
            self.complete = True
        
    def update_stmt(self):
        """
        Transactions with Multiple Active Result Sets (MARS) 
        may return nothing without 'SET NOCOUNT ON;' header.
        """
        self.stmt = 'SET NOCOUNT ON;\n' + self.stmt


@dataclass
class QuerySequence(Mixin, Mapping):

    def run_par(self) -> None:
        """
        Main wrapper for parallel execution of multiple `Query` objects.
        `execute`s all `Query` objects under `multiprocessing.Pool`.
        Then combines `Pool` results.
        """
        with mp.Pool(mp.cpu_count()) as pool:
            results = pool.map_async(Query.execute, self.values()).get()
        logger.debug('Closed query pool')

        for name, result in zip(self.keys(), results):
            self[name].data = result
        logger.debug('Combined pool results')


    def all_confs_equal(self) -> bool:
        """
        Checks if `conf`s are identical across all `Query` objects in `QuerySequence`.
        """
        iter_queries = iter(self.values())
        try:
            first = next(iter_queries).conf
        except StopIteration:
            return True
        return all(first == query.conf for query in iter_queries)


    def prep_cursor(self) -> Cursor | None:
        """
        Creates (and keeps it open) a common `cursor()` instance in case all `conf`s are identical.

        Otherwise each `cursor` created separately per `Query` execution.
        """
        if self.all_confs_equal():
            query: Query = next(iter(self.values()))
            logger.debug('SQL configs identical => Creating group cursor.')
            return query.conf.get_cursor()
            # connection = query.get_connection()
            # return connection.cursor()
        else:
            logger.debug('SQL configs differ => Each query will get its own cursor.')
            return None

    def gen_seq(self) -> Generator[pd.DataFrame | None, None, None]:
        """
        Generator for sequential execution of multiple `Query` objects.
        """
        cursor = self.prep_cursor()
        # assert cursor

        # for query in self.values():
        #     yield query.execute(cursor)
        for key, query in self.items():
            logger.debug(f"Running query: {key}")
            yield query.execute(cursor)
            
        if cursor:
            cursor.close()


    def run_seq(self) -> None:
        """
        Main wrapper for sequential execution.
        """
        for num, data in enumerate(self.gen_seq()):
            
            match data:
                case pd.DataFrame():
                    logger.debug(f"Data shape: {data.shape}")
                case _:
                    logger.debug(f"No data returned")
            
            logger.debug(f"{num + 1} / {len(self)} queries done")
