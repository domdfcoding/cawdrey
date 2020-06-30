"""

Based on http://peter-hoffmann.com/2011/adding-dict-interface-python-leveldb-api.html
"""

# stdlib
import json
from typing import Any, MutableMapping

# 3rd party
import plyvel  # type: ignore

# this package
from cawdrey.base import KT, VT


class LevelDict(MutableMapping[KT, VT]):
	"""
	Dict Wrapper around the Google LevelDB Database. Keys and values must be strings
	"""

	def __init__(self, path):
		"""
		Constructor for LevelDict
		"""

		self.path = path
		self.db = plyvel.DB(self.path, create_if_missing=True, error_if_exists=False)

	def __getitem__(self, key: Any) -> Any:
		return self.db.get(key.encode("UTF-8")).decode("UTF-8")

	def __setitem__(self, key, value):
		self.db.put(key.encode("UTF-8"), value.encode("UTF-8"))

	def __delitem__(self, key):
		self.db.delete(key.encode("UTF-8"))

	def __iter__(self):
		for k, v in self.db:
			yield k.decode("UTF-8")

	def __contains__(self, key: Any) -> Any:
		return self.db.get(key.encode("UTF-8")) is not None

	def __len__(self) -> int:
		return len(list(self))

	def __repr__(self) -> str:
		return f"<{self.__class__.__name__} {dict(self.db)}>"

	def keys(self):
		return list(self)

	def values(self):
		for k, v in self.db:
			yield v.decode("UTF-8")

	def items(self):
		for k, v in self.db:
			yield k.decode("UTF-8"), v.decode("UTF-8")


# TODO:
#   clear, copy, fromkeys, pop, popitem, setdefault, update


class JsonLevelDict(MutableMapping[KT, VT]):
	"""
	Dict Wrapper around the Google LevelDB Database.
	Keys must be strings and values can be any JSON-serialisable value.
	"""

	def __init__(self, path):
		"""Constructor for LevelDict"""
		self.path = path
		self.db = plyvel.DB(self.path, create_if_missing=True, error_if_exists=False)

	def __getitem__(self, key: Any) -> Any:
		return json.loads(self.db.get(key.encode("UTF-8")).decode("UTF-8"))

	def __setitem__(self, key, value):
		self.db.put(key.encode("UTF-8"), json.dumps(value).encode("UTF-8"))

	def __delitem__(self, key):
		self.db.delete(key.encode("UTF-8"))

	def __iter__(self):
		for k, v in self.db:
			yield k.decode("UTF-8")

	def __contains__(self, key: Any) -> Any:
		return self.db.get(key.encode("UTF-8")) is not None

	def __len__(self) -> int:
		return len(list(self))

	def __repr__(self) -> str:
		return f"<{self.__class__.__name__} {dict(self.db)}>"

	def keys(self):
		return list(self)

	def values(self):
		for k, v in self.db:
			yield json.loads(v.decode("UTF-8"))

	def items(self):
		for k, v in self.db:
			yield k.decode("UTF-8"), json.loads(v.decode("UTF-8"))


# TODO:
#   clear, copy, fromkeys, pop, popitem, setdefault, update


class TypedLevelDict(MutableMapping[KT, VT]):
	"""
	Dict Wrapper around the Google LevelDB Database.
	Keys must be strings and values can be any JSON-serialisable value.
	"""

	key_type = str
	value_type = str

	def __init__(self, path):
		"""Constructor for LevelDict"""
		self.path = path
		self.db = plyvel.DB(self.path, create_if_missing=True, error_if_exists=False)

	def __getitem__(self, key: Any) -> Any:
		return self.value_type(self.db.get(str(key).encode("UTF-8")).decode("UTF-8"))

	def __setitem__(self, key, value):
		self.db.put(str(key).encode("UTF-8"), str(value).encode("UTF-8"))

	def __delitem__(self, key):
		self.db.delete(str(key).encode("UTF-8"))

	def __iter__(self):
		for k, v in self.db:
			yield self.key_type(k.decode("UTF-8"))

	def __contains__(self, key: Any) -> Any:
		return self.db.get(str(key).encode("UTF-8")) is not None

	def __len__(self) -> int:
		return len(list(self))

	def __repr__(self) -> str:
		return f"<{self.__class__.__name__} {dict(self.db)}>"

	def keys(self):
		return list(self)

	def values(self):
		for k, v in self.db:
			yield self.value_type(v.decode("UTF-8"))

	def items(self):
		for k, v in self.db:
			yield self.key_type(k.decode("UTF-8")), self.value_type(v.decode("UTF-8"))


# TODO:
#   clear, copy, fromkeys, pop, popitem, setdefault, update
