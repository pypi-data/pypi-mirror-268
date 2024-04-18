import concurrent.futures
import itertools
import os
import re
from collections import Counter
from dataclasses import dataclass
from itertools import zip_longest
from typing import Callable
from typing import Counter as Count
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple

import sage.all
import sage.combinat.permutation
import sage.combinat.symmetric_group_algebra
import sage.matrix.constructor
import sage.modules.free_module_element
from sage.rings.rational_field import QQ

import autoeft
import autoeft.base.classifications as classes
import autoeft.base.groups as symmetry_groups
import autoeft.base.representations as reprs
from autoeft import utils
from autoeft.combinatorics import young
from autoeft.form import contract
from autoeft.form import form

eps_undotted_pattern = re.compile(r"^eps\((\d+)_\d+,(\d+)_\d+\)$")
eps_dotted_pattern = re.compile(
    rf"^eps\((\d+)_\d+{re.escape(autoeft.epsilon_dot_symbol)}"
    rf",(\d+)_\d+{re.escape(autoeft.epsilon_dot_symbol)}\)$",
)
eps_pattern = re.compile(r"^eps\((.*)\)$")


_Permutations = sage.combinat.permutation.Permutations()


# Lorentz structures


class LorentzTensor(utils.Vector):
    def symmetrize(self, symmetrizer: Counter) -> "LorentzTensor":
        res = sum(
            (coeff * tab.symmetrized(symmetrizer) for tab, coeff in self.items()),
            start=LorentzTensor(),
        )
        self.clear()
        self.update(res)
        return self

    def reduction(
        self,
        basis: List["LorentzTableau"],
        N: int,
        n_split: int,
    ) -> "LorentzTensor":
        coeffs = Counter()
        for tab, factor in self.items():
            lr_tab, lr_sign = tab.to_lr_tableau()
            coeffs.update(ibp_reduction(lr_tab, lr_sign * factor))
        comb = LorentzTensor()
        for tab, coeff in coeffs.items():
            ten, lr_sign = tab.to_lorentz_tableau()
            comb[ten] = coeff * lr_sign
        # assert that every tableau is reduced to a combination of SSYTx only
        assert set(comb) <= set(basis)
        return comb


