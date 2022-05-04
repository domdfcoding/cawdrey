# stdlib
import re
from collections import ChainMap, Counter, OrderedDict, defaultdict
from types import MappingProxyType
from typing import Dict, Mapping

# 3rd party
import pytest
from coincidence import not_pypy, only_pypy

# this package
from cawdrey.utils import search_dict


class DictSubclass(dict):
	pass


class TypingDictSubclass(Dict):
	pass


class CustomMapping(Mapping):

	def __init__(self, *args, **kwargs):
		self._dict = dict(*args, **kwargs)

	def __getitem__(self, item):
		return self._dict[item]

	def __iter__(self):
		yield from self._dict

	def __len__(self):
		return len(self._dict)


_custom_type_example = dict(pear="pyrus", grapefruit="citrus")
_custom_type_output = {"pear": "pyrus"}


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
			"regex, mapping, expects",
			[
					pytest.param(
							"pear", DictSubclass(_custom_type_example), _custom_type_output, id="DictSubclass"
							),
					pytest.param(
							"pear",
							TypingDictSubclass(_custom_type_example),
							_custom_type_output,
							id="TypingDictSubclass"
							),
					pytest.param(
							"pear", CustomMapping(_custom_type_example), _custom_type_output, id="CustomMapping"
							),
					pytest.param("pear", OrderedDict(_custom_type_example), _custom_type_output, id="OrderedDict"),
					pytest.param("pear", Counter(pear=1, grapefruit=2), {"pear": 1}, id="Counter"),
					pytest.param(
							"pear", defaultdict(str, _custom_type_example), _custom_type_output, id="defaultdict"
							),
					pytest.param(
							"pear",
							MappingProxyType(_custom_type_example),
							_custom_type_output,
							id="MappingProxyType"
							),
					pytest.param(
							"pear",
							ChainMap(dict(pear="pyrus"), dict(grapefruit="citrus")),
							_custom_type_output,
							id="ChainMap"
							),
					]
			)
	def test_custom_types(self, regex, mapping, expects):
		assert search_dict(mapping, regex) == expects

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
