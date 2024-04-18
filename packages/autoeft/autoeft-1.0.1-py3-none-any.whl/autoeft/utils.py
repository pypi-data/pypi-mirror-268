import fnmatch
import fractions
from collections import Counter
from collections import defaultdict
from pathlib import Path
from pathlib import PosixPath

import rich.text
import sage.all
import sage.matrix.constructor
import semver
import yaml
from sage.matrix import matrix_integer_dense
from sage.rings import integer
from sage.rings.integer_ring import ZZ

from autoeft import exceptions
from autoeft.combinatorics import young


def type_matches(op_type, selection):
    counter = op_type.to_counter()

    def _type_matches(select):
        for field_name, multiplicity in select.items():
            if isinstance(multiplicity, str):
                if multiplicity == "+":
                    if counter[field_name] == 0:
                        return False
                elif multiplicity.startswith(".."):
                    if counter[field_name] > int(multiplicity[2:]):
                        return False
                elif multiplicity.endswith(".."):
                    if counter[field_name] < int(multiplicity[:-2]):
                        return False
                elif r := multiplicity.find(".."):
                    if r < 0:
                        errmsg = f"Invalid range: '{multiplicity}'"
                        raise exceptions.InvalidRangeException(errmsg)
                    if counter[field_name] < int(multiplicity[:r]) or counter[
                        field_name
                    ] > int(multiplicity[(r + 2) :]):
                        return False
                else:
                    errmsg = f"Invalid range: '{multiplicity}'"
                    raise exceptions.InvalidRangeException(errmsg)
            elif isinstance(multiplicity, int):
                if counter[field_name] != multiplicity:
                    return False
            else:
                errmsg = f"Invalid range: '{multiplicity}'"
                raise exceptions.InvalidRangeException(errmsg)
        return True

    return any(_type_matches(select) for select in selection)


def type_matches_legacy(op_type, selection):
    return any(fnmatch.fnmatch(repr(op_type), pattern) for pattern in selection)


class Fraction(fractions.Fraction):
    def __rich__(self):
        return rich.text.Text(str(self))

    def __neg__(self):
        return Fraction(super().__neg__())

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return cls(v)

    @classmethod
    def encode(cls, v):
        if v.denominator == 1:
            return v.numerator
        return str(v)


class IntegerMatrix(matrix_integer_dense.Matrix_integer_dense):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, matrix_integer_dense.Matrix_integer_dense):
            return v
        if isinstance(v, str):
            return sage.matrix.constructor.matrix(
                ZZ,
                [
                    [int(entry) for entry in row.lstrip("[").rstrip("]").split()]
                    for row in v.split("\n")
                ],
            )
        return ValueError


class Version(semver.Version):
    @classmethod
    def _parse(cls, version):
        return cls.parse(version)

    @classmethod
    def __get_validators__(cls):
        yield cls._parse


class Vector(Counter):
    def __add__(self, other):
        if isinstance(other, type(self)):
            (res := self.copy()).update(other)
            return res
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self.update(other)
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, type(self)):
            (res := self.copy()).subtract(other)
            return res
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, type(self)):
            self.subtract(other)
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, fractions.Fraction)):
            return type(self)({tab: coeff * other for tab, coeff in self.items()})
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, fractions.Fraction)):
            return type(self)({tab: other * coeff for tab, coeff in self.items()})
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (int, fractions.Fraction)):
            res = {tab: coeff * other for tab, coeff in self.items()}
            self.clear()
            self.update(res)
            return self
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, fractions.Fraction)):
            return type(self)({tab: coeff / other for tab, coeff in self.items()})
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, (int, fractions.Fraction)):
            res = {tab: coeff / other for tab, coeff in self.items()}
            self.clear()
            self.update(res)
            return self
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, fractions.Fraction)):
            return type(self)({tab: coeff // other for tab, coeff in self.items()})
        return NotImplemented

    def __ifloordiv__(self, other):
        if isinstance(other, (int, fractions.Fraction)):
            res = {tab: coeff // other for tab, coeff in self.items()}
            self.clear()
            self.update(res)
            return self
        return NotImplemented

    def __neg__(self):
        return -1 * self

    def __pos__(self):
        return 1 * self

    def __abs__(self):
        return type(self)({tab: abs(coeff) for tab, coeff in self.items()})

    def reduce(self):
        res = {tab: coeff for tab, coeff in self.items() if coeff}
        self.clear()
        self.update(res)
        return self

    def is_zero(self):
        return not bool(self.reduce())


class FlowSeq(list):
    pass


class FlowMap(dict):
    pass


class BlockMap(dict):
    pass


class YamlDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def flowseq_representer(dumper, data):
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True)


def flowmap_representer(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data, flow_style=True)


def blockmap_representer(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data, flow_style=False)


def matrix_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style="|")


def version_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data))


def path_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data))


YamlDumper.add_representer(defaultdict, yaml.representer.Representer.represent_dict)
YamlDumper.add_representer(FlowSeq, flowseq_representer)
YamlDumper.add_representer(FlowMap, flowmap_representer)
YamlDumper.add_representer(BlockMap, blockmap_representer)
YamlDumper.add_representer(integer.Integer, yaml.representer.Representer.represent_int)
YamlDumper.add_representer(young.Partition, yaml.representer.Representer.represent_list)
YamlDumper.add_representer(
    matrix_integer_dense.Matrix_integer_dense,
    matrix_representer,
)
YamlDumper.add_representer(semver.Version, version_representer)
YamlDumper.add_representer(Version, version_representer)
YamlDumper.add_representer(Path, path_representer)
YamlDumper.add_representer(PosixPath, path_representer)


def non_redundant_json(*args, **kwargs):
    import json

    data = args[0]
    for datum in data["fields"].values():
        del datum["symmetries"]
    return json.dumps(data, *args[1:], **kwargs)


def esc(s: str) -> str:
    return s.replace("+", "_hc")
