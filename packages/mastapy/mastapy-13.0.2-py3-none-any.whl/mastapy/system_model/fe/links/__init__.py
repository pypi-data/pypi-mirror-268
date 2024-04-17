"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2425 import FELink
    from ._2426 import ElectricMachineStatorFELink
    from ._2427 import FELinkWithSelection
    from ._2428 import GearMeshFELink
    from ._2429 import GearWithDuplicatedMeshesFELink
    from ._2430 import MultiAngleConnectionFELink
    from ._2431 import MultiNodeConnectorFELink
    from ._2432 import MultiNodeFELink
    from ._2433 import PlanetaryConnectorMultiNodeFELink
    from ._2434 import PlanetBasedFELink
    from ._2435 import PlanetCarrierFELink
    from ._2436 import PointLoadFELink
    from ._2437 import RollingRingConnectionFELink
    from ._2438 import ShaftHubConnectionFELink
    from ._2439 import SingleNodeFELink
else:
    import_structure = {
        "_2425": ["FELink"],
        "_2426": ["ElectricMachineStatorFELink"],
        "_2427": ["FELinkWithSelection"],
        "_2428": ["GearMeshFELink"],
        "_2429": ["GearWithDuplicatedMeshesFELink"],
        "_2430": ["MultiAngleConnectionFELink"],
        "_2431": ["MultiNodeConnectorFELink"],
        "_2432": ["MultiNodeFELink"],
        "_2433": ["PlanetaryConnectorMultiNodeFELink"],
        "_2434": ["PlanetBasedFELink"],
        "_2435": ["PlanetCarrierFELink"],
        "_2436": ["PointLoadFELink"],
        "_2437": ["RollingRingConnectionFELink"],
        "_2438": ["ShaftHubConnectionFELink"],
        "_2439": ["SingleNodeFELink"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FELink",
    "ElectricMachineStatorFELink",
    "FELinkWithSelection",
    "GearMeshFELink",
    "GearWithDuplicatedMeshesFELink",
    "MultiAngleConnectionFELink",
    "MultiNodeConnectorFELink",
    "MultiNodeFELink",
    "PlanetaryConnectorMultiNodeFELink",
    "PlanetBasedFELink",
    "PlanetCarrierFELink",
    "PointLoadFELink",
    "RollingRingConnectionFELink",
    "ShaftHubConnectionFELink",
    "SingleNodeFELink",
)
