import importlib.metadata
import importlib.resources
import os
import sys
from pathlib import Path

import packaging.version
import rich.console
import rich.text
import rich.theme
import semver

from autoeft import exceptions

program = "AutoEFT"
__program__ = program.lower()

# load metadata
try:
    dist = importlib.metadata.distribution(__program__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "<version>"
    __authors__ = "<authors>"
    __license__ = "<license>"
    __summary__ = "<summary>"
    __webpage__ = "<url>"
else:
    __program__ = dist.metadata["Name"]
    __version__ = dist.metadata["Version"]
    __authors__ = dist.metadata["Author"]
    __license__ = dist.metadata["License"].split("\n")[0]
    __summary__ = dist.metadata["Summary"]
    __webpage__ = dist.metadata["Project-URL"]

pkg_version = packaging.version.Version(__version__)
version = semver.Version(
    *pkg_version.release,
    prerelease=(
        None if pkg_version.pre is None else "".join([str(i) for i in pkg_version.pre])
    ),
    build=None if pkg_version.dev is None else f"dev{pkg_version.dev}",
)

# load resources
try:
    if sys.version_info >= (3, 9):
        __copyright__ = (
            importlib.resources.files(__program__).joinpath("COPYRIGHT").read_text()
        )
        __logo__ = importlib.resources.files(__program__).joinpath("LOGO").read_text()
    else:
        __copyright__ = importlib.resources.read_text(__program__, "COPYRIGHT")
        __logo__ = importlib.resources.read_text(__program__, "LOGO")
except FileNotFoundError:
    __copyright__ = "<copyright>\n"
    __logo__ = "<LOGO>\n"

try:
    if sys.version_info >= (3, 9):
        with importlib.resources.as_file(
            importlib.resources.files(__program__).joinpath("theme.ini"),
        ) as theme_path:
            theme = rich.theme.Theme().read(str(theme_path))
    else:
        with importlib.resources.path(__program__, "theme.ini") as theme_path:
            theme = rich.theme.Theme().read(str(theme_path))
except FileNotFoundError:
    theme = rich.theme.Theme()


console = rich.console.Console(theme=theme)
log_file = Path.cwd() / "autoeft.log"
log_console = rich.console.Console(file=log_file.open("w"), width=80, log_path=False)


def print(*args, dest: str = "both"):  # noqa: A001
    if dest == "both":
        console.print(*args)
        log_console.log(*args)
    elif dest == "terminal":
        console.print(*args)
    elif dest == "log":
        log_console.log(*args)
    else:
        raise ValueError(dest)


logo = rich.text.Text(__logo__)
logo.highlight_regex("[Auto]", style="bold rgb(142,186,229)")
logo.highlight_regex("[EFT]", style="bold rgb(0,84,159)")

disclaimer = rich.text.Text()
disclaimer.append(program, style="bold")
disclaimer.append(" ")
disclaimer.append(str(version), style="italic")
disclaimer.append("\n")
disclaimer.append(__copyright__)
disclaimer.append("This application is licensed under the ")
disclaimer.append(__license__, style="italic")
disclaimer.append(".")

conjugation_symbol = os.getenv("AUTOEFT_CS", "+")
epsilon_dot_symbol = os.getenv("AUTOEFT_DS", "~")

try:
    from sage.version import version as __sage_version__

    sage_version_min = semver.Version(9, 3)
    sage_version = semver.Version.parse(__sage_version__, optional_minor_and_patch=True)
    if sage_version < sage_version_min:
        errmsg = (
            f"The version of SageMath installed is not compatible with {program}."
            "\n"
            f"Please install SageMath version {sage_version_min} or higher."
        )
        raise exceptions.RequirementVersionError(errmsg)
except ModuleNotFoundError as e:
    errmsg = (
        "Unable to import SageMath."
        "\n"
        "Please make sure the module is installed and importable."
    )
    raise exceptions.MissingRequirementError(errmsg) from e
