import concurrent.futures
import itertools
import os
from collections import Counter
from typing import Dict
from typing import Iterator
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Tuple

import sage.all
import sage.matrix.constructor
from sage.rings.rational_field import QQ

import autoeft.base.classifications as classes
import autoeft.base.groups as symmetry_groups
from autoeft import utils
from autoeft.base import tensors
from autoeft.combinatorics import generators
from autoeft.combinatorics import young


class GroupSymmetrizer(NamedTuple):
    group_name: str
    fields_info: Tuple[Tuple[str, young.Partition, int], ...]


def construct_field_symmetrizers(
    group_symmetrizer: GroupSymmetrizer,
    op_type: classes.Type,
) -> Dict[str, Counter]:
    field_numbers = op_type.field_numbers()
    field_symmetrizers = {}
    for field_name, partition, basis_element in group_symmetrizer.fields_info:
        symmetrizer = generators.get_young_basis(partition)[basis_element]
        field_symmetrizers[field_name] = Counter(
            {
                tuple(
                    field_numbers[field_name][entry - 1] for entry in perm
                ): utils.Fraction(int(coeff.numerator()), int(coeff.denominator()))
                for perm, coeff in symmetrizer
            },
        )
    return field_symmetrizers


# Lorentz structures


def construct_symmetrized_lorentz_tensors(
    group_symmetrizer: GroupSymmetrizer,
    op_type: classes.Type,
    tableaux: List[tensors.LorentzTableau],
) -> Iterator[tensors.LorentzTensor]:
    field_symmetrizers = construct_field_symmetrizers(group_symmetrizer, op_type)
    for tableau in tableaux:
        tensor = tensors.LorentzTensor({tableau: 1})
        for field_symmetrizer in field_symmetrizers.values():
            tensor.symmetrize(field_symmetrizer)
        yield tensor.reduce()


def construct_lorentz_matrix(
    op_type: classes.Type,
    group_symmetrizer: GroupSymmetrizer,
    basis: List[tensors.LorentzTableau],
) -> sage.matrix.constructor.Matrix:
    dim = len(basis)
    symmetrized_tensors = construct_symmetrized_lorentz_tensors(
        group_symmetrizer,
        op_type,
        basis,
    )
    matrix = []
    for symmetrized_tensor in symmetrized_tensors:
        tensor = symmetrized_tensor.reduction(
            basis,
            op_type.family.N,
            op_type.family.nr,
        )
        matrix.append([tensor[tab] for tab in basis])
    return sage.matrix.constructor.matrix(QQ, dim, dim, matrix)


# SU(N) structures


def construct_symmetrized_sun_tensors(
    group_symmetrizer: GroupSymmetrizer,
    op_type: classes.Type,
    tableaux: List[tensors.SUNTableau],
) -> Iterator[tensors.SUNTensor]:
    field_symmetrizers = construct_field_symmetrizers(group_symmetrizer, op_type)
    for tableau in tableaux:
        tensor = tensors.SUNTensor({tableau: 1})
        for field_symmetrizer in field_symmetrizers.values():
            tensor.symmetrize(
                field_symmetrizer,
                key=lambda x, y: (x.get(y[0], y[0]), y[1]),
            )
        yield tensor.reduce()


def sun_tensor_reduction(symmetrized_tensor, basis, group, representations, igram):
    tensor = symmetrized_tensor.reduction(
        basis,
        group,
        representations,
        igram,
    )
    return [tensor[tab] for tab in basis]


def construct_sun_matrix(
    op_type: classes.Type,
    group_symmetrizer: GroupSymmetrizer,
    basis: List[tensors.SUNTableau],
    group: symmetry_groups.SUNGroup,
    igram_cache: Dict[str, sage.matrix.constructor.Matrix],
    threads: Optional[int] = None,
) -> sage.matrix.constructor.Matrix:
    dim = len(basis)
    representations = op_type.sun_content(group)
    symmetrized_tensors = construct_symmetrized_sun_tensors(
        group_symmetrizer,
        op_type,
        basis,
    )
    if group.name not in igram_cache:
        igram_cache[group.name] = tensors.calculate_gram_matrix(
            basis,
            group,
            representations,
            threads,
        ).inverse()
    igram = igram_cache[group.name]
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=threads or os.cpu_count(),
    ) as executor:
        matrix = executor.map(
            sun_tensor_reduction,
            symmetrized_tensors,
            itertools.repeat(basis),
            itertools.repeat(group),
            itertools.repeat(representations),
            itertools.repeat(igram),
        )
        return sage.matrix.constructor.matrix(QQ, dim, dim, matrix)
