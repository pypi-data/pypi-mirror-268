import itertools
import math
import string
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Counter
from typing import Dict
from typing import List
from typing import Literal
from typing import Tuple

import pydantic
import yaml

import autoeft
import autoeft.base.classifications as classes
import autoeft.base.model as ir_model
from autoeft import utils
from autoeft.base import tensors
from autoeft.combinatorics import young
from autoeft.tex import tex


class OperatorInfo(pydantic.BaseModel):
    model: ir_model.Model
    version: utils.Version = autoeft.version
    type: Tuple[Counter[str], Literal["real", "complex"]]
    generations: Counter[str]
    n_terms: pydantic.PositiveInt
    n_operators: pydantic.PositiveInt
    invariants: Dict[str, List[Tuple[young.Tableau, int]]]

    def __str__(self):
        return str(self.op_type)

    def __repr__(self):
        return repr(self.op_type)

    def __tex__(self):
        invariants_content = {}
        for group_name, invariants in self.invariants.items():
            group = self.model.symmetries[group_name]
            group_tex = tex(group)
            equations = "\\\\\n".join(
                rf"\mathcal{{O}}_{{{i}}}^{{{group_tex}}} = "
                + invariant[0].render_tableau_tex(self.op_type, group, invariant[1])
                for i, invariant in enumerate(invariants, start=1)
            )
            equation = f"\\begin{{gather}}\n{equations}\n\\end{{gather}}"
            invariants_content[f"${group_tex}$"] = f"\n{equation}"
        invariants_items = (
            rf"\item[{item}]{value}" for item, value in invariants_content.items()
        )
        content = {
            r"$\bullet$": (
                rf"$\mathcal{{N}}_{{\text{{terms}}}}={self.n_terms}"
                r"$\quad\&\quad"
                rf"$\mathcal{{N}}_{{\text{{operators}}}}={self.n_operators}$"
                f"\n\\hfill{{\\small type: \\textit{{{self.type[1]}}}}}"
            ),
            "invariants": "\\hfill\n"
            + "\n".join(
                (
                    r"\begin{description}",
                    *invariants_items,
                    r"\end{description}",
                ),
            ),
        }
        items = (rf"\item[{item}]{value}" for item, value in content.items())
        return "\n".join((r"\begin{description}", *items, r"\end{description}"))

    def __eq__(self, other) -> bool:
        if self.version.to_tuple() != other.version.to_tuple():
            return False
        if self.invariants != other.invariants:
            return False
        return self.dict(exclude={"version", "invariants"}) == other.dict(
            exclude={"version", "invariants"},
        )

    @pydantic.validator("version")
    def parse_version(cls, v):
        if not v.is_compatible(autoeft.version):
            errmsg = (
                f"The version {v} of the operator file is not compatible with"
                f" {autoeft.program} {autoeft.version}."
                "\n"
                f"Please make sure you have the latest version of {autoeft.program}"
                ", or obtain a compatible version of the file."
            )
            raise ValueError(errmsg)
        return v

    @pydantic.validator("invariants", pre=True)
    def parse_invariants(cls, v, values):
        invariants = defaultdict(list)
        if "model" in values:
            model = values["model"]
            lorentz_group = model.symmetries.lorentz_group
            for group_name, contractions in v.items():
                for contraction in contractions.values():
                    T = (
                        tensors.LorentzTableau
                        if group_name == lorentz_group.name
                        else tensors.SUNTableau
                    )
                    tab, sign = T.parse_tableau(contraction)
                    invariants[group_name].append((tab, sign))
        return invariants

    @property
    def op_type(self):
        return classes.Type.from_counter(self.type[0], self.model)

    @property
    def nD(self) -> int:
        return self.op_type.nD

    @property
    def d(self) -> int:
        return self.op_type.d

    @property
    def N(self):
        return self.op_type.family.N

    @property
    def nl(self):
        return self.op_type.family.nl

    @property
    def nr(self):
        return self.op_type.family.nr

    def is_real(self) -> bool:
        return self.op_type.is_real()

    def is_complex(self) -> bool:
        return self.op_type.is_complex()

    def path(self) -> Path:
        return self.op_type.full_path()

    def yaml_dict(self):
        operator_data = self.dict(
            exclude={"model", "invariants", "permutation_symmetries", "expanded"},
        )
        invariants_data = defaultdict(utils.BlockMap)
        for group_name, tableaux in self.invariants.items():
            for i, (tableau, sign) in enumerate(tableaux, start=1):
                if group_name == self.model.symmetries.lorentz_group.name:
                    invariants_data[group_name][f"O({group_name},{i})"] = (
                        tableau.render_tableau(self.op_type, sign)
                    )
                else:
                    invariants_data[group_name][f"O({group_name},{i})"] = (
                        tableau.render_tableau(self.op_type, group_name, sign)
                    )
        operator_data["invariants"] = invariants_data
        return operator_data

    def yaml(self):
        return yaml.dump(
            self.yaml_dict(),
            Dumper=utils.YamlDumper,
            sort_keys=False,
            default_flow_style=None,
            width=math.inf,
        )


