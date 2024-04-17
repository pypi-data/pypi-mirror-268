"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6276 import CombinationAnalysis
    from ._6277 import FlexiblePinAnalysis
    from ._6278 import FlexiblePinAnalysisConceptLevel
    from ._6279 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6280 import FlexiblePinAnalysisGearAndBearingRating
    from ._6281 import FlexiblePinAnalysisManufactureLevel
    from ._6282 import FlexiblePinAnalysisOptions
    from ._6283 import FlexiblePinAnalysisStopStartAnalysis
    from ._6284 import WindTurbineCertificationReport
else:
    import_structure = {
        "_6276": ["CombinationAnalysis"],
        "_6277": ["FlexiblePinAnalysis"],
        "_6278": ["FlexiblePinAnalysisConceptLevel"],
        "_6279": ["FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"],
        "_6280": ["FlexiblePinAnalysisGearAndBearingRating"],
        "_6281": ["FlexiblePinAnalysisManufactureLevel"],
        "_6282": ["FlexiblePinAnalysisOptions"],
        "_6283": ["FlexiblePinAnalysisStopStartAnalysis"],
        "_6284": ["WindTurbineCertificationReport"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CombinationAnalysis",
    "FlexiblePinAnalysis",
    "FlexiblePinAnalysisConceptLevel",
    "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
    "FlexiblePinAnalysisGearAndBearingRating",
    "FlexiblePinAnalysisManufactureLevel",
    "FlexiblePinAnalysisOptions",
    "FlexiblePinAnalysisStopStartAnalysis",
    "WindTurbineCertificationReport",
)