class LorentzTableau(young.Tableau):
    N: int
    n_split: int

    def __new__(cls, _, __, tableau: Optional[Iterable[Iterable]] = None):
        if tableau:
            return super().__new__(
                cls,
                ((int(index) for index in row) for row in tableau),
            )
        return super().__new__(cls, tableau)

    def __init__(self, N: int, n_split: int, _=None):
        self.N = N
        self.n_split = n_split

    @property
    def sign(self):
        _, lr_sign = self.to_lr_tableau()
        return lr_sign

    @property
    def undotted_indices(self) -> Counter:
        lr_tab, _ = self.to_lr_tableau()
        return lr_tab.undotted_indices

    @property
    def dotted_indices(self) -> Counter:
        lr_tab, _ = self.to_lr_tableau()
        return lr_tab.dotted_indices

    def permuted(self, perm: Tuple[int, ...]) -> "LorentzTableau":
        perm_map = dict(zip(sorted(perm), perm))
        return LorentzTableau(
            self.N,
            self.n_split,
            ((perm_map.get(index, index) for index in row) for row in self),
        )

    def symmetrized(self, symmetrizer: Counter) -> LorentzTensor:
        return sum(
            (
                LorentzTensor({self.permuted(perm): coeff})
                for perm, coeff in symmetrizer.items()
            ),
            start=LorentzTensor(),
        )

    def to_lr_tableau(self) -> Tuple["LRTableau", int]:
        l_tab = self[:, self.n_split :]
        r_tab_c = self[:, : self.n_split]
        c_columns, lc_sign = [], 1
        for column in reversed(r_tab_c.transposed()):
            c_columns.append(
                c_column := [i for i in range(1, self.N + 1) if i not in column],
            )
            lc_sign *= _Permutations(list(column) + c_column).sign()
        r_tab = young.Tableau(row for row in zip(*c_columns))
        return LRTableau(self.N, l_tab, r_tab), lc_sign

    def render_eps(self, prefix: str = "") -> str:
        lr_tab, _ = self.to_lr_tableau()
        return lr_tab.render_eps(prefix=prefix)

    def render_tableau(self, op_type: classes.Type, extra_sign: int = 1) -> str:
        sign = "+" if self.sign * extra_sign == 1 else "-"
        tensor = self.render_eps() or "1"
        fields = []
        field_num = 0
        for f, m in op_type:
            for i in range(1, m + 1):
                n_undotted = self.undotted_indices[field_num + i]
                n_dotted = self.dotted_indices[field_num + i]
                nD = min(n_undotted, n_dotted)
                if nD == 1:
                    field = f"(D {f.name})"
                elif nD > 1:
                    field = f"(D^{nD} {f.name})"
                else:
                    field = f.name
                if n_undotted or n_dotted:
                    undotted = [f"{field_num+i}_{j}" for j in range(1, n_undotted + 1)]
                    dotted = [
                        f"{field_num+i}_{j}{autoeft.epsilon_dot_symbol}"
                        for j in range(1, n_dotted + 1)
                    ]
                    field_indices = ",".join(undotted + dotted)
                    field += f"({field_indices})"
                fields.append(field)
            field_num += m
        fields = "*".join(fields)
        return sign + tensor + " * " + fields

    def render_eps_tex(self, lorentz_group: symmetry_groups.LorentzGroup) -> str:
        lr_tab, _ = self.to_lr_tableau()
        return lr_tab.render_eps_tex(lorentz_group)

    def render_tableau_tex(
        self,
        op_type: classes.Type,
        lorentz_group: symmetry_groups.LorentzGroup,
        extra_sign: int = 1,
    ) -> str:
        sign = "+" if self.sign * extra_sign == 1 else "-"
        tensor = self.render_eps_tex(lorentz_group) or "1"
        fields = []
        field_num = 0
        for f, m in op_type:
            for i in range(1, m + 1):
                n_undotted = self.undotted_indices[field_num + i]
                n_dotted = self.dotted_indices[field_num + i]
                nD = min(n_undotted, n_dotted)
                if nD == 1:
                    field = rf"(D\,{f.tex})"
                elif nD > 1:
                    field = rf"(D^{{{nD}}}\,{f.tex})"
                else:
                    field = f.tex
                if n_undotted or n_dotted:
                    undotted = ",".join(
                        lorentz_group.get_l_idx(field_num + i, j)
                        for j in range(1, n_undotted + 1)
                    )
                    dotted = ",".join(
                        lorentz_group.get_r_idx(field_num + i, j)
                        for j in range(1, n_dotted + 1)
                    )
                    field = f"{{{field}}}_{{{undotted}}}^{{{dotted}}}"
                fields.append(field)
            field_num += m
        fields = r"\,".join(fields)
        return rf"{sign} \, {tensor} \; {fields}"

    @classmethod
    def parse_tableau(cls, invariant: str) -> Tuple["LorentzTableau", int]:
        split_invariant = invariant.split(" * ")
        signed_tensor = split_invariant[0]
        fields = split_invariant[1]
        if signed_tensor == "+1":
            return LorentzTableau(0, 0), 1
        if signed_tensor == "-1":
            return LorentzTableau(0, 0), -1
        sign = signed_tensor[0]
        tensor = signed_tensor[1:]
        epsilons = tensor.split("*")
        left_tab = []
        right_tab = []
        for eps in epsilons:
            if match := eps_undotted_pattern.match(eps):
                left_tab.append(map(int, match.groups()))
            elif match := eps_dotted_pattern.match(eps):
                right_tab.append(map(int, match.groups()))
            else:
                errmsg = (
                    "Invalid Lorentz tensor."
                    "\n"
                    "Tensors must be a product of 'eps(i_j,k_l)'."
                    "\n"
                    f"{eps}"
                )
                raise ValueError(errmsg)
        N = len(fields.split("*"))
        lr_tab = LRTableau(
            N,
            young.Tableau(zip(*left_tab)),
            young.Tableau(zip(*right_tab)),
        )
        tab, lc_sign = lr_tab.to_lorentz_tableau()
        sign_map = {"+": 1, "-": -1}
        return tab, sign_map[sign] * lc_sign


