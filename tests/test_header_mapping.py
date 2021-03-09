# 3rd party
import pytest

# this package
from cawdrey.header_mapping import HeaderMapping


def test_instantiation():
	HeaderMapping()


def test_headermapping():
	h: HeaderMapping[str] = HeaderMapping()

	# Setitem
	h["foo"] = "bar"

	assert dict(h) == {"foo": "bar"}

	h["Foo"] = "bar"

	assert dict(h) == {"foo": "bar", "Foo": "bar"}
	assert h.keys() == ["foo", "Foo"]

	h["Foo"] = "baz"

	assert dict(h) == {"foo": "bar", "Foo": "bar"}
	assert h.keys() == ["foo", "Foo", "Foo"]
	assert h.values() == ["bar", "bar", "baz"]
	assert h.items() == [("foo", "bar"), ("Foo", "bar"), ("Foo", "baz")]
	assert h.get_all("foo") == ["bar", "bar", "baz"]
	assert list(iter(h)) == ["foo", "Foo", "Foo"]

	# getitem
	assert h["foo"] == "bar"
	assert h["Foo"] == "bar"

	assert "bar" not in h
	assert 42 not in h

	with pytest.raises(KeyError, match="bar"):
		h["bar"]

	# len
	assert len(h) == 3

	# delitem

	h["bar"] = "baz"

	del h["Foo"]
	assert dict(h) == {"bar": "baz"}

	assert "Foo" not in h
	assert "foo" not in h


def test_get_default():
	h: HeaderMapping[str] = HeaderMapping()

	assert h.get("foo", 42) == 42
	assert h.get_all("foo", 42) == 42

	assert h.get("foo") is None
	assert h.get_all("foo") is None
