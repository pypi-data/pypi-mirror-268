from dataclasses import dataclass, field
from typing import Sequence, Collection, Optional, Generator
from datetime import datetime, date, time, timedelta
import polars as pl


def _diff(time1: time, time2: time) -> timedelta:
	dummy_date = date(2000, 11, 16)
	datetime1 = datetime.combine(dummy_date, time1)
	datetime2 = datetime.combine(dummy_date, time2)
	return datetime2 - datetime1


# Try to make frozen
@dataclass
class BinSchedule:

	bin_duration: timedelta
	open_time: time
	close_time: time
	dates: Sequence[date]
	symbols: Collection[str]
	schedule: Generator[pl.LazyFrame, None, None] = field(init=False)

	def _gen(self) -> Generator[pl.LazyFrame, None, None]:
		lf = pl.LazyFrame({'date': self.dates}).with_columns(
			pl.col('date').dt.combine(self.open_time).alias('open'),
			pl.col('date').dt.combine(self.close_time).alias('close'),
		)
		lf = lf.with_columns(
			pl.datetime_ranges('open', 'close', self.bin_duration).alias('time_list')
		)
		lf = lf.with_columns(pl.col('time_list').explode().alias('time'))
		lf = lf.join(pl.LazyFrame({'symbol': self.symbols}), how='cross')
		df = lf.select('symbol', 'date', 'time').collect()

		while True:
			yield df.lazy()

	def __post_init__(self):
		assert self.open_time < self.close_time, 'Open must be before close'
		assert timedelta(0) < self.bin_duration, 'Bin duration must be positive'

		day_duration = _diff(self.open_time, self.close_time)
		assert day_duration % self.bin_duration == timedelta(0), \
			'Bin duration must be divisor of trade day length'

		if list(self.dates) != sorted(list(set(self.dates))):
			raise ValueError('Dates must be unique and ascending')

		if len(self.symbols) != len(set(self.symbols)):
			raise ValueError('Symbols must be unique')
		
		self._gen()

	def _validate_open_time(self, open_time: Optional[time]) -> time:
		if not open_time:
			return self.open_time
		if open_time < self.open_time or open_time >= self.close_time:
			raise ValueError('Open time not within trading hours')
		if _diff(self.open_time, open_time) % self.bin_duration != timedelta(0):
			raise ValueError('Open time not on time grid')
		return open_time

	def _validate_close_time(self, close_time: Optional[time]) -> time:
		if not close_time:
			return self.close_time
		if close_time <= self.open_time or close_time > self.close_time:
			raise ValueError('Close time not within trading hours')
		if _diff(close_time, self.close_time) % self.bin_duration != timedelta(0):
			raise ValueError('Close time not on time grid')
		return close_time

	def _validate_dates(self, dates: Optional[Sequence[date]]) -> Sequence[date]:
		if not dates:
			return self.dates
		if set(dates) - set(self.dates):
			raise ValueError('Elements of dates lie outside calendar')
		return sorted(list(set(dates)))

	def _validate_symbols(self, symbols: Optional[Collection[str]]
  ) -> Collection[str]:
		if not symbols:
			return self.symbols
		if (symbols := set(symbols)) - set(self.symbols):
			raise ValueError('Elements of symbols are not in symbol set')
		return symbols

	def __call__(
		self,
		open_time: Optional[time] = None,
		close_time: Optional[time] = None,
		dates: Optional[Sequence[date]] = None,
		symbols: Optional[Collection[str]] = None
	) -> pl.LazyFrame:
		'''Produce DataFrame with symbols, dates, and times according to inputs.'''

		open_time = self._validate_open_time(open_time)
		close_time = self._validate_close_time(close_time)
		dates = self._validate_dates(dates)
		symbols = self._validate_symbols(symbols)

		lf = next(self.schedule)
		return lf.filter(
			pl.col('symbol').is_in(symbols)
			& pl.col('date').is_in(dates)
			& (open_time <= pl.col('time') <= close_time)
		)