class PermutationSymmetryInfo(pydantic.BaseModel):
    symmetry: Dict[str, young.Partition]
    n_terms: pydantic.PositiveInt
    n_operators: pydantic.PositiveInt
    matrix: utils.IntegerMatrix

    def __tex__(self):
        sym = (
            "$$"
            + r"\,,\quad".join(
                rf"\lambda_{{${utils.esc(f)}}}\sim{p}" for f, p in self.symmetry.items()
            )
            + "$$"
        )
        ext = (
            rf"$$\mathcal{{N}}_{{\text{{terms}}}}={self.n_terms}$$"
            r"\quad\&\quad"
            rf"$$\mathcal{{N}}_{{\text{{operators}}}}={self.n_operators}$$"
        )
        mat = "\\\\\n".join(
            " & ".join(str(entry) for entry in row) for row in self.matrix
        )
        mat = f"\\begin{{pmatrix}}\n{mat}\n\\end{{pmatrix}}"
        return (
            f"{sym}\n\\hfill{{\\small{ext}}}\n"
            f"\\begin{{gather}}\n\\mathcal{{K}}=\n{mat}\n\\end{{gather}}"
        )


class OperatorInfoPermutation(OperatorInfo):
    permutation_symmetries: List[PermutationSymmetryInfo]

    def __tex__(self):
        tex_fields = {
            utils.esc(f): tex(field) for f, field in self.model.fields.items()
        }
        content = (
            rf"\item {string.Template(tex(sym)).substitute(tex_fields)}"
            for sym in self.permutation_symmetries
        )
        items = "\n".join((r"\begin{itemize}", *content, r"\end{itemize}"))
        all_items = super().__tex__().split("\n")
        return "\n".join(
            (
                *all_items[:-1],
                r"\item[permutation symmetries]\hfill",
                items,
                all_items[-1],
            ),
        )

    @pydantic.validator("invariants", pre=True)
    def parse_invariants(cls, v, values):
        invariants = defaultdict(list)
        if "model" in values:
            model = values["model"]
            lorentz_group = model.symmetries.lorentz_group
            for group_name, contractions in v.items():
                for contraction in contractions.values():
                    if group_name == lorentz_group.name:
                        tab, sign = tensors.LorentzTableau.parse_tableau(contraction)
                        if not tab.is_ssyt():
                            errmsg = (
                                "Invalid tableau encountered in operator file."
                                "\n"
                                "Please make sure the file contains only Lorentz"
                                " structures that correspond to SSYTx."
                            )
                            raise ValueError(errmsg)
                        if sign != 1:
                            errmsg = (
                                "Invalid sign encountered in operator file."
                                "\n"
                                "Please make sure the file contains only Lorentz"
                                " structures that correspond to SSYTx."
                            )
                            raise ValueError(errmsg)
                    else:
                        tab, sign = tensors.SUNTableau.parse_tableau(contraction)
                        if sign != 1:
                            errmsg = (
                                "Invalid sign encountered in operator file."
                                "\n"
                                "Please make sure the file contains only SU(N)"
                                " structures with positive signs."
                            )
                            raise ValueError(errmsg)
                    invariants[group_name].append((tab, sign))
        return invariants

    @pydantic.validator("permutation_symmetries", pre=True)
    def parse_permutation_symmetries(cls, v, values):
        if "model" in values:
            model = values["model"]
            lorentz_group = model.symmetries.lorentz_group
            sun_groups = model.symmetries.sun_groups
            if v[0]["vector"].split(" * ") != [lorentz_group.name, *sun_groups.keys()]:
                errmsg = (
                    "Uncompatible tensor product encountered in operator file."
                    "\n"
                    "Please make sure the file contains the same order of symmetries"
                    " as the IR model."
                )
                raise ValueError(errmsg)
        return v[1:]

    def yaml_dict(self):
        operator_data = super().yaml_dict()
        permutations_data = [utils.BlockMap(vector=" * ".join(self.invariants.keys()))]
        for permutation_symmetry in self.permutation_symmetries:
            permutation_data = {
                "symmetry": utils.FlowMap(permutation_symmetry.symmetry),
            }
            permutation_data.update(permutation_symmetry.dict(exclude={"symmetry"}))
            permutations_data.append(permutation_data)
        operator_data["permutation_symmetries"] = permutations_data
        return operator_data

    def expanded(self) -> "OperatorInfoExpanded":
        return OperatorInfoExpanded.from_op_info_permutation(self)


