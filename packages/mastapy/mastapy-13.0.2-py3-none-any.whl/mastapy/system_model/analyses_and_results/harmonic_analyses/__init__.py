"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5686 import AbstractAssemblyHarmonicAnalysis
    from ._5687 import AbstractPeriodicExcitationDetail
    from ._5688 import AbstractShaftHarmonicAnalysis
    from ._5689 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5690 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5691 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5692 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5693 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5694 import AssemblyHarmonicAnalysis
    from ._5695 import BearingHarmonicAnalysis
    from ._5696 import BeltConnectionHarmonicAnalysis
    from ._5697 import BeltDriveHarmonicAnalysis
    from ._5698 import BevelDifferentialGearHarmonicAnalysis
    from ._5699 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5700 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5701 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5702 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5703 import BevelGearHarmonicAnalysis
    from ._5704 import BevelGearMeshHarmonicAnalysis
    from ._5705 import BevelGearSetHarmonicAnalysis
    from ._5706 import BoltedJointHarmonicAnalysis
    from ._5707 import BoltHarmonicAnalysis
    from ._5708 import ClutchConnectionHarmonicAnalysis
    from ._5709 import ClutchHalfHarmonicAnalysis
    from ._5710 import ClutchHarmonicAnalysis
    from ._5711 import CoaxialConnectionHarmonicAnalysis
    from ._5712 import ComplianceAndForceData
    from ._5713 import ComponentHarmonicAnalysis
    from ._5714 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5715 import ConceptCouplingHalfHarmonicAnalysis
    from ._5716 import ConceptCouplingHarmonicAnalysis
    from ._5717 import ConceptGearHarmonicAnalysis
    from ._5718 import ConceptGearMeshHarmonicAnalysis
    from ._5719 import ConceptGearSetHarmonicAnalysis
    from ._5720 import ConicalGearHarmonicAnalysis
    from ._5721 import ConicalGearMeshHarmonicAnalysis
    from ._5722 import ConicalGearSetHarmonicAnalysis
    from ._5723 import ConnectionHarmonicAnalysis
    from ._5724 import ConnectorHarmonicAnalysis
    from ._5725 import CouplingConnectionHarmonicAnalysis
    from ._5726 import CouplingHalfHarmonicAnalysis
    from ._5727 import CouplingHarmonicAnalysis
    from ._5728 import CVTBeltConnectionHarmonicAnalysis
    from ._5729 import CVTHarmonicAnalysis
    from ._5730 import CVTPulleyHarmonicAnalysis
    from ._5731 import CycloidalAssemblyHarmonicAnalysis
    from ._5732 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5733 import CycloidalDiscHarmonicAnalysis
    from ._5734 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5735 import CylindricalGearHarmonicAnalysis
    from ._5736 import CylindricalGearMeshHarmonicAnalysis
    from ._5737 import CylindricalGearSetHarmonicAnalysis
    from ._5738 import CylindricalPlanetGearHarmonicAnalysis
    from ._5739 import DatumHarmonicAnalysis
    from ._5740 import DynamicModelForHarmonicAnalysis
    from ._5741 import ElectricMachinePeriodicExcitationDetail
    from ._5742 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5743 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5744 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5745 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5746 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5747 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5748 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5749 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5750 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5751 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5752 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5753 import ExportOutputType
    from ._5754 import ExternalCADModelHarmonicAnalysis
    from ._5755 import FaceGearHarmonicAnalysis
    from ._5756 import FaceGearMeshHarmonicAnalysis
    from ._5757 import FaceGearSetHarmonicAnalysis
    from ._5758 import FEPartHarmonicAnalysis
    from ._5759 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5760 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5761 import GearHarmonicAnalysis
    from ._5762 import GearMeshExcitationDetail
    from ._5763 import GearMeshHarmonicAnalysis
    from ._5764 import GearMeshMisalignmentExcitationDetail
    from ._5765 import GearMeshTEExcitationDetail
    from ._5766 import GearSetHarmonicAnalysis
    from ._5767 import GeneralPeriodicExcitationDetail
    from ._5768 import GuideDxfModelHarmonicAnalysis
    from ._5769 import HarmonicAnalysis
    from ._5770 import HarmonicAnalysisDrawStyle
    from ._5771 import HarmonicAnalysisExportOptions
    from ._5772 import HarmonicAnalysisFEExportOptions
    from ._5773 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5774 import HarmonicAnalysisOptions
    from ._5775 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5776 import HarmonicAnalysisShaftExportOptions
    from ._5777 import HarmonicAnalysisTorqueInputType
    from ._5778 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5779 import HypoidGearHarmonicAnalysis
    from ._5780 import HypoidGearMeshHarmonicAnalysis
    from ._5781 import HypoidGearSetHarmonicAnalysis
    from ._5782 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5783 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5784 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5785 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5786 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5787 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5788 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5789 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5790 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5791 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5792 import MassDiscHarmonicAnalysis
    from ._5793 import MeasurementComponentHarmonicAnalysis
    from ._5794 import MountableComponentHarmonicAnalysis
    from ._5795 import OilSealHarmonicAnalysis
    from ._5796 import PartHarmonicAnalysis
    from ._5797 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5798 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5799 import PartToPartShearCouplingHarmonicAnalysis
    from ._5800 import PeriodicExcitationWithReferenceShaft
    from ._5801 import PlanetaryConnectionHarmonicAnalysis
    from ._5802 import PlanetaryGearSetHarmonicAnalysis
    from ._5803 import PlanetCarrierHarmonicAnalysis
    from ._5804 import PointLoadHarmonicAnalysis
    from ._5805 import PowerLoadHarmonicAnalysis
    from ._5806 import PulleyHarmonicAnalysis
    from ._5807 import ResponseCacheLevel
    from ._5808 import RingPinsHarmonicAnalysis
    from ._5809 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5810 import RollingRingAssemblyHarmonicAnalysis
    from ._5811 import RollingRingConnectionHarmonicAnalysis
    from ._5812 import RollingRingHarmonicAnalysis
    from ._5813 import RootAssemblyHarmonicAnalysis
    from ._5814 import ShaftHarmonicAnalysis
    from ._5815 import ShaftHubConnectionHarmonicAnalysis
    from ._5816 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5817 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5818 import SpecialisedAssemblyHarmonicAnalysis
    from ._5819 import SpeedOptionsForHarmonicAnalysisResults
    from ._5820 import SpiralBevelGearHarmonicAnalysis
    from ._5821 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5822 import SpiralBevelGearSetHarmonicAnalysis
    from ._5823 import SpringDamperConnectionHarmonicAnalysis
    from ._5824 import SpringDamperHalfHarmonicAnalysis
    from ._5825 import SpringDamperHarmonicAnalysis
    from ._5826 import StiffnessOptionsForHarmonicAnalysis
    from ._5827 import StraightBevelDiffGearHarmonicAnalysis
    from ._5828 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5829 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5830 import StraightBevelGearHarmonicAnalysis
    from ._5831 import StraightBevelGearMeshHarmonicAnalysis
    from ._5832 import StraightBevelGearSetHarmonicAnalysis
    from ._5833 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5834 import StraightBevelSunGearHarmonicAnalysis
    from ._5835 import SynchroniserHalfHarmonicAnalysis
    from ._5836 import SynchroniserHarmonicAnalysis
    from ._5837 import SynchroniserPartHarmonicAnalysis
    from ._5838 import SynchroniserSleeveHarmonicAnalysis
    from ._5839 import TorqueConverterConnectionHarmonicAnalysis
    from ._5840 import TorqueConverterHarmonicAnalysis
    from ._5841 import TorqueConverterPumpHarmonicAnalysis
    from ._5842 import TorqueConverterTurbineHarmonicAnalysis
    from ._5843 import UnbalancedMassExcitationDetail
    from ._5844 import UnbalancedMassHarmonicAnalysis
    from ._5845 import VirtualComponentHarmonicAnalysis
    from ._5846 import WormGearHarmonicAnalysis
    from ._5847 import WormGearMeshHarmonicAnalysis
    from ._5848 import WormGearSetHarmonicAnalysis
    from ._5849 import ZerolBevelGearHarmonicAnalysis
    from ._5850 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5851 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        "_5686": ["AbstractAssemblyHarmonicAnalysis"],
        "_5687": ["AbstractPeriodicExcitationDetail"],
        "_5688": ["AbstractShaftHarmonicAnalysis"],
        "_5689": ["AbstractShaftOrHousingHarmonicAnalysis"],
        "_5690": ["AbstractShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5691": ["AGMAGleasonConicalGearHarmonicAnalysis"],
        "_5692": ["AGMAGleasonConicalGearMeshHarmonicAnalysis"],
        "_5693": ["AGMAGleasonConicalGearSetHarmonicAnalysis"],
        "_5694": ["AssemblyHarmonicAnalysis"],
        "_5695": ["BearingHarmonicAnalysis"],
        "_5696": ["BeltConnectionHarmonicAnalysis"],
        "_5697": ["BeltDriveHarmonicAnalysis"],
        "_5698": ["BevelDifferentialGearHarmonicAnalysis"],
        "_5699": ["BevelDifferentialGearMeshHarmonicAnalysis"],
        "_5700": ["BevelDifferentialGearSetHarmonicAnalysis"],
        "_5701": ["BevelDifferentialPlanetGearHarmonicAnalysis"],
        "_5702": ["BevelDifferentialSunGearHarmonicAnalysis"],
        "_5703": ["BevelGearHarmonicAnalysis"],
        "_5704": ["BevelGearMeshHarmonicAnalysis"],
        "_5705": ["BevelGearSetHarmonicAnalysis"],
        "_5706": ["BoltedJointHarmonicAnalysis"],
        "_5707": ["BoltHarmonicAnalysis"],
        "_5708": ["ClutchConnectionHarmonicAnalysis"],
        "_5709": ["ClutchHalfHarmonicAnalysis"],
        "_5710": ["ClutchHarmonicAnalysis"],
        "_5711": ["CoaxialConnectionHarmonicAnalysis"],
        "_5712": ["ComplianceAndForceData"],
        "_5713": ["ComponentHarmonicAnalysis"],
        "_5714": ["ConceptCouplingConnectionHarmonicAnalysis"],
        "_5715": ["ConceptCouplingHalfHarmonicAnalysis"],
        "_5716": ["ConceptCouplingHarmonicAnalysis"],
        "_5717": ["ConceptGearHarmonicAnalysis"],
        "_5718": ["ConceptGearMeshHarmonicAnalysis"],
        "_5719": ["ConceptGearSetHarmonicAnalysis"],
        "_5720": ["ConicalGearHarmonicAnalysis"],
        "_5721": ["ConicalGearMeshHarmonicAnalysis"],
        "_5722": ["ConicalGearSetHarmonicAnalysis"],
        "_5723": ["ConnectionHarmonicAnalysis"],
        "_5724": ["ConnectorHarmonicAnalysis"],
        "_5725": ["CouplingConnectionHarmonicAnalysis"],
        "_5726": ["CouplingHalfHarmonicAnalysis"],
        "_5727": ["CouplingHarmonicAnalysis"],
        "_5728": ["CVTBeltConnectionHarmonicAnalysis"],
        "_5729": ["CVTHarmonicAnalysis"],
        "_5730": ["CVTPulleyHarmonicAnalysis"],
        "_5731": ["CycloidalAssemblyHarmonicAnalysis"],
        "_5732": ["CycloidalDiscCentralBearingConnectionHarmonicAnalysis"],
        "_5733": ["CycloidalDiscHarmonicAnalysis"],
        "_5734": ["CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"],
        "_5735": ["CylindricalGearHarmonicAnalysis"],
        "_5736": ["CylindricalGearMeshHarmonicAnalysis"],
        "_5737": ["CylindricalGearSetHarmonicAnalysis"],
        "_5738": ["CylindricalPlanetGearHarmonicAnalysis"],
        "_5739": ["DatumHarmonicAnalysis"],
        "_5740": ["DynamicModelForHarmonicAnalysis"],
        "_5741": ["ElectricMachinePeriodicExcitationDetail"],
        "_5742": ["ElectricMachineRotorXForcePeriodicExcitationDetail"],
        "_5743": ["ElectricMachineRotorXMomentPeriodicExcitationDetail"],
        "_5744": ["ElectricMachineRotorYForcePeriodicExcitationDetail"],
        "_5745": ["ElectricMachineRotorYMomentPeriodicExcitationDetail"],
        "_5746": ["ElectricMachineRotorZForcePeriodicExcitationDetail"],
        "_5747": ["ElectricMachineStatorToothAxialLoadsExcitationDetail"],
        "_5748": ["ElectricMachineStatorToothLoadsExcitationDetail"],
        "_5749": ["ElectricMachineStatorToothMomentsExcitationDetail"],
        "_5750": ["ElectricMachineStatorToothRadialLoadsExcitationDetail"],
        "_5751": ["ElectricMachineStatorToothTangentialLoadsExcitationDetail"],
        "_5752": ["ElectricMachineTorqueRipplePeriodicExcitationDetail"],
        "_5753": ["ExportOutputType"],
        "_5754": ["ExternalCADModelHarmonicAnalysis"],
        "_5755": ["FaceGearHarmonicAnalysis"],
        "_5756": ["FaceGearMeshHarmonicAnalysis"],
        "_5757": ["FaceGearSetHarmonicAnalysis"],
        "_5758": ["FEPartHarmonicAnalysis"],
        "_5759": ["FlexiblePinAssemblyHarmonicAnalysis"],
        "_5760": ["FrequencyOptionsForHarmonicAnalysisResults"],
        "_5761": ["GearHarmonicAnalysis"],
        "_5762": ["GearMeshExcitationDetail"],
        "_5763": ["GearMeshHarmonicAnalysis"],
        "_5764": ["GearMeshMisalignmentExcitationDetail"],
        "_5765": ["GearMeshTEExcitationDetail"],
        "_5766": ["GearSetHarmonicAnalysis"],
        "_5767": ["GeneralPeriodicExcitationDetail"],
        "_5768": ["GuideDxfModelHarmonicAnalysis"],
        "_5769": ["HarmonicAnalysis"],
        "_5770": ["HarmonicAnalysisDrawStyle"],
        "_5771": ["HarmonicAnalysisExportOptions"],
        "_5772": ["HarmonicAnalysisFEExportOptions"],
        "_5773": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_5774": ["HarmonicAnalysisOptions"],
        "_5775": ["HarmonicAnalysisRootAssemblyExportOptions"],
        "_5776": ["HarmonicAnalysisShaftExportOptions"],
        "_5777": ["HarmonicAnalysisTorqueInputType"],
        "_5778": ["HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"],
        "_5779": ["HypoidGearHarmonicAnalysis"],
        "_5780": ["HypoidGearMeshHarmonicAnalysis"],
        "_5781": ["HypoidGearSetHarmonicAnalysis"],
        "_5782": ["InterMountableComponentConnectionHarmonicAnalysis"],
        "_5783": ["KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"],
        "_5784": ["KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"],
        "_5785": ["KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"],
        "_5786": ["KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"],
        "_5787": ["KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis"],
        "_5788": ["KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"],
        "_5789": ["KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis"],
        "_5790": ["KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis"],
        "_5791": ["KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"],
        "_5792": ["MassDiscHarmonicAnalysis"],
        "_5793": ["MeasurementComponentHarmonicAnalysis"],
        "_5794": ["MountableComponentHarmonicAnalysis"],
        "_5795": ["OilSealHarmonicAnalysis"],
        "_5796": ["PartHarmonicAnalysis"],
        "_5797": ["PartToPartShearCouplingConnectionHarmonicAnalysis"],
        "_5798": ["PartToPartShearCouplingHalfHarmonicAnalysis"],
        "_5799": ["PartToPartShearCouplingHarmonicAnalysis"],
        "_5800": ["PeriodicExcitationWithReferenceShaft"],
        "_5801": ["PlanetaryConnectionHarmonicAnalysis"],
        "_5802": ["PlanetaryGearSetHarmonicAnalysis"],
        "_5803": ["PlanetCarrierHarmonicAnalysis"],
        "_5804": ["PointLoadHarmonicAnalysis"],
        "_5805": ["PowerLoadHarmonicAnalysis"],
        "_5806": ["PulleyHarmonicAnalysis"],
        "_5807": ["ResponseCacheLevel"],
        "_5808": ["RingPinsHarmonicAnalysis"],
        "_5809": ["RingPinsToDiscConnectionHarmonicAnalysis"],
        "_5810": ["RollingRingAssemblyHarmonicAnalysis"],
        "_5811": ["RollingRingConnectionHarmonicAnalysis"],
        "_5812": ["RollingRingHarmonicAnalysis"],
        "_5813": ["RootAssemblyHarmonicAnalysis"],
        "_5814": ["ShaftHarmonicAnalysis"],
        "_5815": ["ShaftHubConnectionHarmonicAnalysis"],
        "_5816": ["ShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5817": ["SingleNodePeriodicExcitationWithReferenceShaft"],
        "_5818": ["SpecialisedAssemblyHarmonicAnalysis"],
        "_5819": ["SpeedOptionsForHarmonicAnalysisResults"],
        "_5820": ["SpiralBevelGearHarmonicAnalysis"],
        "_5821": ["SpiralBevelGearMeshHarmonicAnalysis"],
        "_5822": ["SpiralBevelGearSetHarmonicAnalysis"],
        "_5823": ["SpringDamperConnectionHarmonicAnalysis"],
        "_5824": ["SpringDamperHalfHarmonicAnalysis"],
        "_5825": ["SpringDamperHarmonicAnalysis"],
        "_5826": ["StiffnessOptionsForHarmonicAnalysis"],
        "_5827": ["StraightBevelDiffGearHarmonicAnalysis"],
        "_5828": ["StraightBevelDiffGearMeshHarmonicAnalysis"],
        "_5829": ["StraightBevelDiffGearSetHarmonicAnalysis"],
        "_5830": ["StraightBevelGearHarmonicAnalysis"],
        "_5831": ["StraightBevelGearMeshHarmonicAnalysis"],
        "_5832": ["StraightBevelGearSetHarmonicAnalysis"],
        "_5833": ["StraightBevelPlanetGearHarmonicAnalysis"],
        "_5834": ["StraightBevelSunGearHarmonicAnalysis"],
        "_5835": ["SynchroniserHalfHarmonicAnalysis"],
        "_5836": ["SynchroniserHarmonicAnalysis"],
        "_5837": ["SynchroniserPartHarmonicAnalysis"],
        "_5838": ["SynchroniserSleeveHarmonicAnalysis"],
        "_5839": ["TorqueConverterConnectionHarmonicAnalysis"],
        "_5840": ["TorqueConverterHarmonicAnalysis"],
        "_5841": ["TorqueConverterPumpHarmonicAnalysis"],
        "_5842": ["TorqueConverterTurbineHarmonicAnalysis"],
        "_5843": ["UnbalancedMassExcitationDetail"],
        "_5844": ["UnbalancedMassHarmonicAnalysis"],
        "_5845": ["VirtualComponentHarmonicAnalysis"],
        "_5846": ["WormGearHarmonicAnalysis"],
        "_5847": ["WormGearMeshHarmonicAnalysis"],
        "_5848": ["WormGearSetHarmonicAnalysis"],
        "_5849": ["ZerolBevelGearHarmonicAnalysis"],
        "_5850": ["ZerolBevelGearMeshHarmonicAnalysis"],
        "_5851": ["ZerolBevelGearSetHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyHarmonicAnalysis",
    "AbstractPeriodicExcitationDetail",
    "AbstractShaftHarmonicAnalysis",
    "AbstractShaftOrHousingHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    "AGMAGleasonConicalGearHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
    "AGMAGleasonConicalGearSetHarmonicAnalysis",
    "AssemblyHarmonicAnalysis",
    "BearingHarmonicAnalysis",
    "BeltConnectionHarmonicAnalysis",
    "BeltDriveHarmonicAnalysis",
    "BevelDifferentialGearHarmonicAnalysis",
    "BevelDifferentialGearMeshHarmonicAnalysis",
    "BevelDifferentialGearSetHarmonicAnalysis",
    "BevelDifferentialPlanetGearHarmonicAnalysis",
    "BevelDifferentialSunGearHarmonicAnalysis",
    "BevelGearHarmonicAnalysis",
    "BevelGearMeshHarmonicAnalysis",
    "BevelGearSetHarmonicAnalysis",
    "BoltedJointHarmonicAnalysis",
    "BoltHarmonicAnalysis",
    "ClutchConnectionHarmonicAnalysis",
    "ClutchHalfHarmonicAnalysis",
    "ClutchHarmonicAnalysis",
    "CoaxialConnectionHarmonicAnalysis",
    "ComplianceAndForceData",
    "ComponentHarmonicAnalysis",
    "ConceptCouplingConnectionHarmonicAnalysis",
    "ConceptCouplingHalfHarmonicAnalysis",
    "ConceptCouplingHarmonicAnalysis",
    "ConceptGearHarmonicAnalysis",
    "ConceptGearMeshHarmonicAnalysis",
    "ConceptGearSetHarmonicAnalysis",
    "ConicalGearHarmonicAnalysis",
    "ConicalGearMeshHarmonicAnalysis",
    "ConicalGearSetHarmonicAnalysis",
    "ConnectionHarmonicAnalysis",
    "ConnectorHarmonicAnalysis",
    "CouplingConnectionHarmonicAnalysis",
    "CouplingHalfHarmonicAnalysis",
    "CouplingHarmonicAnalysis",
    "CVTBeltConnectionHarmonicAnalysis",
    "CVTHarmonicAnalysis",
    "CVTPulleyHarmonicAnalysis",
    "CycloidalAssemblyHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
    "CycloidalDiscHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
    "CylindricalGearHarmonicAnalysis",
    "CylindricalGearMeshHarmonicAnalysis",
    "CylindricalGearSetHarmonicAnalysis",
    "CylindricalPlanetGearHarmonicAnalysis",
    "DatumHarmonicAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "ElectricMachinePeriodicExcitationDetail",
    "ElectricMachineRotorXForcePeriodicExcitationDetail",
    "ElectricMachineRotorXMomentPeriodicExcitationDetail",
    "ElectricMachineRotorYForcePeriodicExcitationDetail",
    "ElectricMachineRotorYMomentPeriodicExcitationDetail",
    "ElectricMachineRotorZForcePeriodicExcitationDetail",
    "ElectricMachineStatorToothAxialLoadsExcitationDetail",
    "ElectricMachineStatorToothLoadsExcitationDetail",
    "ElectricMachineStatorToothMomentsExcitationDetail",
    "ElectricMachineStatorToothRadialLoadsExcitationDetail",
    "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
    "ElectricMachineTorqueRipplePeriodicExcitationDetail",
    "ExportOutputType",
    "ExternalCADModelHarmonicAnalysis",
    "FaceGearHarmonicAnalysis",
    "FaceGearMeshHarmonicAnalysis",
    "FaceGearSetHarmonicAnalysis",
    "FEPartHarmonicAnalysis",
    "FlexiblePinAssemblyHarmonicAnalysis",
    "FrequencyOptionsForHarmonicAnalysisResults",
    "GearHarmonicAnalysis",
    "GearMeshExcitationDetail",
    "GearMeshHarmonicAnalysis",
    "GearMeshMisalignmentExcitationDetail",
    "GearMeshTEExcitationDetail",
    "GearSetHarmonicAnalysis",
    "GeneralPeriodicExcitationDetail",
    "GuideDxfModelHarmonicAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisDrawStyle",
    "HarmonicAnalysisExportOptions",
    "HarmonicAnalysisFEExportOptions",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptions",
    "HarmonicAnalysisRootAssemblyExportOptions",
    "HarmonicAnalysisShaftExportOptions",
    "HarmonicAnalysisTorqueInputType",
    "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
    "HypoidGearHarmonicAnalysis",
    "HypoidGearMeshHarmonicAnalysis",
    "HypoidGearSetHarmonicAnalysis",
    "InterMountableComponentConnectionHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
    "MassDiscHarmonicAnalysis",
    "MeasurementComponentHarmonicAnalysis",
    "MountableComponentHarmonicAnalysis",
    "OilSealHarmonicAnalysis",
    "PartHarmonicAnalysis",
    "PartToPartShearCouplingConnectionHarmonicAnalysis",
    "PartToPartShearCouplingHalfHarmonicAnalysis",
    "PartToPartShearCouplingHarmonicAnalysis",
    "PeriodicExcitationWithReferenceShaft",
    "PlanetaryConnectionHarmonicAnalysis",
    "PlanetaryGearSetHarmonicAnalysis",
    "PlanetCarrierHarmonicAnalysis",
    "PointLoadHarmonicAnalysis",
    "PowerLoadHarmonicAnalysis",
    "PulleyHarmonicAnalysis",
    "ResponseCacheLevel",
    "RingPinsHarmonicAnalysis",
    "RingPinsToDiscConnectionHarmonicAnalysis",
    "RollingRingAssemblyHarmonicAnalysis",
    "RollingRingConnectionHarmonicAnalysis",
    "RollingRingHarmonicAnalysis",
    "RootAssemblyHarmonicAnalysis",
    "ShaftHarmonicAnalysis",
    "ShaftHubConnectionHarmonicAnalysis",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
    "SingleNodePeriodicExcitationWithReferenceShaft",
    "SpecialisedAssemblyHarmonicAnalysis",
    "SpeedOptionsForHarmonicAnalysisResults",
    "SpiralBevelGearHarmonicAnalysis",
    "SpiralBevelGearMeshHarmonicAnalysis",
    "SpiralBevelGearSetHarmonicAnalysis",
    "SpringDamperConnectionHarmonicAnalysis",
    "SpringDamperHalfHarmonicAnalysis",
    "SpringDamperHarmonicAnalysis",
    "StiffnessOptionsForHarmonicAnalysis",
    "StraightBevelDiffGearHarmonicAnalysis",
    "StraightBevelDiffGearMeshHarmonicAnalysis",
    "StraightBevelDiffGearSetHarmonicAnalysis",
    "StraightBevelGearHarmonicAnalysis",
    "StraightBevelGearMeshHarmonicAnalysis",
    "StraightBevelGearSetHarmonicAnalysis",
    "StraightBevelPlanetGearHarmonicAnalysis",
    "StraightBevelSunGearHarmonicAnalysis",
    "SynchroniserHalfHarmonicAnalysis",
    "SynchroniserHarmonicAnalysis",
    "SynchroniserPartHarmonicAnalysis",
    "SynchroniserSleeveHarmonicAnalysis",
    "TorqueConverterConnectionHarmonicAnalysis",
    "TorqueConverterHarmonicAnalysis",
    "TorqueConverterPumpHarmonicAnalysis",
    "TorqueConverterTurbineHarmonicAnalysis",
    "UnbalancedMassExcitationDetail",
    "UnbalancedMassHarmonicAnalysis",
    "VirtualComponentHarmonicAnalysis",
    "WormGearHarmonicAnalysis",
    "WormGearMeshHarmonicAnalysis",
    "WormGearSetHarmonicAnalysis",
    "ZerolBevelGearHarmonicAnalysis",
    "ZerolBevelGearMeshHarmonicAnalysis",
    "ZerolBevelGearSetHarmonicAnalysis",
)
