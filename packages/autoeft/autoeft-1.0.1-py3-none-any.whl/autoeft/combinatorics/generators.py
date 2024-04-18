import importlib.resources
import itertools
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import Tuple

import numpy as np
import rich.progress
import rich.table
import sage.all
import sage.combinat.permutation
import sage.combinat.symmetric_group_algebra
import sage.matrix.constructor
import sage.modules.free_module_element
import scipy.sparse

import autoeft
from autoeft import exceptions
from autoeft.combinatorics import young

print = autoeft.print  # noqa: A001


default_module = __name__.rsplit(".", 1)[0]
default_path = Path().cwd() / "gens"
N_pattern = re.compile(r"^S_(\d+)$")
P_pattern = re.compile(r"^P_((?:\d+_)+)(cycle|reflection)\.npz$")


# cache young basis
young_basis: Dict[young.Partition, list] = {}
# cache generators
generators: Dict[
    young.Partition,
    Tuple[
        sage.matrix.constructor.Matrix,
        sage.matrix.constructor.Matrix,
        sage.matrix.constructor.Matrix,
    ],
] = {
    young.Partition(): (
        sage.matrix.constructor.Matrix.identity(1),
        sage.matrix.constructor.Matrix.identity(1),
        sage.matrix.constructor.Matrix.identity(1),
    ),
    young.Partition([1]): (
        sage.matrix.constructor.Matrix.identity(1),
        sage.matrix.constructor.Matrix.identity(1),
        sage.matrix.constructor.Matrix.identity(1),
    ),
}


def get_young_basis(irrepr: young.Partition) -> list:
    try:
        return young_basis[irrepr]
    except KeyError:
        tableaux = irrepr.standard_tableaux()
        normal_tableau = tableaux[0]
        young_operator = sage.combinat.symmetric_group_algebra.e_hat(normal_tableau)
        algebra = young_operator.parent()
        basis = [
            algebra.left_action_product(
                sage.combinat.symmetric_group_algebra.pi_ik(normal_tableau, tableau),
                young_operator,
            )
            for tableau in tableaux
        ]
        young_basis[irrepr] = basis
        return basis


def get_path_generators(generators_path: Path, reflection_path: Path, cycle_path: Path):
    D_reflection = sage.matrix.constructor.matrix(
        scipy.sparse.load_npz(generators_path / reflection_path).toarray(),
    )
    D_cycle = sage.matrix.constructor.matrix(
        scipy.sparse.load_npz(generators_path / cycle_path).toarray(),
    )
    return D_reflection, D_cycle


def get_resource_generators(
    generators_path: Path,
    reflection_path: Path,
    cycle_path: Path,
):
    with importlib.resources.files(default_module).joinpath(
        generators_path,
        reflection_path,
    ).open("rb") as reflection_file:
        D_reflection = sage.matrix.constructor.matrix(
            scipy.sparse.load_npz(reflection_file).toarray(),
        )
    with importlib.resources.files(default_module).joinpath(
        generators_path,
        cycle_path,
    ).open("rb") as cycle_file:
        D_cycle = sage.matrix.constructor.matrix(
            scipy.sparse.load_npz(cycle_file).toarray(),
        )
    return D_reflection, D_cycle


def get_resource_generators_lagacy(
    generators_path: str,
    reflection_path: Path,
    cycle_path: Path,
):
    with importlib.resources.open_binary(
        f"{default_module}.{generators_path}",
        reflection_path,
    ) as reflection_file:
        D_reflection = sage.matrix.constructor.matrix(
            scipy.sparse.load_npz(reflection_file).toarray(),
        )
    with importlib.resources.open_binary(
        f"{default_module}.{generators_path}",
        cycle_path,
    ) as cycle_file:
        D_cycle = sage.matrix.constructor.matrix(
            scipy.sparse.load_npz(cycle_file).toarray(),
        )
    return D_reflection, D_cycle


