from vizibridge._vizibridge import DNA as rust_DNA
import re
from typing import Iterator, Self

non_CGTA = re.compile("[^ACGT]")

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

    def enum_canonical_kmer(self, k: int):
        return getattr(self.data, f"enumerate_canonical_kmer{k}")()
