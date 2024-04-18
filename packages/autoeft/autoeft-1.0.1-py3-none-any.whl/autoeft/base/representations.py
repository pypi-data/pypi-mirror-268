import re

import pydantic

from autoeft import utils
from autoeft.combinatorics import young


class Repr(pydantic.BaseModel):
    def __rich__(self):
        return str(self)

    def conjugated(self) -> "Repr":
        raise NotImplementedError

    def is_real(self) -> bool:
        return self == self.conjugated()

    def is_complex(self) -> bool:
        return self != self.conjugated()

    class Config:
        extra = pydantic.Extra.forbid


class LorentzRepr(Repr):
    """A representation of the Lorentz group.

    Characterized by the helicity h = j_r - j_l
    for a massless field in the (j_l, j_r) representation.
    """

    helicity: utils.Fraction

    def __str__(self):
        return str(self.helicity)

    def __rich__(self):
        return self.helicity

    def __bool__(self):
        return bool(self.helicity)

    @pydantic.validator("helicity")
    def parse_helicity(cls, v):
        if v not in (
            utils.Fraction(-2),
            utils.Fraction(-1),
            utils.Fraction(-1, 2),
            utils.Fraction(0),
            utils.Fraction(1, 2),
            utils.Fraction(1),
            utils.Fraction(2),
        ):
            errmsg = f"helicity can only be 0, +-1/2, +-1, or +-2, not {v}"
            raise ValueError(errmsg)
        return v

    def conjugated(self) -> "LorentzRepr":
        """Construct the hermitian conjugate representation."""
        return self.copy(update={"helicity": -self.helicity})


class SUNRepr(Repr):
    """A representation of an SU(N) group.

    Characterized by a SU(N) Young diagram.
    """

    N: pydantic.PositiveInt
    partition: young.Partition

    def __str__(self):
        return str(self.partition)

    def __rich__(self):
        return self.partition

    def __bool__(self):
        return bool(self.partition)

    def __iter__(self):
        return iter(self.partition)

    @pydantic.validator("partition", pre=True)
    def parse_partition(cls, v, values):
        if isinstance(v, (list, young.Partition)):
            if "N" in values and len(v) >= (N := values["N"]):
                errmsg = f"{v} is not a valid SU({N}) representation"
                raise ValueError(errmsg)
            return v
        if isinstance(v, tuple):
            dynkin = v
            if "N" in values and (len(dynkin) + 1) != (N := values["N"]):
                errmsg = f"{v} is not a valid SU({N}) representation"
                raise ValueError(errmsg)
            return young.Partition.from_dynkin(dynkin)
        if isinstance(v, str) and (result := re.match(r"^\((.*)\)$", v)):
            dynkin = list(map(int, result[1].split(",")))
            if "N" in values and (len(dynkin) + 1) != (N := values["N"]):
                errmsg = f"{v} is not a valid SU({N}) representation"
                raise ValueError(errmsg)
            return young.Partition.from_dynkin(dynkin)
        errmsg = f"{v} is not a valid SU(N) representation"
        raise ValueError(errmsg)

    def conjugated(self) -> "SUNRepr":
        """Construct the hermitian conjugate representation.

        This inverts the order of the Dynkin labels of the partition.
        """
        conj_part = young.Partition.from_dynkin(
            list(reversed(self.partition.to_dynkin(self.N))),
        )
        return self.copy(update={"N": self.N, "partition": conj_part})

    def is_real(self):
        dynkin = self.partition.to_dynkin(self.N)
        if dynkin == list(reversed(dynkin)):
            if (self.N + 2) % 4 == 0:
                return dynkin[int(self.N / 2 - 1)] % 2 == 0
            return True
        return False

    def is_pseudo_real(self) -> bool:
        return not self.is_complex() and not self.is_real()


class U1Repr(Repr):
    """A representation of a U(1) group.

    Characterized by a U(1) charge.
    """

    charge: utils.Fraction

    def __str__(self):
        return str(self.charge)

    def __rich__(self):
        return self.charge

    def __bool__(self):
        return bool(self.charge)

    def conjugated(self) -> "U1Repr":
        """Construct the hermitian conjugate representation."""
        return self.copy(update={"charge": -self.charge})
