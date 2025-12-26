# stdlib
import math
from typing import Mapping, Optional, Sequence, Union

# 3rd party
import pytest
from pytest_regressions.data_regression import DataRegressionFixture

# this package
from cawdrey.tally import SupportsMostCommon, Tally


class CounterRegressionFixture(DataRegressionFixture):

	def check(
			self,
			data_dict: Union[Sequence, Mapping],
			basename: Optional[str] = None,
			fullpath: Optional[str] = None,
			) -> None:
		super().check(dict(data_dict), basename=basename, fullpath=fullpath)


@pytest.fixture()
def counter_regression(datadir, original_datadir, request) -> CounterRegressionFixture:  # noqa: MAN001
	return CounterRegressionFixture(datadir, original_datadir, request)


data = [
		"cat",
		"dog",
		"dog",
		"cat",
		"rabbit",
		"dog",
		"dog",
		"cat",
		"snake",
		"gerbil",
		]


def test_as_percentage(counter_regression: CounterRegressionFixture):
	tally = Tally(data)
	percentage = tally.as_percentage()
	counter_regression.check(percentage)
	assert math.isclose(sum(percentage.values()), 1.0)


def test_total():
	tally = Tally(data)
	assert tally.total == len(data)


def test_get_percentage():
	tally = Tally(data)
	assert tally.get_percentage("dog") == 0.4
	assert tally.get_percentage("cat") == 0.3
	assert tally.get_percentage("gerbil") == 0.1
	assert tally.get_percentage("chicken") is None
	assert tally.get_percentage("chicken", 0.0) == 0.0
	assert tally.get_percentage("chicken", 0.1) == 0.1


def mypy_check(percent: bool = False) -> SupportsMostCommon[str]:
	tally: Tally[str] = Tally("abracadabra")

	data: SupportsMostCommon[str]
	if percent:
		data = tally.as_percentage()
	else:
		data = tally

	return data
