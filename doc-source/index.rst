==========
Cawdrey
==========

.. start short_desc

.. documentation-summary::
	:meta:

.. end short_desc
.. start shields

.. only:: html

	.. list-table::
		:stub-columns: 1
		:widths: 10 90

		* - Docs
		  - |docs| |docs_check|
		* - Tests
		  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
		* - PyPI
		  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
		* - Anaconda
		  - |conda-version| |conda-platform|
		* - Activity
		  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
		* - QA
		  - |codefactor| |actions_flake8| |actions_mypy|
		* - Other
		  - |license| |language| |requires|

	.. |docs| rtfd-shield::
		:project: cawdrey
		:alt: Documentation Build Status

	.. |docs_check| actions-shield::
		:workflow: Docs Check
		:alt: Docs Check Status

	.. |actions_linux| actions-shield::
		:workflow: Linux
		:alt: Linux Test Status

	.. |actions_windows| actions-shield::
		:workflow: Windows
		:alt: Windows Test Status

	.. |actions_macos| actions-shield::
		:workflow: macOS
		:alt: macOS Test Status

	.. |actions_flake8| actions-shield::
		:workflow: Flake8
		:alt: Flake8 Status

	.. |actions_mypy| actions-shield::
		:workflow: mypy
		:alt: mypy status

	.. |requires| requires-io-shield::
		:alt: Requirements Status

	.. |coveralls| coveralls-shield::
		:alt: Coverage

	.. |codefactor| codefactor-shield::
		:alt: CodeFactor Grade

	.. |pypi-version| pypi-shield::
		:project: cawdrey
		:version:
		:alt: PyPI - Package Version

	.. |supported-versions| pypi-shield::
		:project: cawdrey
		:py-versions:
		:alt: PyPI - Supported Python Versions

	.. |supported-implementations| pypi-shield::
		:project: cawdrey
		:implementations:
		:alt: PyPI - Supported Implementations

	.. |wheel| pypi-shield::
		:project: cawdrey
		:wheel:
		:alt: PyPI - Wheel

	.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/cawdrey?logo=anaconda
		:target: https://anaconda.org/domdfcoding/cawdrey
		:alt: Conda - Package Version

	.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/cawdrey?label=conda%7Cplatform
		:target: https://anaconda.org/domdfcoding/cawdrey
		:alt: Conda - Platform

	.. |license| github-shield::
		:license:
		:alt: License

	.. |language| github-shield::
		:top-language:
		:alt: GitHub top language

	.. |commits-since| github-shield::
		:commits-since: v0.4.2
		:alt: GitHub commits since tagged version

	.. |commits-latest| github-shield::
		:last-commit:
		:alt: GitHub last commit

	.. |maintained| maintained-shield:: 2021
		:alt: Maintenance

	.. |pypi-downloads| pypi-shield::
		:project: cawdrey
		:downloads: month
		:alt: PyPI - Downloads

.. end shields



Contents
----------

* :class:`~.frozendict`: An immutable dictionary that cannot be changed after creation.
* :class:`~.FrozenOrderedDict`: An immutable :class:`~collections.OrderedDict` where the order of keys is preserved, but that cannot be changed after creation.
* :class:`~.AlphaDict`: A :class:`~.FrozenOrderedDict` where the keys are stored in alphabetical order.
* :class:`~.bdict`: A dictionary where ``key, value`` pairs are stored both ways round.
* :class:`~.Tally`: A subclass of :class:`collections.Counter` with additional methods.
* :class:`~.HeaderMapping`: A :class:`collections.abc.MutableMapping` which supports duplicate, case-insentive keys.


This package also provides two base classes for creating your own custom dictionaries:

* :class:`~.FrozenBase`: An Abstract Base Class for frozen dictionaries.

* :class:`~.MutableBase`: An Abstract Base Class for mutable dictionaries.


Other Dictionary Packages
------------------------------

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

There's also `python-benedict`_, which provides a custom dictionary with **keylist/keypath** support,
**I/O** shortcuts (``Base64``, ``CSV``, ``JSON``, ``TOML``, ``XML``, ``YAML``, ``pickle``, ``query-string``)
and many **utilities**.

.. _python-benedict: https://github.com/fabiocaccamo/python-benedict



Installation
----------------

.. start installation

.. installation:: cawdrey
	:pypi:
	:github:
	:anaconda:
	:conda-channels: conda-forge, domdfcoding

.. end installation


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: API Reference
	:glob:

	classes/*

	base
	docs

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	contributing
	Source

.. sidebar-links::
	:caption: Links
	:github:
	:pypi: cawdrey


.. start links

.. only:: html

	View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

	:github:repo:`Browse the GitHub Repository <domdfcoding/cawdrey>`

.. end links


And Finally:
----------------

`Why "Cawdrey"? <https://en.wikipedia.org/wiki/Robert_Cawdrey>`_
