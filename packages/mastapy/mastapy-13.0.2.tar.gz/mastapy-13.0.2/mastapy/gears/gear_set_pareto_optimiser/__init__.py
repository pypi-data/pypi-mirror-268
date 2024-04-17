"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._905 import BarForPareto
    from ._906 import CandidateDisplayChoice
    from ._907 import ChartInfoBase
    from ._908 import CylindricalGearSetParetoOptimiser
    from ._909 import DesignSpaceSearchBase
    from ._910 import DesignSpaceSearchCandidateBase
    from ._911 import FaceGearSetParetoOptimiser
    from ._912 import GearNameMapper
    from ._913 import GearNamePicker
    from ._914 import GearSetOptimiserCandidate
    from ._915 import GearSetParetoOptimiser
    from ._916 import HypoidGearSetParetoOptimiser
    from ._917 import InputSliderForPareto
    from ._918 import LargerOrSmaller
    from ._919 import MicroGeometryDesignSpaceSearch
    from ._920 import MicroGeometryDesignSpaceSearchCandidate
    from ._921 import MicroGeometryDesignSpaceSearchChartInformation
    from ._922 import MicroGeometryDesignSpaceSearchStrategyDatabase
    from ._923 import MicroGeometryGearSetDesignSpaceSearch
    from ._924 import MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
    from ._925 import MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
    from ._926 import OptimisationTarget
    from ._927 import ParetoConicalRatingOptimisationStrategyDatabase
    from ._928 import ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
    from ._929 import ParetoCylindricalGearSetOptimisationStrategyDatabase
    from ._930 import ParetoCylindricalRatingOptimisationStrategyDatabase
    from ._931 import ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
    from ._932 import ParetoFaceGearSetOptimisationStrategyDatabase
    from ._933 import ParetoFaceRatingOptimisationStrategyDatabase
    from ._934 import ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
    from ._935 import ParetoHypoidGearSetOptimisationStrategyDatabase
    from ._936 import ParetoOptimiserChartInformation
    from ._937 import ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._938 import ParetoSpiralBevelGearSetOptimisationStrategyDatabase
    from ._939 import ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._940 import ParetoStraightBevelGearSetOptimisationStrategyDatabase
    from ._941 import ReasonsForInvalidDesigns
    from ._942 import SpiralBevelGearSetParetoOptimiser
    from ._943 import StraightBevelGearSetParetoOptimiser
else:
    import_structure = {
        "_905": ["BarForPareto"],
        "_906": ["CandidateDisplayChoice"],
        "_907": ["ChartInfoBase"],
        "_908": ["CylindricalGearSetParetoOptimiser"],
        "_909": ["DesignSpaceSearchBase"],
        "_910": ["DesignSpaceSearchCandidateBase"],
        "_911": ["FaceGearSetParetoOptimiser"],
        "_912": ["GearNameMapper"],
        "_913": ["GearNamePicker"],
        "_914": ["GearSetOptimiserCandidate"],
        "_915": ["GearSetParetoOptimiser"],
        "_916": ["HypoidGearSetParetoOptimiser"],
        "_917": ["InputSliderForPareto"],
        "_918": ["LargerOrSmaller"],
        "_919": ["MicroGeometryDesignSpaceSearch"],
        "_920": ["MicroGeometryDesignSpaceSearchCandidate"],
        "_921": ["MicroGeometryDesignSpaceSearchChartInformation"],
        "_922": ["MicroGeometryDesignSpaceSearchStrategyDatabase"],
        "_923": ["MicroGeometryGearSetDesignSpaceSearch"],
        "_924": ["MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"],
        "_925": ["MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase"],
        "_926": ["OptimisationTarget"],
        "_927": ["ParetoConicalRatingOptimisationStrategyDatabase"],
        "_928": ["ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"],
        "_929": ["ParetoCylindricalGearSetOptimisationStrategyDatabase"],
        "_930": ["ParetoCylindricalRatingOptimisationStrategyDatabase"],
        "_931": ["ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase"],
        "_932": ["ParetoFaceGearSetOptimisationStrategyDatabase"],
        "_933": ["ParetoFaceRatingOptimisationStrategyDatabase"],
        "_934": ["ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase"],
        "_935": ["ParetoHypoidGearSetOptimisationStrategyDatabase"],
        "_936": ["ParetoOptimiserChartInformation"],
        "_937": ["ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_938": ["ParetoSpiralBevelGearSetOptimisationStrategyDatabase"],
        "_939": ["ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_940": ["ParetoStraightBevelGearSetOptimisationStrategyDatabase"],
        "_941": ["ReasonsForInvalidDesigns"],
        "_942": ["SpiralBevelGearSetParetoOptimiser"],
        "_943": ["StraightBevelGearSetParetoOptimiser"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BarForPareto",
    "CandidateDisplayChoice",
    "ChartInfoBase",
    "CylindricalGearSetParetoOptimiser",
    "DesignSpaceSearchBase",
    "DesignSpaceSearchCandidateBase",
    "FaceGearSetParetoOptimiser",
    "GearNameMapper",
    "GearNamePicker",
    "GearSetOptimiserCandidate",
    "GearSetParetoOptimiser",
    "HypoidGearSetParetoOptimiser",
    "InputSliderForPareto",
    "LargerOrSmaller",
    "MicroGeometryDesignSpaceSearch",
    "MicroGeometryDesignSpaceSearchCandidate",
    "MicroGeometryDesignSpaceSearchChartInformation",
    "MicroGeometryDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDesignSpaceSearch",
    "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
    "OptimisationTarget",
    "ParetoConicalRatingOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
    "ParetoCylindricalRatingOptimisationStrategyDatabase",
    "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
    "ParetoFaceRatingOptimisationStrategyDatabase",
    "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoHypoidGearSetOptimisationStrategyDatabase",
    "ParetoOptimiserChartInformation",
    "ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetOptimisationStrategyDatabase",
    "ReasonsForInvalidDesigns",
    "SpiralBevelGearSetParetoOptimiser",
    "StraightBevelGearSetParetoOptimiser",
)
