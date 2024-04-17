"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1746 import ScriptingSetup
    from ._1747 import UserDefinedPropertyKey
    from ._1748 import UserSpecifiedData
else:
    import_structure = {
        "_1746": ["ScriptingSetup"],
        "_1747": ["UserDefinedPropertyKey"],
        "_1748": ["UserSpecifiedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ScriptingSetup",
    "UserDefinedPropertyKey",
    "UserSpecifiedData",
)
