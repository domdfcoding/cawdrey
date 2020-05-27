import pytest

from cawdrey import frozendict

################################################################################
# dict fixtures


@pytest.fixture
def fd_dict():
	return {"Sulla": "Marco", "Hicks": "Bill", frozendict({1: 2}): "frozen"}


@pytest.fixture
def fd_dict_eq():
	return {"Hicks": "Bill", "Sulla": "Marco", frozendict({1: 2}): "frozen"}


def fd_dict_2_raw():
	return {"Sulla": "Marco", "Hicks": "Bill", "frozen": frozendict({1: 2})}


fd_dict_2 = pytest.fixture(fd_dict_2_raw)


@pytest.fixture
def fd_sub_dict():
	return {"Hicks": "Bill"}


@pytest.fixture
def fd_nested_dict():
	return {
			"Sulla": ("Marco", "Adele", "Mario", "Giulia"),
			"Hicks": ("Bill", ),
			"others": (
					frozendict({
							"comedians": [
									"Woody Allen",
									"George Carlin",
									"Emo Philips",
									"Groucho Marx",
									"Corrado Guzzanti",
									],
							"comedies": [
									"Bananas",
									"Dogma",
									"E=mo²",
									"A Night at the Opera",
									"Fascisti su Marte",
									]
							})
					)
			}


def math_dict_raw():
	return {"Sulla": "Marò", 5: 7}


math_dict = pytest.fixture(math_dict_raw)

################################################################################
# frozendict fixtures


@pytest.fixture
def fd(fd_dict):
	return frozendict(fd_dict)


@pytest.fixture
def fd_unhashable():
	return frozendict({1: []})


@pytest.fixture
def fd_eq(fd_dict_eq):
	return frozendict(fd_dict_eq)


def fd2_raw():
	return frozendict(fd_dict_2_raw())


fd2 = pytest.fixture(fd2_raw)


@pytest.fixture
def fd_sub(fd_sub_dict):
	return frozendict(fd_sub_dict)


@pytest.fixture
def fd_nested(fd_nested_dict):
	return frozendict(fd_nested_dict)


def math_fd_raw():
	return frozendict(math_dict_raw())


def math_items_raw():
	return tuple(math_dict_raw().items())


@pytest.fixture
def fd_giulia():
	return frozendict({'Marco': 'Sulla', 'Giulia': 'Sulla'})


@pytest.fixture
def fd_items(fd_dict):
	return tuple(fd_dict.items())


@pytest.fixture
def fd_empty():
	return frozendict()


@pytest.fixture
def fd_repr(fd_dict):
	return f"<{frozendict.__name__} {fd_dict!r}>"


################################################################################
# main tests


def test_normalget(fd):
	assert fd["Sulla"] == "Marco"


def test_keyerror(fd):
	with pytest.raises(KeyError):
		fd["Bim"]


def test_len(fd, fd_dict):
	assert len(fd) == len(fd_dict)


def test_in_true(fd):
	assert "Sulla" in fd


def test_not_in_false(fd):
	assert not ("Sulla" not in fd)


def test_in_false(fd):
	assert not ("Bim" in fd)


def test_not_in_true(fd):
	assert "Bim" not in fd


def test_bool_true(fd):
	assert fd


def test_bool_false(fd_empty):
	assert not fd_empty


def test_not_equal(fd, fd_giulia):
	assert fd != fd_giulia


def test_equals_dict(fd, fd_dict):
	assert fd == fd_dict


def test_hash(fd, fd_eq):
	assert hash(fd)
	assert hash(fd) == hash(fd_eq)


def test_constructor_kwargs(fd2, fd_dict_2):
	assert frozendict(**fd_dict_2) == fd2


def test_constructor_iterator(fd, fd_items):
	assert frozendict(fd_items) == fd


def test_sorted_keys(fd2, fd_dict_2):
	fd_sorted = fd2.sorted()
	assert list(fd_sorted) == sorted(fd_dict_2)
	assert fd_sorted is fd_sorted.sorted()


def strangeSort(item):
	return f"{item[0]}{item[1]}"


def test_sorted_items(fd2, fd_dict_2):
	fd_sorted = fd2.sorted(by="items", key=strangeSort)
	assert list(fd_sorted.items()) == sorted(fd_dict_2.items(), key=strangeSort)
	assert fd_sorted is fd_sorted.sorted()


