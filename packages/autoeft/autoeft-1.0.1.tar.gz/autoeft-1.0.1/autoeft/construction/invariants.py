import itertools
from collections import Counter
from math import ceil
from math import floor
from typing import Counter as Count
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional

import sage.all
import sage.combinat.tableau

import autoeft.base.classifications as classes
import autoeft.base.groups as symmetry_groups
import autoeft.base.model as ir_model
import autoeft.combinatorics.symmetric_group as combinat
from autoeft import exceptions
from autoeft import utils
from autoeft.base import tensors


def modified_lr_rule(
    lhs: tensors.SUNTableau,
    rhs: tensors.SUNTableau,
    N: int,
) -> Iterator[tensors.SUNTableau]:
    """Modified Littlewood-Richardson rule.

    Return the product of two tableaux
    using a modified version of the Littlewood-Richardson rule.
    """
    for part, coeff in combinat.lr_rule(lhs.shape, rhs.shape, N).items():
        skew_tableaux = combinat.lr_skew_tableaux(part, lhs.shape, rhs.shape)
        assert len(skew_tableaux) == coeff
        for skew_tab in skew_tableaux:
            rhs_idx = [list(row) for row in rhs]
            yield tensors.SUNTableau(
                (
                    (
                        (
                            lhs[row, col]
                            if row < len(lhs) and col < len(lhs[row])
                            else rhs_idx[skew_tab[row, col] - 1].pop(0)
                        )
                        for col in range(row_len)
                    )
                    for row, row_len in enumerate(part)
                ),
            )


def multi_modified_lr_rule(
    tableaux: Iterable[tensors.SUNTableau],
    N: int,
    initials: Optional[Iterable[tensors.SUNTableau]] = None,
) -> Iterator[tensors.SUNTableau]:
    if initials is None:
        initials = [tensors.SUNTableau([])]
    it = iter(tableaux)
    try:
        rhs = next(it)
    except StopIteration:
        yield from initials
        return
    result = []
    for lhs in initials:
        result += list(modified_lr_rule(lhs, rhs, N))
    yield from multi_modified_lr_rule(it, N, result)


def construct_sun_tableaux(
    op_type: classes.Type,
    group: symmetry_groups.SUNGroup,
) -> List[tensors.SUNTableau]:
    """Return all tensors that transform in the invariant SU(N) representation.

    Raise 'NoContractionException' if no invariants are found.
    """
    partition = op_type.sun_partition(group)
    content = op_type.sun_content(group)
    if not partition and not any(content):
        return [tensors.SUNTableau()]
    tableaux = multi_modified_lr_rule(
        (
            tensors.SUNTableau.fill_tableau(field_repr, field_num)
            for field_num, field_repr in enumerate(content, start=1)
        ),
        group.N,
    )
    tableaux = sorted(tab for tab in tableaux if tab.shape == partition)
    if tableaux:
        return tableaux
    errmsg = group.name
    raise exceptions.NoContractionException(errmsg)  # no invariant contractions found


def construct_lorentz_tableaux(family: classes.Family) -> List[tensors.LorentzTableau]:
    """Return all Lorentz tableaux.

    Return all tensors for the given family that are Lorentz invariant
    and are not related to a total derivative.

    Raise 'NoContractionException' if no invariants are found.
    """
    partition = family.primary_partition()
    content = family.primary_content()
    if not partition and not any(content):
        return [tensors.LorentzTableau(0, 0)]
    assert sum(partition) == sum(content)
    SSYTx = sage.combinat.tableau.SemistandardTableaux
    tableaux = sorted(
        tensors.LorentzTableau(family.N, family.nr, tab)
        for tab in SSYTx(shape=partition, mu=content)
    )
    if tableaux:
        return tableaux
    errmsg = "Lorentz"
    raise exceptions.NoContractionException(errmsg)  # no invariant contractions found


def construct_types(
    family: classes.Family,
    model: ir_model.Model,
    hc_flag: bool = True,
) -> Iterator[classes.Type]:
    def _con_types(
        f_counts: Count[ir_model.Field],
        h_counts: Count[utils.Fraction],
        fields: List[ir_model.Field],
    ):
        if sum(h_counts.values()) == 0:  # all helicity slots are filled
            for name, group in model.symmetries.u1_groups.items():
                tot_charge = sum(
                    f.representations[name].charge * m for f, m in f_counts.items()
                )
                if abs(tot_charge - group.residual) > group.violation:
                    # reject operators with total charge greater than allowed violation
                    return
            for name, group in model.symmetries.sun_groups.items():
                tot_indices = sum(
                    sum(f.representations[name].partition) * m
                    for f, m in f_counts.items()
                )
                if tot_indices % group.N != 0:
                    # reject operators where the total number of SU(N) fundamental
                    # indices is not a multiple of N
                    return
            con_type = classes.Type(f_counts, family)
            if hc_flag or con_type.is_normal():
                yield con_type
        while fields:
            field = fields.pop(0)
            hel = field.helicity
            for nh in range(1, h_counts[hel] + 1):
                new_h_counts = h_counts.copy()
                new_h_counts[hel] -= nh
                new_f_counts = f_counts.copy()
                new_f_counts[field] += nh
                yield from _con_types(new_f_counts, new_h_counts, fields.copy())

    h_counts = Counter(
        dict(zip((utils.Fraction(h2, 2) for h2 in family.hel2), family.n_hel)),
    )
    yield from _con_types(Counter(), h_counts, list(model.fields.values()))


