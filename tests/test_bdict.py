# 3rd party
import pytest

# this package
from cawdrey import bdict


def test_bdict():
	new_dict = bdict(Alice=27, Bob=30, Dom=23)

	assert new_dict[23] == "Dom"
	assert new_dict["Alice"] == 27

	# test deleting key
	del new_dict["Alice"]
	with pytest.raises(KeyError):
		new_dict["Alice"]

	# test booleans
	new_dict["True"] = True
	assert new_dict["True"] is True
	new_dict["False"] = False
	assert new_dict["False"] is False
	new_dict["None"] = None
	assert new_dict["None"] is None

	# test replacing keys

	new_dict = bdict([("Key1", "Value1"), ("Key2", "Value2"), ("Key3", "Value3")])

	new_dict["Key1"] = 1234
	assert "Value1" not in new_dict
	assert new_dict[1234] == "Key1"
	assert new_dict["Key1"] == 1234

	new_dict["Value2"] = 5678
	assert "Key2" not in new_dict
	assert new_dict[5678] == "Value2"
	assert new_dict["Value2"] == 5678


def test_bdict_from_dict():
	original_dict = {"Alice": 27, "Bob": 30, "Dom": 23}

	new_dict = bdict(original_dict)

	assert new_dict[23] == "Dom"
	assert new_dict["Alice"] == 27


def test_bdict_booleans():
	original_dict = {"True": True, "False": False, "None": None}

	new_dict = bdict(original_dict)

	assert new_dict[True] == "True"
	assert new_dict["True"]

	original_dict = {True: True, False: False, None: None}

	new_dict = bdict(original_dict)

	assert new_dict[True]


def test_bdict_from_zip():
	new_dict = bdict(zip(["Alice", "Bob", "Dom"], [27, 30, 23]))

	assert new_dict[23] == "Dom"
	assert new_dict["Alice"] == 27


def test_bdict_from_list():
	new_dict = bdict([("Alice", 27), ("Bob", 30), ("Dom", 23)])

	assert new_dict[23] == "Dom"
	assert new_dict["Alice"] == 27


def test_bdict_bool():
	new_dict = bdict(N=None, T=True, F=False)

	print(new_dict)

	assert None in new_dict
	assert True in new_dict
	assert True in new_dict

	assert isinstance(new_dict["T"], bool) and new_dict["T"]
	assert isinstance(new_dict["F"], bool) and not new_dict["F"]

	assert new_dict[True] == "T"
	assert new_dict[False] == "F"
	assert new_dict[None] == "N"

	assert "_None" in new_dict
	assert new_dict["_None"] == "N"

	# Test for pyMHDAC
	new_dict_2 = bdict(Unspecified=0, _None=1, GC=2, LC=3, CE=4)

	assert None in new_dict_2

	assert new_dict_2[None] == 1
