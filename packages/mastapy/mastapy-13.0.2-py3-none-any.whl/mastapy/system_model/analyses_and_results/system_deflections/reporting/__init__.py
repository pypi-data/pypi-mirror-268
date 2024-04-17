"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2850 import CylindricalGearMeshMisalignmentValue
    from ._2851 import FlexibleGearChart
    from ._2852 import GearInMeshDeflectionResults
    from ._2853 import MeshDeflectionResults
    from ._2854 import PlanetCarrierWindup
    from ._2855 import PlanetPinWindup
    from ._2856 import RigidlyConnectedComponentGroupSystemDeflection
    from ._2857 import ShaftSystemDeflectionSectionsReport
    from ._2858 import SplineFlankContactReporting
else:
    import_structure = {
        "_2850": ["CylindricalGearMeshMisalignmentValue"],
        "_2851": ["FlexibleGearChart"],
        "_2852": ["GearInMeshDeflectionResults"],
        "_2853": ["MeshDeflectionResults"],
        "_2854": ["PlanetCarrierWindup"],
        "_2855": ["PlanetPinWindup"],
        "_2856": ["RigidlyConnectedComponentGroupSystemDeflection"],
        "_2857": ["ShaftSystemDeflectionSectionsReport"],
        "_2858": ["SplineFlankContactReporting"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshMisalignmentValue",
    "FlexibleGearChart",
    "GearInMeshDeflectionResults",
    "MeshDeflectionResults",
    "PlanetCarrierWindup",
    "PlanetPinWindup",
    "RigidlyConnectedComponentGroupSystemDeflection",
    "ShaftSystemDeflectionSectionsReport",
    "SplineFlankContactReporting",
)