@dataclass(frozen=True)
class LRTableau:
    N: int
    left_tableau: young.Tableau
    right_tableau: young.Tableau

    @property
    def nl(self):
        if self.left_tableau:
            return len(self.left_tableau[0])
        return 0

    @property
    def nr(self):
        if self.right_tableau:
            return len(self.right_tableau[0])
        return 0

    @property
    def undotted_indices(self) -> Counter:
        return Counter(index for row in self.left_tableau for index in row)

    @property
    def dotted_indices(self) -> Counter:
        return Counter(index for row in self.right_tableau for index in row)

    def to_lorentz_tableau(self) -> Tuple[LorentzTableau, int]:
        columns, lc_sign = [], 1
        for c_column in reversed(self.right_tableau.transposed()):
            columns.append(
                column := [i for i in range(1, self.N + 1) if i not in c_column],
            )
            lc_sign *= _Permutations(column + list(c_column)).sign()
        ltab = LorentzTableau(
            self.N,
            self.nr,
            (
                r_row + l_row
                for r_row, l_row in zip_longest(
                    zip(*columns),
                    self.left_tableau,
                    fillvalue=(),
                )
            ),
        )
        return ltab, lc_sign

    def normalized(self) -> Tuple["LRTableau", int]:
        def _normalized(tableau: young.Tableau) -> Tuple[young.Tableau, int]:
            normalized_tableau = tableau.to_lists()
            normalization_sign = 1
            for i, column in enumerate(tableau.transposed()):
                if column[0] == column[1]:
                    normalization_sign = 0
                elif column[0] > column[1]:
                    normalized_tableau[0][i], normalized_tableau[1][i] = (
                        tableau[1, i],
                        tableau[0, i],
                    )
                    normalization_sign *= -1
            return (
                young.Tableau(zip(*sorted(zip(*normalized_tableau)))),
                normalization_sign,
            )

        left_tableau, l_sign = _normalized(self.left_tableau)
        right_tableau, r_sign = _normalized(self.right_tableau)
        return LRTableau(self.N, left_tableau, right_tableau), l_sign * r_sign

    def is_sorted(self) -> bool:
        is_sorted_left = is_sorted_right = True
        if self.left_tableau:
            is_sorted_left = list(self.left_tableau[1]) == sorted(self.left_tableau[1])
        if self.right_tableau:
            is_sorted_right = list(self.right_tableau[1]) == sorted(
                self.right_tableau[1],
            )
        return is_sorted_left and is_sorted_right

    def schouten(self) -> Count["LRTableau"]:
        def _schouten(tableau: young.Tableau, c: int = 0) -> Count[young.Tableau]:
            cc = c + 1
            ccc = cc + 1
            if not tableau or cc >= len(tableau[0]):
                return Counter({tableau: 1})
            if tableau[0, c] < tableau[0, cc] and tableau[1, c] > tableau[1, cc]:
                result = Counter()
                result.update(
                    _schouten(
                        young.Tableau(
                            (
                                tableau[0],
                                (
                                    *tableau[1, :c],
                                    tableau[1, cc],
                                    tableau[1, c],
                                    *tableau[1, ccc:],
                                ),
                            ),
                        ),
                    ),
                )
                result.subtract(
                    _schouten(
                        young.Tableau(
                            (
                                (*tableau[0, :cc], tableau[1, cc], *tableau[0, ccc:]),
                                (
                                    *tableau[1, :c],
                                    tableau[0, cc],
                                    tableau[1, c],
                                    *tableau[1, ccc:],
                                ),
                            ),
                        ),
                    ),
                )
                return result
            return _schouten(tableau, cc)

        result = Counter()
        if self.is_sorted():
            return result
        left_tableaux = _schouten(self.left_tableau)
        right_tableaux = _schouten(self.right_tableau)
        for (l_tab, l_coeff), (r_tab, r_coeff) in itertools.product(
            left_tableaux.items(),
            right_tableaux.items(),
        ):
            result[LRTableau(self.N, l_tab, r_tab)] += l_coeff * r_coeff

        return result

    def ibp1(
        self,
        coeff: Optional[utils.Fraction] = None,
    ) -> Count["LRTableau"]:
        if coeff is None:
            coeff = utils.Fraction(1)
        result = Counter()
        l_tab, r_tab = self.left_tableau, self.right_tableau
        for i in range(2, self.N + 1):
            combination = list(
                itertools.product(l_tab.replaced(1, i), r_tab.replaced(1, i)),
            )
            for sl_tab, sr_tab in combination:
                result[LRTableau(self.N, sl_tab, sr_tab)] -= coeff / len(combination)
        return result

    def ibp2a(
        self,
        coeff: Optional[utils.Fraction] = None,
    ) -> Count["LRTableau"]:
        if coeff is None:
            coeff = utils.Fraction(1)
        result = Counter()
        l_tab, r_tab = self.left_tableau, self.right_tableau
        l_tab_T = list(zip(*l_tab))
        try:
            idx = l_tab_T.index((1, 2))
        except ValueError:
            pass
        else:
            for i in range(3, self.N + 1):
                l_tab_T[idx] = (1, i)
                sl_tab = young.Tableau(zip(*l_tab_T))
                sr_tabs = list(r_tab.replaced(2, i))
                for sr_tab in sr_tabs:
                    result[LRTableau(self.N, sl_tab, sr_tab)] -= coeff / len(sr_tabs)
        return result

    def ibp2b(
        self,
        coeff: Optional[utils.Fraction] = None,
    ) -> Count["LRTableau"]:
        if coeff is None:
            coeff = utils.Fraction(1)
        result = Counter()
        l_tab, r_tab = self.left_tableau, self.right_tableau
        r_tab_T = list(zip(*r_tab))
        try:
            idx = r_tab_T.index((1, 2))
        except ValueError:
            pass
        else:
            for i in range(3, self.N + 1):
                r_tab_T[idx] = (1, i)
                sr_tab = young.Tableau(zip(*r_tab_T))
                sl_tabs = list(l_tab.replaced(2, i))
                for sl_tab in sl_tabs:
                    result[LRTableau(self.N, sl_tab, sr_tab)] -= coeff / len(sl_tabs)
        return result

    def ibp3a(
        self,
        coeff: Optional[utils.Fraction] = None,
    ) -> Count["LRTableau"]:
        if coeff is None:
            coeff = utils.Fraction(1)
        result = Counter()
        l_tab, r_tab = self.left_tableau, self.right_tableau
        l_tab_T, r_tab_T = list(zip(*l_tab)), list(zip(*r_tab))
        try:
            l_idx = l_tab_T.index((1, 3))
            r_idx = r_tab_T.index((2, 3))
        except ValueError:
            pass
        else:
            for i in range(4, self.N + 1):
                l_tab_T[l_idx] = (1, i)
                sl_tab = young.Tableau(zip(*l_tab_T))
                r_tab_T[r_idx] = (2, i)
                sr_tab = young.Tableau(zip(*r_tab_T))
                result[LRTableau(self.N, sl_tab, sr_tab)] -= coeff
        return result

    def ibp3b(
        self,
        coeff: Optional[utils.Fraction] = None,
    ) -> Count["LRTableau"]:
        if coeff is None:
            coeff = utils.Fraction(1)
        result = Counter()
        l_tab, r_tab = self.left_tableau, self.right_tableau
        l_tab_T, r_tab_T = list(zip(*l_tab)), list(zip(*r_tab))
        try:
            r_idx = r_tab_T.index((1, 3))
            l_idx = l_tab_T.index((2, 3))
        except ValueError:
            pass
        else:
            for i in range(4, self.N + 1):
                r_tab_T[r_idx] = (1, i)
                sr_tab = young.Tableau(zip(*r_tab_T))
                l_tab_T[l_idx] = (2, i)
                sl_tab = young.Tableau(zip(*l_tab_T))
                result[LRTableau(self.N, sl_tab, sr_tab)] -= coeff
        return result

    def ibp4(
        self,
        coeff: Optional[utils.Fraction] = None,
    ) -> Count["LRTableau"]:
        if coeff is None:
            coeff = utils.Fraction(1)
        result = Counter()
        l_tab, r_tab = self.left_tableau, self.right_tableau
        l_tab_T, r_tab_T = list(zip(*l_tab)), list(zip(*r_tab))
        try:
            l_idx = l_tab_T.index((2, 3))
            r_idx = r_tab_T.index((2, 3))
        except ValueError:
            pass
        else:
            for i in range(2, self.N + 1):
                for j in range(max(4, i + 1), self.N + 1):
                    l_tab_T[l_idx] = (i, j)
                    sl_tab = young.Tableau(zip(*l_tab_T))
                    r_tab_T[r_idx] = (i, j)
                    sr_tab = young.Tableau(zip(*r_tab_T))
                    result[LRTableau(self.N, sl_tab, sr_tab)] -= coeff
        return result

    def render_eps(self, prefix: str = "") -> str:
        def _index(index, counter):
            counter[index] += 1
            return counter[index]

        def _render_index(index, index_num):
            if prefix:
                return f"{prefix}_{index}_{_index(index,index_num)}"
            return f"{index}_{_index(index,index_num)}"

        index_num = Counter()
        undotted = [
            "eps(" + ",".join(_render_index(index, index_num) for index in column) + ")"
            for column in self.left_tableau.transposed()
        ]
        index_num.clear()
        dotted = [
            "eps("
            + ",".join(
                f"{_render_index(index,index_num)}{autoeft.epsilon_dot_symbol}"
                for index in column
            )
            + ")"
            for column in self.right_tableau.transposed()
        ]
        return "*".join(undotted + dotted)

    def render_eps_tex(self, lorentz_group: symmetry_groups.LorentzGroup) -> str:
        def _index(index, counter):
            counter[index] += 1
            return counter[index]

        def _render_index(index, index_num, dot: bool):
            if dot:
                return lorentz_group.get_r_idx(index, _index(index, index_num))
            return lorentz_group.get_l_idx(index, _index(index, index_num))

        index_num = Counter()
        undotted = [
            r"\epsilon^{"
            + " ".join(_render_index(index, index_num, dot=False) for index in column)
            + "}"
            for column in self.left_tableau.transposed()
        ]
        index_num.clear()
        dotted = [
            r"\epsilon_{"
            + " ".join(f"{_render_index(index,index_num,dot=True)}" for index in column)
            + "}"
            for column in self.right_tableau.transposed()
        ]
        return " ".join(undotted + dotted)