@dataclass
class TermInfo:
    op_type: classes.Type
    symmetry: Dict[str, young.Partition]
    n_operators: pydantic.PositiveInt
    term: tensors.CombinedTensor
    operators: List[Tuple[int, ...]]

    def __str__(self):
        return self.term.render_term(self.op_type)


class ExpandedInfo(pydantic.BaseModel):
    symmetry: Dict[str, young.Partition]
    n_terms: pydantic.PositiveInt
    n_operators: pydantic.PositiveInt
    terms: List[tensors.CombinedTensor]
    operators: List[Tuple[int, ...]]


class OperatorInfoExpanded(OperatorInfo):
    expanded: List[ExpandedInfo]

    def __iter__(self):
        return iter(
            TermInfo(
                op_type=self.op_type,
                symmetry=ex_info.symmetry,
                n_operators=len(ex_info.operators),
                term=term,
                operators=ex_info.operators,
            )
            for ex_info in self.expanded
            for term in ex_info.terms
        )

    def yaml_dict(self):
        operator_data = super().yaml_dict()
        expanded_data = []
        for permutation_symmetry in self.expanded:
            permutation_data = {
                "symmetry": utils.FlowMap(permutation_symmetry.symmetry),
            }
            permutation_data.update(
                permutation_symmetry.dict(exclude={"symmetry", "terms", "operators"}),
            )
            permutation_data["terms"] = [
                term.render_term(self.op_type) for term in permutation_symmetry.terms
            ]
            permutation_data["operators"] = permutation_symmetry.operators
            expanded_data.append(permutation_data)
        operator_data["expanded"] = expanded_data
        return operator_data

    @classmethod
    def from_op_info_permutation(cls, op_info) -> "OperatorInfoExpanded":
        if isinstance(op_info, OperatorInfoPermutation):
            lengths = {
                group: len(tensors) for group, tensors in op_info.invariants.items()
            }
            expanded = []
            for permutation_symmetry in op_info.permutation_symmetries:
                gens = []
                for f, symmetry in permutation_symmetry.symmetry.items():
                    field = op_info.model.fields[f]
                    gens.append(
                        [
                            tab.flatten()
                            for tab in young.Partition(symmetry).semistandard_tableaux(
                                field.generations,
                            )
                        ],
                    )
                operators = [
                    tuple(index for indices in operator for index in indices)
                    for operator in itertools.product(*gens)
                ]
                terms = []
                for row in permutation_symmetry.matrix:
                    term = tensors.CombinedTensor()
                    for n, coeff in enumerate(row):
                        if coeff:
                            tabs = {}
                            term_coeff = 1
                            den = 1
                            for group in reversed(op_info.invariants):
                                tab, tab_coeff = op_info.invariants[group][
                                    (n // den) % lengths[group]
                                ]
                                tabs[group] = tab
                                term_coeff *= tab_coeff
                                den *= lengths[group]
                            term[tensors.CombinedTableaux(reversed(tabs.items()))] = (
                                coeff * term_coeff
                            )
                    terms.append(term)
                expanded.append(
                    ExpandedInfo.construct(
                        symmetry=permutation_symmetry.symmetry,
                        n_terms=permutation_symmetry.n_terms,
                        n_operators=permutation_symmetry.n_operators,
                        terms=terms,
                        operators=operators,
                    ),
                )
            return cls.construct(
                model=op_info.model,
                version=op_info.version,
                type=op_info.type,
                generations=op_info.generations,
                n_terms=op_info.n_terms,
                n_operators=op_info.n_operators,
                invariants=op_info.invariants,
                expanded=expanded,
            )
        raise NotImplementedError


class Basis(dict):
    model: ir_model.Model

    def __init__(self, model: ir_model.Model):
        super().__init__()
        self.model = model

    def __getitem__(self, key):
        if isinstance(key, (int, slice)):
            return list(self.values())[key]
        if isinstance(key, dict):
            op_type = classes.Type.from_counter(key, self.model)
            return self[op_type]
        if isinstance(key, classes.Type):
            return self[repr(key)]
        return super().__getitem__(key)
