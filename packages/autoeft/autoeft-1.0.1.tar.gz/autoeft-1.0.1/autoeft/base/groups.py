from typing import Optional
from typing import Tuple

import pydantic
import rich.text

from autoeft import utils

GroupName = pydantic.constr(regex=r"^[a-zA-Z][a-zA-Z0-9()]*[a-zA-Z0-9()]$|^[a-zA-Z]$")


class Group(pydantic.BaseModel):
    name: GroupName
    tex: Optional[str] = None

    def __str__(self):
        return self.name

    def __tex__(self):
        return self.tex

    def __rich__(self):
        return rich.text.Text(str(self), "bold")

    @pydantic.validator("tex", always=True)
    def parse_tex(cls, v, values):
        if "name" in values:
            name = values["name"]
            return v or rf"\mathtt{{{name}}}"
        return v

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid


class LorentzGroup(Group):
    """The universal covering group SL(2,CC) of the restricted Lorentz symmetry."""

    name: str = "Lorentz"
    indices: Tuple[str, ...] = (
        r"\alpha",
        r"\beta",
        r"\gamma",
        r"\delta",
        r"\varepsilon",
        r"\zeta",
        r"\eta",
        r"\theta",
        r"\iota",
        r"\kappa",
        r"\lambda",
    )

    def get_l_idx(self, i: int, j: int):
        """Return an undotted spinor index."""
        p = r"\prime"
        i = i - 1
        m = len(self.indices)
        idx = f"{self.indices[i % m]}_{{{j}}}"
        if repeat := i // m:
            return f"{idx}^{{{p*repeat}}}"
        return idx

    def get_r_idx(self, i: int, j: int):
        """Return a dotted spinor index."""
        p = r"\prime"
        i = i - 1
        m = len(self.indices)
        idx = rf"\dot{self.indices[i % m]}_{{{j}}}"
        if repeat := i // m:
            return f"{idx}^{{{p*repeat}}}"
        return idx


class SUNGroup(Group):
    """An SU(N) internal symmetry."""

    N: pydantic.conint(gt=1)
    indices: Tuple[str, ...] = tuple("abcdefghijk")

    def get_idx(self, i: int, j: int):
        """Return a symmetry/gauge index."""
        p = r"\prime"
        i = i - 1
        m = len(self.indices)
        idx = f"{self.indices[i % m]}_{{{j}}}"
        if repeat := i // m:
            return f"{idx}^{{{p*repeat}}}"
        return idx


class U1Group(Group):
    """A U(1) symmetry/gauge group."""

    violation: utils.Fraction = utils.Fraction(0)
    residual: utils.Fraction = utils.Fraction(0)
