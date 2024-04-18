import datetime
import importlib
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Counter as Count
from typing import Iterable
from typing import Iterator
from typing import Optional

import rich.markup
import yaml

import autoeft
import autoeft.base.model as ir_model
import autoeft.io.basis as io_basis
from autoeft import exceptions
from autoeft import utils
from autoeft.tex import tex

default_module = __name__.rsplit(".", 1)[0]

print = autoeft.print  # noqa: A001

try:
    if sys.version_info >= (3, 9):
        with importlib.resources.as_file(
            importlib.resources.files(default_module).joinpath("main.tex"),
        ) as file_path:
            texfile_path = file_path
    else:
        with importlib.resources.path(default_module, "main.tex") as file_path:
            texfile_path = file_path
except FileNotFoundError:
    texfile_path = None


def dry_run(
    basis,
    select: Optional[list] = None,
    ignore: Optional[list] = None,
):
    for op_info in basis.values():
        if select and not utils.type_matches(op_info.op_type, select):
            continue
        if ignore and utils.type_matches(op_info.op_type, ignore):
            continue
        yield op_info.op_type


def main(args) -> int:
    basis_path = args.basis
    basis_file = io_basis.BasisFile(basis_path)
    try:
        model = basis_file.get_model()
        basis = basis_file.get_basis()
        metadata = basis_file.get_extra()
    except exceptions.BasisNotFoundError as e:
        errmsg = f"{e}\nInvalid basis directory '{basis_file.basis_path}'."
        print(errmsg)
        return 1
    output_path = args.output.resolve()
    output_path /= f"{metadata.eft_name}"
    output_path /= ascii(metadata.dimension)
    output_path.mkdir(parents=True, exist_ok=True)
    operators_path = output_path / "operators"
    operators_path.mkdir(exist_ok=True)
    hc_flag = not metadata.args["no_hc"]
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
            f"[b]{rich.markup.escape(model.name)}[/b] @ [i]d={metadata.dimension}[/i]",
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
        f"Generating TeX files for "
        f"[b]{rich.markup.escape(model.name)}[/b] @ [i]d={metadata.dimension}[/i]",
    )
    families = Counter()
    types = Counter()
    terms = Counter()
    operators = Counter()
    hilbert_series = Counter()
    tensor_product = rf"\[ \mathcal{{O}} \sim {tex(model.symmetries)} \]"
    operator_files = []
    for op_info in basis.values():
        if select and not utils.type_matches(op_info.op_type, select):
            continue
        if ignore and utils.type_matches(op_info.op_type, ignore):
            continue
        op_type = op_info.op_type
        family = op_type.family
        if hc_flag:
            tex_family = tex(family)
            tex_type = tex(op_type)
            hilbert_series[tex_type] = op_info.n_operators
            families[tex_family] = 1
            types[tex_family] += 1
            terms[tex_family] += op_info.n_terms
            operators[tex_family] += op_info.n_operators
        else:
            tex_family = tex(family)
            tex_type = tex(op_type)
            hilbert_series[tex_type] = op_info.n_operators
            hc_mod = 2 if op_type.is_complex() else 1
            if family.is_complex():
                tex_family += r" + \hc"
                families[tex_family] = 2
            else:
                families[tex_family] = 1
            types[tex_family] += 1 * hc_mod
            terms[tex_family] += op_info.n_terms * hc_mod
            operators[tex_family] += op_info.n_operators * hc_mod
        operator_path = operators_path / f"{op_type.path('tex')}"
        produce_texfile(
            operator_path,
            [
                rf"\subsection{{\texorpdfstring{{${tex(op_type)}$}}"
                f"{{{op_info.op_type!s}}}}}",
                tex(op_info),
            ],
        )
        operator_files.append(rf"\input{{operators/{operator_path.stem}}}")
    produce_texfile(
        output_path / "header.tex",
        tex_header(model, metadata.dimension, metadata.timestamp),
    )
    produce_texfile(
        output_path / "model.tex",
        [tex(model)],
    )
    produce_texfile(
        output_path / "numbers_table.tex",
        tex_table(families, types, terms, operators),
    )
    produce_texfile(
        output_path / "hilbert_series.tex",
        tex_series(hilbert_series, metadata.dimension, not hc_flag),
    )
    produce_texfile(
        output_path / "operators.tex",
        [tensor_product, *operator_files],
    )
    if texfile_path.is_file():
        if not (output_path / "main.tex").is_file():
            print(f"No 'main.tex' found, writing default file to {output_path}")
            shutil.copy(texfile_path, output_path)
        else:
            print("Existing 'main.tex' found")
    print(f"TeX files saved under {output_path}")
    if args.compile:
        print(f"[b]{args.compile}[/b]")
        result = subprocess.run(
            args.compile,
            cwd=output_path,
            shell=True,  # noqa: S602
            check=False,
        )
        return result.returncode
    return 0


def tex_header(model: ir_model.Model, dimension: int, timestamp: datetime.datetime):
    yield rf"\title{{{model.name} @ $d={dimension}$}}"
    if model.description:
        yield rf"\subtitle{{{model.description}}}"
    yield rf"\date{{{timestamp}}}"
    yield (
        rf"\author{{Generated by \texttt{{{autoeft.program}}}"
        rf" \textit{{{autoeft.version}}}}}"
    )


def tex_table(
    families: Count[str],
    types: Count[str],
    terms: Count[str],
    operators: Count[str],
) -> Iterator[str]:
    yield r"\begin{longtable}{crrr}"
    yield r"\toprule"
    yield r"family & types & terms & operators \\"
    yield r"\midrule"
    for family in families:
        yield (
            rf"${family}$ & {types[family]}"
            rf" & {terms[family]} & {operators[family]} \\"
        )
    yield r"\midrule"
    yield (
        rf"{sum(families.values())} & {sum(types.values())}"
        rf" & {sum(terms.values())} & {sum(operators.values())} \\"
    )
    yield r"\bottomrule"
    yield r"\end{longtable}"


def tex_series(
    hilbert_series: Count[str],
    dimension: int,
    add_hc: bool = False,
) -> Iterator[str]:
    yield r"\begin{align*}"
    yield r"\begin{autobreak}"
    yield rf"\hat{{H}}_{{{dimension}}} = "
    yield "  " + "\n+ ".join(
        rf"{co}\,{op}" if co > 1 else op for op, co in hilbert_series.items()
    )
    if add_hc:
        yield r"  + \hc"
    yield r"\end{autobreak}"
    yield r"\end{align*}"


def produce_texfile(path: Path, content: Iterable):
    disclaimer = f"% '{path.name}' generated by {autoeft.program} {autoeft.version}\n"
    path.write_text(disclaimer + "\n".join(content))
