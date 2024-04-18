import json
import re
from typing import ClassVar
from typing import Dict
from typing import Optional

import pydantic
import rich.table
import rich.text

import autoeft
import autoeft.base.groups as symmetry_groups
import autoeft.base.representations as reprs
from autoeft import utils
from autoeft.tex import tex


class Symmetries(pydantic.BaseModel, frozen=True, extra=pydantic.Extra.forbid):
    """A collection of the Lorentz, SU(N) and U(1) symmetries."""

    lorentz_group: symmetry_groups.LorentzGroup = symmetry_groups.LorentzGroup()
    sun_groups: Dict[str, symmetry_groups.SUNGroup] = {}
    u1_groups: Dict[str, symmetry_groups.U1Group] = {}

    def __hash__(self):
        return hash(
            (self.lorentz_group, frozenset(self.sun_groups), frozenset(self.u1_groups)),
        )

    def __eq__(self, other):
        if not isinstance(other, Symmetries):
            return False
        lor = self.lorentz_group == other.lorentz_group
        sun = self.sun_groups == other.sun_groups
        u1 = self.u1_groups == other.u1_groups
        order = tuple(self.sun_groups.keys()) == tuple(other.sun_groups.keys())
        return lor and sun and u1 and order

    def __getitem__(self, key):
        all_groups = {
            self.lorentz_group.name: self.lorentz_group,
            **self.sun_groups,
            **self.u1_groups,
        }
        return all_groups[key]

    def __iter__(self):
        all_groups = {
            self.lorentz_group.name: self.lorentz_group,
            **self.sun_groups,
            **self.u1_groups,
        }
        return iter(all_groups)

    def __tex__(self):
        return r" \otimes ".join(
            map(tex, (self.lorentz_group, *self.sun_groups.values())),
        )

    @pydantic.root_validator
    def check_ambiguity(cls, values):
        if {"lorentz_group", "sun_groups", "u1_groups"} <= values.keys():
            names = [values["lorentz_group"].name]
            names += list(values["sun_groups"])
            names += list(values["u1_groups"])
            if len(names) != len(set(names)):
                errmsg = (
                    f"Duplicate group names are not allowed: '{names}'."
                    "\n"
                    "Please make sure each group name is unique."
                )
                raise ValueError(errmsg)
        return values

    @pydantic.validator("sun_groups", pre=True)
    def parse_sun_groups(cls, v):
        return {
            name: symmetry_groups.SUNGroup(name=name, **data)
            for name, data in v.items()
        }

    @pydantic.validator("u1_groups", pre=True)
    def parse_u1_groups(cls, v):
        return {
            name: symmetry_groups.U1Group(name=name, **data) for name, data in v.items()
        }


FieldName = pydantic.constr(
    regex=(
        rf"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9{re.escape(autoeft.conjugation_symbol)}]$"
        r"|^[a-zA-Z]$"
    ),
)


