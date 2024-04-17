"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1804 import GearMeshForTE
    from ._1805 import GearOrderForTE
    from ._1806 import GearPositions
    from ._1807 import HarmonicOrderForTE
    from ._1808 import LabelOnlyOrder
    from ._1809 import OrderForTE
    from ._1810 import OrderSelector
    from ._1811 import OrderWithRadius
    from ._1812 import RollingBearingOrder
    from ._1813 import ShaftOrderForTE
    from ._1814 import UserDefinedOrderForTE
else:
    import_structure = {
        "_1804": ["GearMeshForTE"],
        "_1805": ["GearOrderForTE"],
        "_1806": ["GearPositions"],
        "_1807": ["HarmonicOrderForTE"],
        "_1808": ["LabelOnlyOrder"],
        "_1809": ["OrderForTE"],
        "_1810": ["OrderSelector"],
        "_1811": ["OrderWithRadius"],
        "_1812": ["RollingBearingOrder"],
        "_1813": ["ShaftOrderForTE"],
        "_1814": ["UserDefinedOrderForTE"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMeshForTE",
    "GearOrderForTE",
    "GearPositions",
    "HarmonicOrderForTE",
    "LabelOnlyOrder",
    "OrderForTE",
    "OrderSelector",
    "OrderWithRadius",
    "RollingBearingOrder",
    "ShaftOrderForTE",
    "UserDefinedOrderForTE",
)
