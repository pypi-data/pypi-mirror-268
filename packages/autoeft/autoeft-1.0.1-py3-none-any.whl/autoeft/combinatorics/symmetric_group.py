import itertools
from collections import Counter
from collections import defaultdict
from math import prod
from typing import Counter as Count
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple

import sage.all
import sage.combinat.permutation
import sage.combinat.sf.sf
import sage.combinat.skew_tableau
import sage.combinat.symmetric_group_algebra
import sage.groups.perm_gps.permgroup_named
import sage.matrix.constructor
from sage.libs.lrcalc import lrcalc
from sage.rings.rational_field import QQ

from autoeft import utils
from autoeft.combinatorics import generators
from autoeft.combinatorics import young


def lr_rule(
    lhs: young.Partition,
    rhs: young.Partition,
    N: Optional[int],
    factor: int = 1,
) -> Count[young.Partition]:
    """Interface to SageMath's Littlewood-Richardson rule."""
    return +Counter(
        {
            young.Partition(p): int(c * factor)
            for p, c in lrcalc.mult(lhs, rhs, N).items()
        },
    )


def multi_lr_rule(
    partitions: Iterable[young.Partition],
    N: Optional[int],
    initials: Optional[Count[young.Partition]] = None,
) -> Count[young.Partition]:
    it = iter(partitions)
    try:
        rhs = next(it)
    except StopIteration:
        return Counter(initials)
    if initials is None:
        initials = Counter({young.Partition([]): 1})
    result = Counter()
    for lhs, coeff in initials.items():
        result.update(lr_rule(lhs, rhs, N, coeff))
    return +multi_lr_rule(it, N, result)


def lr_skew_tableaux(
    outer: young.Partition,
    inner: young.Partition,
    weight: young.Partition,
) -> List[young.Tableau]:
    """Return all Littlewood-Richardson tableaux.

    A Littlewood-Richardson tableau is a semistandard skew tableau
    of shape outer/inner and the given weight
    which is also a valid lattice permutation.
    """
    SSSYTx = sage.combinat.skew_tableau.SemistandardSkewTableaux_shape_weight
    return sorted(
        young.Tableau(skew_tableau)
        for skew_tableau in SSSYTx([outer, inner], weight)
        if skew_tableau.to_word().is_yamanouchi()
    )


def plethysm(lhs: young.Partition, rhs: young.Partition) -> Count[young.Partition]:
    """Interface to SageMath's implementation of the plethysm.

    The order matches the definition of the plethysm operation given in
    arXiv:2005.00008 [hep-ph],
    i.e., lhs * rhs = rhs(lhs).
    """
    if not lhs:
        return Counter({young.Partition(): 1})
    schur = sage.combinat.sf.sf.SymmetricFunctions(QQ).s()
    return +Counter({young.Partition(p): c for p, c in schur[rhs].plethysm(schur[lhs])})


def direct_product_decomposition(
    lhs: young.Partition,
    rhs: young.Partition,
    n: int,
    factor: int = 1,
) -> Count[young.Partition]:
    return multi_direct_product_decomposition([lhs, rhs], n, factor)


def multi_direct_product_decomposition(
    partitions: Iterable[young.Partition],
    n: int,
    factor: int = 1,
) -> Count[young.Partition]:
    SG = sage.groups.perm_gps.permgroup_named.SymmetricGroup(n)
    order = SG.order()
    character_table = SG.character_table()
    representations = {
        young.Partition(cc.partition()): i
        for i, cc in enumerate(SG.conjugacy_classes_iterator())
    }
    products = [representations[p] for p in partitions]
    return +Counter(
        {
            representation: sum(
                cc.cardinality()
                * character_table[lam, i]
                * prod(character_table[r, i] for r in products)
                for i, cc in enumerate(SG.conjugacy_classes_iterator())
            )
            * factor
            / order
            for representation, lam in representations.items()
        },
    )


def CGC(
    N: int,
    irrepr: young.Partition,
    j: int,
    i: int,
    decomp: List[Tuple[young.Partition, int]],
    vector: Tuple[int, ...],
) -> utils.Fraction:
    return sum(
        representation_matrix(irrepr, p).inverse()[j, i]
        * prod(representation_matrix(mu, p)[x, y] for (mu, x), y in zip(decomp, vector))
        for p in sage.combinat.permutation.StandardPermutations_n(N)
    ) / sage.combinat.symmetric_group_algebra.kappa(irrepr)


def construct_CGCs(
    N: int,
    partitions: List[young.Partition],
    target: young.Partition,
    multiplicity: int,
) -> sage.matrix.constructor.Matrix:
    basis = list(
        itertools.product(*(range(part.dimension_SN()) for part in partitions)),
    )
    vectors = []
    for vector1 in basis:
        vectors.append(
            [
                CGC(N, target, 0, 0, list(zip(partitions, vector2)), vector1)
                for vector2 in basis
            ],
        )
        if (matrix := sage.matrix.constructor.matrix(vectors)).rank() == multiplicity:
            return matrix[matrix.pivot_rows(), :], basis
    errmsg = "Not enough linear independent vectors found"
    raise RuntimeError(errmsg)


def join_CGCs(
    cgcs: Iterable[Count[Tuple[int, ...]]],
    initials: Optional[Count[Tuple[Tuple[int, ...], ...]]] = None,
) -> Count[Tuple[Tuple[int, ...], ...]]:
    it = iter(cgcs)
    try:
        rhs = next(it)
    except StopIteration:
        return Counter(initials)
    if initials is None:
        initials = Counter({(): 1})
    result = Counter()
    for lhs, coeff1 in initials.items():
        for vector, coeff2 in rhs.items():
            if not lhs:
                merged = tuple((entry,) for entry in vector)
            else:
                merged = tuple((*a, b) for a, b in zip(lhs, vector))
            result[merged] = coeff1 * coeff2
    return join_CGCs(it, result)


# cache representation matrices
representation_matrices: Dict[
    young.Partition,
    Dict[sage.combinat.permutation.Permutation, sage.matrix.constructor.Matrix],
] = defaultdict(dict)


def representation_matrix(
    irrepr: young.Partition,
    group_element: sage.combinat.permutation.Permutation,
) -> sage.matrix.constructor.Matrix:
    try:
        return representation_matrices[irrepr][group_element]
    except KeyError:
        D_reflection, D_cycle, D_cycle_I = generators.get_generators(irrepr)
        dim = irrepr.dimension_SN()
        matrix = prod(
            (
                D_cycle ** (i - 1) * D_reflection * D_cycle_I ** (i - 1)
                for i in group_element.reduced_word()
            ),
            start=sage.matrix.constructor.matrix.identity(QQ, dim),
        )
        representation_matrices[irrepr][group_element] = matrix
        return matrix
