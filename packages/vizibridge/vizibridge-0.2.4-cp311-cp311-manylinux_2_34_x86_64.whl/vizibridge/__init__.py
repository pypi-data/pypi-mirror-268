from vizibridge._vizibridge import DNA as rust_DNA
import vizibridge._vizibridge as rust_types

import re
from typing import Iterator, Self

__all__ = ["DNA", "Kmer"]

non_CGTA = re.compile("[^ACGT]")

Pykmers = [getattr(rust_types, a) for a in dir(rust_types) if a.startswith("PyKmer")]

KmerType = Pykmers[0]
for t in Pykmers[1:]:
    KmerType |= t

KmerTypeMap = {KT.size(): KT for KT in Pykmers}


class DNA:
    __slots__ = ("data",)

    def __init__(self, data: rust_DNA | str):
        if isinstance(data, str):
            self.data = rust_DNA(data)
        elif isinstance(data, rust_DNA):
            self.data = data
        else:
            raise TypeError(type(data))

    @classmethod
    def from_str(cls, seq: str) -> Iterator["DNA"]:
        yield from (cls(subseq) for subseq in non_CGTA.split(seq))

    def __iter__(self) -> Iterator[str]:
        for i in range(len(self.data)):
            self.data.get_index(i)

    def __getitem__(self, __key: int | slice) -> Self | str:
        if isinstance(__key, int):
            return self.data.get_index(__key)
        if isinstance(__key, slice):
            assert __key.step is None
            data = self.data.get_slice(__key.start, __key.stop)
            return type(self)(data)

        raise KeyError(__key)

    def __repr__(self):
        return repr(self.data)

    def __len__(self):
        return len(self.data)

    def enum_canonical_kmer(self, k: int) -> Iterator["Kmer"]:
        return map(
            lambda e: Kmer(e, k), getattr(self.data, f"enumerate_canonical_kmer{k}")()
        )

    def enum_kmer(self, k: int) -> Iterator["Kmer"]:
        return map(lambda e: Kmer(e, k), getattr(self.data, f"enumerate_kmer{k}")())


class Kmer:
    __slots__ = ("__data",)

    def __init__(self, data: KmerType | int, size: int | None = None):
        if isinstance(data, int):
            assert size
            data = KmerTypeMap[size](data)
        self.__data = data

    @property
    def size(self) -> int:
        return self.data.size()

    @property
    def data(self) -> int:
        return self.__data.data

    def __repr__(self):
        return repr(self.__data)

    def __str__(self):
        return str(self.__data)

    def __hash__(self):
        return hash(self.__data)

    def add_left_nucleotid(self, c: str) -> Self:
        return type(self)(self.__data.add_left_nucleotid(c))

    def add_right_nucleotid(self, c: str) -> Self:
        return type(self)(self.__data.add_right_nucleotid(c))

    def __lt__(self, other) -> bool:
        return self.__data < other.__data

    def __gt__(self, other) -> bool:
        return self.__data < other.__data
