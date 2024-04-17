"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5537 import AbstractAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5538 import AbstractShaftCompoundMultibodyDynamicsAnalysis
    from ._5539 import AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
    from ._5540 import (
        AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5541 import AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
    from ._5542 import AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5543 import AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5544 import AssemblyCompoundMultibodyDynamicsAnalysis
    from ._5545 import BearingCompoundMultibodyDynamicsAnalysis
    from ._5546 import BeltConnectionCompoundMultibodyDynamicsAnalysis
    from ._5547 import BeltDriveCompoundMultibodyDynamicsAnalysis
    from ._5548 import BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
    from ._5549 import BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5550 import BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
    from ._5551 import BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5552 import BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
    from ._5553 import BevelGearCompoundMultibodyDynamicsAnalysis
    from ._5554 import BevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5555 import BevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5556 import BoltCompoundMultibodyDynamicsAnalysis
    from ._5557 import BoltedJointCompoundMultibodyDynamicsAnalysis
    from ._5558 import ClutchCompoundMultibodyDynamicsAnalysis
    from ._5559 import ClutchConnectionCompoundMultibodyDynamicsAnalysis
    from ._5560 import ClutchHalfCompoundMultibodyDynamicsAnalysis
    from ._5561 import CoaxialConnectionCompoundMultibodyDynamicsAnalysis
    from ._5562 import ComponentCompoundMultibodyDynamicsAnalysis
    from ._5563 import ConceptCouplingCompoundMultibodyDynamicsAnalysis
    from ._5564 import ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5565 import ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5566 import ConceptGearCompoundMultibodyDynamicsAnalysis
    from ._5567 import ConceptGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5568 import ConceptGearSetCompoundMultibodyDynamicsAnalysis
    from ._5569 import ConicalGearCompoundMultibodyDynamicsAnalysis
    from ._5570 import ConicalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5571 import ConicalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5572 import ConnectionCompoundMultibodyDynamicsAnalysis
    from ._5573 import ConnectorCompoundMultibodyDynamicsAnalysis
    from ._5574 import CouplingCompoundMultibodyDynamicsAnalysis
    from ._5575 import CouplingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5576 import CouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5577 import CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
    from ._5578 import CVTCompoundMultibodyDynamicsAnalysis
    from ._5579 import CVTPulleyCompoundMultibodyDynamicsAnalysis
    from ._5580 import CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5581 import (
        CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5582 import CycloidalDiscCompoundMultibodyDynamicsAnalysis
    from ._5583 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5584 import CylindricalGearCompoundMultibodyDynamicsAnalysis
    from ._5585 import CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5586 import CylindricalGearSetCompoundMultibodyDynamicsAnalysis
    from ._5587 import CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5588 import DatumCompoundMultibodyDynamicsAnalysis
    from ._5589 import ExternalCADModelCompoundMultibodyDynamicsAnalysis
    from ._5590 import FaceGearCompoundMultibodyDynamicsAnalysis
    from ._5591 import FaceGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5592 import FaceGearSetCompoundMultibodyDynamicsAnalysis
    from ._5593 import FEPartCompoundMultibodyDynamicsAnalysis
    from ._5594 import FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5595 import GearCompoundMultibodyDynamicsAnalysis
    from ._5596 import GearMeshCompoundMultibodyDynamicsAnalysis
    from ._5597 import GearSetCompoundMultibodyDynamicsAnalysis
    from ._5598 import GuideDxfModelCompoundMultibodyDynamicsAnalysis
    from ._5599 import HypoidGearCompoundMultibodyDynamicsAnalysis
    from ._5600 import HypoidGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5601 import HypoidGearSetCompoundMultibodyDynamicsAnalysis
    from ._5602 import (
        InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5603 import (
        KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis,
    )
    from ._5604 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis,
    )
    from ._5605 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis,
    )
    from ._5606 import (
        KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis,
    )
    from ._5607 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis,
    )
    from ._5608 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis,
    )
    from ._5609 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis,
    )
    from ._5610 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis,
    )
    from ._5611 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis,
    )
    from ._5612 import MassDiscCompoundMultibodyDynamicsAnalysis
    from ._5613 import MeasurementComponentCompoundMultibodyDynamicsAnalysis
    from ._5614 import MountableComponentCompoundMultibodyDynamicsAnalysis
    from ._5615 import OilSealCompoundMultibodyDynamicsAnalysis
    from ._5616 import PartCompoundMultibodyDynamicsAnalysis
    from ._5617 import PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
    from ._5618 import (
        PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5619 import PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
    from ._5620 import PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
    from ._5621 import PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
    from ._5622 import PlanetCarrierCompoundMultibodyDynamicsAnalysis
    from ._5623 import PointLoadCompoundMultibodyDynamicsAnalysis
    from ._5624 import PowerLoadCompoundMultibodyDynamicsAnalysis
    from ._5625 import PulleyCompoundMultibodyDynamicsAnalysis
    from ._5626 import RingPinsCompoundMultibodyDynamicsAnalysis
    from ._5627 import RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
    from ._5628 import RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5629 import RollingRingCompoundMultibodyDynamicsAnalysis
    from ._5630 import RollingRingConnectionCompoundMultibodyDynamicsAnalysis
    from ._5631 import RootAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5632 import ShaftCompoundMultibodyDynamicsAnalysis
    from ._5633 import ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
    from ._5634 import (
        ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis,
    )
    from ._5635 import SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
    from ._5636 import SpiralBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5637 import SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5638 import SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5639 import SpringDamperCompoundMultibodyDynamicsAnalysis
    from ._5640 import SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
    from ._5641 import SpringDamperHalfCompoundMultibodyDynamicsAnalysis
    from ._5642 import StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
    from ._5643 import StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5644 import StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
    from ._5645 import StraightBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5646 import StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5647 import StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
    from ._5648 import StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
    from ._5649 import StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
    from ._5650 import SynchroniserCompoundMultibodyDynamicsAnalysis
    from ._5651 import SynchroniserHalfCompoundMultibodyDynamicsAnalysis
    from ._5652 import SynchroniserPartCompoundMultibodyDynamicsAnalysis
    from ._5653 import SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
    from ._5654 import TorqueConverterCompoundMultibodyDynamicsAnalysis
    from ._5655 import TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
    from ._5656 import TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
    from ._5657 import TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
    from ._5658 import UnbalancedMassCompoundMultibodyDynamicsAnalysis
    from ._5659 import VirtualComponentCompoundMultibodyDynamicsAnalysis
    from ._5660 import WormGearCompoundMultibodyDynamicsAnalysis
    from ._5661 import WormGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5662 import WormGearSetCompoundMultibodyDynamicsAnalysis
    from ._5663 import ZerolBevelGearCompoundMultibodyDynamicsAnalysis
    from ._5664 import ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
    from ._5665 import ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
else:
    import_structure = {
        "_5537": ["AbstractAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5538": ["AbstractShaftCompoundMultibodyDynamicsAnalysis"],
        "_5539": ["AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis"],
        "_5540": [
            "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5541": ["AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis"],
        "_5542": ["AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5543": ["AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5544": ["AssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5545": ["BearingCompoundMultibodyDynamicsAnalysis"],
        "_5546": ["BeltConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5547": ["BeltDriveCompoundMultibodyDynamicsAnalysis"],
        "_5548": ["BevelDifferentialGearCompoundMultibodyDynamicsAnalysis"],
        "_5549": ["BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5550": ["BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5551": ["BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis"],
        "_5552": ["BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis"],
        "_5553": ["BevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5554": ["BevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5555": ["BevelGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5556": ["BoltCompoundMultibodyDynamicsAnalysis"],
        "_5557": ["BoltedJointCompoundMultibodyDynamicsAnalysis"],
        "_5558": ["ClutchCompoundMultibodyDynamicsAnalysis"],
        "_5559": ["ClutchConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5560": ["ClutchHalfCompoundMultibodyDynamicsAnalysis"],
        "_5561": ["CoaxialConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5562": ["ComponentCompoundMultibodyDynamicsAnalysis"],
        "_5563": ["ConceptCouplingCompoundMultibodyDynamicsAnalysis"],
        "_5564": ["ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5565": ["ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis"],
        "_5566": ["ConceptGearCompoundMultibodyDynamicsAnalysis"],
        "_5567": ["ConceptGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5568": ["ConceptGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5569": ["ConicalGearCompoundMultibodyDynamicsAnalysis"],
        "_5570": ["ConicalGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5571": ["ConicalGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5572": ["ConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5573": ["ConnectorCompoundMultibodyDynamicsAnalysis"],
        "_5574": ["CouplingCompoundMultibodyDynamicsAnalysis"],
        "_5575": ["CouplingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5576": ["CouplingHalfCompoundMultibodyDynamicsAnalysis"],
        "_5577": ["CVTBeltConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5578": ["CVTCompoundMultibodyDynamicsAnalysis"],
        "_5579": ["CVTPulleyCompoundMultibodyDynamicsAnalysis"],
        "_5580": ["CycloidalAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5581": [
            "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5582": ["CycloidalDiscCompoundMultibodyDynamicsAnalysis"],
        "_5583": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5584": ["CylindricalGearCompoundMultibodyDynamicsAnalysis"],
        "_5585": ["CylindricalGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5586": ["CylindricalGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5587": ["CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis"],
        "_5588": ["DatumCompoundMultibodyDynamicsAnalysis"],
        "_5589": ["ExternalCADModelCompoundMultibodyDynamicsAnalysis"],
        "_5590": ["FaceGearCompoundMultibodyDynamicsAnalysis"],
        "_5591": ["FaceGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5592": ["FaceGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5593": ["FEPartCompoundMultibodyDynamicsAnalysis"],
        "_5594": ["FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5595": ["GearCompoundMultibodyDynamicsAnalysis"],
        "_5596": ["GearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5597": ["GearSetCompoundMultibodyDynamicsAnalysis"],
        "_5598": ["GuideDxfModelCompoundMultibodyDynamicsAnalysis"],
        "_5599": ["HypoidGearCompoundMultibodyDynamicsAnalysis"],
        "_5600": ["HypoidGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5601": ["HypoidGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5602": ["InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5603": [
            "KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ],
        "_5604": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis"
        ],
        "_5605": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis"
        ],
        "_5606": [
            "KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ],
        "_5607": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis"
        ],
        "_5608": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis"
        ],
        "_5609": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis"
        ],
        "_5610": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis"
        ],
        "_5611": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis"
        ],
        "_5612": ["MassDiscCompoundMultibodyDynamicsAnalysis"],
        "_5613": ["MeasurementComponentCompoundMultibodyDynamicsAnalysis"],
        "_5614": ["MountableComponentCompoundMultibodyDynamicsAnalysis"],
        "_5615": ["OilSealCompoundMultibodyDynamicsAnalysis"],
        "_5616": ["PartCompoundMultibodyDynamicsAnalysis"],
        "_5617": ["PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis"],
        "_5618": ["PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5619": ["PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis"],
        "_5620": ["PlanetaryConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5621": ["PlanetaryGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5622": ["PlanetCarrierCompoundMultibodyDynamicsAnalysis"],
        "_5623": ["PointLoadCompoundMultibodyDynamicsAnalysis"],
        "_5624": ["PowerLoadCompoundMultibodyDynamicsAnalysis"],
        "_5625": ["PulleyCompoundMultibodyDynamicsAnalysis"],
        "_5626": ["RingPinsCompoundMultibodyDynamicsAnalysis"],
        "_5627": ["RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5628": ["RollingRingAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5629": ["RollingRingCompoundMultibodyDynamicsAnalysis"],
        "_5630": ["RollingRingConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5631": ["RootAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5632": ["ShaftCompoundMultibodyDynamicsAnalysis"],
        "_5633": ["ShaftHubConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5634": [
            "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ],
        "_5635": ["SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"],
        "_5636": ["SpiralBevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5637": ["SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5638": ["SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5639": ["SpringDamperCompoundMultibodyDynamicsAnalysis"],
        "_5640": ["SpringDamperConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5641": ["SpringDamperHalfCompoundMultibodyDynamicsAnalysis"],
        "_5642": ["StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis"],
        "_5643": ["StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5644": ["StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5645": ["StraightBevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5646": ["StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5647": ["StraightBevelGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5648": ["StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis"],
        "_5649": ["StraightBevelSunGearCompoundMultibodyDynamicsAnalysis"],
        "_5650": ["SynchroniserCompoundMultibodyDynamicsAnalysis"],
        "_5651": ["SynchroniserHalfCompoundMultibodyDynamicsAnalysis"],
        "_5652": ["SynchroniserPartCompoundMultibodyDynamicsAnalysis"],
        "_5653": ["SynchroniserSleeveCompoundMultibodyDynamicsAnalysis"],
        "_5654": ["TorqueConverterCompoundMultibodyDynamicsAnalysis"],
        "_5655": ["TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis"],
        "_5656": ["TorqueConverterPumpCompoundMultibodyDynamicsAnalysis"],
        "_5657": ["TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis"],
        "_5658": ["UnbalancedMassCompoundMultibodyDynamicsAnalysis"],
        "_5659": ["VirtualComponentCompoundMultibodyDynamicsAnalysis"],
        "_5660": ["WormGearCompoundMultibodyDynamicsAnalysis"],
        "_5661": ["WormGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5662": ["WormGearSetCompoundMultibodyDynamicsAnalysis"],
        "_5663": ["ZerolBevelGearCompoundMultibodyDynamicsAnalysis"],
        "_5664": ["ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis"],
        "_5665": ["ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
    "AbstractShaftCompoundMultibodyDynamicsAnalysis",
    "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
    "AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    "AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis",
    "AssemblyCompoundMultibodyDynamicsAnalysis",
    "BearingCompoundMultibodyDynamicsAnalysis",
    "BeltConnectionCompoundMultibodyDynamicsAnalysis",
    "BeltDriveCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialGearCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis",
    "BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis",
    "BevelGearCompoundMultibodyDynamicsAnalysis",
    "BevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "BevelGearSetCompoundMultibodyDynamicsAnalysis",
    "BoltCompoundMultibodyDynamicsAnalysis",
    "BoltedJointCompoundMultibodyDynamicsAnalysis",
    "ClutchCompoundMultibodyDynamicsAnalysis",
    "ClutchConnectionCompoundMultibodyDynamicsAnalysis",
    "ClutchHalfCompoundMultibodyDynamicsAnalysis",
    "CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
    "ComponentCompoundMultibodyDynamicsAnalysis",
    "ConceptCouplingCompoundMultibodyDynamicsAnalysis",
    "ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis",
    "ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis",
    "ConceptGearCompoundMultibodyDynamicsAnalysis",
    "ConceptGearMeshCompoundMultibodyDynamicsAnalysis",
    "ConceptGearSetCompoundMultibodyDynamicsAnalysis",
    "ConicalGearCompoundMultibodyDynamicsAnalysis",
    "ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    "ConicalGearSetCompoundMultibodyDynamicsAnalysis",
    "ConnectionCompoundMultibodyDynamicsAnalysis",
    "ConnectorCompoundMultibodyDynamicsAnalysis",
    "CouplingCompoundMultibodyDynamicsAnalysis",
    "CouplingConnectionCompoundMultibodyDynamicsAnalysis",
    "CouplingHalfCompoundMultibodyDynamicsAnalysis",
    "CVTBeltConnectionCompoundMultibodyDynamicsAnalysis",
    "CVTCompoundMultibodyDynamicsAnalysis",
    "CVTPulleyCompoundMultibodyDynamicsAnalysis",
    "CycloidalAssemblyCompoundMultibodyDynamicsAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
    "CycloidalDiscCompoundMultibodyDynamicsAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis",
    "CylindricalGearCompoundMultibodyDynamicsAnalysis",
    "CylindricalGearMeshCompoundMultibodyDynamicsAnalysis",
    "CylindricalGearSetCompoundMultibodyDynamicsAnalysis",
    "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
    "DatumCompoundMultibodyDynamicsAnalysis",
    "ExternalCADModelCompoundMultibodyDynamicsAnalysis",
    "FaceGearCompoundMultibodyDynamicsAnalysis",
    "FaceGearMeshCompoundMultibodyDynamicsAnalysis",
    "FaceGearSetCompoundMultibodyDynamicsAnalysis",
    "FEPartCompoundMultibodyDynamicsAnalysis",
    "FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis",
    "GearCompoundMultibodyDynamicsAnalysis",
    "GearMeshCompoundMultibodyDynamicsAnalysis",
    "GearSetCompoundMultibodyDynamicsAnalysis",
    "GuideDxfModelCompoundMultibodyDynamicsAnalysis",
    "HypoidGearCompoundMultibodyDynamicsAnalysis",
    "HypoidGearMeshCompoundMultibodyDynamicsAnalysis",
    "HypoidGearSetCompoundMultibodyDynamicsAnalysis",
    "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
    "MassDiscCompoundMultibodyDynamicsAnalysis",
    "MeasurementComponentCompoundMultibodyDynamicsAnalysis",
    "MountableComponentCompoundMultibodyDynamicsAnalysis",
    "OilSealCompoundMultibodyDynamicsAnalysis",
    "PartCompoundMultibodyDynamicsAnalysis",
    "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
    "PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis",
    "PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis",
    "PlanetaryConnectionCompoundMultibodyDynamicsAnalysis",
    "PlanetaryGearSetCompoundMultibodyDynamicsAnalysis",
    "PlanetCarrierCompoundMultibodyDynamicsAnalysis",
    "PointLoadCompoundMultibodyDynamicsAnalysis",
    "PowerLoadCompoundMultibodyDynamicsAnalysis",
    "PulleyCompoundMultibodyDynamicsAnalysis",
    "RingPinsCompoundMultibodyDynamicsAnalysis",
    "RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis",
    "RollingRingAssemblyCompoundMultibodyDynamicsAnalysis",
    "RollingRingCompoundMultibodyDynamicsAnalysis",
    "RollingRingConnectionCompoundMultibodyDynamicsAnalysis",
    "RootAssemblyCompoundMultibodyDynamicsAnalysis",
    "ShaftCompoundMultibodyDynamicsAnalysis",
    "ShaftHubConnectionCompoundMultibodyDynamicsAnalysis",
    "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
    "SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
    "SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis",
    "SpringDamperCompoundMultibodyDynamicsAnalysis",
    "SpringDamperConnectionCompoundMultibodyDynamicsAnalysis",
    "SpringDamperHalfCompoundMultibodyDynamicsAnalysis",
    "StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis",
    "StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis",
    "StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis",
    "StraightBevelGearCompoundMultibodyDynamicsAnalysis",
    "StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "StraightBevelGearSetCompoundMultibodyDynamicsAnalysis",
    "StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis",
    "StraightBevelSunGearCompoundMultibodyDynamicsAnalysis",
    "SynchroniserCompoundMultibodyDynamicsAnalysis",
    "SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
    "SynchroniserPartCompoundMultibodyDynamicsAnalysis",
    "SynchroniserSleeveCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterPumpCompoundMultibodyDynamicsAnalysis",
    "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
    "UnbalancedMassCompoundMultibodyDynamicsAnalysis",
    "VirtualComponentCompoundMultibodyDynamicsAnalysis",
    "WormGearCompoundMultibodyDynamicsAnalysis",
    "WormGearMeshCompoundMultibodyDynamicsAnalysis",
    "WormGearSetCompoundMultibodyDynamicsAnalysis",
    "ZerolBevelGearCompoundMultibodyDynamicsAnalysis",
    "ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis",
    "ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis",
)
