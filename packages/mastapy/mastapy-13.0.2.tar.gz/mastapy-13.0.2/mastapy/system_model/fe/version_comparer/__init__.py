"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2419 import DesignResults
    from ._2420 import FESubstructureResults
    from ._2421 import FESubstructureVersionComparer
    from ._2422 import LoadCaseResults
    from ._2423 import LoadCasesToRun
    from ._2424 import NodeComparisonResult
else:
    import_structure = {
        "_2419": ["DesignResults"],
        "_2420": ["FESubstructureResults"],
        "_2421": ["FESubstructureVersionComparer"],
        "_2422": ["LoadCaseResults"],
        "_2423": ["LoadCasesToRun"],
        "_2424": ["NodeComparisonResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignResults",
    "FESubstructureResults",
    "FESubstructureVersionComparer",
    "LoadCaseResults",
    "LoadCasesToRun",
    "NodeComparisonResult",
)
