# stdlib
import re

# 3rd party
import pytest
from domdf_python_tools.testing import not_pypy, only_pypy

# this package
from cawdrey.utils import search_dict


class TestSearchDict:

	example_dict = {
			"apple": "malus",
			"pear": "pyrus",
			"orange": "citrus",
			"grapefruit": "citrus",
			"lime": "citrus",
			"peach": "prunus",
			"plum": "prunus",
			"banana": "musa",
			"mango": "mangifera",
			"strawberry": "fragaria",
			"raspberry": "rubus",
			}

	@pytest.mark.parametrize(
			"regex, expects",
			[
					("pear", {"pear": "pyrus"}),
					("^pe", {"pear": "pyrus", "peach": "prunus"}),
					("grape", {"grapefruit": "citrus"}),
					("fruit", {}),
					(".*fruit$", {"grapefruit": "citrus"}),
					(re.compile("pear"), {"pear": "pyrus"}),
					(re.compile("^pe"), {"pear": "pyrus", "peach": "prunus"}),
					(re.compile("grape"), {"grapefruit": "citrus"}),
					(re.compile("fruit"), {}),
					(re.compile(".*fruit$"), {"grapefruit": "citrus"}),
					]
			)
	def test_success(self, regex, expects):
		assert search_dict(self.example_dict, regex) == expects

	@pytest.mark.parametrize(
			"dictionary, expects, match",
			[
					("abc", AttributeError, ".* object has no attribute 'items'"),
					(1234, AttributeError, ".* object has no attribute 'items'"),
					(12.34, AttributeError, ".* object has no attribute 'items'"),
					([12.34, "abc", 1234], AttributeError, ".* object has no attribute 'items'"),
					((12.34, "abc", 1234), AttributeError, ".* object has no attribute 'items'"),
					({12.34, "abc", 1234}, AttributeError, ".* object has no attribute 'items'"),
					pytest.param(
							{12.34: "abc"},
							TypeError,
							"expected string or bytes-like object",
							marks=not_pypy(),
							),
					pytest.param(
							{12.34: "abc"},
							TypeError,
							"can't use a string pattern on a bytes-like object",
							marks=only_pypy(),
							),
					]
			)
	def test_errors_dict(self, dictionary, expects, match):
		with pytest.raises(expects, match=match):
			search_dict(dictionary, '')

	@pytest.mark.parametrize(
			"regex, expects, match",
			[
					(1234, TypeError, "first argument must be string or compiled pattern"),
					(12.34, TypeError, "first argument must be string or compiled pattern"),
					([12.34, "abc", 1234], TypeError, "unhashable type: 'list'"),
					((12.34, "abc", 1234), TypeError, "first argument must be string or compiled pattern"),
					({12.34, "abc", 1234}, TypeError, "unhashable type: 'set'"),
					({12.34: "abc"}, TypeError, "unhashable type: 'dict'"),
					]
			)
	def test_errors_regex(self, regex, expects, match):
		with pytest.raises(expects, match=match):
			search_dict(self.example_dict, regex)