def test_sorted_values(fd, fd_dict):
	fd_sorted = fd.sorted(by="values")

	res = []

	for k, v in fd_dict.items():
		if not res:
			res.append((k, v))
		else:
			pos = None

			for i, entry in enumerate(res):
				if v < entry[1]:
					pos = i
					break

			if pos is None:
				res.append((k, v))
			else:
				res.insert(pos, (k, v))

	assert list(fd_sorted.items()) == res
	assert fd_sorted is fd_sorted.sorted(by="values")


def test_sorted_empty(fd_empty):
	assert fd_empty.sorted() is fd_empty


def test_sorted_bad_by(fd):
	with pytest.raises(ValueError):
		fd_sorted = fd.sorted(by="value")


def test_unhashable_value(fd_unhashable):
	with pytest.raises(TypeError):
		hash(fd_unhashable)

	# hash is cached
	with pytest.raises(TypeError):
		hash(fd_unhashable)


def test_todict(fd, fd_dict):
	assert dict(fd) == fd_dict


def test_get(fd):
	assert fd.get("Sulla") == "Marco"


def test_get_fail(fd):
	default = object()
	assert fd.get("Bim", default) is default


def test_keys(fd, fd_dict):
	assert tuple(fd.keys()) == tuple(fd_dict.keys())


def test_values(fd, fd_dict):
	assert tuple(fd.values()) == tuple(fd_dict.values())


def test_items(fd, fd_dict):
	assert tuple(fd.items()) == tuple(fd_dict.items())


def test_fromkeys(fd, fd_giulia):
	assert frozendict.fromkeys(["Marco", "Giulia"], "Sulla") == fd_giulia


def test_repr(fd, fd_repr):
	assert repr(fd) == fd_repr


def test_str(fd, fd_repr):
	assert str(fd) == fd_repr


def test_format(fd, fd_repr):
	assert format(fd) == fd_repr


def test_iter(fd):
	items = []

	for x in iter(fd):
		items.append((x, fd[x]))

	assert tuple(fd.items()) == tuple(items)


@pytest.mark.parametrize(
		"addend", (
				math_dict_raw(),
				math_fd_raw(),
				pytest.param("hell-o", marks=pytest.mark.xfail),
				)
		)
def test_add(fd, addend):
	newd = dict(fd)
	newd.update(addend)
	newfrozen = frozendict(newd)
	assert fd + addend == newfrozen
	fd += addend
	assert fd == newfrozen


@pytest.mark.parametrize("subtrahend", (
		math_dict_raw(),
		math_fd_raw(),
		math_items_raw(),
		))
def test_sub(fd, fd_dict, subtrahend):
	fd_copy = fd.copy()
	newd = {k: v for k, v in fd.items() if (k, v) not in subtrahend}
	newfrozen = frozendict(newd)
	assert fd - subtrahend == newfrozen
	fd -= subtrahend
	assert fd == newfrozen


@pytest.mark.parametrize(
		"other", (
				fd2_raw(),
				("frozen", "Sulla", "Hicks"),
				pytest.param(5, marks=pytest.mark.xfail),
				)
		)
def test_bitwise_and(fd_eq, other):
	assert fd_eq & other == {"Sulla": "Marco", "Hicks": "Bill"}


################################################################################
# immutability tests


def test_normalset(fd):
	with pytest.raises(TypeError):
		fd["Sulla"] = "Silla"


def test_del(fd):
	with pytest.raises(TypeError):
		del fd["Sulla"]


def test_clear(fd):
	with pytest.raises(AttributeError):
		fd.clear()


def test_pop(fd):
	with pytest.raises(AttributeError):
		fd.pop("Sulla")


def test_popitem(fd):
	with pytest.raises(AttributeError):
		fd.popitem()


def test_setdefault(fd):
	with pytest.raises(AttributeError):
		fd.setdefault("Sulla")


def test_update(fd):
	with pytest.raises(AttributeError):
		fd.update({"Bim": "James May"})


def test_init(fd):
	with pytest.raises(TypeError):
		fd.__init__({"Trump": "Donald"})


def test_delvar(fd):
	del fd

	with pytest.raises(NameError):
		fd
