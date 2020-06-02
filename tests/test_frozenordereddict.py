# stdlib
from collections import OrderedDict

# 3rd party
import pytest  # type: ignore

# this package
from cawdrey import FrozenOrderedDict

ITEMS_1 = (
		("b", 2),
		("a", 1),
		)
ITEMS_2 = (
		("d", 4),
		("c", 3),
		)

ODICT_1 = OrderedDict(ITEMS_1)
ODICT_2 = OrderedDict(ITEMS_2)


def test_init_from_items():
	fod = FrozenOrderedDict(ITEMS_1)
	assert list(ITEMS_1) == list(fod.items())


def test_init_from_ordereddict():
	fod = FrozenOrderedDict(ODICT_1)
	assert list(ITEMS_1) == list(fod.items())


def test_setitem():
	fod = FrozenOrderedDict()

	with pytest.raises(TypeError):
		fod[1] = "b"


def test_delitem():
	fod = FrozenOrderedDict(ITEMS_1)

	with pytest.raises(TypeError):
		del fod[1]


def test_copy_no_items():
	fod1 = FrozenOrderedDict(ITEMS_1)
	fod2 = fod1.copy()

	assert id(fod1) != id(fod2)
	assert fod1.items() == fod2.items()
	assert repr(fod1) == repr(fod2)
	assert len(fod1) == len(fod2)
	assert hash(fod1) == hash(fod2)


@pytest.mark.xfail
def test_copy_tuple_items():
	fod1 = FrozenOrderedDict(ITEMS_1)
	fod2 = fod1.copy(ITEMS_2)

	assert id(fod1) != id(fod2)
	assert list(fod1) + list(ITEMS_2) == list(fod2)


@pytest.mark.xfail
def test_copy_ordereddict_items():
	fod1 = FrozenOrderedDict(ITEMS_1)
	fod2 = fod1.copy(ODICT_2)

	assert id(fod1) != id(fod2)
	assert list(fod1) + list(ITEMS_2) == list(fod2)


def test_copy_kwargs():
	fod1 = FrozenOrderedDict(ITEMS_1)
	fod2 = fod1.copy(**ODICT_2)

	assert id(fod1) != id(fod2)
	assert dict(**fod1, **ODICT_2) == fod2
