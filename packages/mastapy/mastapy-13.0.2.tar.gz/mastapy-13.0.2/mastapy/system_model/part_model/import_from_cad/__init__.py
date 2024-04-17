"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2500 import AbstractShaftFromCAD
    from ._2501 import ClutchFromCAD
    from ._2502 import ComponentFromCAD
    from ._2503 import ConceptBearingFromCAD
    from ._2504 import ConnectorFromCAD
    from ._2505 import CylindricalGearFromCAD
    from ._2506 import CylindricalGearInPlanetarySetFromCAD
    from ._2507 import CylindricalPlanetGearFromCAD
    from ._2508 import CylindricalRingGearFromCAD
    from ._2509 import CylindricalSunGearFromCAD
    from ._2510 import HousedOrMounted
    from ._2511 import MountableComponentFromCAD
    from ._2512 import PlanetShaftFromCAD
    from ._2513 import PulleyFromCAD
    from ._2514 import RigidConnectorFromCAD
    from ._2515 import RollingBearingFromCAD
    from ._2516 import ShaftFromCAD
else:
    import_structure = {
        "_2500": ["AbstractShaftFromCAD"],
        "_2501": ["ClutchFromCAD"],
        "_2502": ["ComponentFromCAD"],
        "_2503": ["ConceptBearingFromCAD"],
        "_2504": ["ConnectorFromCAD"],
        "_2505": ["CylindricalGearFromCAD"],
        "_2506": ["CylindricalGearInPlanetarySetFromCAD"],
        "_2507": ["CylindricalPlanetGearFromCAD"],
        "_2508": ["CylindricalRingGearFromCAD"],
        "_2509": ["CylindricalSunGearFromCAD"],
        "_2510": ["HousedOrMounted"],
        "_2511": ["MountableComponentFromCAD"],
        "_2512": ["PlanetShaftFromCAD"],
        "_2513": ["PulleyFromCAD"],
        "_2514": ["RigidConnectorFromCAD"],
        "_2515": ["RollingBearingFromCAD"],
        "_2516": ["ShaftFromCAD"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
)
