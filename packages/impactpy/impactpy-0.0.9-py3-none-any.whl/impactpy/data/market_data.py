from collections import OrderedDict
import polars as pl
from polars import DataType
from .bin_schedule import BinSchedule


class BinnedData:

	@property
	def df(self) -> pl.DataFrame:
		return self._df

	@staticmethod
	def _validate_schema(schema: OrderedDict[str, DataType]) -> None:
		required_cols = {
			'stock': pl.Categorical, 'date': pl.Date, 'time': pl.Time,
			'mid': pl.Float64, 'trade': pl.Int32
		}
		assert dict(schema) == required_cols, f'Schema mismatch'
		     
	@staticmethod
	def _fill_missing(df: pl.DataFrame) -> pl.DataFrame: ...

	def __init__(self, df: pl.DataFrame, schedule: BinSchedule) -> None:
		self._df = df