class Field(pydantic.BaseModel, frozen=True, extra=pydantic.Extra.forbid):
    """Represent a field by its quantum numbers and representations.

    This class holds all information of a field provided in the model file.
    """

    name: FieldName
    generations: pydantic.PositiveInt = 1
    symmetries: Symmetries
    representations: Dict[str, reprs.Repr]
    conjugate: Optional[bool] = None
    anticommute: Optional[bool] = None
    tex: Optional[str] = None
    tex_hc: Optional[str] = None

    def __str__(self):
        return self.name

    def __tex__(self):
        return self.tex or rf"\mathtt{{{self.name}}}"

    def __rich__(self):
        return rich.text.Text(str(self), "bold")

    def __hash__(self):
        return hash(self.name)

    @pydantic.validator("name")
    def parse_name(cls, v):
        if v == "D":
            errmsg = f"{v} is a reserved name"
            raise ValueError(errmsg)
        return v

    @pydantic.validator("tex", always=True)
    def parse_tex(cls, v, values):
        if "name" in values:
            name = values["name"]
            return v or rf"\mathtt{{{name}}}"
        return v

    @pydantic.validator("tex_hc", always=True)
    def parse_tex_hc(cls, v, values):
        if {"tex", "conjugate"} <= values.keys():
            tex = values["tex"]
            return v or rf"{{{tex}}}^\dagger" if values["conjugate"] else tex
        return v

    @pydantic.validator("representations", pre=True)
    def parse_representations(cls, v, values):
        representations = {}
        if "symmetries" in values:
            lorentz_group = values["symmetries"].lorentz_group
            representations[lorentz_group.name] = reprs.LorentzRepr(
                helicity=v.get(lorentz_group.name, 0),
            )
            representations.update(
                {
                    name: reprs.SUNRepr(N=group.N, partition=v.get(name, []))
                    for name, group in values["symmetries"].sun_groups.items()
                },
            )
            representations.update(
                {
                    name: reprs.U1Repr(charge=v.get(name, 0))
                    for name in values["symmetries"].u1_groups
                },
            )
        return representations

    @pydantic.validator("conjugate", always=True)
    def parse_conjugate(cls, v, values):
        if v is not None:
            return v
        if {"symmetries", "representations"} <= values.keys():
            lorentz_group = values["symmetries"].lorentz_group
            sun_groups = values["symmetries"].sun_groups
            u1_groups = values["symmetries"].u1_groups
            if values["representations"][lorentz_group.name].is_complex():
                return True
            pseudo_reals = 0
            for group_name in sun_groups:
                if values["representations"][group_name].is_complex():
                    return True
                if values["representations"][group_name].is_pseudo_real():
                    pseudo_reals += 1
            if pseudo_reals % 2:
                return True
            for group_name in u1_groups:
                if values["representations"][group_name].is_complex():
                    return True
            return False
        return v

    @pydantic.validator("anticommute", always=True)
    def parse_anticommute(cls, v, values):
        if {"symmetries", "representations"} <= values.keys():
            lorentz_group = values["symmetries"].lorentz_group
            helicity = values["representations"][lorentz_group.name].helicity
            return v if v is not None else helicity.denominator == 2
        return v

    @property
    def helicity(self) -> utils.Fraction:
        return self.representations[self.symmetries.lorentz_group.name].helicity

    def is_fermionic(self) -> bool:
        return self.helicity.denominator == 2

    def conjugated_name(self, conjugation_symbol: str = autoeft.conjugation_symbol):
        if self.name.endswith(conjugation_symbol):
            return self.name.rstrip(conjugation_symbol)
        return self.name + conjugation_symbol

    def hermitian_conjugated(self) -> "Field":
        """Return the hermitian conjugated field."""
        data = {}
        data["name"] = self.conjugated_name()
        data["tex"], data["tex_hc"] = self.tex_hc, self.tex
        data["representations"] = {
            group: sym_repr.conjugated()
            for group, sym_repr in self.representations.items()
        }
        return self.copy(update=data)


