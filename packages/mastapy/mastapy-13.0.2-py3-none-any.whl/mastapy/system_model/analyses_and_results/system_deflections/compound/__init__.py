"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2859 import AbstractAssemblyCompoundSystemDeflection
    from ._2860 import AbstractShaftCompoundSystemDeflection
    from ._2861 import AbstractShaftOrHousingCompoundSystemDeflection
    from ._2862 import (
        AbstractShaftToMountableComponentConnectionCompoundSystemDeflection,
    )
    from ._2863 import AGMAGleasonConicalGearCompoundSystemDeflection
    from ._2864 import AGMAGleasonConicalGearMeshCompoundSystemDeflection
    from ._2865 import AGMAGleasonConicalGearSetCompoundSystemDeflection
    from ._2866 import AssemblyCompoundSystemDeflection
    from ._2867 import BearingCompoundSystemDeflection
    from ._2868 import BeltConnectionCompoundSystemDeflection
    from ._2869 import BeltDriveCompoundSystemDeflection
    from ._2870 import BevelDifferentialGearCompoundSystemDeflection
    from ._2871 import BevelDifferentialGearMeshCompoundSystemDeflection
    from ._2872 import BevelDifferentialGearSetCompoundSystemDeflection
    from ._2873 import BevelDifferentialPlanetGearCompoundSystemDeflection
    from ._2874 import BevelDifferentialSunGearCompoundSystemDeflection
    from ._2875 import BevelGearCompoundSystemDeflection
    from ._2876 import BevelGearMeshCompoundSystemDeflection
    from ._2877 import BevelGearSetCompoundSystemDeflection
    from ._2878 import BoltCompoundSystemDeflection
    from ._2879 import BoltedJointCompoundSystemDeflection
    from ._2880 import ClutchCompoundSystemDeflection
    from ._2881 import ClutchConnectionCompoundSystemDeflection
    from ._2882 import ClutchHalfCompoundSystemDeflection
    from ._2883 import CoaxialConnectionCompoundSystemDeflection
    from ._2884 import ComponentCompoundSystemDeflection
    from ._2885 import ConceptCouplingCompoundSystemDeflection
    from ._2886 import ConceptCouplingConnectionCompoundSystemDeflection
    from ._2887 import ConceptCouplingHalfCompoundSystemDeflection
    from ._2888 import ConceptGearCompoundSystemDeflection
    from ._2889 import ConceptGearMeshCompoundSystemDeflection
    from ._2890 import ConceptGearSetCompoundSystemDeflection
    from ._2891 import ConicalGearCompoundSystemDeflection
    from ._2892 import ConicalGearMeshCompoundSystemDeflection
    from ._2893 import ConicalGearSetCompoundSystemDeflection
    from ._2894 import ConnectionCompoundSystemDeflection
    from ._2895 import ConnectorCompoundSystemDeflection
    from ._2896 import CouplingCompoundSystemDeflection
    from ._2897 import CouplingConnectionCompoundSystemDeflection
    from ._2898 import CouplingHalfCompoundSystemDeflection
    from ._2899 import CVTBeltConnectionCompoundSystemDeflection
    from ._2900 import CVTCompoundSystemDeflection
    from ._2901 import CVTPulleyCompoundSystemDeflection
    from ._2902 import CycloidalAssemblyCompoundSystemDeflection
    from ._2903 import CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
    from ._2904 import CycloidalDiscCompoundSystemDeflection
    from ._2905 import CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
    from ._2906 import CylindricalGearCompoundSystemDeflection
    from ._2907 import CylindricalGearMeshCompoundSystemDeflection
    from ._2908 import CylindricalGearSetCompoundSystemDeflection
    from ._2909 import CylindricalPlanetGearCompoundSystemDeflection
    from ._2910 import DatumCompoundSystemDeflection
    from ._2911 import DutyCycleEfficiencyResults
    from ._2912 import ExternalCADModelCompoundSystemDeflection
    from ._2913 import FaceGearCompoundSystemDeflection
    from ._2914 import FaceGearMeshCompoundSystemDeflection
    from ._2915 import FaceGearSetCompoundSystemDeflection
    from ._2916 import FEPartCompoundSystemDeflection
    from ._2917 import FlexiblePinAssemblyCompoundSystemDeflection
    from ._2918 import GearCompoundSystemDeflection
    from ._2919 import GearMeshCompoundSystemDeflection
    from ._2920 import GearSetCompoundSystemDeflection
    from ._2921 import GuideDxfModelCompoundSystemDeflection
    from ._2922 import HypoidGearCompoundSystemDeflection
    from ._2923 import HypoidGearMeshCompoundSystemDeflection
    from ._2924 import HypoidGearSetCompoundSystemDeflection
    from ._2925 import InterMountableComponentConnectionCompoundSystemDeflection
    from ._2926 import KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
    from ._2927 import KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
    from ._2928 import KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
    from ._2929 import KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
    from ._2930 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
    from ._2931 import KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
    from ._2932 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
    from ._2933 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection,
    )
    from ._2934 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection,
    )
    from ._2935 import MassDiscCompoundSystemDeflection
    from ._2936 import MeasurementComponentCompoundSystemDeflection
    from ._2937 import MountableComponentCompoundSystemDeflection
    from ._2938 import OilSealCompoundSystemDeflection
    from ._2939 import PartCompoundSystemDeflection
    from ._2940 import PartToPartShearCouplingCompoundSystemDeflection
    from ._2941 import PartToPartShearCouplingConnectionCompoundSystemDeflection
    from ._2942 import PartToPartShearCouplingHalfCompoundSystemDeflection
    from ._2943 import PlanetaryConnectionCompoundSystemDeflection
    from ._2944 import PlanetaryGearSetCompoundSystemDeflection
    from ._2945 import PlanetCarrierCompoundSystemDeflection
    from ._2946 import PointLoadCompoundSystemDeflection
    from ._2947 import PowerLoadCompoundSystemDeflection
    from ._2948 import PulleyCompoundSystemDeflection
    from ._2949 import RingPinsCompoundSystemDeflection
    from ._2950 import RingPinsToDiscConnectionCompoundSystemDeflection
    from ._2951 import RollingRingAssemblyCompoundSystemDeflection
    from ._2952 import RollingRingCompoundSystemDeflection
    from ._2953 import RollingRingConnectionCompoundSystemDeflection
    from ._2954 import RootAssemblyCompoundSystemDeflection
    from ._2955 import ShaftCompoundSystemDeflection
    from ._2956 import ShaftDutyCycleSystemDeflection
    from ._2957 import ShaftHubConnectionCompoundSystemDeflection
    from ._2958 import ShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2959 import SpecialisedAssemblyCompoundSystemDeflection
    from ._2960 import SpiralBevelGearCompoundSystemDeflection
    from ._2961 import SpiralBevelGearMeshCompoundSystemDeflection
    from ._2962 import SpiralBevelGearSetCompoundSystemDeflection
    from ._2963 import SpringDamperCompoundSystemDeflection
    from ._2964 import SpringDamperConnectionCompoundSystemDeflection
    from ._2965 import SpringDamperHalfCompoundSystemDeflection
    from ._2966 import StraightBevelDiffGearCompoundSystemDeflection
    from ._2967 import StraightBevelDiffGearMeshCompoundSystemDeflection
    from ._2968 import StraightBevelDiffGearSetCompoundSystemDeflection
    from ._2969 import StraightBevelGearCompoundSystemDeflection
    from ._2970 import StraightBevelGearMeshCompoundSystemDeflection
    from ._2971 import StraightBevelGearSetCompoundSystemDeflection
    from ._2972 import StraightBevelPlanetGearCompoundSystemDeflection
    from ._2973 import StraightBevelSunGearCompoundSystemDeflection
    from ._2974 import SynchroniserCompoundSystemDeflection
    from ._2975 import SynchroniserHalfCompoundSystemDeflection
    from ._2976 import SynchroniserPartCompoundSystemDeflection
    from ._2977 import SynchroniserSleeveCompoundSystemDeflection
    from ._2978 import TorqueConverterCompoundSystemDeflection
    from ._2979 import TorqueConverterConnectionCompoundSystemDeflection
    from ._2980 import TorqueConverterPumpCompoundSystemDeflection
    from ._2981 import TorqueConverterTurbineCompoundSystemDeflection
    from ._2982 import UnbalancedMassCompoundSystemDeflection
    from ._2983 import VirtualComponentCompoundSystemDeflection
    from ._2984 import WormGearCompoundSystemDeflection
    from ._2985 import WormGearMeshCompoundSystemDeflection
    from ._2986 import WormGearSetCompoundSystemDeflection
    from ._2987 import ZerolBevelGearCompoundSystemDeflection
    from ._2988 import ZerolBevelGearMeshCompoundSystemDeflection
    from ._2989 import ZerolBevelGearSetCompoundSystemDeflection
