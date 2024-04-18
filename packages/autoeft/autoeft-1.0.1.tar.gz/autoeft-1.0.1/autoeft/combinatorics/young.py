import itertools
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

import rich.text
import sage.all
import sage.combinat.partition
import sage.combinat.tableau

Composition = Tuple[int, ...]
Dynkin = List[int]


class Partition(tuple):
    """A partition of a non-negative integer n.

    Representet by a non-increasing tuple of positive integers with total sum n.
    """

    def __new__(cls, partition: Optional[Iterable[int]] = None):
        if partition is None:
            return super().__new__(cls)
        stripped_part = tuple(itertools.takewhile(lambda x: x > 0, partition))
        if not cls.is_partition(stripped_part):
            errmsg = f"{stripped_part} is not a valid partition"
            raise ValueError(errmsg)
        return super().__new__(cls, stripped_part)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"[{','.join(str(i) for i in self)}]"

    def __rich__(self):
        return rich.text.Text.assemble(
            ("[", "bold"),
            ",".join(str(i) for i in self),
            ("]", "bold"),
        )

    def dimension_SN(self) -> int:
        SYTx = sage.combinat.tableau.StandardTableaux_shape
        return SYTx(
            sage.combinat.partition._Partitions(self),  # noqa: SLF001
        ).cardinality()

    def dimension_SUN(self, max_entry: Optional[int] = None) -> int:
        SSYTx = sage.combinat.tableau.SemistandardTableaux
        if max_entry:
            return SSYTx(shape=self, max_entry=max_entry).cardinality()
        return SSYTx(shape=self).cardinality()

    def normal_tableau(self) -> "Tableau":
        num = 0
        return Tableau((num := num + 1 for _ in range(row_len)) for row_len in self)

    def standard_tableaux(self) -> List["Tableau"]:
        SYTx = sage.combinat.tableau.StandardTableaux_shape
        return sorted(
            Tableau(t)
            for t in SYTx(sage.combinat.partition._Partitions(self))  # noqa: SLF001
        )

    def semistandard_tableaux(self, max_entry: Optional[int] = None) -> List["Tableau"]:
        SSYTx = sage.combinat.tableau.SemistandardTableaux
        if max_entry:
            return sorted(Tableau(t) for t in SSYTx(shape=self, max_entry=max_entry))
        return sorted(Tableau(t) for t in SSYTx(shape=self))

    def to_dynkin(self, N: int) -> Dynkin:
        """Return the Dynkin labels corresponding to this partition.

        For a partition (p1, p2, p3, ..., pn) the corresponding
        Dynkin labels are [p1 - p2, p2 - p3, ..., pn-1 - pn].
        """
        extended_part = list(self) + [0] * (N - len(self))
        return [p1 - p2 for p1, p2 in zip(extended_part, extended_part[1:])]

    @classmethod
    def from_dynkin(cls, dynkin: Dynkin) -> "Partition":
        """Construct partition from Dynkin labels.

        For the Dynkin labels [l1, l2, l3, ..., ln] the corresponding
        partition is given by (l1 + l2 + l3 + ... + ln, l2 + l3 + ... + ln, ..., ln).
        """
        return cls(sum(dynkin[label:]) for label in range(len(dynkin)))

    @classmethod
    def partitions(cls, m: int) -> Iterator["Partition"]:
        yield from (Partition(p) for p in sage.combinat.partition.Partitions_n(m))

    @staticmethod
    def is_partition(partition: Iterable[int], n: Optional[int] = None) -> bool:
        """Check if given partition is valid.

        If n is given also check if its a partition of n.
        Allow positive entries only.
        """
        if any(x <= 0 for x in partition):
            return False
        if list(partition) != sorted(partition, reverse=True):
            return False
        if n is not None:
            return sum(partition) == n
        return True

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return cls(v)


class Tableau(tuple):
    """A tableau of given shape and content.

    Represented by a tuple of tuples containing arbitrary elements.
    """

    def __new__(cls, tableau: Optional[Iterable[Iterable]] = None):
        if tableau is None:
            return super().__new__(cls)
        return super().__new__(cls, (tuple(row) for row in tableau if row))

    def __contains__(self, item):
        if isinstance(item, int):
            return any(item in row for row in self)
        return super().__contains__(item)

    def __getitem__(self, key):
        err_msg = (
            "tableau indices must be an integer,"
            " two integers, a slice, or two slices,"
            f" not {type(key).__name__}"
        )
        if isinstance(key, int):
            return list(super().__getitem__(key))
        if isinstance(key, slice):
            return Tableau(super().__getitem__(key))
        if isinstance(key, tuple):
            if len(key) > 2:
                raise TypeError(err_msg)
            if isinstance(key[0], int) and isinstance(key[1], int):
                return super().__getitem__(key[0])[key[1]]
            if isinstance(key[0], int) and isinstance(key[1], slice):
                return list(super().__getitem__(key[0])[key[1]])
            if isinstance(key[0], slice) and isinstance(key[1], slice):
                return Tableau(row[key[1]] for row in super().__getitem__(key[0]))
            if isinstance(key[0], slice) and isinstance(key[1], int):
                if key[1] >= max(self.shape):
                    errmsg = "tuple index out of range"
                    raise IndexError(errmsg)
                return [
                    row[key[1]]
                    for row in super().__getitem__(key[0])
                    if key[1] < len(row)
                ]
        raise TypeError(err_msg)

    @property
    def shape(self) -> Partition:
        """Return the shape of the tableau."""
        return Partition(len(row) for row in self)

    def is_ssyt(self) -> bool:
        return sage.combinat.tableau.Tableau(self).is_semistandard()

    def transposed(self) -> "Tableau":
        """Return the transposed tableau."""
        return Tableau(self[:, c] for c in range(max(self.shape, default=0)))

    def to_lists(self) -> List[list]:
        return [list(row) for row in self]

    def replaced(self, element, replacement) -> Iterator["Tableau"]:
        for i, row in enumerate(self):
            for j, entry in enumerate(row):
                if entry == element:
                    tableau = self.to_lists()
                    tableau[i][j] = replacement
                    yield Tableau(tableau)

    def flatten(self) -> tuple:
        return tuple(entry for row in self for entry in row)
