"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6683 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6684 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6685 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6686 import (
        AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6687 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6688 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6689 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6690 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6691 import BearingCompoundCriticalSpeedAnalysis
    from ._6692 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6693 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6694 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6695 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6696 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6697 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6698 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6699 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6700 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6701 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6702 import BoltCompoundCriticalSpeedAnalysis
    from ._6703 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6704 import ClutchCompoundCriticalSpeedAnalysis
    from ._6705 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6706 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6707 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6708 import ComponentCompoundCriticalSpeedAnalysis
    from ._6709 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6710 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6711 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6712 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6713 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6714 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6715 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6716 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6717 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6718 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6719 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6720 import CouplingCompoundCriticalSpeedAnalysis
    from ._6721 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6722 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6723 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6724 import CVTCompoundCriticalSpeedAnalysis
    from ._6725 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6726 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6727 import (
        CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6728 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6729 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6730 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6731 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6732 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6733 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6734 import DatumCompoundCriticalSpeedAnalysis
    from ._6735 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6736 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6737 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6738 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6739 import FEPartCompoundCriticalSpeedAnalysis
    from ._6740 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6741 import GearCompoundCriticalSpeedAnalysis
    from ._6742 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6743 import GearSetCompoundCriticalSpeedAnalysis
    from ._6744 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6745 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6746 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6747 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6748 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6749 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6750 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6751 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6752 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6753 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6754 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6755 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis,
    )
    from ._6756 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6757 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6758 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6759 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6760 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6761 import OilSealCompoundCriticalSpeedAnalysis
    from ._6762 import PartCompoundCriticalSpeedAnalysis
    from ._6763 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6764 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6765 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6766 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6767 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6768 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6769 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6770 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6771 import PulleyCompoundCriticalSpeedAnalysis
    from ._6772 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6773 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6774 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6775 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6776 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6777 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6778 import ShaftCompoundCriticalSpeedAnalysis
    from ._6779 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6780 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6781 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6782 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6783 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6784 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6785 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6786 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6787 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6788 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6789 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6790 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6791 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6792 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6793 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6794 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6795 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6796 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6797 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6798 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6799 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6800 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6801 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6802 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6803 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6804 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6805 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6806 import WormGearCompoundCriticalSpeedAnalysis
    from ._6807 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6808 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6809 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6810 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6811 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        "_6683": ["AbstractAssemblyCompoundCriticalSpeedAnalysis"],
        "_6684": ["AbstractShaftCompoundCriticalSpeedAnalysis"],
        "_6685": ["AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"],
        "_6686": [
            "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6687": ["AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"],
        "_6688": ["AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6689": ["AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6690": ["AssemblyCompoundCriticalSpeedAnalysis"],
        "_6691": ["BearingCompoundCriticalSpeedAnalysis"],
        "_6692": ["BeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6693": ["BeltDriveCompoundCriticalSpeedAnalysis"],
        "_6694": ["BevelDifferentialGearCompoundCriticalSpeedAnalysis"],
        "_6695": ["BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"],
        "_6696": ["BevelDifferentialGearSetCompoundCriticalSpeedAnalysis"],
        "_6697": ["BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6698": ["BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"],
        "_6699": ["BevelGearCompoundCriticalSpeedAnalysis"],
        "_6700": ["BevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6701": ["BevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6702": ["BoltCompoundCriticalSpeedAnalysis"],
        "_6703": ["BoltedJointCompoundCriticalSpeedAnalysis"],
        "_6704": ["ClutchCompoundCriticalSpeedAnalysis"],
        "_6705": ["ClutchConnectionCompoundCriticalSpeedAnalysis"],
        "_6706": ["ClutchHalfCompoundCriticalSpeedAnalysis"],
        "_6707": ["CoaxialConnectionCompoundCriticalSpeedAnalysis"],
        "_6708": ["ComponentCompoundCriticalSpeedAnalysis"],
        "_6709": ["ConceptCouplingCompoundCriticalSpeedAnalysis"],
        "_6710": ["ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6711": ["ConceptCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6712": ["ConceptGearCompoundCriticalSpeedAnalysis"],
        "_6713": ["ConceptGearMeshCompoundCriticalSpeedAnalysis"],
        "_6714": ["ConceptGearSetCompoundCriticalSpeedAnalysis"],
        "_6715": ["ConicalGearCompoundCriticalSpeedAnalysis"],
        "_6716": ["ConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6717": ["ConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6718": ["ConnectionCompoundCriticalSpeedAnalysis"],
        "_6719": ["ConnectorCompoundCriticalSpeedAnalysis"],
        "_6720": ["CouplingCompoundCriticalSpeedAnalysis"],
        "_6721": ["CouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6722": ["CouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6723": ["CVTBeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6724": ["CVTCompoundCriticalSpeedAnalysis"],
        "_6725": ["CVTPulleyCompoundCriticalSpeedAnalysis"],
        "_6726": ["CycloidalAssemblyCompoundCriticalSpeedAnalysis"],
        "_6727": ["CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"],
        "_6728": ["CycloidalDiscCompoundCriticalSpeedAnalysis"],
        "_6729": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6730": ["CylindricalGearCompoundCriticalSpeedAnalysis"],
        "_6731": ["CylindricalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6732": ["CylindricalGearSetCompoundCriticalSpeedAnalysis"],
        "_6733": ["CylindricalPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6734": ["DatumCompoundCriticalSpeedAnalysis"],
        "_6735": ["ExternalCADModelCompoundCriticalSpeedAnalysis"],
        "_6736": ["FaceGearCompoundCriticalSpeedAnalysis"],
        "_6737": ["FaceGearMeshCompoundCriticalSpeedAnalysis"],
        "_6738": ["FaceGearSetCompoundCriticalSpeedAnalysis"],
        "_6739": ["FEPartCompoundCriticalSpeedAnalysis"],
        "_6740": ["FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"],
        "_6741": ["GearCompoundCriticalSpeedAnalysis"],
        "_6742": ["GearMeshCompoundCriticalSpeedAnalysis"],
        "_6743": ["GearSetCompoundCriticalSpeedAnalysis"],
        "_6744": ["GuideDxfModelCompoundCriticalSpeedAnalysis"],
        "_6745": ["HypoidGearCompoundCriticalSpeedAnalysis"],
        "_6746": ["HypoidGearMeshCompoundCriticalSpeedAnalysis"],
        "_6747": ["HypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6748": ["InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6749": ["KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"],
        "_6750": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6751": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6752": ["KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"],
        "_6753": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6754": ["KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6755": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ],
        "_6756": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6757": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6758": ["MassDiscCompoundCriticalSpeedAnalysis"],
        "_6759": ["MeasurementComponentCompoundCriticalSpeedAnalysis"],
        "_6760": ["MountableComponentCompoundCriticalSpeedAnalysis"],
        "_6761": ["OilSealCompoundCriticalSpeedAnalysis"],
        "_6762": ["PartCompoundCriticalSpeedAnalysis"],
        "_6763": ["PartToPartShearCouplingCompoundCriticalSpeedAnalysis"],
        "_6764": ["PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6765": ["PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6766": ["PlanetaryConnectionCompoundCriticalSpeedAnalysis"],
        "_6767": ["PlanetaryGearSetCompoundCriticalSpeedAnalysis"],
        "_6768": ["PlanetCarrierCompoundCriticalSpeedAnalysis"],
        "_6769": ["PointLoadCompoundCriticalSpeedAnalysis"],
        "_6770": ["PowerLoadCompoundCriticalSpeedAnalysis"],
        "_6771": ["PulleyCompoundCriticalSpeedAnalysis"],
        "_6772": ["RingPinsCompoundCriticalSpeedAnalysis"],
        "_6773": ["RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"],
        "_6774": ["RollingRingAssemblyCompoundCriticalSpeedAnalysis"],
        "_6775": ["RollingRingCompoundCriticalSpeedAnalysis"],
        "_6776": ["RollingRingConnectionCompoundCriticalSpeedAnalysis"],
        "_6777": ["RootAssemblyCompoundCriticalSpeedAnalysis"],
        "_6778": ["ShaftCompoundCriticalSpeedAnalysis"],
        "_6779": ["ShaftHubConnectionCompoundCriticalSpeedAnalysis"],
        "_6780": ["ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6781": ["SpecialisedAssemblyCompoundCriticalSpeedAnalysis"],
        "_6782": ["SpiralBevelGearCompoundCriticalSpeedAnalysis"],
        "_6783": ["SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6784": ["SpiralBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6785": ["SpringDamperCompoundCriticalSpeedAnalysis"],
        "_6786": ["SpringDamperConnectionCompoundCriticalSpeedAnalysis"],
        "_6787": ["SpringDamperHalfCompoundCriticalSpeedAnalysis"],
        "_6788": ["StraightBevelDiffGearCompoundCriticalSpeedAnalysis"],
        "_6789": ["StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis"],
        "_6790": ["StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"],
        "_6791": ["StraightBevelGearCompoundCriticalSpeedAnalysis"],
        "_6792": ["StraightBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6793": ["StraightBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6794": ["StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6795": ["StraightBevelSunGearCompoundCriticalSpeedAnalysis"],
        "_6796": ["SynchroniserCompoundCriticalSpeedAnalysis"],
        "_6797": ["SynchroniserHalfCompoundCriticalSpeedAnalysis"],
        "_6798": ["SynchroniserPartCompoundCriticalSpeedAnalysis"],
        "_6799": ["SynchroniserSleeveCompoundCriticalSpeedAnalysis"],
        "_6800": ["TorqueConverterCompoundCriticalSpeedAnalysis"],
        "_6801": ["TorqueConverterConnectionCompoundCriticalSpeedAnalysis"],
        "_6802": ["TorqueConverterPumpCompoundCriticalSpeedAnalysis"],
        "_6803": ["TorqueConverterTurbineCompoundCriticalSpeedAnalysis"],
        "_6804": ["UnbalancedMassCompoundCriticalSpeedAnalysis"],
        "_6805": ["VirtualComponentCompoundCriticalSpeedAnalysis"],
        "_6806": ["WormGearCompoundCriticalSpeedAnalysis"],
        "_6807": ["WormGearMeshCompoundCriticalSpeedAnalysis"],
        "_6808": ["WormGearSetCompoundCriticalSpeedAnalysis"],
        "_6809": ["ZerolBevelGearCompoundCriticalSpeedAnalysis"],
        "_6810": ["ZerolBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6811": ["ZerolBevelGearSetCompoundCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    "AssemblyCompoundCriticalSpeedAnalysis",
    "BearingCompoundCriticalSpeedAnalysis",
    "BeltConnectionCompoundCriticalSpeedAnalysis",
    "BeltDriveCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCompoundCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
    "BevelGearCompoundCriticalSpeedAnalysis",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
    "BoltCompoundCriticalSpeedAnalysis",
    "BoltedJointCompoundCriticalSpeedAnalysis",
    "ClutchCompoundCriticalSpeedAnalysis",
    "ClutchConnectionCompoundCriticalSpeedAnalysis",
    "ClutchHalfCompoundCriticalSpeedAnalysis",
    "CoaxialConnectionCompoundCriticalSpeedAnalysis",
    "ComponentCompoundCriticalSpeedAnalysis",
    "ConceptCouplingCompoundCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
    "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
    "ConceptGearCompoundCriticalSpeedAnalysis",
    "ConceptGearMeshCompoundCriticalSpeedAnalysis",
    "ConceptGearSetCompoundCriticalSpeedAnalysis",
    "ConicalGearCompoundCriticalSpeedAnalysis",
    "ConicalGearMeshCompoundCriticalSpeedAnalysis",
    "ConicalGearSetCompoundCriticalSpeedAnalysis",
    "ConnectionCompoundCriticalSpeedAnalysis",
    "ConnectorCompoundCriticalSpeedAnalysis",
    "CouplingCompoundCriticalSpeedAnalysis",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
    "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
    "CVTCompoundCriticalSpeedAnalysis",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
    "CycloidalAssemblyCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCompoundCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis",
    "CylindricalGearCompoundCriticalSpeedAnalysis",
    "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
    "CylindricalGearSetCompoundCriticalSpeedAnalysis",
    "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
    "DatumCompoundCriticalSpeedAnalysis",
    "ExternalCADModelCompoundCriticalSpeedAnalysis",
    "FaceGearCompoundCriticalSpeedAnalysis",
    "FaceGearMeshCompoundCriticalSpeedAnalysis",
    "FaceGearSetCompoundCriticalSpeedAnalysis",
    "FEPartCompoundCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
    "GearCompoundCriticalSpeedAnalysis",
    "GearMeshCompoundCriticalSpeedAnalysis",
    "GearSetCompoundCriticalSpeedAnalysis",
    "GuideDxfModelCompoundCriticalSpeedAnalysis",
    "HypoidGearCompoundCriticalSpeedAnalysis",
    "HypoidGearMeshCompoundCriticalSpeedAnalysis",
    "HypoidGearSetCompoundCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "MassDiscCompoundCriticalSpeedAnalysis",
    "MeasurementComponentCompoundCriticalSpeedAnalysis",
    "MountableComponentCompoundCriticalSpeedAnalysis",
    "OilSealCompoundCriticalSpeedAnalysis",
    "PartCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
    "PlanetaryConnectionCompoundCriticalSpeedAnalysis",
    "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
    "PlanetCarrierCompoundCriticalSpeedAnalysis",
    "PointLoadCompoundCriticalSpeedAnalysis",
    "PowerLoadCompoundCriticalSpeedAnalysis",
    "PulleyCompoundCriticalSpeedAnalysis",
    "RingPinsCompoundCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
    "RollingRingAssemblyCompoundCriticalSpeedAnalysis",
    "RollingRingCompoundCriticalSpeedAnalysis",
    "RollingRingConnectionCompoundCriticalSpeedAnalysis",
    "RootAssemblyCompoundCriticalSpeedAnalysis",
    "ShaftCompoundCriticalSpeedAnalysis",
    "ShaftHubConnectionCompoundCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "SpringDamperCompoundCriticalSpeedAnalysis",
    "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
    "SpringDamperHalfCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelGearCompoundCriticalSpeedAnalysis",
    "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
    "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
    "SynchroniserCompoundCriticalSpeedAnalysis",
    "SynchroniserHalfCompoundCriticalSpeedAnalysis",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
    "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
    "TorqueConverterCompoundCriticalSpeedAnalysis",
    "TorqueConverterConnectionCompoundCriticalSpeedAnalysis",
    "TorqueConverterPumpCompoundCriticalSpeedAnalysis",
    "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
    "WormGearCompoundCriticalSpeedAnalysis",
    "WormGearMeshCompoundCriticalSpeedAnalysis",
    "WormGearSetCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
)
