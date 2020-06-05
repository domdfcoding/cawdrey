# stdlib
from typing import Optional

# this package
from cawdrey import AlphaDict, FrozenOrderedDict, NonelessDict, NonelessOrderedDict, bdict, frozendict


def takes_alphadict(a: AlphaDict[str, int]):
	a.keys()
	a.items()
	a.values()
	for k, v in a.items():
		print(k, v)


def takes_bdict(b: "bdict[str, str]"):
	b.keys()
	b.items()
	b.values()
	for k, v in b.items():
		print(k, v)


def takes_frozendict(f: frozendict[str, int]):
	f.keys()
	f.items()
	f.values()
	for k, v in f.items():
		print(k, v)


def takes_frozenordereddict(f: FrozenOrderedDict[str, Optional[int]]):
	f.keys()
	f.items()
	f.values()
	for k, v in f.items():
		print(k, v)


def takes_nonelessdict(n: NonelessDict[str, int]):
	n.keys()
	n.items()
	n.values()
	for k, v in n.items():
		print(k, v)


def takes_nonelessordereddict(n: NonelessOrderedDict[str, int]):
	n.keys()
	n.items()
	n.values()
	for k, v in n.items():
		print(k, v)