else:
    import_structure = {
        "_2859": ["AbstractAssemblyCompoundSystemDeflection"],
        "_2860": ["AbstractShaftCompoundSystemDeflection"],
        "_2861": ["AbstractShaftOrHousingCompoundSystemDeflection"],
        "_2862": [
            "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ],
        "_2863": ["AGMAGleasonConicalGearCompoundSystemDeflection"],
        "_2864": ["AGMAGleasonConicalGearMeshCompoundSystemDeflection"],
        "_2865": ["AGMAGleasonConicalGearSetCompoundSystemDeflection"],
        "_2866": ["AssemblyCompoundSystemDeflection"],
        "_2867": ["BearingCompoundSystemDeflection"],
        "_2868": ["BeltConnectionCompoundSystemDeflection"],
        "_2869": ["BeltDriveCompoundSystemDeflection"],
        "_2870": ["BevelDifferentialGearCompoundSystemDeflection"],
        "_2871": ["BevelDifferentialGearMeshCompoundSystemDeflection"],
        "_2872": ["BevelDifferentialGearSetCompoundSystemDeflection"],
        "_2873": ["BevelDifferentialPlanetGearCompoundSystemDeflection"],
        "_2874": ["BevelDifferentialSunGearCompoundSystemDeflection"],
        "_2875": ["BevelGearCompoundSystemDeflection"],
        "_2876": ["BevelGearMeshCompoundSystemDeflection"],
        "_2877": ["BevelGearSetCompoundSystemDeflection"],
        "_2878": ["BoltCompoundSystemDeflection"],
        "_2879": ["BoltedJointCompoundSystemDeflection"],
        "_2880": ["ClutchCompoundSystemDeflection"],
        "_2881": ["ClutchConnectionCompoundSystemDeflection"],
        "_2882": ["ClutchHalfCompoundSystemDeflection"],
        "_2883": ["CoaxialConnectionCompoundSystemDeflection"],
        "_2884": ["ComponentCompoundSystemDeflection"],
        "_2885": ["ConceptCouplingCompoundSystemDeflection"],
        "_2886": ["ConceptCouplingConnectionCompoundSystemDeflection"],
        "_2887": ["ConceptCouplingHalfCompoundSystemDeflection"],
        "_2888": ["ConceptGearCompoundSystemDeflection"],
        "_2889": ["ConceptGearMeshCompoundSystemDeflection"],
        "_2890": ["ConceptGearSetCompoundSystemDeflection"],
        "_2891": ["ConicalGearCompoundSystemDeflection"],
        "_2892": ["ConicalGearMeshCompoundSystemDeflection"],
        "_2893": ["ConicalGearSetCompoundSystemDeflection"],
        "_2894": ["ConnectionCompoundSystemDeflection"],
        "_2895": ["ConnectorCompoundSystemDeflection"],
        "_2896": ["CouplingCompoundSystemDeflection"],
        "_2897": ["CouplingConnectionCompoundSystemDeflection"],
        "_2898": ["CouplingHalfCompoundSystemDeflection"],
        "_2899": ["CVTBeltConnectionCompoundSystemDeflection"],
        "_2900": ["CVTCompoundSystemDeflection"],
        "_2901": ["CVTPulleyCompoundSystemDeflection"],
        "_2902": ["CycloidalAssemblyCompoundSystemDeflection"],
        "_2903": ["CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"],
        "_2904": ["CycloidalDiscCompoundSystemDeflection"],
        "_2905": ["CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"],
        "_2906": ["CylindricalGearCompoundSystemDeflection"],
        "_2907": ["CylindricalGearMeshCompoundSystemDeflection"],
        "_2908": ["CylindricalGearSetCompoundSystemDeflection"],
        "_2909": ["CylindricalPlanetGearCompoundSystemDeflection"],
        "_2910": ["DatumCompoundSystemDeflection"],
        "_2911": ["DutyCycleEfficiencyResults"],
        "_2912": ["ExternalCADModelCompoundSystemDeflection"],
        "_2913": ["FaceGearCompoundSystemDeflection"],
        "_2914": ["FaceGearMeshCompoundSystemDeflection"],
        "_2915": ["FaceGearSetCompoundSystemDeflection"],
        "_2916": ["FEPartCompoundSystemDeflection"],
        "_2917": ["FlexiblePinAssemblyCompoundSystemDeflection"],
        "_2918": ["GearCompoundSystemDeflection"],
        "_2919": ["GearMeshCompoundSystemDeflection"],
        "_2920": ["GearSetCompoundSystemDeflection"],
        "_2921": ["GuideDxfModelCompoundSystemDeflection"],
        "_2922": ["HypoidGearCompoundSystemDeflection"],
        "_2923": ["HypoidGearMeshCompoundSystemDeflection"],
        "_2924": ["HypoidGearSetCompoundSystemDeflection"],
        "_2925": ["InterMountableComponentConnectionCompoundSystemDeflection"],
        "_2926": ["KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"],
        "_2927": ["KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"],
        "_2928": ["KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"],
        "_2929": ["KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"],
        "_2930": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"],
        "_2931": ["KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection"],
        "_2932": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"],
        "_2933": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ],
        "_2934": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"],
        "_2935": ["MassDiscCompoundSystemDeflection"],
        "_2936": ["MeasurementComponentCompoundSystemDeflection"],
        "_2937": ["MountableComponentCompoundSystemDeflection"],
        "_2938": ["OilSealCompoundSystemDeflection"],
        "_2939": ["PartCompoundSystemDeflection"],
        "_2940": ["PartToPartShearCouplingCompoundSystemDeflection"],
        "_2941": ["PartToPartShearCouplingConnectionCompoundSystemDeflection"],
        "_2942": ["PartToPartShearCouplingHalfCompoundSystemDeflection"],
        "_2943": ["PlanetaryConnectionCompoundSystemDeflection"],
        "_2944": ["PlanetaryGearSetCompoundSystemDeflection"],
        "_2945": ["PlanetCarrierCompoundSystemDeflection"],
        "_2946": ["PointLoadCompoundSystemDeflection"],
        "_2947": ["PowerLoadCompoundSystemDeflection"],
        "_2948": ["PulleyCompoundSystemDeflection"],
        "_2949": ["RingPinsCompoundSystemDeflection"],
        "_2950": ["RingPinsToDiscConnectionCompoundSystemDeflection"],
        "_2951": ["RollingRingAssemblyCompoundSystemDeflection"],
        "_2952": ["RollingRingCompoundSystemDeflection"],
        "_2953": ["RollingRingConnectionCompoundSystemDeflection"],
        "_2954": ["RootAssemblyCompoundSystemDeflection"],
        "_2955": ["ShaftCompoundSystemDeflection"],
        "_2956": ["ShaftDutyCycleSystemDeflection"],
        "_2957": ["ShaftHubConnectionCompoundSystemDeflection"],
        "_2958": ["ShaftToMountableComponentConnectionCompoundSystemDeflection"],
        "_2959": ["SpecialisedAssemblyCompoundSystemDeflection"],
        "_2960": ["SpiralBevelGearCompoundSystemDeflection"],
        "_2961": ["SpiralBevelGearMeshCompoundSystemDeflection"],
        "_2962": ["SpiralBevelGearSetCompoundSystemDeflection"],
        "_2963": ["SpringDamperCompoundSystemDeflection"],
        "_2964": ["SpringDamperConnectionCompoundSystemDeflection"],
        "_2965": ["SpringDamperHalfCompoundSystemDeflection"],
        "_2966": ["StraightBevelDiffGearCompoundSystemDeflection"],
        "_2967": ["StraightBevelDiffGearMeshCompoundSystemDeflection"],
        "_2968": ["StraightBevelDiffGearSetCompoundSystemDeflection"],
        "_2969": ["StraightBevelGearCompoundSystemDeflection"],
        "_2970": ["StraightBevelGearMeshCompoundSystemDeflection"],
        "_2971": ["StraightBevelGearSetCompoundSystemDeflection"],
        "_2972": ["StraightBevelPlanetGearCompoundSystemDeflection"],
        "_2973": ["StraightBevelSunGearCompoundSystemDeflection"],
        "_2974": ["SynchroniserCompoundSystemDeflection"],
        "_2975": ["SynchroniserHalfCompoundSystemDeflection"],
        "_2976": ["SynchroniserPartCompoundSystemDeflection"],
        "_2977": ["SynchroniserSleeveCompoundSystemDeflection"],
        "_2978": ["TorqueConverterCompoundSystemDeflection"],
        "_2979": ["TorqueConverterConnectionCompoundSystemDeflection"],
        "_2980": ["TorqueConverterPumpCompoundSystemDeflection"],
        "_2981": ["TorqueConverterTurbineCompoundSystemDeflection"],
        "_2982": ["UnbalancedMassCompoundSystemDeflection"],
        "_2983": ["VirtualComponentCompoundSystemDeflection"],
        "_2984": ["WormGearCompoundSystemDeflection"],
        "_2985": ["WormGearMeshCompoundSystemDeflection"],
        "_2986": ["WormGearSetCompoundSystemDeflection"],
        "_2987": ["ZerolBevelGearCompoundSystemDeflection"],
        "_2988": ["ZerolBevelGearMeshCompoundSystemDeflection"],
        "_2989": ["ZerolBevelGearSetCompoundSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSystemDeflection",
    "AbstractShaftCompoundSystemDeflection",
    "AbstractShaftOrHousingCompoundSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
    "AssemblyCompoundSystemDeflection",
    "BearingCompoundSystemDeflection",
    "BeltConnectionCompoundSystemDeflection",
    "BeltDriveCompoundSystemDeflection",
    "BevelDifferentialGearCompoundSystemDeflection",
    "BevelDifferentialGearMeshCompoundSystemDeflection",
    "BevelDifferentialGearSetCompoundSystemDeflection",
    "BevelDifferentialPlanetGearCompoundSystemDeflection",
    "BevelDifferentialSunGearCompoundSystemDeflection",
    "BevelGearCompoundSystemDeflection",
    "BevelGearMeshCompoundSystemDeflection",
    "BevelGearSetCompoundSystemDeflection",
    "BoltCompoundSystemDeflection",
    "BoltedJointCompoundSystemDeflection",
    "ClutchCompoundSystemDeflection",
    "ClutchConnectionCompoundSystemDeflection",
    "ClutchHalfCompoundSystemDeflection",
    "CoaxialConnectionCompoundSystemDeflection",
    "ComponentCompoundSystemDeflection",
    "ConceptCouplingCompoundSystemDeflection",
    "ConceptCouplingConnectionCompoundSystemDeflection",
    "ConceptCouplingHalfCompoundSystemDeflection",
    "ConceptGearCompoundSystemDeflection",
    "ConceptGearMeshCompoundSystemDeflection",
    "ConceptGearSetCompoundSystemDeflection",
    "ConicalGearCompoundSystemDeflection",
    "ConicalGearMeshCompoundSystemDeflection",
    "ConicalGearSetCompoundSystemDeflection",
    "ConnectionCompoundSystemDeflection",
    "ConnectorCompoundSystemDeflection",
    "CouplingCompoundSystemDeflection",
    "CouplingConnectionCompoundSystemDeflection",
    "CouplingHalfCompoundSystemDeflection",
    "CVTBeltConnectionCompoundSystemDeflection",
    "CVTCompoundSystemDeflection",
    "CVTPulleyCompoundSystemDeflection",
    "CycloidalAssemblyCompoundSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    "CycloidalDiscCompoundSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    "CylindricalGearCompoundSystemDeflection",
    "CylindricalGearMeshCompoundSystemDeflection",
    "CylindricalGearSetCompoundSystemDeflection",
    "CylindricalPlanetGearCompoundSystemDeflection",
    "DatumCompoundSystemDeflection",
    "DutyCycleEfficiencyResults",
    "ExternalCADModelCompoundSystemDeflection",
    "FaceGearCompoundSystemDeflection",
    "FaceGearMeshCompoundSystemDeflection",
    "FaceGearSetCompoundSystemDeflection",
    "FEPartCompoundSystemDeflection",
    "FlexiblePinAssemblyCompoundSystemDeflection",
    "GearCompoundSystemDeflection",
    "GearMeshCompoundSystemDeflection",
    "GearSetCompoundSystemDeflection",
    "GuideDxfModelCompoundSystemDeflection",
    "HypoidGearCompoundSystemDeflection",
    "HypoidGearMeshCompoundSystemDeflection",
    "HypoidGearSetCompoundSystemDeflection",
    "InterMountableComponentConnectionCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    "MassDiscCompoundSystemDeflection",
    "MeasurementComponentCompoundSystemDeflection",
    "MountableComponentCompoundSystemDeflection",
    "OilSealCompoundSystemDeflection",
    "PartCompoundSystemDeflection",
    "PartToPartShearCouplingCompoundSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundSystemDeflection",
    "PartToPartShearCouplingHalfCompoundSystemDeflection",
    "PlanetaryConnectionCompoundSystemDeflection",
    "PlanetaryGearSetCompoundSystemDeflection",
    "PlanetCarrierCompoundSystemDeflection",
    "PointLoadCompoundSystemDeflection",
    "PowerLoadCompoundSystemDeflection",
    "PulleyCompoundSystemDeflection",
    "RingPinsCompoundSystemDeflection",
    "RingPinsToDiscConnectionCompoundSystemDeflection",
    "RollingRingAssemblyCompoundSystemDeflection",
    "RollingRingCompoundSystemDeflection",
    "RollingRingConnectionCompoundSystemDeflection",
    "RootAssemblyCompoundSystemDeflection",
    "ShaftCompoundSystemDeflection",
    "ShaftDutyCycleSystemDeflection",
    "ShaftHubConnectionCompoundSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundSystemDeflection",
    "SpecialisedAssemblyCompoundSystemDeflection",
    "SpiralBevelGearCompoundSystemDeflection",
    "SpiralBevelGearMeshCompoundSystemDeflection",
    "SpiralBevelGearSetCompoundSystemDeflection",
    "SpringDamperCompoundSystemDeflection",
    "SpringDamperConnectionCompoundSystemDeflection",
    "SpringDamperHalfCompoundSystemDeflection",
    "StraightBevelDiffGearCompoundSystemDeflection",
    "StraightBevelDiffGearMeshCompoundSystemDeflection",
    "StraightBevelDiffGearSetCompoundSystemDeflection",
    "StraightBevelGearCompoundSystemDeflection",
    "StraightBevelGearMeshCompoundSystemDeflection",
    "StraightBevelGearSetCompoundSystemDeflection",
    "StraightBevelPlanetGearCompoundSystemDeflection",
    "StraightBevelSunGearCompoundSystemDeflection",
    "SynchroniserCompoundSystemDeflection",
    "SynchroniserHalfCompoundSystemDeflection",
    "SynchroniserPartCompoundSystemDeflection",
    "SynchroniserSleeveCompoundSystemDeflection",
    "TorqueConverterCompoundSystemDeflection",
    "TorqueConverterConnectionCompoundSystemDeflection",
    "TorqueConverterPumpCompoundSystemDeflection",
    "TorqueConverterTurbineCompoundSystemDeflection",
    "UnbalancedMassCompoundSystemDeflection",
    "VirtualComponentCompoundSystemDeflection",
    "WormGearCompoundSystemDeflection",
    "WormGearMeshCompoundSystemDeflection",
    "WormGearSetCompoundSystemDeflection",
    "ZerolBevelGearCompoundSystemDeflection",
    "ZerolBevelGearMeshCompoundSystemDeflection",
    "ZerolBevelGearSetCompoundSystemDeflection",
)
