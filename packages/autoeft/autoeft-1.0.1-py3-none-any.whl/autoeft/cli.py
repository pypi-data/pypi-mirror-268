import argparse
import os
import sys
from pathlib import Path
from typing import List
from typing import Optional

import autoeft
import autoeft.base.model as model_entry
import autoeft.combinatorics.generators as generators_entry
import autoeft.construction.main as construction_entry
import autoeft.io.check as check_entry
import autoeft.io.count as count_entry
import autoeft.tex.main as latex_entry

print = autoeft.print  # noqa: A001


def create_chk_subparser(subparsers):
    parser = subparsers.add_parser(
        "check",
        add_help=False,
        help="check functionality of this installation",
    )
    parser.set_defaults(main_func=check_entry.main)
    return parser


def create_spl_subparser(subparsers):
    parser = subparsers.add_parser(
        "sample-model",
        add_help=False,
        help="produce a sample model file",
    )
    parser.set_defaults(main_func=model_entry.main, quiet=True)
    return parser


def create_con_subparser(subparsers):
    desc = (
        "Construct an operator basis for a given IR model and mass dimension. "
        "The operator basis is a minimal set of non-redundant operators. "
        "In order to generate an operator basis,"
        " provide a model file and the desired mass dimension."
    )
    parser = subparsers.add_parser(
        "construct",
        aliases=["c"],
        description=desc,
        help="construct an operator basis for a given model and dimension",
    )
    parser.add_argument("model", type=Path, help="model file")
    parser.add_argument("dimension", type=int, help="mass dimension")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="show intermediate construction output",
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=os.cpu_count(),
        help="set number of threads starting FORM (default: %(default)s)",
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="set the EFT name (default: <model>-eft)",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        type=Path,
        default=Path().cwd() / "efts",
        help="set output path (default: %(default)s)",
    )
    parser.add_argument(
        "-s",
        "--select",
        action="append",
        type=str,
        help="only construct selected types (default: All)",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        action="append",
        type=str,
        help="do not construct ignored types (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only list the types that match the current selection",
    )
    parser.add_argument(
        "--generators",
        metavar="PATH",
        type=Path,
        default=Path().cwd() / "gens",
        help="set generators path (default: %(default)s)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing output files",
    )
    parser.add_argument(
        "--no_hc",
        action="store_true",
        help="prevent the explicit construction of conjugate operator types",
    )
    parser.set_defaults(main_func=construction_entry.main)
    return parser


def create_cnt_subparser(subparsers):
    desc = (
        "Count the number of families, types, terms, and operators for a given basis."
    )
    parser = subparsers.add_parser(
        "count",
        description=desc,
        help="count invariant classes for a given basis",
    )
    parser.add_argument("basis", type=Path, help="basis directory")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="show model details and operator type numbers",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        type=Path,
        default=Path().cwd() / "counts.yml",
        help="write the numbers to FILE (default: %(default)s)",
    )
    parser.add_argument(
        "-s",
        "--select",
        action="append",
        type=str,
        help="only include selected types (default: All)",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        action="append",
        type=str,
        help="do not include ignored types (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only list the types that match the current selection",
    )
    parser.add_argument(
        "--no_hc",
        action="store_true",
        help="prevent the implicit counting of conjugate operator types",
    )
    parser.set_defaults(main_func=count_entry.main)
    return parser


def create_tex_subparser(subparsers):
    desc = (
        "Generate TeX files for a given basis."
        " The TeX files represent all the information encoded in the operator files"
        " as LaTeX markup."
        " The resulting files compose a valid LaTeX document"
        " that can be compiled to a single PDF file."
    )
    parser = subparsers.add_parser(
        "latex",
        aliases=["l"],
        description=desc,
        help="generate TeX files for a given basis",
    )
    parser.add_argument("basis", type=Path, help="basis directory")
    parser.add_argument(
        "-c",
        "--compile",
        type=str,
        metavar="COMMAND",
        help="compile TeX files using `COMMAND`",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        type=Path,
        default=Path().cwd() / "tex",
        help="set output path (default: %(default)s)",
    )
    parser.add_argument(
        "-s",
        "--select",
        action="append",
        type=str,
        help="only include selected types (default: All)",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        action="append",
        type=str,
        help="do not include ignored types (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only list the types that match the current selection",
    )
    parser.set_defaults(main_func=latex_entry.main)
    return parser


def create_gen_subparser(subparsers):
    desc = (
        "View or create generator matrices of"
        " symmetric group representations. "
        "These matrices are used to generate"
        " the irreducible representation matrices. "
        "The generators can be constructed"
        " for the whole symmetric group"
        " or specific irreducible representations."
    )
    parser = subparsers.add_parser(
        "generators",
        aliases=["g"],
        description=desc,
        help="view or create generators of the symmetric group",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        type=Path,
        default=Path().cwd() / "gens",
        help="set output path (default: %(default)s)",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-S",
        dest="N",
        type=int,
        help="construct all generators for the symmetric group of degree `N`",
    )
    group.add_argument(
        "-P",
        dest="partition",
        metavar="p",
        nargs="+",
        type=int,
        help=(
            "construct all generators for the irreducible representation "
            "given by the partition as a non-increasing list of integers `p`"
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing output files",
    )
    parser.set_defaults(main_func=generators_entry.main)
    return parser


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=autoeft.__summary__,
        epilog=str(autoeft.disclaimer),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=str(autoeft.version),
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="suppress all output",
    )
    subparsers = parser.add_subparsers(title="commands")
    create_chk_subparser(subparsers)
    create_spl_subparser(subparsers)
    create_con_subparser(subparsers)
    create_cnt_subparser(subparsers)
    create_tex_subparser(subparsers)
    create_gen_subparser(subparsers)
    return parser


def main(cli_args: Optional[List[str]] = None) -> int:
    print(*sys.argv, dest="log")
    parser = create_parser()
    args = parser.parse_args(args=cli_args)
    if not hasattr(args, "main_func"):
        parser.print_help()
        raise SystemExit
    autoeft.console.quiet = args.quiet
    print(autoeft.logo)
    print(autoeft.disclaimer)
    print()
    return args.main_func(args)