def get_generators(
    irrepr: young.Partition,
) -> Tuple[
    sage.matrix.constructor.Matrix,
    sage.matrix.constructor.Matrix,
    sage.matrix.constructor.Matrix,
]:
    try:
        return generators[irrepr]
    except KeyError:
        N = sum(irrepr)
        str_irrepr = "_".join(str(i) for i in irrepr)
        reflection_path = Path(f"P_{str_irrepr}_reflection.npz")
        cycle_path = Path(f"P_{str_irrepr}_cycle.npz")
        try:
            generators_path = default_path / f"S_{N}"
            D_reflection, D_cycle = get_path_generators(
                generators_path,
                reflection_path,
                cycle_path,
            )
        except FileNotFoundError:
            try:
                if sys.version_info >= (3, 9):
                    generators_path = Path("gens", f"S_{N}")
                    D_reflection, D_cycle = get_resource_generators(
                        generators_path,
                        reflection_path,
                        cycle_path,
                    )
                else:
                    generators_path = f"gens.S_{N}"
                    D_reflection, D_cycle = get_resource_generators_lagacy(
                        generators_path,
                        reflection_path,
                        cycle_path,
                    )
            except (ModuleNotFoundError, FileNotFoundError) as e:
                errmsg = (
                    "Required generator matrices for irreducible representation"
                    f" {irrepr} not found."
                    "\n"
                    "You can try to generate them using 'autoeft generators'."
                )
                raise exceptions.MissingResourcesError(errmsg) from e
        D_cycle_I = D_cycle.inverse()
        generators[irrepr] = D_reflection, D_cycle, D_cycle_I
        return D_reflection, D_cycle, D_cycle_I


def generator_matrices(
    irrepr: young.Partition,
) -> Tuple[scipy.sparse.csc_matrix, scipy.sparse.csc_matrix]:
    with rich.progress.Progress(
        rich.progress.TextColumn("{task.description}", style="bold"),
        rich.progress.BarColumn(),
        rich.progress.MofNCompleteColumn(),
        rich.progress.TimeRemainingColumn(compact=True, elapsed_when_finished=True),
        console=autoeft.console,
    ) as progress:
        N = sum(irrepr)
        task = progress.add_task(f"{irrepr!s:<{2*N+1}}", total=None)
        group = sage.combinat.permutation.StandardPermutations_n(N)
        reflection = group.simple_reflection(1)
        cycle = sage.combinat.permutation.from_cycles(N, [list(range(1, N + 1))])
        basis = get_young_basis(irrepr)
        dim = len(basis)
        algebra = basis[0].parent()
        A = sage.matrix.constructor.matrix(
            sage.modules.free_module_element.vector(e) for e in basis
        )
        D_reflection = scipy.sparse.dok_array((dim, dim), dtype=np.int32)
        D_cycle = scipy.sparse.dok_array((dim, dim), dtype=np.int32)
        progress.update(task, total=dim)
        for i, element in enumerate(basis):
            Y_reflection = sage.modules.free_module_element.vector(
                algebra.left_action_product(reflection, element),
            )
            X_reflection = A.solve_left(Y_reflection)
            for j, value in enumerate(X_reflection):
                if value:
                    D_reflection[j, i] = value
            Y_cycle = sage.modules.free_module_element.vector(
                algebra.left_action_product(cycle, element),
            )
            X_cycle = A.solve_left(Y_cycle)
            for j, value in enumerate(X_cycle):
                if value:
                    D_cycle[(j, i)] = value
            progress.advance(task, 1)
    return D_reflection.tocsc(), D_cycle.tocsc()


def save_matrices(
    matrices_path: Path,
    irrepr: young.Partition,
    overwrite: bool = False,
):
    str_irrepr = "_".join(str(i) for i in irrepr)
    reflection_path = matrices_path / f"P_{str_irrepr}_reflection.npz"
    cycle_path = matrices_path / f"P_{str_irrepr}_cycle.npz"
    N = sum(irrepr)
    if overwrite or not (reflection_path.is_file() and cycle_path.is_file()):
        D_reflection, D_cycle = generator_matrices(irrepr)
        scipy.sparse.save_npz(reflection_path, D_reflection)
        scipy.sparse.save_npz(cycle_path, D_cycle)
        print(f"[white b]{irrepr!s:<{2*N+1}}[/] [dim]calculated, saved[/]", dest="log")
    else:
        print(f"[white b]{irrepr!s:<{2*N+1}}[/] [dim]already exists, skipped[/]")


def collect_generators_path(matrices_path: Path) -> Iterator[tuple]:
    for group_path in matrices_path.glob("S_*/"):
        if match_N := N_pattern.match(group_path.name):
            N = int(match_N[1])
            for partition_path in group_path.glob("P_*.npz"):
                if match_P := P_pattern.match(partition_path.name):
                    partition = young.Partition(
                        int(i) for i in match_P[1].split("_") if i
                    )
                    assert sum(partition) == N
                    try:
                        printed_path = partition_path.relative_to(Path().cwd())
                    except ValueError:
                        printed_path = partition_path
                    yield N, partition, match_P[2], printed_path


