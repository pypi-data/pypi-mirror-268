from dataclasses import dataclass, field
from typing import Sequence, Collection, Optional, Generator
from datetime import datetime, date, time, timedelta
import polars as pl


def _dt(t: time) -> datetime:
	dummy_date = date(2000, 11, 16)
	return datetime.combine(dummy_date, t)


def _diff(time1: time, time2: time) -> timedelta:
	return _dt(time2) - _dt(time1)


# Try to make frozen
@dataclass
class BinSchedule:

	bin_duration: timedelta
	open_time: time
	close_time: time
	dates: Sequence[date]
	symbols: Collection[str]
	_schedule: Generator[pl.LazyFrame, None, None] = field(init=False)

	def _gen(self) -> Generator[pl.LazyFrame, None, None]:
		lf = pl.LazyFrame(list(self.symbols), schema={'symbol': pl.Categorical})
		lf = lf.join(pl.LazyFrame({'date': self.dates}), how='cross')
		lf = lf.with_columns(
			time=pl.datetime_ranges(
				_dt(self.open_time), _dt(self.close_time), self.bin_duration
			)
		)
		lf = lf.explode('time').with_columns(pl.col('time').cast(pl.Time))

		while True:
			yield lf

	def __post_init__(self):
		if self.open_time > self.close_time:
			raise ValueError('Open cannot be after close')

		if timedelta(0) >= self.bin_duration:
			raise ValueError('Bin duration must be positive')
		
		day_duration = _diff(self.open_time, self.close_time)
		assert day_duration % self.bin_duration == timedelta(0), \
			'Bin duration must be divisor of trade day length'

		if list(self.dates) != sorted(list(set(self.dates))):
			raise ValueError('Dates must be unique and ascending')

		if len(self.symbols) != len(set(self.symbols)):
			raise ValueError('Symbols must be unique')

		self._schedule = self._gen()

	def _validate_start_time(self, open_time: Optional[time]) -> time:
		if not open_time:
			return self.open_time

		if open_time < self.open_time or open_time >= self.close_time:
			raise ValueError('Open time not within trading hours')

		if _diff(self.open_time, open_time) % self.bin_duration != timedelta(0):
			raise ValueError('Open time not on time grid')

		return open_time

	def _validate_end_time(self, close_time: Optional[time]) -> time:
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
		*,
		start_time: Optional[time] = None,
		end_time: Optional[time] = None,
		dates: Optional[Sequence[date]] = None,
		symbols: Optional[Collection[str]] = None
	) -> pl.LazyFrame:
		'''Produce DataFrame with symbols, dates, and times according to inputs.'''

		start_time = self._validate_start_time(start_time)
		end_time = self._validate_end_time(end_time)
		dates = self._validate_dates(dates)
		symbols = self._validate_symbols(symbols)

		return next(self._schedule).filter(
			pl.col('symbol').is_in(symbols)
			& pl.col('date').is_in(dates)
			& pl.col('time').ge(start_time)
			& pl.col('time').le(end_time)
		)
