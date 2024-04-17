"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1245 import ProSolveMpcType
    from ._1246 import ProSolveSolverType
else:
    import_structure = {
        "_1245": ["ProSolveMpcType"],
        "_1246": ["ProSolveSolverType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProSolveMpcType",
    "ProSolveSolverType",
)
