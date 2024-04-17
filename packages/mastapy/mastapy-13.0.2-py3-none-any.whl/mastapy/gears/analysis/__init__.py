"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1221 import AbstractGearAnalysis
    from ._1222 import AbstractGearMeshAnalysis
    from ._1223 import AbstractGearSetAnalysis
    from ._1224 import GearDesignAnalysis
    from ._1225 import GearImplementationAnalysis
    from ._1226 import GearImplementationAnalysisDutyCycle
    from ._1227 import GearImplementationDetail
    from ._1228 import GearMeshDesignAnalysis
    from ._1229 import GearMeshImplementationAnalysis
    from ._1230 import GearMeshImplementationAnalysisDutyCycle
    from ._1231 import GearMeshImplementationDetail
    from ._1232 import GearSetDesignAnalysis
    from ._1233 import GearSetGroupDutyCycle
    from ._1234 import GearSetImplementationAnalysis
    from ._1235 import GearSetImplementationAnalysisAbstract
    from ._1236 import GearSetImplementationAnalysisDutyCycle
    from ._1237 import GearSetImplementationDetail
else:
    import_structure = {
        "_1221": ["AbstractGearAnalysis"],
        "_1222": ["AbstractGearMeshAnalysis"],
        "_1223": ["AbstractGearSetAnalysis"],
        "_1224": ["GearDesignAnalysis"],
        "_1225": ["GearImplementationAnalysis"],
        "_1226": ["GearImplementationAnalysisDutyCycle"],
        "_1227": ["GearImplementationDetail"],
        "_1228": ["GearMeshDesignAnalysis"],
        "_1229": ["GearMeshImplementationAnalysis"],
        "_1230": ["GearMeshImplementationAnalysisDutyCycle"],
        "_1231": ["GearMeshImplementationDetail"],
        "_1232": ["GearSetDesignAnalysis"],
        "_1233": ["GearSetGroupDutyCycle"],
        "_1234": ["GearSetImplementationAnalysis"],
        "_1235": ["GearSetImplementationAnalysisAbstract"],
        "_1236": ["GearSetImplementationAnalysisDutyCycle"],
        "_1237": ["GearSetImplementationDetail"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearAnalysis",
    "AbstractGearMeshAnalysis",
    "AbstractGearSetAnalysis",
    "GearDesignAnalysis",
    "GearImplementationAnalysis",
    "GearImplementationAnalysisDutyCycle",
    "GearImplementationDetail",
    "GearMeshDesignAnalysis",
    "GearMeshImplementationAnalysis",
    "GearMeshImplementationAnalysisDutyCycle",
    "GearMeshImplementationDetail",
    "GearSetDesignAnalysis",
    "GearSetGroupDutyCycle",
    "GearSetImplementationAnalysis",
    "GearSetImplementationAnalysisAbstract",
    "GearSetImplementationAnalysisDutyCycle",
    "GearSetImplementationDetail",
)
