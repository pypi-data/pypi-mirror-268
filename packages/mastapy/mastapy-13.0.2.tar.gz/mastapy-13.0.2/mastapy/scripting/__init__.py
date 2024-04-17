"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7570 import ApiEnumForAttribute
    from ._7571 import ApiVersion
    from ._7572 import SMTBitmap
    from ._7574 import MastaPropertyAttribute
    from ._7575 import PythonCommand
    from ._7576 import ScriptingCommand
    from ._7577 import ScriptingExecutionCommand
    from ._7578 import ScriptingObjectCommand
    from ._7579 import ApiVersioning
else:
    import_structure = {
        "_7570": ["ApiEnumForAttribute"],
        "_7571": ["ApiVersion"],
        "_7572": ["SMTBitmap"],
        "_7574": ["MastaPropertyAttribute"],
        "_7575": ["PythonCommand"],
        "_7576": ["ScriptingCommand"],
        "_7577": ["ScriptingExecutionCommand"],
        "_7578": ["ScriptingObjectCommand"],
        "_7579": ["ApiVersioning"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ApiEnumForAttribute",
    "ApiVersion",
    "SMTBitmap",
    "MastaPropertyAttribute",
    "PythonCommand",
    "ScriptingCommand",
    "ScriptingExecutionCommand",
    "ScriptingObjectCommand",
    "ApiVersioning",
)
