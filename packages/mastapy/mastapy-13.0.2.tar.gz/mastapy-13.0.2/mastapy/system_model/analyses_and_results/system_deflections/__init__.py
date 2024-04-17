"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2693 import AbstractAssemblySystemDeflection
    from ._2694 import AbstractShaftOrHousingSystemDeflection
    from ._2695 import AbstractShaftSystemDeflection
    from ._2696 import AbstractShaftToMountableComponentConnectionSystemDeflection
    from ._2697 import AGMAGleasonConicalGearMeshSystemDeflection
    from ._2698 import AGMAGleasonConicalGearSetSystemDeflection
    from ._2699 import AGMAGleasonConicalGearSystemDeflection
    from ._2700 import AssemblySystemDeflection
    from ._2701 import BearingDynamicElementContactPropertyWrapper
    from ._2702 import BearingDynamicElementPropertyWrapper
    from ._2703 import BearingDynamicPostAnalysisResultWrapper
    from ._2704 import BearingDynamicResultsPropertyWrapper
    from ._2705 import BearingDynamicResultsUIWrapper
    from ._2706 import BearingSystemDeflection
    from ._2707 import BeltConnectionSystemDeflection
    from ._2708 import BeltDriveSystemDeflection
    from ._2709 import BevelDifferentialGearMeshSystemDeflection
    from ._2710 import BevelDifferentialGearSetSystemDeflection
    from ._2711 import BevelDifferentialGearSystemDeflection
    from ._2712 import BevelDifferentialPlanetGearSystemDeflection
    from ._2713 import BevelDifferentialSunGearSystemDeflection
    from ._2714 import BevelGearMeshSystemDeflection
    from ._2715 import BevelGearSetSystemDeflection
    from ._2716 import BevelGearSystemDeflection
    from ._2717 import BoltedJointSystemDeflection
    from ._2718 import BoltSystemDeflection
    from ._2719 import ClutchConnectionSystemDeflection
    from ._2720 import ClutchHalfSystemDeflection
    from ._2721 import ClutchSystemDeflection
    from ._2722 import CoaxialConnectionSystemDeflection
    from ._2723 import ComponentSystemDeflection
    from ._2724 import ConcentricPartGroupCombinationSystemDeflectionResults
    from ._2725 import ConceptCouplingConnectionSystemDeflection
    from ._2726 import ConceptCouplingHalfSystemDeflection
    from ._2727 import ConceptCouplingSystemDeflection
    from ._2728 import ConceptGearMeshSystemDeflection
    from ._2729 import ConceptGearSetSystemDeflection
    from ._2730 import ConceptGearSystemDeflection
    from ._2731 import ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2732 import ConicalGearMeshSystemDeflection
    from ._2733 import ConicalGearSetSystemDeflection
    from ._2734 import ConicalGearSystemDeflection
    from ._2735 import ConnectionSystemDeflection
    from ._2736 import ConnectorSystemDeflection
    from ._2737 import CouplingConnectionSystemDeflection
    from ._2738 import CouplingHalfSystemDeflection
    from ._2739 import CouplingSystemDeflection
    from ._2740 import CVTBeltConnectionSystemDeflection
    from ._2741 import CVTPulleySystemDeflection
    from ._2742 import CVTSystemDeflection
    from ._2743 import CycloidalAssemblySystemDeflection
    from ._2744 import CycloidalDiscCentralBearingConnectionSystemDeflection
    from ._2745 import CycloidalDiscPlanetaryBearingConnectionSystemDeflection
    from ._2746 import CycloidalDiscSystemDeflection
    from ._2747 import CylindricalGearMeshSystemDeflection
    from ._2748 import CylindricalGearMeshSystemDeflectionTimestep
    from ._2749 import CylindricalGearMeshSystemDeflectionWithLTCAResults
    from ._2750 import CylindricalGearSetSystemDeflection
    from ._2751 import CylindricalGearSetSystemDeflectionTimestep
    from ._2752 import CylindricalGearSetSystemDeflectionWithLTCAResults
    from ._2753 import CylindricalGearSystemDeflection
    from ._2754 import CylindricalGearSystemDeflectionTimestep
    from ._2755 import CylindricalGearSystemDeflectionWithLTCAResults
    from ._2756 import CylindricalMeshedGearFlankSystemDeflection
    from ._2757 import CylindricalMeshedGearSystemDeflection
    from ._2758 import CylindricalPlanetGearSystemDeflection
    from ._2759 import DatumSystemDeflection
    from ._2760 import ExternalCADModelSystemDeflection
    from ._2761 import FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2762 import FaceGearMeshSystemDeflection
    from ._2763 import FaceGearSetSystemDeflection
    from ._2764 import FaceGearSystemDeflection
    from ._2765 import FEPartSystemDeflection
    from ._2766 import FlexiblePinAssemblySystemDeflection
    from ._2767 import GearMeshSystemDeflection
    from ._2768 import GearSetSystemDeflection
    from ._2769 import GearSystemDeflection
    from ._2770 import GuideDxfModelSystemDeflection
    from ._2771 import HypoidGearMeshSystemDeflection
    from ._2772 import HypoidGearSetSystemDeflection
    from ._2773 import HypoidGearSystemDeflection
    from ._2774 import InformationForContactAtPointAlongFaceWidth
    from ._2775 import InterMountableComponentConnectionSystemDeflection
    from ._2776 import KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
    from ._2777 import KlingelnbergCycloPalloidConicalGearSetSystemDeflection
    from ._2778 import KlingelnbergCycloPalloidConicalGearSystemDeflection
    from ._2779 import KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
    from ._2780 import KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
    from ._2781 import KlingelnbergCycloPalloidHypoidGearSystemDeflection
    from ._2782 import KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
    from ._2783 import KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
    from ._2784 import KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
    from ._2785 import LoadCaseOverallEfficiencyResult
    from ._2786 import LoadSharingFactorReporter
    from ._2787 import MassDiscSystemDeflection
    from ._2788 import MeasurementComponentSystemDeflection
    from ._2789 import MeshSeparationsAtFaceWidth
    from ._2790 import MountableComponentSystemDeflection
    from ._2791 import ObservedPinStiffnessReporter
    from ._2792 import OilSealSystemDeflection
    from ._2793 import PartSystemDeflection
    from ._2794 import PartToPartShearCouplingConnectionSystemDeflection
    from ._2795 import PartToPartShearCouplingHalfSystemDeflection
    from ._2796 import PartToPartShearCouplingSystemDeflection
    from ._2797 import PlanetaryConnectionSystemDeflection
    from ._2798 import PlanetCarrierSystemDeflection
    from ._2799 import PointLoadSystemDeflection
    from ._2800 import PowerLoadSystemDeflection
    from ._2801 import PulleySystemDeflection
    from ._2802 import RingPinsSystemDeflection
    from ._2803 import RingPinsToDiscConnectionSystemDeflection
    from ._2804 import RingPinToDiscContactReporting
    from ._2805 import RollingRingAssemblySystemDeflection
    from ._2806 import RollingRingConnectionSystemDeflection
    from ._2807 import RollingRingSystemDeflection
    from ._2808 import RootAssemblySystemDeflection
    from ._2809 import ShaftHubConnectionSystemDeflection
    from ._2810 import ShaftSectionEndResultsSystemDeflection
    from ._2811 import ShaftSectionSystemDeflection
    from ._2812 import ShaftSystemDeflection
    from ._2813 import ShaftToMountableComponentConnectionSystemDeflection
    from ._2814 import SpecialisedAssemblySystemDeflection
    from ._2815 import SpiralBevelGearMeshSystemDeflection
    from ._2816 import SpiralBevelGearSetSystemDeflection
    from ._2817 import SpiralBevelGearSystemDeflection
    from ._2818 import SpringDamperConnectionSystemDeflection
    from ._2819 import SpringDamperHalfSystemDeflection
    from ._2820 import SpringDamperSystemDeflection
    from ._2821 import StraightBevelDiffGearMeshSystemDeflection
    from ._2822 import StraightBevelDiffGearSetSystemDeflection
    from ._2823 import StraightBevelDiffGearSystemDeflection
    from ._2824 import StraightBevelGearMeshSystemDeflection
    from ._2825 import StraightBevelGearSetSystemDeflection
    from ._2826 import StraightBevelGearSystemDeflection
    from ._2827 import StraightBevelPlanetGearSystemDeflection
    from ._2828 import StraightBevelSunGearSystemDeflection
    from ._2829 import SynchroniserHalfSystemDeflection
    from ._2830 import SynchroniserPartSystemDeflection
    from ._2831 import SynchroniserSleeveSystemDeflection
    from ._2832 import SynchroniserSystemDeflection
    from ._2833 import SystemDeflection
    from ._2834 import SystemDeflectionDrawStyle
    from ._2835 import SystemDeflectionOptions
    from ._2836 import TorqueConverterConnectionSystemDeflection
    from ._2837 import TorqueConverterPumpSystemDeflection
    from ._2838 import TorqueConverterSystemDeflection
    from ._2839 import TorqueConverterTurbineSystemDeflection
    from ._2840 import TorsionalSystemDeflection
    from ._2841 import TransmissionErrorResult
    from ._2842 import UnbalancedMassSystemDeflection
    from ._2843 import VirtualComponentSystemDeflection
    from ._2844 import WormGearMeshSystemDeflection
    from ._2845 import WormGearSetSystemDeflection
    from ._2846 import WormGearSystemDeflection
    from ._2847 import ZerolBevelGearMeshSystemDeflection
    from ._2848 import ZerolBevelGearSetSystemDeflection
    from ._2849 import ZerolBevelGearSystemDeflection
