"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2493 import ConcentricOrParallelPartGroup
    from ._2494 import ConcentricPartGroup
    from ._2495 import ConcentricPartGroupParallelToThis
    from ._2496 import DesignMeasurements
    from ._2497 import ParallelPartGroup
    from ._2498 import ParallelPartGroupSelection
    from ._2499 import PartGroup
else:
    import_structure = {
        "_2493": ["ConcentricOrParallelPartGroup"],
        "_2494": ["ConcentricPartGroup"],
        "_2495": ["ConcentricPartGroupParallelToThis"],
        "_2496": ["DesignMeasurements"],
        "_2497": ["ParallelPartGroup"],
        "_2498": ["ParallelPartGroupSelection"],
        "_2499": ["PartGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConcentricOrParallelPartGroup",
    "ConcentricPartGroup",
    "ConcentricPartGroupParallelToThis",
    "DesignMeasurements",
    "ParallelPartGroup",
    "ParallelPartGroupSelection",
    "PartGroup",
)
