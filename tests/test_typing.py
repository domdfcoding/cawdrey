from typing import Optional

from cawdrey import AlphaDict, bdict, frozendict, FrozenOrderedDict, NonelessOrderedDict, NonelessDict


def takes_alphadict(a: AlphaDict[str, int]):
	a.keys()
	a.items()
	a.values()
	for k, v in a.items():
		print(k, v)
	pass


def takes_bdict(b: "bdict[str, str]"):
	b.keys()
	b.items()
	b.values()
	for k, v in b.items():
		print(k, v)
	pass


def takes_frozendict(f: frozendict[str, int]):
	f.keys()
	f.items()
	f.values()
	for k, v in f.items():
		print(k, v)
	pass


def takes_frozenordereddict(f: FrozenOrderedDict[str, Optional[int]]):
	f.keys()
	f.items()
	f.values()
	for k, v in f.items():
		print(k, v)
	pass


def takes_nonelessdict(n: NonelessDict[str, int]):
	n.keys()
	n.items()
	n.values()
	for k, v in n.items():
		print(k, v)
	pass


def takes_nonelessordereddict(n: NonelessOrderedDict[str, int]):
	n.keys()
	n.items()
	n.values()
	for k, v in n.items():
		print(k, v)
	pass
