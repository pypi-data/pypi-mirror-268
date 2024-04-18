import subprocess
from typing import Iterable
from typing import List

import autoeft.form
from autoeft import utils

script = """#-
Off statistics;
Format nospaces;
Dimension {sun_dimension};
AutoDeclare Index F;
{exprs}
contract 0;
.sort
#do i=1,{basis_dimension}
#write "%E", expr`i'
#enddo
.end
"""


def contract_basis(
    tensor: str,
    sbasis: Iterable[str],
    sun_dimension: int,
    basis_dimension: int,
) -> List[utils.Fraction]:
    exprs = "\n".join(
        f"Local expr{i} = ({tensor})*({element});"
        for i, element in enumerate(sbasis, start=1)
    )
    data = script.format(
        sun_dimension=sun_dimension,
        exprs=exprs,
        basis_dimension=basis_dimension,
    )
    command = [autoeft.form.executable, "-q", "-M", "-"]
    contract_cmd = subprocess.run(
        command,  # noqa: S603
        input=data,
        capture_output=True,
        text=True,
        check=True,
    )
    return [utils.Fraction(res) for res in contract_cmd.stdout.splitlines()]
