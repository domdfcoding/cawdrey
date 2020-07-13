#!/usr/bin/env python3
"""
Benchmark script

Requires https://github.com/MagicStack/immutables
"""
#  Copyright (c) Marco Sulla
#  From https://github.com/Marco-Sulla/python-frozendict
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


# stdlib
import timeit
import uuid

# 3rd party
import immutables

# this package
from cawdrey import frozendict

dictionary_sizes = (8, 1000,)
max_size = max(dictionary_sizes)


def getUuid():
	return str(uuid.uuid4())


x3000 = {"iterations": 3000}
x100000 = {"iterations": 100000}
x10000000 = {"iterations": 10000000}
x20000000 = {"iterations": 20000000}
skip_setup = {"setup": "pass"}
setup_getuid = {"setup": "key = getUuid()"}
size_unaffected = {"size_affected": False}
size_affected = {"size_affected": True}

statements = (
		{
				"code": "get(key)", "setup": "key = getUuid(); get = x.get",
				"iterations": 13000000, "name": "d.get(key)", **size_unaffected
				},
		{
				"code": "x['12323f29-c31f-478c-9b15-e7acc5354df9']", **skip_setup,
				**x10000000, "name": "d[key]", **size_unaffected
				},
		{"code": "key in x", **setup_getuid, **x10000000, "name": "key in d", **size_unaffected},
		{"code": "key not in x", **setup_getuid, **x20000000, "name": "key not in d", **size_unaffected},
		{"code": "hash(x)", **skip_setup, **x10000000, "name": "hash(d)", **size_unaffected},
		{"code": "len(x)", **skip_setup, **x20000000, "name": "len(d)", **size_unaffected},
		{
				"code": "for _ in keys(): pass", "setup": "keys = x.keys",
				**x100000, "name": "d.keys()", **size_affected},
		{
				"code": "for _ in values(): pass", "setup": "values = x.values",
				**x100000, "name": "d.values()", **size_affected},
		{
				"code": "for _ in items(): pass", "setup": "items = x.items",
				"iterations": 50000, "name": "d.items()", **size_affected},
		{"code": "for _ in iter(x): pass", **skip_setup, **x100000, "name": "iter(d)", **size_affected},
		{
				"code": "klass(d)", "setup": "klass = type(x)",
				"iterations": 10000, "name": "constructor(dict)", **size_affected},
		{
				"code": "klass(v)", "setup": "klass = type(x); v = tuple(d.items())",
				"iterations": 10000, "name": "constructor(d.items())", **size_affected},
		{
				"code": "klass(**d)", "setup": "klass = type(x)",
				"iterations": 5000, "name": "constructor(**d)", **size_affected},
		{
				"code": "klass(x)", "setup": "klass = type(x)",
				"iterations": 50000, "name": "constructor(self)", **size_affected},
		{"code": "x == d", **skip_setup, **x100000, "name": "d1 == d2", **size_affected},
		{"code": "x == x", **skip_setup, **x100000, "name": "self == self", **size_affected},
		{"code": "repr(x)", **skip_setup, **x3000, "name": "repr(d)", **size_affected},
		{"code": "str(x)", **skip_setup, **x3000, "name": "str(d)", **size_affected},
		)

for n in dictionary_sizes:
	print("#" * 80)
	d = dict()

	for i in range(n - 1):
		d[getUuid()] = getUuid()

	d['12323f29-c31f-478c-9b15-e7acc5354df9'] = getUuid()

	h = immutables.Map(d)
	fd = frozendict(d)

	for statement in statements:
		print("/"*80)

		for x in (d, h, fd):
			if statement["name"] == "hash(d)" and isinstance(x, dict):
				continue

			if statement["size_affected"]:
				iterations = int(statement["iterations"] * max_size / n)
			else:
				iterations = statement["iterations"]
			print(statement)
			t = timeit.timeit(
					stmt=statement["code"],
					setup=statement["setup"],
					globals={"x": x, "getUuid": getUuid, "d": d},
					number=iterations
					)

			print("Dictionary size: {: >4}; Type: {: >10}; Statement: {: <25} time: {:.3f}; iterations: {: >8}".format(
					n,
					type(x).__name__,
					"`{}`;".format(statement["name"]),
					t,
					iterations
					))
