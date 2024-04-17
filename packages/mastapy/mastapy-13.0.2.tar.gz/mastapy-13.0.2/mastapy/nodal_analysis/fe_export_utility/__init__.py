"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._168 import BoundaryConditionType
    from ._169 import FEExportFormat
    from ._170 import FESubstructuringFileFormat
else:
    import_structure = {
        "_168": ["BoundaryConditionType"],
        "_169": ["FEExportFormat"],
        "_170": ["FESubstructuringFileFormat"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoundaryConditionType",
    "FEExportFormat",
    "FESubstructuringFileFormat",
)
