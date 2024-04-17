"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2583 import BeltDrive
    from ._2584 import BeltDriveType
    from ._2585 import Clutch
    from ._2586 import ClutchHalf
    from ._2587 import ClutchType
    from ._2588 import ConceptCoupling
    from ._2589 import ConceptCouplingHalf
    from ._2590 import ConceptCouplingHalfPositioning
    from ._2591 import Coupling
    from ._2592 import CouplingHalf
    from ._2593 import CrowningSpecification
    from ._2594 import CVT
    from ._2595 import CVTPulley
    from ._2596 import PartToPartShearCoupling
    from ._2597 import PartToPartShearCouplingHalf
    from ._2598 import Pulley
    from ._2599 import RigidConnectorStiffnessType
    from ._2600 import RigidConnectorTiltStiffnessTypes
    from ._2601 import RigidConnectorToothLocation
    from ._2602 import RigidConnectorToothSpacingType
    from ._2603 import RigidConnectorTypes
    from ._2604 import RollingRing
    from ._2605 import RollingRingAssembly
    from ._2606 import ShaftHubConnection
    from ._2607 import SplineLeadRelief
    from ._2608 import SpringDamper
    from ._2609 import SpringDamperHalf
    from ._2610 import Synchroniser
    from ._2611 import SynchroniserCone
    from ._2612 import SynchroniserHalf
    from ._2613 import SynchroniserPart
    from ._2614 import SynchroniserSleeve
    from ._2615 import TorqueConverter
    from ._2616 import TorqueConverterPump
    from ._2617 import TorqueConverterSpeedRatio
    from ._2618 import TorqueConverterTurbine
else:
    import_structure = {
        "_2583": ["BeltDrive"],
        "_2584": ["BeltDriveType"],
        "_2585": ["Clutch"],
        "_2586": ["ClutchHalf"],
        "_2587": ["ClutchType"],
        "_2588": ["ConceptCoupling"],
        "_2589": ["ConceptCouplingHalf"],
        "_2590": ["ConceptCouplingHalfPositioning"],
        "_2591": ["Coupling"],
        "_2592": ["CouplingHalf"],
        "_2593": ["CrowningSpecification"],
        "_2594": ["CVT"],
        "_2595": ["CVTPulley"],
        "_2596": ["PartToPartShearCoupling"],
        "_2597": ["PartToPartShearCouplingHalf"],
        "_2598": ["Pulley"],
        "_2599": ["RigidConnectorStiffnessType"],
        "_2600": ["RigidConnectorTiltStiffnessTypes"],
        "_2601": ["RigidConnectorToothLocation"],
        "_2602": ["RigidConnectorToothSpacingType"],
        "_2603": ["RigidConnectorTypes"],
        "_2604": ["RollingRing"],
        "_2605": ["RollingRingAssembly"],
        "_2606": ["ShaftHubConnection"],
        "_2607": ["SplineLeadRelief"],
        "_2608": ["SpringDamper"],
        "_2609": ["SpringDamperHalf"],
        "_2610": ["Synchroniser"],
        "_2611": ["SynchroniserCone"],
        "_2612": ["SynchroniserHalf"],
        "_2613": ["SynchroniserPart"],
        "_2614": ["SynchroniserSleeve"],
        "_2615": ["TorqueConverter"],
        "_2616": ["TorqueConverterPump"],
        "_2617": ["TorqueConverterSpeedRatio"],
        "_2618": ["TorqueConverterTurbine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "ConceptCouplingHalfPositioning",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "Pulley",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineLeadRelief",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)
