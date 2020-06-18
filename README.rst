==========
Cawdrey
==========

.. start short_desc

**Several useful custom dictionaries for Python 📖 🐍**

.. end short_desc

.. start shields 

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |actions_windows| |actions_macos| |coveralls| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/cawdrey/latest?logo=read-the-docs
	:target: https://cawdrey.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status
	
.. |docs_check| image:: https://github.com/domdfcoding/cawdrey/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/cawdrey/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/domdfcoding/cawdrey/master?logo=travis
	:target: https://travis-ci.org/domdfcoding/cawdrey
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/cawdrey/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/cawdrey/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/cawdrey/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/cawdrey/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/cawdrey/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/cawdrey/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/cawdrey/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/cawdrey?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/cawdrey?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/cawdrey
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/cawdrey?logo=anaconda
	:alt: Conda - Package Version
	:target: https://anaconda.org/domdfcoding/cawdrey

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/cawdrey?label=conda%7Cplatform
	:alt: Conda - Platform
	:target: https://anaconda.org/domdfcoding/cawdrey

.. |license| image:: https://img.shields.io/github/license/domdfcoding/cawdrey
	:alt: License
	:target: https://github.com/domdfcoding/cawdrey/blob/master/LICENSE

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/cawdrey
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/cawdrey/v0.1.6
	:target: https://github.com/domdfcoding/cawdrey/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/cawdrey
	:target: https://github.com/domdfcoding/cawdrey/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. end shields

Contents
=============

* ``frozendict``: An immutable dictionary that cannot be changed after creation.
* ``FrozenOrderedDict``: An immutable ``OrderedDict`` where the order of keys is preserved, but that cannot be changed after creation.
* ``AlphaDict``: A ``FrozenOrderedDict`` where the keys are stored in alphabetical order.
* ``bdict``: A dictionary where `key, value` pairs are stored both ways round.

|

This package also provides two base classes for creating your own custom dictionaries:

* ``FrozenBase``: An Abstract Base Class for Frozen dictionaries.

* ``MutableBase``: An Abstract Base Class for mutable dictionaries.

|

Other Dictionary Packages
===========================

If you're looking to unflatten a dictionary, such as to go from this:

.. code-block:: python

	{'foo.bar': 'val'}

to this:

.. code-block:: python

	{'foo': {'bar': 'val'}}

check out `unflatten`_, `flattery`_ or `morph`_  to accomplish that.

.. _unflatten: https://github.com/dairiki/unflatten
.. _morph: https://github.com/metagriffin/morph
.. _flattery: https://github.com/acg/python-flattery


`indexed`_ provides an OrederedDict where the values can be accessed by their index as well as by their keys.

.. _indexed: https://github.com/niklasf/indexed.py

There's also `python-benedict`_, which provides a custom dictionary with **keylist/keypath** support, **I/O** shortcuts (``Base64``, ``CSV``, ``JSON``, ``TOML``, ``XML``, ``YAML``, ``pickle``, ``query-string``) and many **utilities**.

.. _python-benedict: https://github.com/fabiocaccamo/python-benedict

Installation
===========================

.. start installation

``cawdrey`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install cawdrey

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels http://conda.anaconda.org/domdfcoding
		$ conda config --add channels http://conda.anaconda.org/conda-forge

	* Then install

	.. code-block:: bash

		$ conda install cawdrey

.. end installation



And Finally:
==============

`Why "Cawdrey"? <https://en.wikipedia.org/wiki/Robert_Cawdrey>`_
