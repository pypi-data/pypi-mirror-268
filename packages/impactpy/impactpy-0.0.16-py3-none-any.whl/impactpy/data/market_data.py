from dataclasses import dataclass
import polars as pl
from .bin_schedule import BinSchedule


@dataclass
class BinnedData:

	schedule: BinSchedule
	data: pl.LazyFrame

	def __post_init__(self):
		self.data = self.schedule(self.data)