class Model(pydantic.BaseModel):
    """Represents a model by its symmetries and fields.

    This class holds all information provided in the model file.
    """

    name: str
    description: Optional[str] = None
    symmetries: Symmetries
    fields: Dict[str, Field]

    def __str__(self):
        if self.description:
            return f"{self.name}: {self.description}"
        return self.name

    def __tex__(self):
        def ___tex__():
            lorentz_group = self.symmetries.lorentz_group
            sun_groups = self.symmetries.sun_groups
            u1_groups = self.symmetries.u1_groups
            c = "(+)"
            ac = "(-)"
            alignment = "lr" + "r" * (len(sun_groups) + len(u1_groups)) + "rc"
            yield rf"\begin{{longtable}}{{{alignment}}}"
            yield r"\toprule"
            top_row = f"Field & ${tex(lorentz_group)}$ & "
            if sun_groups:
                top_row += " & ".join(f"${tex(g)}$" for g in sun_groups.values())
                top_row += " & "
            if u1_groups:
                top_row += " & ".join(f"${tex(g)}$" for g in u1_groups.values())
                top_row += " & "
            top_row += r"$g$ & $\pm$ \\"
            yield top_row
            yield r"\midrule"
            for f in self.fields.values():
                field_row = f"${tex(f)}$ & ${f.representations[lorentz_group.name]}$ & "
                if sun_groups:
                    field_row += " & ".join(
                        f"${tex(f.representations[g])}$" for g in sun_groups
                    )
                    field_row += " & "
                if u1_groups:
                    field_row += " & ".join(
                        f"${tex(f.representations[g])}$" for g in u1_groups
                    )
                    field_row += " & "
                field_row += (
                    rf"${f.generations}$ & ${c if not f.anticommute else ac}$ \\"
                )
                yield field_row
            yield r"\bottomrule"
            yield r"\end{longtable}"

        return "\n".join(___tex__())

    def __rich__(self):
        lorentz_group = self.symmetries.lorentz_group
        sun_groups = self.symmetries.sun_groups
        u1_groups = self.symmetries.u1_groups
        table = rich.table.Table(
            title=self.name,
            caption=self.description,
            show_edge=False,
            row_styles=["", "dim"],
        )
        table.add_column("Field")
        table.add_column(lorentz_group, justify="right")
        for sun_group in sun_groups:
            table.add_column(sun_group, justify="right")
        for u1_group in u1_groups:
            table.add_column(u1_group, justify="right")
        table.add_column("g", justify="right")
        table.add_column("+/-", justify="center")
        for f in self.fields.values():
            table.add_row(
                f,
                f.representations[lorentz_group.name],
                *(f.representations[g] for g in sun_groups),
                *(f.representations[g] for g in u1_groups),
                str(f.generations),
                "(+)" if not f.anticommute else "(-)",
            )
        return table

    def __eq__(self, other):
        if not isinstance(other, Model):
            return False
        return self.symmetries == other.symmetries and self.dict() == other.dict()

    @pydantic.validator("fields", pre=True)
    def parse_fields(cls, v, values):
        fields = {}
        if "symmetries" in values:
            for name, data in v.items():
                if name in fields:
                    errmsg = (
                        f"Found multiple definitions for '{name}'"
                        "\nConsider setting the 'conjugate' option to 'False'"
                    )
                    raise ValueError(errmsg)
                fields[name] = field = Field(
                    name=name,
                    symmetries=values["symmetries"],
                    **data,
                )
                if field.conjugate:
                    hc_field = field.hermitian_conjugated()
                    if hc_field.name in fields:
                        errmsg = (
                            f"Found multiple definitions for '{hc_field.name}'."
                            "\nConsider setting the 'conjugate' option to 'False'"
                        )
                        raise ValueError(errmsg)
                    fields[hc_field.name] = hc_field
        return fields

    @classmethod
    def parse_json(cls, data) -> "Model":
        model_data = json.loads(data)
        lorentz_group = symmetry_groups.LorentzGroup(
            **model_data["symmetries"]["lorentz_group"],
        )
        sun_groups = {}
        for name, group in model_data["symmetries"]["sun_groups"].items():
            sun_groups[name] = symmetry_groups.SUNGroup(**group)
        u1_groups = {}
        for name, group in model_data["symmetries"]["u1_groups"].items():
            u1_groups[name] = symmetry_groups.U1Group(**group)
        del model_data["symmetries"]
        symmetries = Symmetries.construct(
            lorentz_group=lorentz_group,
            sun_groups=sun_groups,
            u1_groups=u1_groups,
        )
        fields = {}
        for name, field in model_data["fields"].items():
            representations = {}
            for group, representation in field["representations"].items():
                if group == symmetries.lorentz_group.name:
                    representations[group] = representation["helicity"]
                elif group in symmetries.sun_groups:
                    representations[group] = representation["partition"]
                elif group in symmetries.u1_groups:
                    representations[group] = representation["charge"]
            del field["representations"]
            fields[name] = Field(
                **field,
                symmetries=symmetries,
                representations=representations,
            )
        del model_data["fields"]
        return cls.construct(**model_data, symmetries=symmetries, fields=fields)

    class Config:
        extra = pydantic.Extra.forbid
        json_dumps = utils.non_redundant_json
        json_encoders: ClassVar[dict] = {utils.Fraction: utils.Fraction.encode}


def main(args=None):
    import importlib.resources
    import sys

    import autoeft

    try:
        if sys.version_info >= (3, 9):
            sample = (
                importlib.resources.files(autoeft.__program__)
                .joinpath("sm.yml")
                .read_text()
            )
        else:
            sample = importlib.resources.read_text(autoeft.__program__, "sm.yml")
    except FileNotFoundError:
        sample = "name: <sample-model>\nsymmetries: {}\nfields: {}\n"
    sys.stdout.write(sample)
    return 0
