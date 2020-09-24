# stdlib
from typing import Union

# this package
from cawdrey import NonelessDict


def testToFromNormalDictionary():
	sample_dict = {"hello": "world", "key": 42}
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(sample_dict)
	assert sample_dict == dict(noneless)


def testNoneNotAdded():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless["reality"] = None
	assert "reality" not in noneless
	normal = dict(noneless)
	assert "reality" not in normal


def testEmptyNotAdded():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless["empty"] = []
	assert "empty" not in noneless
	normal = dict(noneless)
	assert "empty" not in normal


def testStrictNoneAddsEmpty():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless.set_with_strict_none_check("empty", [])
	assert "empty" in noneless
	assert noneless["empty"] == []


def testStrictNoneWithNone():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless.set_with_strict_none_check("reality", None)
	assert "reality" not in noneless
