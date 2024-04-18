from typing import Any


def tex(obj: Any) -> str:
    """Call the TeX representation of an object."""
    if hasattr(type(obj), "__tex__"):
        return type(obj).__tex__(obj)
    return str(obj)
