"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1394 import DetailedRigidConnectorDesign
    from ._1395 import DetailedRigidConnectorHalfDesign
else:
    import_structure = {
        "_1394": ["DetailedRigidConnectorDesign"],
        "_1395": ["DetailedRigidConnectorHalfDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DetailedRigidConnectorDesign",
    "DetailedRigidConnectorHalfDesign",
)
