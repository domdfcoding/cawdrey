==========
frozendict
==========

About
========

:class:`~cawdrey._frozendict.frozendict` is an immutable wrapper around dictionaries that implements the
complete mapping interface. It can be used as a drop-in replacement for
dictionaries where immutability is desired.

Of course, this is ``python``, and you can still poke around the object's
internals if you want.

The :class:`~cawdrey._frozendict.frozendict` constructor mimics :class:`dict`, and all of the expected
interfaces (``iter``, ``len``, ``repr``, ``hash``, ``getitem``) are provided.
Note that a :class:`~cawdrey._frozendict.frozendict` does not guarantee the immutability of its values, so
the utility of the ``hash`` method is restricted by usage.

The only difference is that the ``copy()`` method of :class:`~cawdrey._frozendict.frozendict` takes
variable keyword arguments, which will be present as key/value pairs in the new,
immutable copy.

Usage
========

.. code-block:: python3

	>>> from cawdrey import frozendict
	>>>
	>>> fd = frozendict({ 'hello': 'World' })
	>>>
	>>> print fd
	<frozendict {'hello': 'World'}>
	>>>
	>>> print fd['hello']
	'World'
	>>>
	>>> print fd.copy(another='key/value')
	<frozendict {'hello': 'World', 'another': 'key/value'}>
	>>>

In addition, :class:`~cawdrey._frozendict.frozendict` supports the ``+`` and ``-`` operands. If you add a
:class:`dict`-like object, a new :class:`~cawdrey._frozendict.frozendict` will be returned, equal to the old
:class:`~cawdrey._frozendict.frozendict` updated with the other object. Example:

.. code-block:: python3

	>>> frozendict({"Sulla": "Marco", 2: 3}) + {"Sulla": "Marò", 4: 7}
	<frozendict {'Sulla': 'Marò', 2: 3, 4: 7}>
	>>>

You can also subtract an iterable from a :class:`~cawdrey._frozendict.frozendict`. A new :class:`~cawdrey._frozendict.frozendict`
will be returned, without the keys that are in the iterable. Examples:

.. code-block::

	>>> frozendict({"Sulla": "Marco", 2: 3}) - {"Sulla": "Marò", 4: 7}
	<frozendict {'Sulla': 'Marco', 2: 3}>
	>>> frozendict({"Sulla": "Marco", 2: 3}) - [2, 4]
	<frozendict {'Sulla': 'Marco'}>
	>>>


Some other examples:

.. code-block:: python3

	>>> from cawdrey import frozendict
	>>> fd = frozendict({"Sulla": "Marco", "Hicks": "Bill"})
	>>> print(fd)
	<frozendict {'Sulla': 'Marco', 'Hicks': 'Bill'}>
	>>> print(fd["Sulla"])
	Marco
	>>> fd["Bim"]
	KeyError: 'Bim'
	>>> len(fd)
	2
	>>> "Sulla" in fd
	True
	>>> "Sulla" not in fd
	False
	>>> "Bim" in fd
	False
	>>> hash(fd)
	835910019049608535
	>>> fd_unhashable = frozendict({1: []})
	>>> hash(fd_unhashable)
	TypeError: unhashable type: 'list'
	>>> fd2 = frozendict({"Hicks": "Bill", "Sulla": "Marco"})
	>>> print(fd2)
	<frozendict {'Hicks': 'Bill', 'Sulla': 'Marco'}>
	>>> fd2 is fd
	False
	>>> fd2 == fd
	True
	>>> frozendict()
	<frozendict {}>
	>>> frozendict(Sulla="Marco", Hicks="Bill")
	<frozendict {'Sulla': 'Marco', 'Hicks': 'Bill'}>
	>>> frozendict((("Sulla", "Marco"), ("Hicks", "Bill")))
	<frozendict {'Sulla': 'Marco', 'Hicks': 'Bill'}>
	>>> fd.get("Sulla")
	'Marco'
	>>> print(fd.get("God"))
	None
	>>> tuple(fd.keys())
	('Sulla', 'Hicks')
	>>> tuple(fd.values())
	('Marco', 'Bill')
	>>> tuple(fd.items())
	(('Sulla', 'Marco'), ('Hicks', 'Bill'))
	>>> iter(fd)
	<dict_keyiterator object at 0x7feb75c49188>
	>>> frozendict.fromkeys(["Marco", "Giulia"], "Sulla")
	<frozendict {'Marco': 'Sulla', 'Giulia': 'Sulla'}>
	>>> fd["Sulla"] = "Silla"
	TypeError: 'frozendict' object does not support item assignment
	>>> del fd["Sulla"]
	TypeError: 'frozendict' object does not support item deletion
	>>> fd.clear()
	AttributeError: 'frozendict' object has no attribute 'clear'
	>>> fd.pop("Sulla")
	AttributeError: 'frozendict' object has no attribute 'pop'
	>>> fd.popitem()
	AttributeError: 'frozendict' object has no attribute 'popitem'
	>>> fd.setdefault("Sulla")
	AttributeError: 'frozendict' object has no attribute 'setdefault'
	>>> fd.update({"Bim": "James May"})
	AttributeError: 'frozendict' object has no attribute 'update'



API Reference
===========================

.. autoclass:: cawdrey._frozendict.frozendict
	:exclude-members: dict_cls

Copyright
=========

| Based on https://github.com/slezica/python-frozendict and https://github.com/mredolatti/python-frozendict .
| Copyright (c) 2012 Santiago Lezica
| Licensed under the MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

| Also based on https://github.com/Marco-Sulla/python-frozendict
| Copyright (c) Marco Sulla
| Licensed under the `GNU Lesser General Public License Version 3 <https://www.gnu.org/licenses/lgpl-3.0.en.html>`_
