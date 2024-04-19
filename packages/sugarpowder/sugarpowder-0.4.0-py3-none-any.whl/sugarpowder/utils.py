import base64
from io import BytesIO
from typing import Iterable, TypeVar
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


T = TypeVar("T")


def df_to_parquetstream(df: pd.DataFrame) -> bytes:
    pqstream = BytesIO()
    pq.write_table(pa.Table.from_pandas(df), pqstream)
    pqbytes = pqstream.getvalue()
    return pqbytes


def parquetstream_to_df(pqbytes: bytes) -> pd.DataFrame:
    pqstream = BytesIO(pqbytes)
    pqtable = pq.read_table(pqstream)
    return pqtable.to_pandas()


def df_to_hex(df: pd.DataFrame) -> str:
    pqbytes = df_to_parquetstream(df)
    return pqbytes.hex()


def hex_to_df(hexed_df: str) -> pd.DataFrame:
    pqbytes = bytes.fromhex(hexed_df)
    return parquetstream_to_df(pqbytes)


def df_to_base64(df: pd.DataFrame) -> bytes:
    pqbytes = df_to_parquetstream(df)
    return base64.b64encode(pqbytes)


def base64_to_df(base64_df: bytes) -> pd.DataFrame:
    pqbytes = base64.b64decode(base64_df)
    return parquetstream_to_df(pqbytes)


def deduplist(seq: Iterable[T], keep_order=True) -> list[T]:
    if keep_order:
        return list(dict.fromkeys(seq))
    return list(set(seq))
