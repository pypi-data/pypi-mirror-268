from collections import defaultdict
from typing import Optional

import rich.markup
import rich.tree
import yaml

import autoeft
import autoeft.io.basis as io_basis
from autoeft import exceptions
from autoeft import utils

print = autoeft.print  # noqa: A001


class Stats(defaultdict):
    hc_flag: bool = True

    def hc_mod(self, invariant):
        if self.hc_flag:
            hc_mod = 1 if invariant.is_real() else 2
            return hc_mod if invariant.is_normal() else 0
        return 1

    @property
    def n_families(self):
        return sum(self.hc_mod(family) for family in self)

    @property
    def n_types(self):
        return sum(
            sum(self.hc_mod(op_type) for op_type in types) for types in self.values()
        )

    @property
    def n_terms(self):
        return sum(
            sum(self.hc_mod(op_type) * t for op_type, (t, _) in types.items())
            for types in self.values()
        )

    @property
    def n_operators(self):
        return sum(
            sum(self.hc_mod(op_type) * o for op_type, (_, o) in types.items())
            for types in self.values()
        )

    def yaml(self):
        return {
            str(family): {
                str(op_type): utils.FlowSeq(
                    (self.hc_mod(op_type) * t, self.hc_mod(op_type) * o),
                )
                for op_type, (t, o) in types.items()
            }
            for family, types in self.items()
        }


def count_classes(
    basis,
    select: Optional[list] = None,
    ignore: Optional[list] = None,
):
    classes = Stats(dict)
    for op_info in basis.values():
        op_type = op_info.op_type
        family = op_type.family
        if select and not utils.type_matches(op_type, select):
            continue
        if ignore and utils.type_matches(op_type, ignore):
            continue
        if op_info.n_terms and op_info.n_operators:
            classes[family][op_type] = (op_info.n_terms, op_info.n_operators)
    return classes


def dry_run(
    basis,
    select: Optional[list] = None,
    ignore: Optional[list] = None,
):
    for op_info in basis.values():
        op_type = op_info.op_type
        if select and not utils.type_matches(op_type, select):
            continue
        if ignore and utils.type_matches(op_type, ignore):
            continue
        yield op_type


def main(args) -> int:
    basis_path = args.basis
    basis_file = io_basis.BasisFile(basis_path)
    try:
        model = basis_file.get_model()
        basis = basis_file.get_basis()
        dimension = basis_file.get_extra().dimension
        hc_flag = not args.no_hc
    except exceptions.BasisNotFoundError as e:
        errmsg = f"{e}\nInvalid basis directory '{basis_file.basis_path}'."
        print(errmsg)
        return 1
    if args.verbose:
        print(model)
        print()
    try:
        select = (
            [yaml.safe_load(s.replace(":", ": ")) for s in args.select]
            if args.select
            else None
        )
        ignore = (
            [yaml.safe_load(i.replace(":", ": ")) for i in args.ignore]
            if args.ignore
            else None
        )
    except yaml.YAMLError as e:
        errmsg = f"{e}\nCould not parse select/ignore options."
        print(errmsg)
        return 1
    if args.dry_run:
        print(
            f"Dry run for "
            f"[b]{rich.markup.escape(model.name)}[/b] @ [i]d={dimension}[/i]",
        )
        print(f"[i]select[/i]: {select}")
        print(f"[i]ignore[/i]: {ignore}")
        print()
        print("[b]types:[/b]")
        for op_type in dry_run(
            basis,
            select,
            ignore,
        ):
            print(f"[bold white]{op_type}[/bold white]", dest="terminal")
            print(op_type, dest="log")
        return 0

    print(
        f"Counting invariant classes for "
        f"[b]{rich.markup.escape(model.name)}[/b] @ [i]d={dimension}[/i]",
    )
    if not hc_flag:
        print("[i](no Hermitian conjugation implied)[/i]")
    stats = count_classes(basis, select, ignore)
    stats.hc_flag = hc_flag
    if args.verbose:
        eft_tree = rich.tree.Tree(
            f"[d]{rich.markup.escape(model.name)}[/d] @ [i]d={dimension}[/i]",
            style="bold",
            highlight=True,
        )
        for family, types in stats.items():
            if hc_flag and not family.is_normal():
                continue
            hc_str = (
                "[dim italic not bold] + h.c.[/]"
                if hc_flag and family.is_complex()
                else ""
            )
            family_tree = eft_tree.add(
                str(family) + hc_str,
                style="bold",
                highlight=True,
            )
            for op_type, (n_term, n_operator) in types.items():
                if hc_flag and not op_type.is_normal():
                    continue
                hc_mod = 2 if hc_flag and op_type.is_complex() else 1
                hc_str = (
                    "[dim italic not bold] + h.c.[/]"
                    if hc_flag and op_type.is_complex()
                    else ""
                )
                type_tree = family_tree.add(str(op_type) + hc_str)
                type_tree.add(f"#terms={hc_mod*n_term}", style="not bold")
                type_tree.add(f"#operators={hc_mod*n_operator}", style="not bold")
        autoeft.console.rule()
        print(eft_tree)
        autoeft.console.rule()
    print(f"[b]#[/b]families={stats.n_families:,}")
    print(f"[b]#[/b]types={stats.n_types:,}")
    print(f"[b]#[/b]terms={stats.n_terms:,}")
    print(f"[b]#[/b]operators={stats.n_operators:,}")
    if args.output:
        stats_file = args.output.resolve()
        data = {}
        if args.verbose:
            data = {"classes": stats.yaml()}
        data["n_families"] = stats.n_families
        data["n_types"] = stats.n_types
        data["n_terms"] = stats.n_terms
        data["n_operators"] = stats.n_operators
        try:
            hc_comment = "" if hc_flag else "# no Hermitian conjugation implied\n"
            stats_file.write_text(
                hc_comment + yaml.dump(data, sort_keys=False, Dumper=utils.YamlDumper),
            )
        except IsADirectoryError:
            errmsg = f"'{stats_file}' is not a valid output directory."
            print(errmsg)
            return 1
    print(f"Saved numbers in {stats_file}")
    return 0