# SU(N) structures


class SUNTensor(utils.Vector):
    def __form__(self):
        return " + ".join(f"({coeff})*({form(tab)})" for tab, coeff in self.items())

    def symmetrize(self, symmetrizer: Counter, key: Callable) -> "SUNTensor":
        res = sum(
            (coeff * tab.symmetrized(symmetrizer, key) for tab, coeff in self.items()),
            start=SUNTensor(),
        )
        self.clear()
        self.update(res)
        return self

    def reduction(
        self,
        basis: List["SUNTableau"],
        group: symmetry_groups.SUNGroup,
        representations: List[reprs.SUNRepr],
        inverse_gram: Optional[sage.matrix.constructor.Matrix] = None,
    ) -> "SUNTensor":
        if not self:
            return SUNTensor()
        dim = len(basis)
        if not inverse_gram:
            inverse_gram = calculate_gram_matrix(
                basis,
                group,
                representations,
            ).inverse()
        it = (form(tab.symmetrize_sun_indices(representations)) for tab in basis)
        v = contract.contract_basis(form(self), it, group.N, dim)
        coeffs = sage.modules.free_module_element.vector(QQ, dim, v) * inverse_gram
        return SUNTensor(dict(zip(basis, coeffs)))


class SUNTableau(young.Tableau):
    def __form__(self) -> str:
        return "*".join(
            "e_(" + ",".join(f"F{index[0]}I{index[1]}" for index in column) + ")"
            for column in self.transposed()
        )

    def permuted(self, perm: Tuple[int, ...], key: Callable) -> "SUNTableau":
        perm_map = dict(zip(sorted(perm), perm))
        return SUNTableau((key(perm_map, index) for index in row) for row in self)

    def symmetrized(self, symmetrizer: Counter, key: Callable) -> SUNTensor:
        return sum(
            (
                SUNTensor({self.permuted(perm, key): coeff})
                for perm, coeff in symmetrizer.items()
            ),
            start=SUNTensor(),
        )

    def symmetrize_sun_indices(self, representations: List[reprs.SUNRepr]) -> SUNTensor:
        tensor = SUNTensor({self: 1})
        for field_num, field_repr in enumerate(representations, start=1):
            normal_tableau = field_repr.partition.normal_tableau()
            young_operator = sage.combinat.symmetric_group_algebra.e_hat(normal_tableau)
            algebra = young_operator.parent()
            young_operator_antipode = algebra.antipode(young_operator)
            symmetrizer = algebra.left_action_product(
                young_operator_antipode,
                young_operator,
            )
            index_symmetrizer = Counter(
                {
                    perm: utils.Fraction(
                        int(coeff.numerator()),
                        int(coeff.denominator()),
                    )
                    for perm, coeff in symmetrizer
                },
            )
            tensor.symmetrize(
                index_symmetrizer,
                key=lambda x, y: (y[0], x.get(y[1], y[1])) if field_num == y[0] else y,
            )
        return tensor

    def render_eps(self, prefix: str = "") -> str:
        def _render_index(index, index_num):
            if prefix:
                return f"{prefix}_{index}_{index_num}"
            return f"{index}_{index_num}"

        return "*".join(
            "eps("
            + ",".join(_render_index(index[0], index[1]) for index in column)
            + ")"
            for column in self.transposed()
        )

    def render_tableau(
        self,
        op_type: classes.Type,
        group_name: str,
        extra_sign: int = 1,
    ) -> str:
        sign = "+" if extra_sign == 1 else "-"
        tensor = self.render_eps() or "1"
        fields = []
        field_num = 0
        for f, m in op_type:
            for i in range(1, m + 1):
                field = f.name
                n = sum(f.representations[group_name].partition)
                if n:
                    field_indices = ",".join(
                        f"{field_num+i}_{j}" for j in range(1, n + 1)
                    )
                    field += f"({field_indices})"
                fields.append(field)
            field_num += m
        fields = "*".join(fields)
        return sign + tensor + " * " + fields

    def render_eps_tex(self, sun_group: symmetry_groups.SUNGroup) -> str:
        return " ".join(
            r"\epsilon^{"
            + " ".join(sun_group.get_idx(*index) for index in column)
            + "}"
            for column in self.transposed()
        )

    def render_tableau_tex(
        self,
        op_type: classes.Type,
        sun_group: symmetry_groups.SUNGroup,
        extra_sign: int = 1,
    ) -> str:
        sign = "+" if extra_sign == 1 else "-"
        tensor = self.render_eps_tex(sun_group) or "1"
        fields = []
        field_num = 0
        for f, m in op_type:
            for i in range(1, m + 1):
                field = f.tex
                n = sum(f.representations[sun_group.name].partition)
                if n:
                    field_indices = " ".join(
                        sun_group.get_idx(field_num + i, j) for j in range(1, n + 1)
                    )
                    field = f"{{{field}}}_{{{field_indices}}}"
                fields.append(field)
            field_num += m
        fields = r"\,".join(fields)
        return rf"{sign} \, {tensor} \; {fields}"

    @classmethod
    def parse_eps(cls, tensor: str) -> "SUNTableau":
        tab = []
        for eps in tensor.split("*"):
            if match := eps_pattern.match(eps):
                tab.append(
                    tuple(map(int, idx.split("_"))) for idx in match[1].split(",")
                )
            else:
                errmsg = (
                    "Invalid SU(N) tensor."
                    "\n"
                    "Tensors must be a product of 'eps(...)'."
                    "\n"
                    f"{eps}"
                )
                raise ValueError(errmsg)
        return cls(zip(*tab))

    @classmethod
    def parse_tableau(cls, invariant: str) -> Tuple["SUNTableau", int]:
        signed_tensor = invariant.split(" * ")[0]
        if signed_tensor == "+1":
            return SUNTableau(), 1
        if signed_tensor == "-1":
            return SUNTableau(), -1
        sign = signed_tensor[0]
        tensor = signed_tensor[1:]
        tab = cls.parse_eps(tensor)
        sign_map = {"+": 1, "-": -1}
        return tab, sign_map[sign]

    @classmethod
    def fill_tableau(cls, field_repr: reprs.SUNRepr, field_num: int) -> "SUNTableau":
        """Construct tableau of given shape with field indices in canonical ordering.

        The tableau is filled with increasing indices
        from left to right and top to bottom.
        """
        index_num = 0
        return cls(
            ((field_num, index_num := index_num + 1) for _ in range(row_len))
            for row_len in field_repr
        )