else:
    import_structure = {
        "_2693": ["AbstractAssemblySystemDeflection"],
        "_2694": ["AbstractShaftOrHousingSystemDeflection"],
        "_2695": ["AbstractShaftSystemDeflection"],
        "_2696": ["AbstractShaftToMountableComponentConnectionSystemDeflection"],
        "_2697": ["AGMAGleasonConicalGearMeshSystemDeflection"],
        "_2698": ["AGMAGleasonConicalGearSetSystemDeflection"],
        "_2699": ["AGMAGleasonConicalGearSystemDeflection"],
        "_2700": ["AssemblySystemDeflection"],
        "_2701": ["BearingDynamicElementContactPropertyWrapper"],
        "_2702": ["BearingDynamicElementPropertyWrapper"],
        "_2703": ["BearingDynamicPostAnalysisResultWrapper"],
        "_2704": ["BearingDynamicResultsPropertyWrapper"],
        "_2705": ["BearingDynamicResultsUIWrapper"],
        "_2706": ["BearingSystemDeflection"],
        "_2707": ["BeltConnectionSystemDeflection"],
        "_2708": ["BeltDriveSystemDeflection"],
        "_2709": ["BevelDifferentialGearMeshSystemDeflection"],
        "_2710": ["BevelDifferentialGearSetSystemDeflection"],
        "_2711": ["BevelDifferentialGearSystemDeflection"],
        "_2712": ["BevelDifferentialPlanetGearSystemDeflection"],
        "_2713": ["BevelDifferentialSunGearSystemDeflection"],
        "_2714": ["BevelGearMeshSystemDeflection"],
        "_2715": ["BevelGearSetSystemDeflection"],
        "_2716": ["BevelGearSystemDeflection"],
        "_2717": ["BoltedJointSystemDeflection"],
        "_2718": ["BoltSystemDeflection"],
        "_2719": ["ClutchConnectionSystemDeflection"],
        "_2720": ["ClutchHalfSystemDeflection"],
        "_2721": ["ClutchSystemDeflection"],
        "_2722": ["CoaxialConnectionSystemDeflection"],
        "_2723": ["ComponentSystemDeflection"],
        "_2724": ["ConcentricPartGroupCombinationSystemDeflectionResults"],
        "_2725": ["ConceptCouplingConnectionSystemDeflection"],
        "_2726": ["ConceptCouplingHalfSystemDeflection"],
        "_2727": ["ConceptCouplingSystemDeflection"],
        "_2728": ["ConceptGearMeshSystemDeflection"],
        "_2729": ["ConceptGearSetSystemDeflection"],
        "_2730": ["ConceptGearSystemDeflection"],
        "_2731": ["ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2732": ["ConicalGearMeshSystemDeflection"],
        "_2733": ["ConicalGearSetSystemDeflection"],
        "_2734": ["ConicalGearSystemDeflection"],
        "_2735": ["ConnectionSystemDeflection"],
        "_2736": ["ConnectorSystemDeflection"],
        "_2737": ["CouplingConnectionSystemDeflection"],
        "_2738": ["CouplingHalfSystemDeflection"],
        "_2739": ["CouplingSystemDeflection"],
        "_2740": ["CVTBeltConnectionSystemDeflection"],
        "_2741": ["CVTPulleySystemDeflection"],
        "_2742": ["CVTSystemDeflection"],
        "_2743": ["CycloidalAssemblySystemDeflection"],
        "_2744": ["CycloidalDiscCentralBearingConnectionSystemDeflection"],
        "_2745": ["CycloidalDiscPlanetaryBearingConnectionSystemDeflection"],
        "_2746": ["CycloidalDiscSystemDeflection"],
        "_2747": ["CylindricalGearMeshSystemDeflection"],
        "_2748": ["CylindricalGearMeshSystemDeflectionTimestep"],
        "_2749": ["CylindricalGearMeshSystemDeflectionWithLTCAResults"],
        "_2750": ["CylindricalGearSetSystemDeflection"],
        "_2751": ["CylindricalGearSetSystemDeflectionTimestep"],
        "_2752": ["CylindricalGearSetSystemDeflectionWithLTCAResults"],
        "_2753": ["CylindricalGearSystemDeflection"],
        "_2754": ["CylindricalGearSystemDeflectionTimestep"],
        "_2755": ["CylindricalGearSystemDeflectionWithLTCAResults"],
        "_2756": ["CylindricalMeshedGearFlankSystemDeflection"],
        "_2757": ["CylindricalMeshedGearSystemDeflection"],
        "_2758": ["CylindricalPlanetGearSystemDeflection"],
        "_2759": ["DatumSystemDeflection"],
        "_2760": ["ExternalCADModelSystemDeflection"],
        "_2761": ["FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2762": ["FaceGearMeshSystemDeflection"],
        "_2763": ["FaceGearSetSystemDeflection"],
        "_2764": ["FaceGearSystemDeflection"],
        "_2765": ["FEPartSystemDeflection"],
        "_2766": ["FlexiblePinAssemblySystemDeflection"],
        "_2767": ["GearMeshSystemDeflection"],
        "_2768": ["GearSetSystemDeflection"],
        "_2769": ["GearSystemDeflection"],
        "_2770": ["GuideDxfModelSystemDeflection"],
        "_2771": ["HypoidGearMeshSystemDeflection"],
        "_2772": ["HypoidGearSetSystemDeflection"],
        "_2773": ["HypoidGearSystemDeflection"],
        "_2774": ["InformationForContactAtPointAlongFaceWidth"],
        "_2775": ["InterMountableComponentConnectionSystemDeflection"],
        "_2776": ["KlingelnbergCycloPalloidConicalGearMeshSystemDeflection"],
        "_2777": ["KlingelnbergCycloPalloidConicalGearSetSystemDeflection"],
        "_2778": ["KlingelnbergCycloPalloidConicalGearSystemDeflection"],
        "_2779": ["KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection"],
        "_2780": ["KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"],
        "_2781": ["KlingelnbergCycloPalloidHypoidGearSystemDeflection"],
        "_2782": ["KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"],
        "_2783": ["KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection"],
        "_2784": ["KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection"],
        "_2785": ["LoadCaseOverallEfficiencyResult"],
        "_2786": ["LoadSharingFactorReporter"],
        "_2787": ["MassDiscSystemDeflection"],
        "_2788": ["MeasurementComponentSystemDeflection"],
        "_2789": ["MeshSeparationsAtFaceWidth"],
        "_2790": ["MountableComponentSystemDeflection"],
        "_2791": ["ObservedPinStiffnessReporter"],
        "_2792": ["OilSealSystemDeflection"],
        "_2793": ["PartSystemDeflection"],
        "_2794": ["PartToPartShearCouplingConnectionSystemDeflection"],
        "_2795": ["PartToPartShearCouplingHalfSystemDeflection"],
        "_2796": ["PartToPartShearCouplingSystemDeflection"],
        "_2797": ["PlanetaryConnectionSystemDeflection"],
        "_2798": ["PlanetCarrierSystemDeflection"],
        "_2799": ["PointLoadSystemDeflection"],
        "_2800": ["PowerLoadSystemDeflection"],
        "_2801": ["PulleySystemDeflection"],
        "_2802": ["RingPinsSystemDeflection"],
        "_2803": ["RingPinsToDiscConnectionSystemDeflection"],
        "_2804": ["RingPinToDiscContactReporting"],
        "_2805": ["RollingRingAssemblySystemDeflection"],
        "_2806": ["RollingRingConnectionSystemDeflection"],
        "_2807": ["RollingRingSystemDeflection"],
        "_2808": ["RootAssemblySystemDeflection"],
        "_2809": ["ShaftHubConnectionSystemDeflection"],
        "_2810": ["ShaftSectionEndResultsSystemDeflection"],
        "_2811": ["ShaftSectionSystemDeflection"],
        "_2812": ["ShaftSystemDeflection"],
        "_2813": ["ShaftToMountableComponentConnectionSystemDeflection"],
        "_2814": ["SpecialisedAssemblySystemDeflection"],
        "_2815": ["SpiralBevelGearMeshSystemDeflection"],
        "_2816": ["SpiralBevelGearSetSystemDeflection"],
        "_2817": ["SpiralBevelGearSystemDeflection"],
        "_2818": ["SpringDamperConnectionSystemDeflection"],
        "_2819": ["SpringDamperHalfSystemDeflection"],
        "_2820": ["SpringDamperSystemDeflection"],
        "_2821": ["StraightBevelDiffGearMeshSystemDeflection"],
        "_2822": ["StraightBevelDiffGearSetSystemDeflection"],
        "_2823": ["StraightBevelDiffGearSystemDeflection"],
        "_2824": ["StraightBevelGearMeshSystemDeflection"],
        "_2825": ["StraightBevelGearSetSystemDeflection"],
        "_2826": ["StraightBevelGearSystemDeflection"],
        "_2827": ["StraightBevelPlanetGearSystemDeflection"],
        "_2828": ["StraightBevelSunGearSystemDeflection"],
        "_2829": ["SynchroniserHalfSystemDeflection"],
        "_2830": ["SynchroniserPartSystemDeflection"],
        "_2831": ["SynchroniserSleeveSystemDeflection"],
        "_2832": ["SynchroniserSystemDeflection"],
        "_2833": ["SystemDeflection"],
        "_2834": ["SystemDeflectionDrawStyle"],
        "_2835": ["SystemDeflectionOptions"],
        "_2836": ["TorqueConverterConnectionSystemDeflection"],
        "_2837": ["TorqueConverterPumpSystemDeflection"],
        "_2838": ["TorqueConverterSystemDeflection"],
        "_2839": ["TorqueConverterTurbineSystemDeflection"],
        "_2840": ["TorsionalSystemDeflection"],
        "_2841": ["TransmissionErrorResult"],
        "_2842": ["UnbalancedMassSystemDeflection"],
        "_2843": ["VirtualComponentSystemDeflection"],
        "_2844": ["WormGearMeshSystemDeflection"],
        "_2845": ["WormGearSetSystemDeflection"],
        "_2846": ["WormGearSystemDeflection"],
        "_2847": ["ZerolBevelGearMeshSystemDeflection"],
        "_2848": ["ZerolBevelGearSetSystemDeflection"],
        "_2849": ["ZerolBevelGearSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySystemDeflection",
    "AbstractShaftOrHousingSystemDeflection",
    "AbstractShaftSystemDeflection",
    "AbstractShaftToMountableComponentConnectionSystemDeflection",
    "AGMAGleasonConicalGearMeshSystemDeflection",
    "AGMAGleasonConicalGearSetSystemDeflection",
    "AGMAGleasonConicalGearSystemDeflection",
    "AssemblySystemDeflection",
    "BearingDynamicElementContactPropertyWrapper",
    "BearingDynamicElementPropertyWrapper",
    "BearingDynamicPostAnalysisResultWrapper",
    "BearingDynamicResultsPropertyWrapper",
    "BearingDynamicResultsUIWrapper",
    "BearingSystemDeflection",
    "BeltConnectionSystemDeflection",
    "BeltDriveSystemDeflection",
    "BevelDifferentialGearMeshSystemDeflection",
    "BevelDifferentialGearSetSystemDeflection",
    "BevelDifferentialGearSystemDeflection",
    "BevelDifferentialPlanetGearSystemDeflection",
    "BevelDifferentialSunGearSystemDeflection",
    "BevelGearMeshSystemDeflection",
    "BevelGearSetSystemDeflection",
    "BevelGearSystemDeflection",
    "BoltedJointSystemDeflection",
    "BoltSystemDeflection",
    "ClutchConnectionSystemDeflection",
    "ClutchHalfSystemDeflection",
    "ClutchSystemDeflection",
    "CoaxialConnectionSystemDeflection",
    "ComponentSystemDeflection",
    "ConcentricPartGroupCombinationSystemDeflectionResults",
    "ConceptCouplingConnectionSystemDeflection",
    "ConceptCouplingHalfSystemDeflection",
    "ConceptCouplingSystemDeflection",
    "ConceptGearMeshSystemDeflection",
    "ConceptGearSetSystemDeflection",
    "ConceptGearSystemDeflection",
    "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "ConicalGearMeshSystemDeflection",
    "ConicalGearSetSystemDeflection",
    "ConicalGearSystemDeflection",
    "ConnectionSystemDeflection",
    "ConnectorSystemDeflection",
    "CouplingConnectionSystemDeflection",
    "CouplingHalfSystemDeflection",
    "CouplingSystemDeflection",
    "CVTBeltConnectionSystemDeflection",
    "CVTPulleySystemDeflection",
    "CVTSystemDeflection",
    "CycloidalAssemblySystemDeflection",
    "CycloidalDiscCentralBearingConnectionSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
    "CycloidalDiscSystemDeflection",
    "CylindricalGearMeshSystemDeflection",
    "CylindricalGearMeshSystemDeflectionTimestep",
    "CylindricalGearMeshSystemDeflectionWithLTCAResults",
    "CylindricalGearSetSystemDeflection",
    "CylindricalGearSetSystemDeflectionTimestep",
    "CylindricalGearSetSystemDeflectionWithLTCAResults",
    "CylindricalGearSystemDeflection",
    "CylindricalGearSystemDeflectionTimestep",
    "CylindricalGearSystemDeflectionWithLTCAResults",
    "CylindricalMeshedGearFlankSystemDeflection",
    "CylindricalMeshedGearSystemDeflection",
    "CylindricalPlanetGearSystemDeflection",
    "DatumSystemDeflection",
    "ExternalCADModelSystemDeflection",
    "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "FaceGearMeshSystemDeflection",
    "FaceGearSetSystemDeflection",
    "FaceGearSystemDeflection",
    "FEPartSystemDeflection",
    "FlexiblePinAssemblySystemDeflection",
    "GearMeshSystemDeflection",
    "GearSetSystemDeflection",
    "GearSystemDeflection",
    "GuideDxfModelSystemDeflection",
    "HypoidGearMeshSystemDeflection",
    "HypoidGearSetSystemDeflection",
    "HypoidGearSystemDeflection",
    "InformationForContactAtPointAlongFaceWidth",
    "InterMountableComponentConnectionSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
    "LoadCaseOverallEfficiencyResult",
    "LoadSharingFactorReporter",
    "MassDiscSystemDeflection",
    "MeasurementComponentSystemDeflection",
    "MeshSeparationsAtFaceWidth",
    "MountableComponentSystemDeflection",
    "ObservedPinStiffnessReporter",
    "OilSealSystemDeflection",
    "PartSystemDeflection",
    "PartToPartShearCouplingConnectionSystemDeflection",
    "PartToPartShearCouplingHalfSystemDeflection",
    "PartToPartShearCouplingSystemDeflection",
    "PlanetaryConnectionSystemDeflection",
    "PlanetCarrierSystemDeflection",
    "PointLoadSystemDeflection",
    "PowerLoadSystemDeflection",
    "PulleySystemDeflection",
    "RingPinsSystemDeflection",
    "RingPinsToDiscConnectionSystemDeflection",
    "RingPinToDiscContactReporting",
    "RollingRingAssemblySystemDeflection",
    "RollingRingConnectionSystemDeflection",
    "RollingRingSystemDeflection",
    "RootAssemblySystemDeflection",
    "ShaftHubConnectionSystemDeflection",
    "ShaftSectionEndResultsSystemDeflection",
    "ShaftSectionSystemDeflection",
    "ShaftSystemDeflection",
    "ShaftToMountableComponentConnectionSystemDeflection",
    "SpecialisedAssemblySystemDeflection",
    "SpiralBevelGearMeshSystemDeflection",
    "SpiralBevelGearSetSystemDeflection",
    "SpiralBevelGearSystemDeflection",
    "SpringDamperConnectionSystemDeflection",
    "SpringDamperHalfSystemDeflection",
    "SpringDamperSystemDeflection",
    "StraightBevelDiffGearMeshSystemDeflection",
    "StraightBevelDiffGearSetSystemDeflection",
    "StraightBevelDiffGearSystemDeflection",
    "StraightBevelGearMeshSystemDeflection",
    "StraightBevelGearSetSystemDeflection",
    "StraightBevelGearSystemDeflection",
    "StraightBevelPlanetGearSystemDeflection",
    "StraightBevelSunGearSystemDeflection",
    "SynchroniserHalfSystemDeflection",
    "SynchroniserPartSystemDeflection",
    "SynchroniserSleeveSystemDeflection",
    "SynchroniserSystemDeflection",
    "SystemDeflection",
    "SystemDeflectionDrawStyle",
    "SystemDeflectionOptions",
    "TorqueConverterConnectionSystemDeflection",
    "TorqueConverterPumpSystemDeflection",
    "TorqueConverterSystemDeflection",
    "TorqueConverterTurbineSystemDeflection",
    "TorsionalSystemDeflection",
    "TransmissionErrorResult",
    "UnbalancedMassSystemDeflection",
    "VirtualComponentSystemDeflection",
    "WormGearMeshSystemDeflection",
    "WormGearSetSystemDeflection",
    "WormGearSystemDeflection",
    "ZerolBevelGearMeshSystemDeflection",
    "ZerolBevelGearSetSystemDeflection",
    "ZerolBevelGearSystemDeflection",
)
