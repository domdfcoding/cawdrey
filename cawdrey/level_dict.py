#!/usr/bin/env python
#
#  level_dict.py
"""
Provides an experimental dictionary wrapper to Google's LevelDB.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Based on http://peter-hoffmann.com/2011/adding-dict-interface-python-leveldb-api.html
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

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