def collect_generators_resource() -> Iterator[tuple]:
    resource = importlib.resources.files(default_module).joinpath("gens")
    for group_resource in resource.iterdir():
        if (
            match_N := N_pattern.match(group_resource.name)
        ) and group_resource.is_dir():
            N = int(match_N[1])
            for partition_resource in group_resource.iterdir():
                if (
                    match_P := P_pattern.match(partition_resource.name)
                ) and partition_resource.is_file():
                    partition = young.Partition(
                        int(i) for i in match_P[1].split("_") if i
                    )
                    assert sum(partition) == N
                    with importlib.resources.as_file(
                        partition_resource,
                    ) as partition_path:
                        yield N, partition, match_P[2], partition_path


def collect_generators_resource_lagacy() -> Iterator[tuple]:
    resource = f"{default_module}.gens"
    for group_name in importlib.resources.contents(resource):
        if match_N := N_pattern.match(group_name):
            N = int(match_N[1])
            for partition_name in importlib.resources.contents(resource + f".S_{N}"):
                if match_P := P_pattern.match(partition_name):
                    partition = young.Partition(
                        int(i) for i in match_P[1].split("_") if i
                    )
                    assert sum(partition) == N
                    with importlib.resources.path(
                        resource + f".S_{N}",
                        partition_name,
                    ) as partition_path:
                        yield N, partition, match_P[2], partition_path


def collect_generators(matrices_path: Path) -> dict:
    system_generators = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for N, part, kind, path in collect_generators_path(matrices_path):
        system_generators[N][part][kind]["path"] = path
    if sys.version_info >= (3, 9):
        for N, part, kind, path in collect_generators_resource():
            system_generators[N][part][kind]["resource"] = path
    else:
        for N, part, kind, path in collect_generators_resource_lagacy():
            system_generators[N][part][kind]["resource"] = path
    return system_generators


def show_generators(matrices_path: Path):
    system_generators = collect_generators(matrices_path)
    caption = (
        f"This table shows all generators that {autoeft.program}"
        " loads with the given options."
    )
    table = rich.table.Table(title="Generators", caption=caption, highlight=True)
    table.add_column("N")
    table.add_column("Partition")
    table.add_column("Cycle", overflow="fold")
    table.add_column("Reflection", overflow="fold")
    for N in sorted(system_generators):
        element = itertools.chain([str(N)], itertools.repeat(None))
        for partition in sorted(system_generators[N], reverse=True):
            system_generator = system_generators[N][partition]
            print_cycle = print_reflection = "[bold red]MISSING[/bold red]"
            if "cycle" in system_generator:
                cycle = system_generator["cycle"].get(
                    "path",
                    system_generator["cycle"]["resource"],
                )
                print_cycle = f"[link=file:{cycle.absolute()}]{cycle}[/link]"
            if "reflection" in system_generator:
                reflection = system_generator["reflection"].get(
                    "path",
                    system_generator["reflection"]["resource"],
                )
                print_reflection = (
                    f"[link=file:{reflection.absolute()}]{reflection}[/link]"
                )
            table.add_row(next(element), str(partition), print_cycle, print_reflection)
        table.add_section()
    print(table)


def main(args) -> int:
    output_path = args.output.resolve()
    if args.N is not None:
        N = args.N
        if N < 2:
            print(f"Generators for [b]S{N}[/b] are not required.")
            return 1
        print(f"Constructing generators for [b]S{N}[/b]")
        output_path /= f"S_{N}"
        output_path.mkdir(parents=True, exist_ok=True)
        for irrepr in young.Partition.partitions(N):
            save_matrices(output_path, irrepr, args.overwrite)
        print(f"Saved generators in [link=file:{output_path}]{output_path}[/link]")
    elif args.partition is not None:
        irrepr = young.Partition(args.partition)
        N = sum(irrepr)
        if N < 2:
            print(f"Generators for [b]S{N}[/b] are not required.")
            return 1
        print(f"Constructing generators for representation {irrepr}")
        output_path /= f"S_{N}"
        output_path.mkdir(parents=True, exist_ok=True)
        save_matrices(output_path, irrepr, args.overwrite)
        print(f"Saved generators in [link=file:{output_path}]{output_path}[/link]")
    else:
        show_generators(output_path)
    return 0
