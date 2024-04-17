"""__init__.py

All modules in this sub-package were hand-written.
"""

from .helpers import (
    _MASTA_PROPERTIES,
    _MASTA_SETTERS,
    DebugEnvironment,
    MastaInitException,
    MastaPropertyException,
    MastaPropertyTypeException,
    masta_property,
    _mastafile_hook,
    masta_before,
    masta_after,
    _match_versions,
    _init_no_api_access,
    init,
    start_debugging,
)
from .version import __version__, __api_version__
from .tuple_with_name import TupleWithName
from .cast_exception import CastException
from .mastapy_import_exception import MastapyImportException
from .overridable_constructor import overridable
from .measurement_type import MeasurementType
from .type_enforcement import TypeCheckException
from .licences import masta_licences


__all__ = (
    "_MASTA_PROPERTIES",
    "_MASTA_SETTERS",
    "DebugEnvironment",
    "MastaInitException",
    "MastaPropertyException",
    "MastaPropertyTypeException",
    "masta_property",
    "_mastafile_hook",
    "masta_before",
    "masta_after",
    "_init_no_api_access",
    "init",
    "start_debugging",
    "__version__",
    "__api_version__",
    "TupleWithName",
    "CastException",
    "MastapyImportException",
    "overridable",
    "MeasurementType",
    "TypeCheckException",
    "masta_licences",
)


try:
    _match_versions()
except ImportError:
    pass
