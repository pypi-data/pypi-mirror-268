"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4724 import CalculateFullFEResultsForMode
    from ._4725 import CampbellDiagramReport
    from ._4726 import ComponentPerModeResult
    from ._4727 import DesignEntityModalAnalysisGroupResults
    from ._4728 import ModalCMSResultsForModeAndFE
    from ._4729 import PerModeResultsReport
    from ._4730 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4731 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4732 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4733 import ShaftPerModeResult
    from ._4734 import SingleExcitationResultsModalAnalysis
    from ._4735 import SingleModeResults
else:
    import_structure = {
        "_4724": ["CalculateFullFEResultsForMode"],
        "_4725": ["CampbellDiagramReport"],
        "_4726": ["ComponentPerModeResult"],
        "_4727": ["DesignEntityModalAnalysisGroupResults"],
        "_4728": ["ModalCMSResultsForModeAndFE"],
        "_4729": ["PerModeResultsReport"],
        "_4730": ["RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"],
        "_4731": ["RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis"],
        "_4732": ["RigidlyConnectedDesignEntityGroupModalAnalysis"],
        "_4733": ["ShaftPerModeResult"],
        "_4734": ["SingleExcitationResultsModalAnalysis"],
        "_4735": ["SingleModeResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculateFullFEResultsForMode",
    "CampbellDiagramReport",
    "ComponentPerModeResult",
    "DesignEntityModalAnalysisGroupResults",
    "ModalCMSResultsForModeAndFE",
    "PerModeResultsReport",
    "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    "RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis",
    "RigidlyConnectedDesignEntityGroupModalAnalysis",
    "ShaftPerModeResult",
    "SingleExcitationResultsModalAnalysis",
    "SingleModeResults",
)
