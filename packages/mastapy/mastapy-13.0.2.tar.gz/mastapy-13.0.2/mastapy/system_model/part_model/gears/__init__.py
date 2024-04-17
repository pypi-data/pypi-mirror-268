"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2517 import ActiveCylindricalGearSetDesignSelection
    from ._2518 import ActiveGearSetDesignSelection
    from ._2519 import ActiveGearSetDesignSelectionGroup
    from ._2520 import AGMAGleasonConicalGear
    from ._2521 import AGMAGleasonConicalGearSet
    from ._2522 import BevelDifferentialGear
    from ._2523 import BevelDifferentialGearSet
    from ._2524 import BevelDifferentialPlanetGear
    from ._2525 import BevelDifferentialSunGear
    from ._2526 import BevelGear
    from ._2527 import BevelGearSet
    from ._2528 import ConceptGear
    from ._2529 import ConceptGearSet
    from ._2530 import ConicalGear
    from ._2531 import ConicalGearSet
    from ._2532 import CylindricalGear
    from ._2533 import CylindricalGearSet
    from ._2534 import CylindricalPlanetGear
    from ._2535 import FaceGear
    from ._2536 import FaceGearSet
    from ._2537 import Gear
    from ._2538 import GearOrientations
    from ._2539 import GearSet
    from ._2540 import GearSetConfiguration
    from ._2541 import HypoidGear
    from ._2542 import HypoidGearSet
    from ._2543 import KlingelnbergCycloPalloidConicalGear
    from ._2544 import KlingelnbergCycloPalloidConicalGearSet
    from ._2545 import KlingelnbergCycloPalloidHypoidGear
    from ._2546 import KlingelnbergCycloPalloidHypoidGearSet
    from ._2547 import KlingelnbergCycloPalloidSpiralBevelGear
    from ._2548 import KlingelnbergCycloPalloidSpiralBevelGearSet
    from ._2549 import PlanetaryGearSet
    from ._2550 import SpiralBevelGear
    from ._2551 import SpiralBevelGearSet
    from ._2552 import StraightBevelDiffGear
    from ._2553 import StraightBevelDiffGearSet
    from ._2554 import StraightBevelGear
    from ._2555 import StraightBevelGearSet
    from ._2556 import StraightBevelPlanetGear
    from ._2557 import StraightBevelSunGear
    from ._2558 import WormGear
    from ._2559 import WormGearSet
    from ._2560 import ZerolBevelGear
    from ._2561 import ZerolBevelGearSet
else:
    import_structure = {
        "_2517": ["ActiveCylindricalGearSetDesignSelection"],
        "_2518": ["ActiveGearSetDesignSelection"],
        "_2519": ["ActiveGearSetDesignSelectionGroup"],
        "_2520": ["AGMAGleasonConicalGear"],
        "_2521": ["AGMAGleasonConicalGearSet"],
        "_2522": ["BevelDifferentialGear"],
        "_2523": ["BevelDifferentialGearSet"],
        "_2524": ["BevelDifferentialPlanetGear"],
        "_2525": ["BevelDifferentialSunGear"],
        "_2526": ["BevelGear"],
        "_2527": ["BevelGearSet"],
        "_2528": ["ConceptGear"],
        "_2529": ["ConceptGearSet"],
        "_2530": ["ConicalGear"],
        "_2531": ["ConicalGearSet"],
        "_2532": ["CylindricalGear"],
        "_2533": ["CylindricalGearSet"],
        "_2534": ["CylindricalPlanetGear"],
        "_2535": ["FaceGear"],
        "_2536": ["FaceGearSet"],
        "_2537": ["Gear"],
        "_2538": ["GearOrientations"],
        "_2539": ["GearSet"],
        "_2540": ["GearSetConfiguration"],
        "_2541": ["HypoidGear"],
        "_2542": ["HypoidGearSet"],
        "_2543": ["KlingelnbergCycloPalloidConicalGear"],
        "_2544": ["KlingelnbergCycloPalloidConicalGearSet"],
        "_2545": ["KlingelnbergCycloPalloidHypoidGear"],
        "_2546": ["KlingelnbergCycloPalloidHypoidGearSet"],
        "_2547": ["KlingelnbergCycloPalloidSpiralBevelGear"],
        "_2548": ["KlingelnbergCycloPalloidSpiralBevelGearSet"],
        "_2549": ["PlanetaryGearSet"],
        "_2550": ["SpiralBevelGear"],
        "_2551": ["SpiralBevelGearSet"],
        "_2552": ["StraightBevelDiffGear"],
        "_2553": ["StraightBevelDiffGearSet"],
        "_2554": ["StraightBevelGear"],
        "_2555": ["StraightBevelGearSet"],
        "_2556": ["StraightBevelPlanetGear"],
        "_2557": ["StraightBevelSunGear"],
        "_2558": ["WormGear"],
        "_2559": ["WormGearSet"],
        "_2560": ["ZerolBevelGear"],
        "_2561": ["ZerolBevelGearSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveCylindricalGearSetDesignSelection",
    "ActiveGearSetDesignSelection",
    "ActiveGearSetDesignSelectionGroup",
    "AGMAGleasonConicalGear",
    "AGMAGleasonConicalGearSet",
    "BevelDifferentialGear",
    "BevelDifferentialGearSet",
    "BevelDifferentialPlanetGear",
    "BevelDifferentialSunGear",
    "BevelGear",
    "BevelGearSet",
    "ConceptGear",
    "ConceptGearSet",
    "ConicalGear",
    "ConicalGearSet",
    "CylindricalGear",
    "CylindricalGearSet",
    "CylindricalPlanetGear",
    "FaceGear",
    "FaceGearSet",
    "Gear",
    "GearOrientations",
    "GearSet",
    "GearSetConfiguration",
    "HypoidGear",
    "HypoidGearSet",
    "KlingelnbergCycloPalloidConicalGear",
    "KlingelnbergCycloPalloidConicalGearSet",
    "KlingelnbergCycloPalloidHypoidGear",
    "KlingelnbergCycloPalloidHypoidGearSet",
    "KlingelnbergCycloPalloidSpiralBevelGear",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
    "PlanetaryGearSet",
    "SpiralBevelGear",
    "SpiralBevelGearSet",
    "StraightBevelDiffGear",
    "StraightBevelDiffGearSet",
    "StraightBevelGear",
    "StraightBevelGearSet",
    "StraightBevelPlanetGear",
    "StraightBevelSunGear",
    "WormGear",
    "WormGearSet",
    "ZerolBevelGear",
    "ZerolBevelGearSet",
)
