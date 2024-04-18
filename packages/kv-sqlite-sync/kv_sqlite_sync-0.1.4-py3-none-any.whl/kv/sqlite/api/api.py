from typing import AsyncIterable, TypeVar, Generic, Callable, Never, cast
from dataclasses import dataclass
import haskellian.either as E
import haskellian.asyn.promises as P
import haskellian.asyn.iter as AI
from pydantic import RootModel
from kv.api import KV
from kv.api.errors import InexistentItem, DBError, InvalidData
import sqlite3
import os
from .. import queries

T = TypeVar('T')
M = TypeVar('M')

@dataclass
class SQLiteKV(KV[T], Generic[T]):

  conn: sqlite3.Connection
  table: str = 'kv'
  parse: Callable[[str], E.Either[InvalidData, T]] = lambda x: E.Right(cast(T, x)) # type: ignore
  dump: Callable[[T], str] = lambda x: str(x)
  dtype: str = 'TEXT'

  @classmethod
  def at(
    cls, db_path: str, table: str = 'kv',
    parse: Callable[[str], E.Either[InvalidData, T]] = lambda x: E.Right(cast(T, x)),
    dump: Callable[[T], str] = lambda x: str(x),
    dtype: str = 'TEXT'
  ) -> 'SQLiteKV[T]':
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return SQLiteKV(sqlite3.connect(db_path), table, parse, dump, dtype)

  @classmethod
  def validated(cls, Type: type[M], db_path: str, table: str = 'kv') -> 'SQLiteKV[M]':
    Model = RootModel[Type]
    return cls.at(
      db_path=db_path, table=table, dtype='JSON',
      parse=lambda b: E.validate_json(b, Model).fmap(lambda x: x.root).mapl(InvalidData),
      dump=lambda x: Model(x).model_dump_json(exclude_none=True)
    )

  def __post_init__(self):
    self.conn.execute(*queries.create(self.table, self.dtype))

  def execute(self, query: queries.Query) -> E.Either[DBError, sqlite3.Cursor]:
    """Safely execute `query` on `self.conn`"""
    try:
      cur = self.conn.execute(*query)
      self.conn.commit()
      return E.Right(cur)
    except sqlite3.Error as err:
      return E.Left(DBError(str(err)))

  @P.lift
  async def update(self, key: str, value: T) -> E.Either[DBError|InexistentItem, None]:
    return self.execute(queries.update(key, self.dump(value), table=self.table)).bind(
      lambda cur: E.Left(InexistentItem(key)) if cur.rowcount == 0 else E.Right(None)
    )
  
  @P.lift
  async def insert(self, key: str, value: T, *, replace = False) -> E.Either[DBError, None]:
    make_query = queries.upsert if replace else queries.insert
    return self.execute(make_query(key, self.dump(value), table=self.table)) | (lambda _: None)
  
  @P.lift
  async def read(self, key: str) -> E.Either[DBError | InvalidData | InexistentItem, T]:
    res = self.execute(queries.read(key, table=self.table)) \
      | sqlite3.Cursor.fetchone
    match res:
      case E.Right(None):
        return E.Left(InexistentItem(key))
      case E.Right([data]):
        return self.parse(data)
      case E.Right(bad_data):
        return E.Left(InvalidData(detail=f'Found invalid row: {bad_data}'))
      case err:
        return err

  @P.lift
  async def delete(self, key: str) -> E.Either[DBError | InexistentItem, None]:
    return self.execute(queries.delete(key, table=self.table)) \
      & (lambda cur: E.Left(InexistentItem(key)) if cur.rowcount == 0 else E.Right(None))
  
  @AI.lift
  async def keys(self, batch_size: int | None = None) -> AsyncIterable[E.Either[DBError, str]]:
    match self.execute(queries.keys(self.table)):
      case E.Right(cur):
        while (batch := cur.fetchmany(batch_size or 256)) != []:
          for [key] in batch:
            yield E.Right(key)
      case E.Left(err):
        yield E.Left(err)

  @AI.lift
  async def items(self, batch_size: int | None = None) -> AsyncIterable[E.Either[DBError | InvalidData, tuple[str, T]]]:
    match self.execute(queries.items(self.table)):
      case E.Right(cur):
        while (batch := cur.fetchmany(batch_size or 256)) != []:
          for k, v in batch:
            yield self.parse(v) | (lambda v: (k, v))
      case E.Left(err):
        yield E.Left(err)
  
  @P.lift
  async def commit(self) -> E.Either[Never, None]:
    return E.Right(self.conn.commit())
  
  @P.lift
  async def rollback(self) -> E.Either[Never, None]:
    return E.Right(self.conn.rollback())