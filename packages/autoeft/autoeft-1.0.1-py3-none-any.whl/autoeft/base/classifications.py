import itertools
from collections import Counter
from math import ceil
from math import floor
from pathlib import Path
from typing import Counter as Count
from typing import Dict
from typing import List
from typing import Tuple

import autoeft.base.groups as symmetry_groups
import autoeft.base.model as ir_model
import autoeft.base.representations as reprs
from autoeft.combinatorics import young
from autoeft.tex import tex


class Family(tuple):
    hel2 = (-2, -1, 0, 1, 2)
    _repr = ("FL", "psiL", "phi", "psiR", "FR", "D")
    _str = ("FL", "psiL", "phi", "psiR", "FR", "D")
    _tex = (
        r"F_{\mathrm{L}}",
        r"\psi_{\mathrm{L}}",
        r"\phi",
        r"\psi_{\mathrm{R}}",
        r"F_{\mathrm{R}}",
        r"D",
    )

    def __new__(cls, n_hel, nD):
        return super().__new__(cls, (*n_hel, nD))

    def __repr__(self):
        return "_".join(f"{m}{f}" for f, m in zip(self._repr, self) if m)

    def __str__(self):
        return " ".join(f"{f}({m})" for f, m in zip(self._str, self) if m)

    def __tex__(self):
        return " ".join(
            f"{{{f}}}^{{{m}}}" if m > 1 else f for f, m in zip(self._tex, self) if m
        )

    @property
    def n_hel(self) -> Tuple[int, ...]:
        return self[:-1]

    @property
    def nD(self) -> int:
        return self[-1]

    @property
    def N(self) -> int:
        return sum(self.n_hel)

    @property
    def nl(self) -> int:
        left = floor(len(self.n_hel) / 2)
        nl2 = sum(
            (abs(h2) * nh for h2, nh in zip(self.hel2[:left], self.n_hel[:left])),
            start=self.nD,
        )
        assert nl2 % 2 == 0
        return nl2 // 2

    @property
    def nr(self) -> int:
        right = ceil(len(self.n_hel) / 2)
        nr2 = sum(
            (abs(h2) * nh for h2, nh in zip(self.hel2[right:], self.n_hel[right:])),
            start=self.nD,
        )
        assert nr2 % 2 == 0
        return nr2 // 2

    @property
    def d(self) -> int:
        return self.N + self.nl + self.nr

    def tuple_repr(self) -> str:
        return "(" + ", ".join(str(nh) for nh in self.n_hel) + "; " + str(self.nD) + ")"

    def path(self) -> Path:
        return Path(ascii(self.N)) / f"{self!a}"

    def is_real(self) -> bool:
        """Return true if is equal to its own conjugate."""
        return list(self.n_hel) == list(reversed(self.n_hel))

    def is_complex(self) -> bool:
        """Return true if is unequal to its own conjugate."""
        return not self.is_real()

    def is_normal(self) -> bool:
        return list(self.n_hel) >= list(reversed(self.n_hel))

    def conjugated(self) -> "Family":
        return type(self)(reversed(self.n_hel), self.nD)

    def field_helicities2(self) -> List[int]:
        """Return a list of the doubled field helicities."""
        return list(
            itertools.chain.from_iterable(
                itertools.repeat(h2, nh) for h2, nh in zip(self.hel2, self.n_hel)
            ),
        )

    def primary_partition(self) -> young.Partition:
        """Return the primary partition.

        The primary partition is defined by the Young diagram with
        nr columns of length N - 2 and nl columns of length 2.
        """
        if self.N == 3 and self.nl == 0:
            return young.Partition([self.nr])
        return young.Partition([self.nl + self.nr] * 2 + [self.nr] * (self.N - 4))

    def primary_content(self) -> Tuple[int, ...]:
        return tuple(self.nr - h2 for h2 in self.field_helicities2())


