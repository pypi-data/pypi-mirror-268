import importlib.resources
import sys
from pathlib import Path

import yaml

import autoeft
import autoeft.base.basis as eft_basis
import autoeft.base.model as ir_model
import autoeft.construction.main as con_main
from autoeft import exceptions

print = autoeft.print  # noqa: A001


default_module = __name__.rsplit(".", 1)[0]


def get_resource_basis(
    basis_path: Path,
) -> eft_basis.Basis:
    model_path = Path("model.json")
    try:
        model = ir_model.Model.parse_json(
            importlib.resources.files(default_module)
            .joinpath(basis_path, model_path)
            .read_text(),
        )
    except FileNotFoundError as e:
        errmsg = f"No '{model_path.name}' in basis directory."
        raise exceptions.BasisNotFoundError(errmsg) from e

    def traverse(anchor):
        for resource in anchor.iterdir():
            if resource.is_file() and resource.name.endswith(".yml"):
                yield resource
            elif resource.is_dir() and resource.name != "__pychache__":
                yield from traverse(
                    importlib.resources.files(default_module).joinpath(
                        anchor,
                        resource,
                    ),
                )

    operators = {}
    for operator_path in traverse(
        importlib.resources.files(default_module).joinpath(basis_path),
    ):
        op_info = eft_basis.OperatorInfoPermutation(
            model=model,
            **yaml.safe_load(operator_path.read_text()),
        )
        operators[repr(op_info)] = op_info

    def _sort(op_info: eft_basis.OperatorInfo):
        family = tuple(-nh for nh in op_info.op_type.family)
        op_type = tuple((f.name, m) for f, m in op_info.op_type)
        return op_info.N, (-op_info.nl, -op_info.nr), family, op_type

    operators_sorted = sorted(operators.items(), key=lambda item: _sort(item[1]))
    operator_basis = eft_basis.Basis(model)
    operator_basis.update(operators_sorted)
    return operator_basis


def get_resource_basis_lagacy(
    basis_path: str,
) -> eft_basis.Basis:
    model_path = Path("model.json")
    try:
        model = ir_model.Model.parse_json(
            importlib.resources.read_text(f"{default_module}.{basis_path}", model_path),
        )
    except FileNotFoundError as e:
        errmsg = f"No '{model_path.name}' in basis directory."
        raise exceptions.BasisNotFoundError(errmsg) from e

    def traverse(anchor):
        for resource in importlib.resources.contents(anchor):
            if resource.endswith(".yml"):
                yield anchor, resource
            elif "." not in resource and resource not in {
                "__pycache__",
                "__init__.py",
            }:
                yield from traverse(f"{anchor}.{resource}")

    operators = {}
    for operator_module, operator_path in traverse(f"{default_module}.{basis_path}"):
        op_info = eft_basis.OperatorInfoPermutation(
            model=model,
            **yaml.safe_load(
                importlib.resources.read_text(operator_module, operator_path),
            ),
        )
        operators[repr(op_info)] = op_info

    def _sort(op_info: eft_basis.OperatorInfo):
        family = tuple(-nh for nh in op_info.op_type.family)
        op_type = tuple((f.name, m) for f, m in op_info.op_type)
        return op_info.N, (-op_info.nl, -op_info.nr), family, op_type

    operators_sorted = sorted(operators.items(), key=lambda item: _sort(item[1]))
    operator_basis = eft_basis.Basis(model)
    operator_basis.update(operators_sorted)
    return operator_basis


def main(args) -> int:
    try:
        if sys.version_info >= (3, 9):
            sample = (
                importlib.resources.files(autoeft.__program__)
                .joinpath("sm.yml")
                .read_text()
            )
        else:
            sample = importlib.resources.read_text(autoeft.__program__, "sm.yml")
    except FileNotFoundError:
        sample = "name: <sample-model>\nsymmetries: {}\nfields: {}\n"
    model = ir_model.Model(**yaml.safe_load(sample))
    print("Checking AutoEFT's functionality:")
    print("Constructing operator basis for [b]SMEFT[/b] @ [i]d=6[/i]")
    basis, _ = con_main.plain_main(model, 6, True, False)
    if sys.version_info >= (3, 9):
        resource_basis = get_resource_basis(
            Path(f"check_basis-{autoeft.version}".replace(".", "_")),
        )
    else:
        resource_basis = get_resource_basis_lagacy(
            f"check_basis-{autoeft.version}".replace(".", "_"),
        )
    print("Check against pre-constructed basis...")
    if basis != resource_basis:
        print("[b]Failure[/b] - found divergent bases!")
        return 1
    print("[b]Success[/b] - found complete agreement!")
    return 0
