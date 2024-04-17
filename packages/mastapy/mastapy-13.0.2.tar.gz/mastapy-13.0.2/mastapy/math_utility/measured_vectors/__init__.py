"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1566 import AbstractForceAndDisplacementResults
    from ._1567 import ForceAndDisplacementResults
    from ._1568 import ForceResults
    from ._1569 import NodeResults
    from ._1570 import OverridableDisplacementBoundaryCondition
    from ._1571 import VectorWithLinearAndAngularComponents
else:
    import_structure = {
        "_1566": ["AbstractForceAndDisplacementResults"],
        "_1567": ["ForceAndDisplacementResults"],
        "_1568": ["ForceResults"],
        "_1569": ["NodeResults"],
        "_1570": ["OverridableDisplacementBoundaryCondition"],
        "_1571": ["VectorWithLinearAndAngularComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractForceAndDisplacementResults",
    "ForceAndDisplacementResults",
    "ForceResults",
    "NodeResults",
    "OverridableDisplacementBoundaryCondition",
    "VectorWithLinearAndAngularComponents",
)
