"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2306 import AGMAGleasonConicalGearMesh
    from ._2307 import AGMAGleasonConicalGearTeethSocket
    from ._2308 import BevelDifferentialGearMesh
    from ._2309 import BevelDifferentialGearTeethSocket
    from ._2310 import BevelGearMesh
    from ._2311 import BevelGearTeethSocket
    from ._2312 import ConceptGearMesh
    from ._2313 import ConceptGearTeethSocket
    from ._2314 import ConicalGearMesh
    from ._2315 import ConicalGearTeethSocket
    from ._2316 import CylindricalGearMesh
    from ._2317 import CylindricalGearTeethSocket
    from ._2318 import FaceGearMesh
    from ._2319 import FaceGearTeethSocket
    from ._2320 import GearMesh
    from ._2321 import GearTeethSocket
    from ._2322 import HypoidGearMesh
    from ._2323 import HypoidGearTeethSocket
    from ._2324 import KlingelnbergConicalGearTeethSocket
    from ._2325 import KlingelnbergCycloPalloidConicalGearMesh
    from ._2326 import KlingelnbergCycloPalloidHypoidGearMesh
    from ._2327 import KlingelnbergCycloPalloidSpiralBevelGearMesh
    from ._2328 import KlingelnbergHypoidGearTeethSocket
    from ._2329 import KlingelnbergSpiralBevelGearTeethSocket
    from ._2330 import SpiralBevelGearMesh
    from ._2331 import SpiralBevelGearTeethSocket
    from ._2332 import StraightBevelDiffGearMesh
    from ._2333 import StraightBevelDiffGearTeethSocket
    from ._2334 import StraightBevelGearMesh
    from ._2335 import StraightBevelGearTeethSocket
    from ._2336 import WormGearMesh
    from ._2337 import WormGearTeethSocket
    from ._2338 import ZerolBevelGearMesh
    from ._2339 import ZerolBevelGearTeethSocket
else:
    import_structure = {
        "_2306": ["AGMAGleasonConicalGearMesh"],
        "_2307": ["AGMAGleasonConicalGearTeethSocket"],
        "_2308": ["BevelDifferentialGearMesh"],
        "_2309": ["BevelDifferentialGearTeethSocket"],
        "_2310": ["BevelGearMesh"],
        "_2311": ["BevelGearTeethSocket"],
        "_2312": ["ConceptGearMesh"],
        "_2313": ["ConceptGearTeethSocket"],
        "_2314": ["ConicalGearMesh"],
        "_2315": ["ConicalGearTeethSocket"],
        "_2316": ["CylindricalGearMesh"],
        "_2317": ["CylindricalGearTeethSocket"],
        "_2318": ["FaceGearMesh"],
        "_2319": ["FaceGearTeethSocket"],
        "_2320": ["GearMesh"],
        "_2321": ["GearTeethSocket"],
        "_2322": ["HypoidGearMesh"],
        "_2323": ["HypoidGearTeethSocket"],
        "_2324": ["KlingelnbergConicalGearTeethSocket"],
        "_2325": ["KlingelnbergCycloPalloidConicalGearMesh"],
        "_2326": ["KlingelnbergCycloPalloidHypoidGearMesh"],
        "_2327": ["KlingelnbergCycloPalloidSpiralBevelGearMesh"],
        "_2328": ["KlingelnbergHypoidGearTeethSocket"],
        "_2329": ["KlingelnbergSpiralBevelGearTeethSocket"],
        "_2330": ["SpiralBevelGearMesh"],
        "_2331": ["SpiralBevelGearTeethSocket"],
        "_2332": ["StraightBevelDiffGearMesh"],
        "_2333": ["StraightBevelDiffGearTeethSocket"],
        "_2334": ["StraightBevelGearMesh"],
        "_2335": ["StraightBevelGearTeethSocket"],
        "_2336": ["WormGearMesh"],
        "_2337": ["WormGearTeethSocket"],
        "_2338": ["ZerolBevelGearMesh"],
        "_2339": ["ZerolBevelGearTeethSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMesh",
    "AGMAGleasonConicalGearTeethSocket",
    "BevelDifferentialGearMesh",
    "BevelDifferentialGearTeethSocket",
    "BevelGearMesh",
    "BevelGearTeethSocket",
    "ConceptGearMesh",
    "ConceptGearTeethSocket",
    "ConicalGearMesh",
    "ConicalGearTeethSocket",
    "CylindricalGearMesh",
    "CylindricalGearTeethSocket",
    "FaceGearMesh",
    "FaceGearTeethSocket",
    "GearMesh",
    "GearTeethSocket",
    "HypoidGearMesh",
    "HypoidGearTeethSocket",
    "KlingelnbergConicalGearTeethSocket",
    "KlingelnbergCycloPalloidConicalGearMesh",
    "KlingelnbergCycloPalloidHypoidGearMesh",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
    "KlingelnbergHypoidGearTeethSocket",
    "KlingelnbergSpiralBevelGearTeethSocket",
    "SpiralBevelGearMesh",
    "SpiralBevelGearTeethSocket",
    "StraightBevelDiffGearMesh",
    "StraightBevelDiffGearTeethSocket",
    "StraightBevelGearMesh",
    "StraightBevelGearTeethSocket",
    "WormGearMesh",
    "WormGearTeethSocket",
    "ZerolBevelGearMesh",
    "ZerolBevelGearTeethSocket",
)
