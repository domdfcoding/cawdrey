===================
FrozenOrderedDict
===================

About
========

:class:`~cawdrey.frozenordereddict.FrozenOrderedDict` is a immutable wrapper around an OrderedDict.

:class:`~cawdrey.frozenordereddict.FrozenOrderedDict` is similar to ``frozendict``, and with regards to immutability it
solves the same problems:

	- Because dictionaries are mutable, they are not hashable and cannot be used in sets or as dictionary keys.
	- Nasty bugs can and do occur when mutable data structures are passed around.

It can be initialized just like a :class:`~python:dict` or :class:`~python:collections.OrderedDict`.
Once instantiated, an instance of :class:`~cawdrey.frozenordereddict.FrozenOrderedDict` cannot be altered,
since it does not implement the ``MutableMapping`` interface.

It does implement the ``Mapping`` interface, so can be used just like a
normal dictionary in most cases.

In order to modify the contents of a :class:`~cawdrey.frozenordereddict.FrozenOrderedDict`, a new
instance must be created. The easiest way to do that is by
calling the `.copy()` method. It will return a new instance of
:class:`~cawdrey.frozenordereddict.FrozenOrderedDict` initialized using the following steps:

	1. A copy of the wrapped OrderedDict instance will be created.
	2. If any arguments or keyword arguments are passed to the `.copy()` method, they will be used to create another OrderedDict instance, which will then be used to update the copy made in step #1.
	3. Finally, `self.__class__()` will be called, passing the copy as the only argument.

API Reference
===========================

.. autoclass:: cawdrey.frozenordereddict.FrozenOrderedDict
	:members:
	:undoc-members:


Copyright
=========

Based on https://github.com/slezica/python-frozendict and https://github.com/mredolatti/python-frozendict .

Copyright (c) 2012 Santiago Lezica

Licensed under the MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

|

Also based on
https://github.com/Marco-Sulla/python-frozendict
Copyright (c) Marco Sulla
Licensed under the `GNU Lesser General Public License Version 3 <https://www.gnu.org/licenses/lgpl-3.0.en.html>`_

|

Also based on https://github.com/wsmith323/frozenordereddict

Copyright (c) 2015 Warren Smith

Licensed under the MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