# combined structures


class CombinedTensor(utils.Vector):
    def render_term(self, op_type: classes.Type) -> str:
        def _render_tableaux(coeff: int, tableaux: CombinedTableaux):
            rendered, sign = tableaux.render_tableaux(op_type)
            return f"({coeff*sign}) * {rendered}"

        return " + ".join(
            _render_tableaux(coeff, tableaux) for tableaux, coeff in self.items()
        )


class CombinedTableaux(dict):
    def __hash__(self):
        return hash(frozenset(self.items()))

    def render_eps(self) -> str:
        return "*".join(
            tableau.render_eps(group) for group, tableau in self.items() if tableau
        )

    def render_tableaux(
        self,
        op_type: classes.Type,
    ) -> Tuple[str, int]:
        tensor = self.render_eps()
        lr_tab, lr_sign = None, 1
        fields = []
        field_num = 0
        for f, m in op_type:
            for i in range(1, m + 1):
                nD = 0
                field_indices = {}
                for group, tableau in self.items():
                    group_indices = []
                    if isinstance(tableau, LorentzTableau):
                        if not lr_tab:
                            lr_tab, lr_sign = tableau.to_lr_tableau()
                        n_undotted = lr_tab.undotted_indices[field_num + i]
                        n_dotted = lr_tab.dotted_indices[field_num + i]
                        nD = min(n_undotted, n_dotted)
                        undotted = [
                            f"{group}_{field_num+i}_{j}"
                            for j in range(1, n_undotted + 1)
                        ]
                        dotted = [
                            f"{group}_{field_num+i}_{j}{autoeft.epsilon_dot_symbol}"
                            for j in range(1, n_dotted + 1)
                        ]
                        group_indices = undotted + dotted
                    else:
                        n = sum(f.representations[group].partition)
                        group_indices = [
                            f"{group}_{field_num+i}_{j}" for j in range(1, n + 1)
                        ]
                    field_indices[group] = group_indices
                building_block = ""
                if nD == 1:
                    building_block = f"(D {f.name})"
                elif nD > 1:
                    building_block = f"(D^{nD} {f.name})"
                else:
                    building_block = f.name
                indices = ""
                indices = ";".join(
                    ",".join(group_indices)
                    for group_indices in field_indices.values()
                    if group_indices
                )
                if indices:
                    fields.append(f"{building_block}({indices})")
                else:
                    fields.append(building_block)
            field_num += m
        fields = "*".join(fields)
        return tensor + " * " + fields, lr_sign


