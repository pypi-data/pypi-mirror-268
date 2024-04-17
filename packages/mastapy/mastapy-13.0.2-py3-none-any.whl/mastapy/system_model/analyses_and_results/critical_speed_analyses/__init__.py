"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6551 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6552 import AbstractShaftCriticalSpeedAnalysis
    from ._6553 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6554 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6555 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6556 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6557 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6558 import AssemblyCriticalSpeedAnalysis
    from ._6559 import BearingCriticalSpeedAnalysis
    from ._6560 import BeltConnectionCriticalSpeedAnalysis
    from ._6561 import BeltDriveCriticalSpeedAnalysis
    from ._6562 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6563 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6564 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6565 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6566 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6567 import BevelGearCriticalSpeedAnalysis
    from ._6568 import BevelGearMeshCriticalSpeedAnalysis
    from ._6569 import BevelGearSetCriticalSpeedAnalysis
    from ._6570 import BoltCriticalSpeedAnalysis
    from ._6571 import BoltedJointCriticalSpeedAnalysis
    from ._6572 import ClutchConnectionCriticalSpeedAnalysis
    from ._6573 import ClutchCriticalSpeedAnalysis
    from ._6574 import ClutchHalfCriticalSpeedAnalysis
    from ._6575 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6576 import ComponentCriticalSpeedAnalysis
    from ._6577 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6578 import ConceptCouplingCriticalSpeedAnalysis
    from ._6579 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6580 import ConceptGearCriticalSpeedAnalysis
    from ._6581 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6582 import ConceptGearSetCriticalSpeedAnalysis
    from ._6583 import ConicalGearCriticalSpeedAnalysis
    from ._6584 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6585 import ConicalGearSetCriticalSpeedAnalysis
    from ._6586 import ConnectionCriticalSpeedAnalysis
    from ._6587 import ConnectorCriticalSpeedAnalysis
    from ._6588 import CouplingConnectionCriticalSpeedAnalysis
    from ._6589 import CouplingCriticalSpeedAnalysis
    from ._6590 import CouplingHalfCriticalSpeedAnalysis
    from ._6591 import CriticalSpeedAnalysis
    from ._6592 import CriticalSpeedAnalysisDrawStyle
    from ._6593 import CriticalSpeedAnalysisOptions
    from ._6594 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6595 import CVTCriticalSpeedAnalysis
    from ._6596 import CVTPulleyCriticalSpeedAnalysis
    from ._6597 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6598 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6599 import CycloidalDiscCriticalSpeedAnalysis
    from ._6600 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6601 import CylindricalGearCriticalSpeedAnalysis
    from ._6602 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6603 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6604 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6605 import DatumCriticalSpeedAnalysis
    from ._6606 import ExternalCADModelCriticalSpeedAnalysis
    from ._6607 import FaceGearCriticalSpeedAnalysis
    from ._6608 import FaceGearMeshCriticalSpeedAnalysis
    from ._6609 import FaceGearSetCriticalSpeedAnalysis
    from ._6610 import FEPartCriticalSpeedAnalysis
    from ._6611 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6612 import GearCriticalSpeedAnalysis
    from ._6613 import GearMeshCriticalSpeedAnalysis
    from ._6614 import GearSetCriticalSpeedAnalysis
    from ._6615 import GuideDxfModelCriticalSpeedAnalysis
    from ._6616 import HypoidGearCriticalSpeedAnalysis
    from ._6617 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6618 import HypoidGearSetCriticalSpeedAnalysis
    from ._6619 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6620 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6621 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6622 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6623 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6624 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6625 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6626 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6627 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6628 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6629 import MassDiscCriticalSpeedAnalysis
    from ._6630 import MeasurementComponentCriticalSpeedAnalysis
    from ._6631 import MountableComponentCriticalSpeedAnalysis
    from ._6632 import OilSealCriticalSpeedAnalysis
    from ._6633 import PartCriticalSpeedAnalysis
    from ._6634 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6635 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6636 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6637 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6638 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6639 import PlanetCarrierCriticalSpeedAnalysis
    from ._6640 import PointLoadCriticalSpeedAnalysis
    from ._6641 import PowerLoadCriticalSpeedAnalysis
    from ._6642 import PulleyCriticalSpeedAnalysis
    from ._6643 import RingPinsCriticalSpeedAnalysis
    from ._6644 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6645 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6646 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6647 import RollingRingCriticalSpeedAnalysis
    from ._6648 import RootAssemblyCriticalSpeedAnalysis
    from ._6649 import ShaftCriticalSpeedAnalysis
    from ._6650 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6651 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6652 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6653 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6654 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6655 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6656 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6657 import SpringDamperCriticalSpeedAnalysis
    from ._6658 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6659 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6660 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6661 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6662 import StraightBevelGearCriticalSpeedAnalysis
    from ._6663 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6664 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6665 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6666 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6667 import SynchroniserCriticalSpeedAnalysis
    from ._6668 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6669 import SynchroniserPartCriticalSpeedAnalysis
    from ._6670 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6671 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6672 import TorqueConverterCriticalSpeedAnalysis
    from ._6673 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6674 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6675 import UnbalancedMassCriticalSpeedAnalysis
    from ._6676 import VirtualComponentCriticalSpeedAnalysis
    from ._6677 import WormGearCriticalSpeedAnalysis
    from ._6678 import WormGearMeshCriticalSpeedAnalysis
    from ._6679 import WormGearSetCriticalSpeedAnalysis
    from ._6680 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6681 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6682 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        "_6551": ["AbstractAssemblyCriticalSpeedAnalysis"],
        "_6552": ["AbstractShaftCriticalSpeedAnalysis"],
        "_6553": ["AbstractShaftOrHousingCriticalSpeedAnalysis"],
        "_6554": ["AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6555": ["AGMAGleasonConicalGearCriticalSpeedAnalysis"],
        "_6556": ["AGMAGleasonConicalGearMeshCriticalSpeedAnalysis"],
        "_6557": ["AGMAGleasonConicalGearSetCriticalSpeedAnalysis"],
        "_6558": ["AssemblyCriticalSpeedAnalysis"],
        "_6559": ["BearingCriticalSpeedAnalysis"],
        "_6560": ["BeltConnectionCriticalSpeedAnalysis"],
        "_6561": ["BeltDriveCriticalSpeedAnalysis"],
        "_6562": ["BevelDifferentialGearCriticalSpeedAnalysis"],
        "_6563": ["BevelDifferentialGearMeshCriticalSpeedAnalysis"],
        "_6564": ["BevelDifferentialGearSetCriticalSpeedAnalysis"],
        "_6565": ["BevelDifferentialPlanetGearCriticalSpeedAnalysis"],
        "_6566": ["BevelDifferentialSunGearCriticalSpeedAnalysis"],
        "_6567": ["BevelGearCriticalSpeedAnalysis"],
        "_6568": ["BevelGearMeshCriticalSpeedAnalysis"],
        "_6569": ["BevelGearSetCriticalSpeedAnalysis"],
        "_6570": ["BoltCriticalSpeedAnalysis"],
        "_6571": ["BoltedJointCriticalSpeedAnalysis"],
        "_6572": ["ClutchConnectionCriticalSpeedAnalysis"],
        "_6573": ["ClutchCriticalSpeedAnalysis"],
        "_6574": ["ClutchHalfCriticalSpeedAnalysis"],
        "_6575": ["CoaxialConnectionCriticalSpeedAnalysis"],
        "_6576": ["ComponentCriticalSpeedAnalysis"],
        "_6577": ["ConceptCouplingConnectionCriticalSpeedAnalysis"],
        "_6578": ["ConceptCouplingCriticalSpeedAnalysis"],
        "_6579": ["ConceptCouplingHalfCriticalSpeedAnalysis"],
        "_6580": ["ConceptGearCriticalSpeedAnalysis"],
        "_6581": ["ConceptGearMeshCriticalSpeedAnalysis"],
        "_6582": ["ConceptGearSetCriticalSpeedAnalysis"],
        "_6583": ["ConicalGearCriticalSpeedAnalysis"],
        "_6584": ["ConicalGearMeshCriticalSpeedAnalysis"],
        "_6585": ["ConicalGearSetCriticalSpeedAnalysis"],
        "_6586": ["ConnectionCriticalSpeedAnalysis"],
        "_6587": ["ConnectorCriticalSpeedAnalysis"],
        "_6588": ["CouplingConnectionCriticalSpeedAnalysis"],
        "_6589": ["CouplingCriticalSpeedAnalysis"],
        "_6590": ["CouplingHalfCriticalSpeedAnalysis"],
        "_6591": ["CriticalSpeedAnalysis"],
        "_6592": ["CriticalSpeedAnalysisDrawStyle"],
        "_6593": ["CriticalSpeedAnalysisOptions"],
        "_6594": ["CVTBeltConnectionCriticalSpeedAnalysis"],
        "_6595": ["CVTCriticalSpeedAnalysis"],
        "_6596": ["CVTPulleyCriticalSpeedAnalysis"],
        "_6597": ["CycloidalAssemblyCriticalSpeedAnalysis"],
        "_6598": ["CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"],
        "_6599": ["CycloidalDiscCriticalSpeedAnalysis"],
        "_6600": ["CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"],
        "_6601": ["CylindricalGearCriticalSpeedAnalysis"],
        "_6602": ["CylindricalGearMeshCriticalSpeedAnalysis"],
        "_6603": ["CylindricalGearSetCriticalSpeedAnalysis"],
        "_6604": ["CylindricalPlanetGearCriticalSpeedAnalysis"],
        "_6605": ["DatumCriticalSpeedAnalysis"],
        "_6606": ["ExternalCADModelCriticalSpeedAnalysis"],
        "_6607": ["FaceGearCriticalSpeedAnalysis"],
        "_6608": ["FaceGearMeshCriticalSpeedAnalysis"],
        "_6609": ["FaceGearSetCriticalSpeedAnalysis"],
        "_6610": ["FEPartCriticalSpeedAnalysis"],
        "_6611": ["FlexiblePinAssemblyCriticalSpeedAnalysis"],
        "_6612": ["GearCriticalSpeedAnalysis"],
        "_6613": ["GearMeshCriticalSpeedAnalysis"],
        "_6614": ["GearSetCriticalSpeedAnalysis"],
        "_6615": ["GuideDxfModelCriticalSpeedAnalysis"],
        "_6616": ["HypoidGearCriticalSpeedAnalysis"],
        "_6617": ["HypoidGearMeshCriticalSpeedAnalysis"],
        "_6618": ["HypoidGearSetCriticalSpeedAnalysis"],
        "_6619": ["InterMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6620": ["KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"],
        "_6621": ["KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"],
        "_6622": ["KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"],
        "_6623": ["KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"],
        "_6624": ["KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"],
        "_6625": ["KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"],
        "_6626": ["KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis"],
        "_6627": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6628": ["KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6629": ["MassDiscCriticalSpeedAnalysis"],
        "_6630": ["MeasurementComponentCriticalSpeedAnalysis"],
        "_6631": ["MountableComponentCriticalSpeedAnalysis"],
        "_6632": ["OilSealCriticalSpeedAnalysis"],
        "_6633": ["PartCriticalSpeedAnalysis"],
        "_6634": ["PartToPartShearCouplingConnectionCriticalSpeedAnalysis"],
        "_6635": ["PartToPartShearCouplingCriticalSpeedAnalysis"],
        "_6636": ["PartToPartShearCouplingHalfCriticalSpeedAnalysis"],
        "_6637": ["PlanetaryConnectionCriticalSpeedAnalysis"],
        "_6638": ["PlanetaryGearSetCriticalSpeedAnalysis"],
        "_6639": ["PlanetCarrierCriticalSpeedAnalysis"],
        "_6640": ["PointLoadCriticalSpeedAnalysis"],
        "_6641": ["PowerLoadCriticalSpeedAnalysis"],
        "_6642": ["PulleyCriticalSpeedAnalysis"],
        "_6643": ["RingPinsCriticalSpeedAnalysis"],
        "_6644": ["RingPinsToDiscConnectionCriticalSpeedAnalysis"],
        "_6645": ["RollingRingAssemblyCriticalSpeedAnalysis"],
        "_6646": ["RollingRingConnectionCriticalSpeedAnalysis"],
        "_6647": ["RollingRingCriticalSpeedAnalysis"],
        "_6648": ["RootAssemblyCriticalSpeedAnalysis"],
        "_6649": ["ShaftCriticalSpeedAnalysis"],
        "_6650": ["ShaftHubConnectionCriticalSpeedAnalysis"],
        "_6651": ["ShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6652": ["SpecialisedAssemblyCriticalSpeedAnalysis"],
        "_6653": ["SpiralBevelGearCriticalSpeedAnalysis"],
        "_6654": ["SpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6655": ["SpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6656": ["SpringDamperConnectionCriticalSpeedAnalysis"],
        "_6657": ["SpringDamperCriticalSpeedAnalysis"],
        "_6658": ["SpringDamperHalfCriticalSpeedAnalysis"],
        "_6659": ["StraightBevelDiffGearCriticalSpeedAnalysis"],
        "_6660": ["StraightBevelDiffGearMeshCriticalSpeedAnalysis"],
        "_6661": ["StraightBevelDiffGearSetCriticalSpeedAnalysis"],
        "_6662": ["StraightBevelGearCriticalSpeedAnalysis"],
        "_6663": ["StraightBevelGearMeshCriticalSpeedAnalysis"],
        "_6664": ["StraightBevelGearSetCriticalSpeedAnalysis"],
        "_6665": ["StraightBevelPlanetGearCriticalSpeedAnalysis"],
        "_6666": ["StraightBevelSunGearCriticalSpeedAnalysis"],
        "_6667": ["SynchroniserCriticalSpeedAnalysis"],
        "_6668": ["SynchroniserHalfCriticalSpeedAnalysis"],
        "_6669": ["SynchroniserPartCriticalSpeedAnalysis"],
        "_6670": ["SynchroniserSleeveCriticalSpeedAnalysis"],
        "_6671": ["TorqueConverterConnectionCriticalSpeedAnalysis"],
        "_6672": ["TorqueConverterCriticalSpeedAnalysis"],
        "_6673": ["TorqueConverterPumpCriticalSpeedAnalysis"],
        "_6674": ["TorqueConverterTurbineCriticalSpeedAnalysis"],
        "_6675": ["UnbalancedMassCriticalSpeedAnalysis"],
        "_6676": ["VirtualComponentCriticalSpeedAnalysis"],
        "_6677": ["WormGearCriticalSpeedAnalysis"],
        "_6678": ["WormGearMeshCriticalSpeedAnalysis"],
        "_6679": ["WormGearSetCriticalSpeedAnalysis"],
        "_6680": ["ZerolBevelGearCriticalSpeedAnalysis"],
        "_6681": ["ZerolBevelGearMeshCriticalSpeedAnalysis"],
        "_6682": ["ZerolBevelGearSetCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCriticalSpeedAnalysis",
    "AbstractShaftCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
    "AssemblyCriticalSpeedAnalysis",
    "BearingCriticalSpeedAnalysis",
    "BeltConnectionCriticalSpeedAnalysis",
    "BeltDriveCriticalSpeedAnalysis",
    "BevelDifferentialGearCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCriticalSpeedAnalysis",
    "BevelGearCriticalSpeedAnalysis",
    "BevelGearMeshCriticalSpeedAnalysis",
    "BevelGearSetCriticalSpeedAnalysis",
    "BoltCriticalSpeedAnalysis",
    "BoltedJointCriticalSpeedAnalysis",
    "ClutchConnectionCriticalSpeedAnalysis",
    "ClutchCriticalSpeedAnalysis",
    "ClutchHalfCriticalSpeedAnalysis",
    "CoaxialConnectionCriticalSpeedAnalysis",
    "ComponentCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCriticalSpeedAnalysis",
    "ConceptCouplingCriticalSpeedAnalysis",
    "ConceptCouplingHalfCriticalSpeedAnalysis",
    "ConceptGearCriticalSpeedAnalysis",
    "ConceptGearMeshCriticalSpeedAnalysis",
    "ConceptGearSetCriticalSpeedAnalysis",
    "ConicalGearCriticalSpeedAnalysis",
    "ConicalGearMeshCriticalSpeedAnalysis",
    "ConicalGearSetCriticalSpeedAnalysis",
    "ConnectionCriticalSpeedAnalysis",
    "ConnectorCriticalSpeedAnalysis",
    "CouplingConnectionCriticalSpeedAnalysis",
    "CouplingCriticalSpeedAnalysis",
    "CouplingHalfCriticalSpeedAnalysis",
    "CriticalSpeedAnalysis",
    "CriticalSpeedAnalysisDrawStyle",
    "CriticalSpeedAnalysisOptions",
    "CVTBeltConnectionCriticalSpeedAnalysis",
    "CVTCriticalSpeedAnalysis",
    "CVTPulleyCriticalSpeedAnalysis",
    "CycloidalAssemblyCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
    "CycloidalDiscCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    "CylindricalGearCriticalSpeedAnalysis",
    "CylindricalGearMeshCriticalSpeedAnalysis",
    "CylindricalGearSetCriticalSpeedAnalysis",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
    "DatumCriticalSpeedAnalysis",
    "ExternalCADModelCriticalSpeedAnalysis",
    "FaceGearCriticalSpeedAnalysis",
    "FaceGearMeshCriticalSpeedAnalysis",
    "FaceGearSetCriticalSpeedAnalysis",
    "FEPartCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCriticalSpeedAnalysis",
    "GearCriticalSpeedAnalysis",
    "GearMeshCriticalSpeedAnalysis",
    "GearSetCriticalSpeedAnalysis",
    "GuideDxfModelCriticalSpeedAnalysis",
    "HypoidGearCriticalSpeedAnalysis",
    "HypoidGearMeshCriticalSpeedAnalysis",
    "HypoidGearSetCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    "MassDiscCriticalSpeedAnalysis",
    "MeasurementComponentCriticalSpeedAnalysis",
    "MountableComponentCriticalSpeedAnalysis",
    "OilSealCriticalSpeedAnalysis",
    "PartCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCriticalSpeedAnalysis",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
    "PlanetaryConnectionCriticalSpeedAnalysis",
    "PlanetaryGearSetCriticalSpeedAnalysis",
    "PlanetCarrierCriticalSpeedAnalysis",
    "PointLoadCriticalSpeedAnalysis",
    "PowerLoadCriticalSpeedAnalysis",
    "PulleyCriticalSpeedAnalysis",
    "RingPinsCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
    "RollingRingAssemblyCriticalSpeedAnalysis",
    "RollingRingConnectionCriticalSpeedAnalysis",
    "RollingRingCriticalSpeedAnalysis",
    "RootAssemblyCriticalSpeedAnalysis",
    "ShaftCriticalSpeedAnalysis",
    "ShaftHubConnectionCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
    "SpiralBevelGearCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
    "SpiralBevelGearSetCriticalSpeedAnalysis",
    "SpringDamperConnectionCriticalSpeedAnalysis",
    "SpringDamperCriticalSpeedAnalysis",
    "SpringDamperHalfCriticalSpeedAnalysis",
    "StraightBevelDiffGearCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCriticalSpeedAnalysis",
    "StraightBevelGearCriticalSpeedAnalysis",
    "StraightBevelGearMeshCriticalSpeedAnalysis",
    "StraightBevelGearSetCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCriticalSpeedAnalysis",
    "StraightBevelSunGearCriticalSpeedAnalysis",
    "SynchroniserCriticalSpeedAnalysis",
    "SynchroniserHalfCriticalSpeedAnalysis",
    "SynchroniserPartCriticalSpeedAnalysis",
    "SynchroniserSleeveCriticalSpeedAnalysis",
    "TorqueConverterConnectionCriticalSpeedAnalysis",
    "TorqueConverterCriticalSpeedAnalysis",
    "TorqueConverterPumpCriticalSpeedAnalysis",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
    "UnbalancedMassCriticalSpeedAnalysis",
    "VirtualComponentCriticalSpeedAnalysis",
    "WormGearCriticalSpeedAnalysis",
    "WormGearMeshCriticalSpeedAnalysis",
    "WormGearSetCriticalSpeedAnalysis",
    "ZerolBevelGearCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCriticalSpeedAnalysis",
    "ZerolBevelGearSetCriticalSpeedAnalysis",
)
