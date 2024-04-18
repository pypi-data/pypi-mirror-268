import itertools
from collections import defaultdict
from typing import Counter as Count
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

import autoeft.base.classifications as classes
import autoeft.base.model as ir_model
import autoeft.combinatorics.symmetric_group as combinat
import autoeft.construction.symmetrizers as sym_reprs
from autoeft.combinatorics import young

GroupName = FieldName = str
DirectProduct = Dict[GroupName, Dict[FieldName, young.Partition]]
ProductDecomposition = Dict[FieldName, Count[young.Partition]]
ClebschGordanDecomposition = Dict[
    FieldName,
    Dict[young.Partition, List[Count[Tuple[int, ...]]]],
]


def construct_factorized_symmetries(
    direct_product: DirectProduct,
    product_decomposition: ProductDecomposition,
    clebsch_gordan_decomposition: ClebschGordanDecomposition,
) -> Iterator[
    Tuple[
        Dict[FieldName, young.Partition],
        Count[Tuple[sym_reprs.GroupSymmetrizer, ...]],
    ]
]:
    total_permutation_symmetries = (
        dict(zip(product_decomposition.keys(), symmetry))
        for symmetry in itertools.product(*product_decomposition.values())
    )
    for permutation_symmetry in total_permutation_symmetries:
        multiplicities = itertools.product(
            *(
                range(int(product_decomposition[field_name][permutation]))
                for field_name, permutation in permutation_symmetry.items()
            ),
        )
        for multiplicity in multiplicities:
            cgcs = (
                clebsch_gordan_decomposition[field_name][symmetry][j]
                for j, (field_name, symmetry) in zip(
                    multiplicity,
                    permutation_symmetry.items(),
                )
            )
            combination = {
                tuple(
                    sym_reprs.GroupSymmetrizer(
                        group_name,
                        tuple(
                            (field_name, group_permutation, entry)
                            for (field_name, group_permutation), entry in zip(
                                group_permutations.items(),
                                vector,
                            )
                        ),
                    )
                    for (group_name, group_permutations), vector in zip(
                        direct_product.items(),
                        vectors,
                    )
                ): cgc
                for vectors, cgc in combinat.join_CGCs(cgcs).items()
                if cgc
            }
            yield permutation_symmetry, combination


def construct_permutation_symmetries(
    op_type: classes.Type,
    allowed_group_permutations: Dict[GroupName, List[Dict[FieldName, young.Partition]]],
) -> Iterator[Tuple[DirectProduct, ProductDecomposition, ClebschGordanDecomposition]]:
    combined_permutations = (
        dict(zip(allowed_group_permutations.keys(), combined_permutation))
        for combined_permutation in itertools.product(
            *allowed_group_permutations.values(),
        )
    )
    for permutation in combined_permutations:
        field_permutations = defaultdict(dict)
        for group_name, allowed_permutation in permutation.items():
            for field_name, group_permutation in allowed_permutation.items():
                field_permutations[field_name][group_name] = group_permutation
        permutation_symmetry = {}
        clebsch_gordan_coefficients = defaultdict(dict)
        for f, m in op_type:
            partitions = list(field_permutations[f.name].values())
            if bool(f.anticommute) ^ bool(op_type.family.nr % 2):
                partitions.append(young.Partition([1] * m))
            targets = permutation_symmetry[f.name] = {
                symmetry: mult
                for symmetry, mult in combinat.multi_direct_product_decomposition(
                    partitions,
                    m,
                ).items()
                if len(symmetry) <= f.generations
            }
            for target, multiplicity in targets.items():
                matrix, basis = combinat.construct_CGCs(
                    m,
                    partitions,
                    target,
                    multiplicity,
                )
                if bool(f.anticommute) ^ bool(op_type.family.nr % 2):
                    basis = [vector[:-1] for vector in basis]
                clebsch_gordan_coefficients[f.name][target] = [
                    dict(zip(basis, vector)) for vector in matrix
                ]
        yield permutation, permutation_symmetry, clebsch_gordan_coefficients


def construct_group_permutations(
    op_type: classes.Type,
    symmetries: ir_model.Symmetries,
) -> Dict[GroupName, List[Dict[FieldName, young.Partition]]]:
    family = op_type.family
    lorentz_group = symmetries.lorentz_group
    sun_groups = symmetries.sun_groups
    targets = {}
    if target := family.primary_partition():
        targets[lorentz_group.name] = target
    for group_name, group in sun_groups.items():
        if target := op_type.sun_partition(group):
            targets[group_name] = target
    representations = defaultdict(dict)
    permutations = defaultdict(dict)
    for f, m in op_type:
        lorentz_repr = young.Partition([int(family.nr - 2 * f.helicity)])
        representations[lorentz_group.name][f.name] = lorentz_repr
        permutations[lorentz_group.name][f.name] = young.Partition.partitions(m)
        for group_name in sun_groups:
            sun_repr = f.representations[group_name].partition
            representations[group_name][f.name] = sun_repr
            permutations[group_name][f.name] = young.Partition.partitions(m)
    allowed_permutations = defaultdict(list)
    for group_name, target in targets.items():
        all_permutations = (
            dict(zip(permutations[group_name].keys(), permutation))
            for permutation in itertools.product(*permutations[group_name].values())
        )
        for perm in all_permutations:
            for partitions in itertools.product(
                *(
                    combinat.plethysm(field_repr, perm[field_name]).keys()
                    for field_name, field_repr in representations[group_name].items()
                ),
            ):
                if target in combinat.multi_lr_rule(partitions, None):
                    allowed_permutations[group_name].append(perm)
                    break
    return allowed_permutations