# misc


def ibp_reduction(
    lr_tableau: LRTableau,
    coeff: Optional[utils.Fraction] = None,
) -> Count[LRTableau]:
    if coeff is None:
        coeff = utils.Fraction(1)
    result = Counter()
    lr_tab, lr_sign = lr_tableau.normalized()
    if not lr_sign * coeff:
        return result
    if ibp := lr_tab.ibp1():
        for tab, factor in ibp.items():
            result.update(ibp_reduction(tab, lr_sign * coeff * factor))
        return result
    if ibp := lr_tab.ibp2a():
        for tab, factor in ibp.items():
            result.update(ibp_reduction(tab, lr_sign * coeff * factor))
        return result
    if ibp := lr_tab.ibp2b():
        for tab, factor in ibp.items():
            result.update(ibp_reduction(tab, lr_sign * coeff * factor))
        return result
    if ibp := lr_tab.ibp3a():
        for tab, factor in ibp.items():
            result.update(ibp_reduction(tab, lr_sign * coeff * factor))
        return result
    if ibp := lr_tab.ibp3b():
        for tab, factor in ibp.items():
            result.update(ibp_reduction(tab, lr_sign * coeff * factor))
        return result
    if ibp := lr_tab.ibp4():
        for tab, factor in ibp.items():
            result.update(ibp_reduction(tab, lr_sign * coeff * factor))
        return result
    if schouten := lr_tab.schouten():
        for tab, factor in schouten.items():
            result.update(ibp_reduction(tab, lr_sign * coeff * factor))
        return result
    result[lr_tab] = lr_sign * coeff
    return result


def calculate_gram_matrix(
    basis: List[SUNTableau],
    group: symmetry_groups.SUNGroup,
    representations: List[reprs.SUNRepr],
    threads: Optional[int] = None,
) -> sage.matrix.constructor.Matrix:
    dim = len(basis)
    form_sbasis = [form(tab.symmetrize_sun_indices(representations)) for tab in basis]
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=threads or os.cpu_count(),
    ) as executor:
        matrix = list(
            executor.map(
                contract.contract_basis,
                (form(tab) for tab in basis),
                (form_sbasis[i:] for i in range(len(basis))),
                itertools.repeat(group.N),
                (dim - i for i in range(len(basis))),
            ),
        )
        return sage.matrix.constructor.matrix(
            QQ,
            dim,
            dim,
            lambda i, j: matrix[i][j - i] if i <= j else matrix[j][i - j],
        )
