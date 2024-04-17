"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2268 import AdvancedTimeSteppingAnalysisForModulationModeViewOptions
    from ._2269 import ExcitationAnalysisViewOption
    from ._2270 import ModalContributionViewOptions
else:
    import_structure = {
        "_2268": ["AdvancedTimeSteppingAnalysisForModulationModeViewOptions"],
        "_2269": ["ExcitationAnalysisViewOption"],
        "_2270": ["ModalContributionViewOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
    "ExcitationAnalysisViewOption",
    "ModalContributionViewOptions",
)