class FamilyGR(Family):
    hel2 = (-4, -2, -1, 0, 1, 2, 4)
    _repr = ("CL", "FL", "psiL", "phi", "psiR", "FR", "CR", "D")
    _str = ("CL", "FL", "psiL", "phi", "psiR", "FR", "CR", "D")
    _tex = (
        r"C_{\mathrm{L}}",
        r"F_{\mathrm{L}}",
        r"\psi_{\mathrm{L}}",
        r"\phi",
        r"\psi_{\mathrm{R}}",
        r"F_{\mathrm{R}}",
        r"C_{\mathrm{R}}",
        r"D",
    )

    @property
    def nGR(self) -> int:
        return self.n_hel[0] + self.n_hel[-1]

    @property
    def d(self) -> int:
        return self.N + self.nl + self.nr - self.nGR


class Type(tuple):
    family: Family

    def __new__(
        cls,
        field_counts: Count[ir_model.Field],
        _,
    ):
        if field_counts is None:
            return super().__new__(cls)
        return super().__new__(
            cls,
            sorted(
                ((f, m) for f, m in field_counts.items() if m),
                key=lambda x: (
                    x[0].helicity,
                    x[0].name,
                ),
            ),
        )

    def __init__(
        self,
        _,
        family: Family,
    ) -> None:
        self.family = family

    def __repr__(self):
        return "_".join(f"{m}{f}" for f, m in self.with_deriv if m)

    def __str__(self):
        return " ".join(f"{f}({m})" for f, m in self.with_deriv if m)

    def __tex__(self):
        return " ".join(
            f"{{{tex(f)}}}^{{{m}}}" if m > 1 else f"{tex(f)}"
            for f, m in self.with_deriv
            if m
        )

    @property
    def nD(self) -> int:
        return self.family.nD

    @property
    def d(self) -> int:
        return self.family.d

    @property
    def with_deriv(self):
        return (*self, ("D", self.nD))

    def path(self, extension: str = "yml") -> Path:
        return Path(f"{self!a}.{extension}")

    def full_path(self, extension: str = "yml") -> Path:
        return self.family.path() / self.path(extension)

    def is_real(self) -> bool:
        """Return true if is equal to its own conjugate."""
        return self.family.is_real() and self == self.conjugated()

    def is_complex(self) -> bool:
        """Return true if is unequal to its own conjugate."""
        return not self.is_real()

    def is_normal(self) -> bool:
        if self.family.is_normal():
            if self.family.is_real():
                normal_form = tuple((f.name, m) for f, m in self)
                cnormal_form = tuple((f.name, m) for f, m in self.conjugated())
                return self.family.is_normal() and normal_form <= cnormal_form
            return True
        return False

    def conjugated(self) -> "Type":
        return type(self)(
            {f.hermitian_conjugated(): m for f, m in self},
            self.family.conjugated(),
        )

    def sun_partition(self, group: symmetry_groups.SUNGroup) -> young.Partition:
        total = sum(sum(f.representations[group.name]) * m for f, m in self)
        assert total % group.N == 0
        return young.Partition([total // group.N] * group.N)

    def sun_content(self, group: symmetry_groups.SUNGroup) -> List[reprs.SUNRepr]:
        return list(
            itertools.chain.from_iterable(
                itertools.repeat(f.representations[group.name], m) for f, m in self
            ),
        )

    def field_numbers(self) -> Dict[str, List[int]]:
        field_number = 1
        return {
            f.name: list(range(field_number, field_number := field_number + m))
            for f, m in self
        }

    def to_counter(self) -> Counter:
        return +Counter({str(f): m for f, m in self.with_deriv})

    @classmethod
    def from_counter(cls, field_content: Count[str], model: ir_model.Model) -> "Type":
        field_content = field_content.copy()
        nD = field_content.pop("D", 0)
        hel2_counts = Counter()
        field_counts = Counter()
        gr_flag = False
        for field_name, multiplicity in field_content.items():
            field = model.fields[field_name]
            hel2 = int(2 * field.helicity)
            hel2_counts[hel2] += multiplicity
            field_counts[field] += multiplicity
            if abs(hel2) == 4:
                gr_flag = True
        F = FamilyGR if gr_flag else Family
        assert set(hel2_counts) <= set(F.hel2)
        n_hel = (hel2_counts[hel2] for hel2 in F.hel2)
        family = F(n_hel, nD)
        return cls(field_counts, family)
