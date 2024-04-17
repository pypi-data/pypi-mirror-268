"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2117 import InnerRingFittingThermalResults
    from ._2118 import InterferenceComponents
    from ._2119 import OuterRingFittingThermalResults
    from ._2120 import RingFittingThermalResults
else:
    import_structure = {
        "_2117": ["InnerRingFittingThermalResults"],
        "_2118": ["InterferenceComponents"],
        "_2119": ["OuterRingFittingThermalResults"],
        "_2120": ["RingFittingThermalResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "InnerRingFittingThermalResults",
    "InterferenceComponents",
    "OuterRingFittingThermalResults",
    "RingFittingThermalResults",
)
