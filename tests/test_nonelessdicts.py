# stdlib
from typing import Union

# this package
from cawdrey import NonelessDict


def test_to_from_normal_dictionary():
	sample_dict = {"hello": "world", "key": 42}
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(sample_dict)
	assert sample_dict == dict(noneless)


def test_none_not_added():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless["reality"] = None
	assert "reality" not in noneless
	normal = dict(noneless)
	assert "reality" not in normal


def test_empty_not_added():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless["empty"] = []  # type: ignore[assignment]
	assert "empty" not in noneless
	normal = dict(noneless)
	assert "empty" not in normal


def test_strict_none_adds_empty():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless.set_with_strict_none_check("empty", [])  # type: ignore[arg-type]
	assert "empty" in noneless
	assert noneless["empty"] == []


def test_strict_none_with_none():
	noneless: NonelessDict[str, Union[str, int]] = NonelessDict(hello="world", key=42)
	noneless.set_with_strict_none_check("reality", None)
	assert "reality" not in noneless
