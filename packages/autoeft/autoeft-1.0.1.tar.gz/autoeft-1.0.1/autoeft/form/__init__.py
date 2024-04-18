import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

import semver

from autoeft import exceptions

if (path := shutil.which("form", path=os.getenv("AUTOEFT_PATH"))) is None:
    errmsg = (
        "Unable to locate FORM."
        "\n"
        "Please make sure FORM is installed and added to the system PATH"
        " or to AUTOEFT_PATH."
    )
    raise exceptions.MissingRequirementError(errmsg)
executable = Path(path)
version_cmd = subprocess.run(
    (executable, "-version"),  # noqa: S603
    capture_output=True,
    text=True,
    check=True,
)
if (match := re.match(r"^FORM (\d+(?:\.\d+)*)", version_cmd.stdout)) is None:
    errmsg = "Invalid FORM version string '{version_cmd.stdout}'."
    raise exceptions.RequirementVersionError(errmsg)
__version__ = match[1]
version = semver.Version.parse(__version__, optional_minor_and_patch=True)


def form(obj: Any) -> str:
    """Call the FORM representation of an object."""
    return type(obj).__form__(obj)