def _construct_families(
    N: int,
    nl: int,
    nr: int,
    hc_flag: bool = True,
) -> Iterator[classes.Family]:
    for nD in range(2 * min(nl, nr) + 1):
        for nFR in range(nr - ceil(nD / 2) + 1):
            for nFL in range(nl - ceil(nD / 2) + 1):
                nPsiD = 2 * nr - 2 * nFR - nD
                nPsi = 2 * nl - 2 * nFL - nD
                nPhi = N - nFR - nFL - nPsiD - nPsi
                n_hel = (nFL, nPsi, nPhi, nPsiD, nFR)
                fh2 = list(
                    itertools.chain.from_iterable(
                        itertools.repeat(h2, n)
                        for h2, n in zip((-2, -1, 0, 1, 2), n_hel)
                    ),
                )
                if (
                    all(nh >= 0 for nh in n_hel)
                    and nD >= max(nPsiD % 2, -nPsi % 2)
                    and nD >= -2 * min(fh2) - (2 * nFL + nPsi)
                    and nD >= 2 * max(fh2) - (2 * nFR + nPsiD)
                ):
                    con_family = classes.Family(n_hel, nD)
                    if hc_flag or con_family.is_normal():
                        yield con_family


def _construct_families_gr(
    N: int,
    nl: int,
    nr: int,
    nGR: int,
    hc_flag: bool = True,
) -> Iterator[classes.Family]:
    for nD in range(2 * min(nl, nr) + 1):
        for nCR in range(ceil(nr / 2 - nD / 4) + 1):
            nCL = nGR - nCR
            for nFR in range(nr - 2 * nCR - ceil(nD / 2) + 1):
                for nFL in range(nl - 2 * nCL - ceil(nD / 2) + 1):
                    nPsiD = 2 * nr - 4 * nCR - 2 * nFR - nD
                    nPsi = 2 * nl - 4 * nCL - 2 * nFL - nD
                    nPhi = N - nCR - nCL - nFR - nFL - nPsiD - nPsi
                    n_hel = (nCL, nFL, nPsi, nPhi, nPsiD, nFR, nCR)
                    fh2 = list(
                        itertools.chain.from_iterable(
                            itertools.repeat(h2, n)
                            for h2, n in zip((-4, -2, -1, 0, 1, 2, 4), n_hel)
                        ),
                    )
                    if (
                        all(nh >= 0 for nh in n_hel)
                        and nD >= max(nPsiD % 2, -nPsi % 2)
                        and nD >= -2 * min(fh2) - (4 * nCL + 2 * nFL + nPsi)
                        and nD >= 2 * max(fh2) - (4 * nCR + 2 * nFR + nPsiD)
                    ):
                        con_family = classes.FamilyGR(n_hel, nD)
                        if hc_flag or con_family.is_normal():
                            yield con_family


def construct_families(
    d: int,
    hc_flag: bool = True,
    gr_flag: bool = False,
) -> Iterator[classes.Family]:
    """Generate all families for the given dimension.

    The first elements corresponds to the so-called 'special kinematics',
    cf. arXiv:2005.00008 [hep-ph], p.16.
    """
    if not gr_flag:
        yield from _construct_families(3, d - 3, 0, hc_flag=hc_flag)
        if hc_flag:
            yield from _construct_families(3, 0, d - 3, hc_flag=hc_flag)
        for N in range(4, d + 1):
            bound_r = (d - N) if hc_flag else floor((d - N) / 2)
            for nr in range(bound_r + 1):
                yield from _construct_families(N, d - N - nr, nr, hc_flag=hc_flag)
    else:
        for nGR in range(floor(min(d / 2, 3)) + 1):
            yield from _construct_families_gr(3, d - 3 + nGR, 0, nGR, hc_flag=hc_flag)
            if hc_flag:
                yield from _construct_families_gr(
                    3,
                    0,
                    d - 3 + nGR,
                    nGR,
                    hc_flag=hc_flag,
                )
        for N in range(4, d + 1):
            for nGR in range(floor(min(d / 2, N)) + 1):
                bound_r = (d - N + nGR) if hc_flag else floor((d - N + nGR) / 2)
                for nr in range(bound_r + 1):
                    yield from _construct_families_gr(
                        N,
                        d - N - nr + nGR,
                        nr,
                        nGR,
                        hc_flag=hc_flag,
                    )
