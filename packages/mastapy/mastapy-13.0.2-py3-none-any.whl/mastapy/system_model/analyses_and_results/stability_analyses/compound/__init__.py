"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3905 import AbstractAssemblyCompoundStabilityAnalysis
    from ._3906 import AbstractShaftCompoundStabilityAnalysis
    from ._3907 import AbstractShaftOrHousingCompoundStabilityAnalysis
    from ._3908 import (
        AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis,
    )
    from ._3909 import AGMAGleasonConicalGearCompoundStabilityAnalysis
    from ._3910 import AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
    from ._3911 import AGMAGleasonConicalGearSetCompoundStabilityAnalysis
    from ._3912 import AssemblyCompoundStabilityAnalysis
    from ._3913 import BearingCompoundStabilityAnalysis
    from ._3914 import BeltConnectionCompoundStabilityAnalysis
    from ._3915 import BeltDriveCompoundStabilityAnalysis
    from ._3916 import BevelDifferentialGearCompoundStabilityAnalysis
    from ._3917 import BevelDifferentialGearMeshCompoundStabilityAnalysis
    from ._3918 import BevelDifferentialGearSetCompoundStabilityAnalysis
    from ._3919 import BevelDifferentialPlanetGearCompoundStabilityAnalysis
    from ._3920 import BevelDifferentialSunGearCompoundStabilityAnalysis
    from ._3921 import BevelGearCompoundStabilityAnalysis
    from ._3922 import BevelGearMeshCompoundStabilityAnalysis
    from ._3923 import BevelGearSetCompoundStabilityAnalysis
    from ._3924 import BoltCompoundStabilityAnalysis
    from ._3925 import BoltedJointCompoundStabilityAnalysis
    from ._3926 import ClutchCompoundStabilityAnalysis
    from ._3927 import ClutchConnectionCompoundStabilityAnalysis
    from ._3928 import ClutchHalfCompoundStabilityAnalysis
    from ._3929 import CoaxialConnectionCompoundStabilityAnalysis
    from ._3930 import ComponentCompoundStabilityAnalysis
    from ._3931 import ConceptCouplingCompoundStabilityAnalysis
    from ._3932 import ConceptCouplingConnectionCompoundStabilityAnalysis
    from ._3933 import ConceptCouplingHalfCompoundStabilityAnalysis
    from ._3934 import ConceptGearCompoundStabilityAnalysis
    from ._3935 import ConceptGearMeshCompoundStabilityAnalysis
    from ._3936 import ConceptGearSetCompoundStabilityAnalysis
    from ._3937 import ConicalGearCompoundStabilityAnalysis
    from ._3938 import ConicalGearMeshCompoundStabilityAnalysis
    from ._3939 import ConicalGearSetCompoundStabilityAnalysis
    from ._3940 import ConnectionCompoundStabilityAnalysis
    from ._3941 import ConnectorCompoundStabilityAnalysis
    from ._3942 import CouplingCompoundStabilityAnalysis
    from ._3943 import CouplingConnectionCompoundStabilityAnalysis
    from ._3944 import CouplingHalfCompoundStabilityAnalysis
    from ._3945 import CVTBeltConnectionCompoundStabilityAnalysis
    from ._3946 import CVTCompoundStabilityAnalysis
    from ._3947 import CVTPulleyCompoundStabilityAnalysis
    from ._3948 import CycloidalAssemblyCompoundStabilityAnalysis
    from ._3949 import CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
    from ._3950 import CycloidalDiscCompoundStabilityAnalysis
    from ._3951 import CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
    from ._3952 import CylindricalGearCompoundStabilityAnalysis
    from ._3953 import CylindricalGearMeshCompoundStabilityAnalysis
    from ._3954 import CylindricalGearSetCompoundStabilityAnalysis
    from ._3955 import CylindricalPlanetGearCompoundStabilityAnalysis
    from ._3956 import DatumCompoundStabilityAnalysis
    from ._3957 import ExternalCADModelCompoundStabilityAnalysis
    from ._3958 import FaceGearCompoundStabilityAnalysis
    from ._3959 import FaceGearMeshCompoundStabilityAnalysis
    from ._3960 import FaceGearSetCompoundStabilityAnalysis
    from ._3961 import FEPartCompoundStabilityAnalysis
    from ._3962 import FlexiblePinAssemblyCompoundStabilityAnalysis
    from ._3963 import GearCompoundStabilityAnalysis
    from ._3964 import GearMeshCompoundStabilityAnalysis
    from ._3965 import GearSetCompoundStabilityAnalysis
    from ._3966 import GuideDxfModelCompoundStabilityAnalysis
    from ._3967 import HypoidGearCompoundStabilityAnalysis
    from ._3968 import HypoidGearMeshCompoundStabilityAnalysis
    from ._3969 import HypoidGearSetCompoundStabilityAnalysis
    from ._3970 import InterMountableComponentConnectionCompoundStabilityAnalysis
    from ._3971 import KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
    from ._3972 import KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
    from ._3973 import KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
    from ._3974 import KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
    from ._3975 import KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
    from ._3976 import KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
    from ._3977 import KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
    from ._3978 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis,
    )
    from ._3979 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis,
    )
    from ._3980 import MassDiscCompoundStabilityAnalysis
    from ._3981 import MeasurementComponentCompoundStabilityAnalysis
    from ._3982 import MountableComponentCompoundStabilityAnalysis
    from ._3983 import OilSealCompoundStabilityAnalysis
    from ._3984 import PartCompoundStabilityAnalysis
    from ._3985 import PartToPartShearCouplingCompoundStabilityAnalysis
    from ._3986 import PartToPartShearCouplingConnectionCompoundStabilityAnalysis
    from ._3987 import PartToPartShearCouplingHalfCompoundStabilityAnalysis
    from ._3988 import PlanetaryConnectionCompoundStabilityAnalysis
    from ._3989 import PlanetaryGearSetCompoundStabilityAnalysis
    from ._3990 import PlanetCarrierCompoundStabilityAnalysis
    from ._3991 import PointLoadCompoundStabilityAnalysis
    from ._3992 import PowerLoadCompoundStabilityAnalysis
    from ._3993 import PulleyCompoundStabilityAnalysis
    from ._3994 import RingPinsCompoundStabilityAnalysis
    from ._3995 import RingPinsToDiscConnectionCompoundStabilityAnalysis
    from ._3996 import RollingRingAssemblyCompoundStabilityAnalysis
    from ._3997 import RollingRingCompoundStabilityAnalysis
    from ._3998 import RollingRingConnectionCompoundStabilityAnalysis
    from ._3999 import RootAssemblyCompoundStabilityAnalysis
    from ._4000 import ShaftCompoundStabilityAnalysis
    from ._4001 import ShaftHubConnectionCompoundStabilityAnalysis
    from ._4002 import ShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._4003 import SpecialisedAssemblyCompoundStabilityAnalysis
    from ._4004 import SpiralBevelGearCompoundStabilityAnalysis
    from ._4005 import SpiralBevelGearMeshCompoundStabilityAnalysis
    from ._4006 import SpiralBevelGearSetCompoundStabilityAnalysis
    from ._4007 import SpringDamperCompoundStabilityAnalysis
    from ._4008 import SpringDamperConnectionCompoundStabilityAnalysis
    from ._4009 import SpringDamperHalfCompoundStabilityAnalysis
    from ._4010 import StraightBevelDiffGearCompoundStabilityAnalysis
    from ._4011 import StraightBevelDiffGearMeshCompoundStabilityAnalysis
    from ._4012 import StraightBevelDiffGearSetCompoundStabilityAnalysis
    from ._4013 import StraightBevelGearCompoundStabilityAnalysis
    from ._4014 import StraightBevelGearMeshCompoundStabilityAnalysis
    from ._4015 import StraightBevelGearSetCompoundStabilityAnalysis
    from ._4016 import StraightBevelPlanetGearCompoundStabilityAnalysis
    from ._4017 import StraightBevelSunGearCompoundStabilityAnalysis
    from ._4018 import SynchroniserCompoundStabilityAnalysis
    from ._4019 import SynchroniserHalfCompoundStabilityAnalysis
    from ._4020 import SynchroniserPartCompoundStabilityAnalysis
    from ._4021 import SynchroniserSleeveCompoundStabilityAnalysis
    from ._4022 import TorqueConverterCompoundStabilityAnalysis
    from ._4023 import TorqueConverterConnectionCompoundStabilityAnalysis
    from ._4024 import TorqueConverterPumpCompoundStabilityAnalysis
    from ._4025 import TorqueConverterTurbineCompoundStabilityAnalysis
    from ._4026 import UnbalancedMassCompoundStabilityAnalysis
    from ._4027 import VirtualComponentCompoundStabilityAnalysis
    from ._4028 import WormGearCompoundStabilityAnalysis
    from ._4029 import WormGearMeshCompoundStabilityAnalysis
    from ._4030 import WormGearSetCompoundStabilityAnalysis
    from ._4031 import ZerolBevelGearCompoundStabilityAnalysis
    from ._4032 import ZerolBevelGearMeshCompoundStabilityAnalysis
    from ._4033 import ZerolBevelGearSetCompoundStabilityAnalysis
else:
    import_structure = {
        "_3905": ["AbstractAssemblyCompoundStabilityAnalysis"],
        "_3906": ["AbstractShaftCompoundStabilityAnalysis"],
        "_3907": ["AbstractShaftOrHousingCompoundStabilityAnalysis"],
        "_3908": [
            "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ],
        "_3909": ["AGMAGleasonConicalGearCompoundStabilityAnalysis"],
        "_3910": ["AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"],
        "_3911": ["AGMAGleasonConicalGearSetCompoundStabilityAnalysis"],
        "_3912": ["AssemblyCompoundStabilityAnalysis"],
        "_3913": ["BearingCompoundStabilityAnalysis"],
        "_3914": ["BeltConnectionCompoundStabilityAnalysis"],
        "_3915": ["BeltDriveCompoundStabilityAnalysis"],
        "_3916": ["BevelDifferentialGearCompoundStabilityAnalysis"],
        "_3917": ["BevelDifferentialGearMeshCompoundStabilityAnalysis"],
        "_3918": ["BevelDifferentialGearSetCompoundStabilityAnalysis"],
        "_3919": ["BevelDifferentialPlanetGearCompoundStabilityAnalysis"],
        "_3920": ["BevelDifferentialSunGearCompoundStabilityAnalysis"],
        "_3921": ["BevelGearCompoundStabilityAnalysis"],
        "_3922": ["BevelGearMeshCompoundStabilityAnalysis"],
        "_3923": ["BevelGearSetCompoundStabilityAnalysis"],
        "_3924": ["BoltCompoundStabilityAnalysis"],
        "_3925": ["BoltedJointCompoundStabilityAnalysis"],
        "_3926": ["ClutchCompoundStabilityAnalysis"],
        "_3927": ["ClutchConnectionCompoundStabilityAnalysis"],
        "_3928": ["ClutchHalfCompoundStabilityAnalysis"],
        "_3929": ["CoaxialConnectionCompoundStabilityAnalysis"],
        "_3930": ["ComponentCompoundStabilityAnalysis"],
        "_3931": ["ConceptCouplingCompoundStabilityAnalysis"],
        "_3932": ["ConceptCouplingConnectionCompoundStabilityAnalysis"],
        "_3933": ["ConceptCouplingHalfCompoundStabilityAnalysis"],
        "_3934": ["ConceptGearCompoundStabilityAnalysis"],
        "_3935": ["ConceptGearMeshCompoundStabilityAnalysis"],
        "_3936": ["ConceptGearSetCompoundStabilityAnalysis"],
        "_3937": ["ConicalGearCompoundStabilityAnalysis"],
        "_3938": ["ConicalGearMeshCompoundStabilityAnalysis"],
        "_3939": ["ConicalGearSetCompoundStabilityAnalysis"],
        "_3940": ["ConnectionCompoundStabilityAnalysis"],
        "_3941": ["ConnectorCompoundStabilityAnalysis"],
        "_3942": ["CouplingCompoundStabilityAnalysis"],
        "_3943": ["CouplingConnectionCompoundStabilityAnalysis"],
        "_3944": ["CouplingHalfCompoundStabilityAnalysis"],
        "_3945": ["CVTBeltConnectionCompoundStabilityAnalysis"],
        "_3946": ["CVTCompoundStabilityAnalysis"],
        "_3947": ["CVTPulleyCompoundStabilityAnalysis"],
        "_3948": ["CycloidalAssemblyCompoundStabilityAnalysis"],
        "_3949": ["CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"],
        "_3950": ["CycloidalDiscCompoundStabilityAnalysis"],
        "_3951": ["CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis"],
        "_3952": ["CylindricalGearCompoundStabilityAnalysis"],
        "_3953": ["CylindricalGearMeshCompoundStabilityAnalysis"],
        "_3954": ["CylindricalGearSetCompoundStabilityAnalysis"],
        "_3955": ["CylindricalPlanetGearCompoundStabilityAnalysis"],
        "_3956": ["DatumCompoundStabilityAnalysis"],
        "_3957": ["ExternalCADModelCompoundStabilityAnalysis"],
        "_3958": ["FaceGearCompoundStabilityAnalysis"],
        "_3959": ["FaceGearMeshCompoundStabilityAnalysis"],
        "_3960": ["FaceGearSetCompoundStabilityAnalysis"],
        "_3961": ["FEPartCompoundStabilityAnalysis"],
        "_3962": ["FlexiblePinAssemblyCompoundStabilityAnalysis"],
        "_3963": ["GearCompoundStabilityAnalysis"],
        "_3964": ["GearMeshCompoundStabilityAnalysis"],
        "_3965": ["GearSetCompoundStabilityAnalysis"],
        "_3966": ["GuideDxfModelCompoundStabilityAnalysis"],
        "_3967": ["HypoidGearCompoundStabilityAnalysis"],
        "_3968": ["HypoidGearMeshCompoundStabilityAnalysis"],
        "_3969": ["HypoidGearSetCompoundStabilityAnalysis"],
        "_3970": ["InterMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3971": ["KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"],
        "_3972": ["KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"],
        "_3973": ["KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"],
        "_3974": ["KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"],
        "_3975": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"],
        "_3976": ["KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"],
        "_3977": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis"],
        "_3978": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ],
        "_3979": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ],
        "_3980": ["MassDiscCompoundStabilityAnalysis"],
        "_3981": ["MeasurementComponentCompoundStabilityAnalysis"],
        "_3982": ["MountableComponentCompoundStabilityAnalysis"],
        "_3983": ["OilSealCompoundStabilityAnalysis"],
        "_3984": ["PartCompoundStabilityAnalysis"],
        "_3985": ["PartToPartShearCouplingCompoundStabilityAnalysis"],
        "_3986": ["PartToPartShearCouplingConnectionCompoundStabilityAnalysis"],
        "_3987": ["PartToPartShearCouplingHalfCompoundStabilityAnalysis"],
        "_3988": ["PlanetaryConnectionCompoundStabilityAnalysis"],
        "_3989": ["PlanetaryGearSetCompoundStabilityAnalysis"],
        "_3990": ["PlanetCarrierCompoundStabilityAnalysis"],
        "_3991": ["PointLoadCompoundStabilityAnalysis"],
        "_3992": ["PowerLoadCompoundStabilityAnalysis"],
        "_3993": ["PulleyCompoundStabilityAnalysis"],
        "_3994": ["RingPinsCompoundStabilityAnalysis"],
        "_3995": ["RingPinsToDiscConnectionCompoundStabilityAnalysis"],
        "_3996": ["RollingRingAssemblyCompoundStabilityAnalysis"],
        "_3997": ["RollingRingCompoundStabilityAnalysis"],
        "_3998": ["RollingRingConnectionCompoundStabilityAnalysis"],
        "_3999": ["RootAssemblyCompoundStabilityAnalysis"],
        "_4000": ["ShaftCompoundStabilityAnalysis"],
        "_4001": ["ShaftHubConnectionCompoundStabilityAnalysis"],
        "_4002": ["ShaftToMountableComponentConnectionCompoundStabilityAnalysis"],
        "_4003": ["SpecialisedAssemblyCompoundStabilityAnalysis"],
        "_4004": ["SpiralBevelGearCompoundStabilityAnalysis"],
        "_4005": ["SpiralBevelGearMeshCompoundStabilityAnalysis"],
        "_4006": ["SpiralBevelGearSetCompoundStabilityAnalysis"],
        "_4007": ["SpringDamperCompoundStabilityAnalysis"],
        "_4008": ["SpringDamperConnectionCompoundStabilityAnalysis"],
        "_4009": ["SpringDamperHalfCompoundStabilityAnalysis"],
        "_4010": ["StraightBevelDiffGearCompoundStabilityAnalysis"],
        "_4011": ["StraightBevelDiffGearMeshCompoundStabilityAnalysis"],
        "_4012": ["StraightBevelDiffGearSetCompoundStabilityAnalysis"],
        "_4013": ["StraightBevelGearCompoundStabilityAnalysis"],
        "_4014": ["StraightBevelGearMeshCompoundStabilityAnalysis"],
        "_4015": ["StraightBevelGearSetCompoundStabilityAnalysis"],
        "_4016": ["StraightBevelPlanetGearCompoundStabilityAnalysis"],
        "_4017": ["StraightBevelSunGearCompoundStabilityAnalysis"],
        "_4018": ["SynchroniserCompoundStabilityAnalysis"],
        "_4019": ["SynchroniserHalfCompoundStabilityAnalysis"],
        "_4020": ["SynchroniserPartCompoundStabilityAnalysis"],
        "_4021": ["SynchroniserSleeveCompoundStabilityAnalysis"],
        "_4022": ["TorqueConverterCompoundStabilityAnalysis"],
        "_4023": ["TorqueConverterConnectionCompoundStabilityAnalysis"],
        "_4024": ["TorqueConverterPumpCompoundStabilityAnalysis"],
        "_4025": ["TorqueConverterTurbineCompoundStabilityAnalysis"],
        "_4026": ["UnbalancedMassCompoundStabilityAnalysis"],
        "_4027": ["VirtualComponentCompoundStabilityAnalysis"],
        "_4028": ["WormGearCompoundStabilityAnalysis"],
        "_4029": ["WormGearMeshCompoundStabilityAnalysis"],
        "_4030": ["WormGearSetCompoundStabilityAnalysis"],
        "_4031": ["ZerolBevelGearCompoundStabilityAnalysis"],
        "_4032": ["ZerolBevelGearMeshCompoundStabilityAnalysis"],
        "_4033": ["ZerolBevelGearSetCompoundStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundStabilityAnalysis",
    "AbstractShaftCompoundStabilityAnalysis",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
    "AssemblyCompoundStabilityAnalysis",
    "BearingCompoundStabilityAnalysis",
    "BeltConnectionCompoundStabilityAnalysis",
    "BeltDriveCompoundStabilityAnalysis",
    "BevelDifferentialGearCompoundStabilityAnalysis",
    "BevelDifferentialGearMeshCompoundStabilityAnalysis",
    "BevelDifferentialGearSetCompoundStabilityAnalysis",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
    "BevelGearCompoundStabilityAnalysis",
    "BevelGearMeshCompoundStabilityAnalysis",
    "BevelGearSetCompoundStabilityAnalysis",
    "BoltCompoundStabilityAnalysis",
    "BoltedJointCompoundStabilityAnalysis",
    "ClutchCompoundStabilityAnalysis",
    "ClutchConnectionCompoundStabilityAnalysis",
    "ClutchHalfCompoundStabilityAnalysis",
    "CoaxialConnectionCompoundStabilityAnalysis",
    "ComponentCompoundStabilityAnalysis",
    "ConceptCouplingCompoundStabilityAnalysis",
    "ConceptCouplingConnectionCompoundStabilityAnalysis",
    "ConceptCouplingHalfCompoundStabilityAnalysis",
    "ConceptGearCompoundStabilityAnalysis",
    "ConceptGearMeshCompoundStabilityAnalysis",
    "ConceptGearSetCompoundStabilityAnalysis",
    "ConicalGearCompoundStabilityAnalysis",
    "ConicalGearMeshCompoundStabilityAnalysis",
    "ConicalGearSetCompoundStabilityAnalysis",
    "ConnectionCompoundStabilityAnalysis",
    "ConnectorCompoundStabilityAnalysis",
    "CouplingCompoundStabilityAnalysis",
    "CouplingConnectionCompoundStabilityAnalysis",
    "CouplingHalfCompoundStabilityAnalysis",
    "CVTBeltConnectionCompoundStabilityAnalysis",
    "CVTCompoundStabilityAnalysis",
    "CVTPulleyCompoundStabilityAnalysis",
    "CycloidalAssemblyCompoundStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    "CycloidalDiscCompoundStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis",
    "CylindricalGearCompoundStabilityAnalysis",
    "CylindricalGearMeshCompoundStabilityAnalysis",
    "CylindricalGearSetCompoundStabilityAnalysis",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
    "DatumCompoundStabilityAnalysis",
    "ExternalCADModelCompoundStabilityAnalysis",
    "FaceGearCompoundStabilityAnalysis",
    "FaceGearMeshCompoundStabilityAnalysis",
    "FaceGearSetCompoundStabilityAnalysis",
    "FEPartCompoundStabilityAnalysis",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
    "GearCompoundStabilityAnalysis",
    "GearMeshCompoundStabilityAnalysis",
    "GearSetCompoundStabilityAnalysis",
    "GuideDxfModelCompoundStabilityAnalysis",
    "HypoidGearCompoundStabilityAnalysis",
    "HypoidGearMeshCompoundStabilityAnalysis",
    "HypoidGearSetCompoundStabilityAnalysis",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    "MassDiscCompoundStabilityAnalysis",
    "MeasurementComponentCompoundStabilityAnalysis",
    "MountableComponentCompoundStabilityAnalysis",
    "OilSealCompoundStabilityAnalysis",
    "PartCompoundStabilityAnalysis",
    "PartToPartShearCouplingCompoundStabilityAnalysis",
    "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
    "PartToPartShearCouplingHalfCompoundStabilityAnalysis",
    "PlanetaryConnectionCompoundStabilityAnalysis",
    "PlanetaryGearSetCompoundStabilityAnalysis",
    "PlanetCarrierCompoundStabilityAnalysis",
    "PointLoadCompoundStabilityAnalysis",
    "PowerLoadCompoundStabilityAnalysis",
    "PulleyCompoundStabilityAnalysis",
    "RingPinsCompoundStabilityAnalysis",
    "RingPinsToDiscConnectionCompoundStabilityAnalysis",
    "RollingRingAssemblyCompoundStabilityAnalysis",
    "RollingRingCompoundStabilityAnalysis",
    "RollingRingConnectionCompoundStabilityAnalysis",
    "RootAssemblyCompoundStabilityAnalysis",
    "ShaftCompoundStabilityAnalysis",
    "ShaftHubConnectionCompoundStabilityAnalysis",
    "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
    "SpiralBevelGearCompoundStabilityAnalysis",
    "SpiralBevelGearMeshCompoundStabilityAnalysis",
    "SpiralBevelGearSetCompoundStabilityAnalysis",
    "SpringDamperCompoundStabilityAnalysis",
    "SpringDamperConnectionCompoundStabilityAnalysis",
    "SpringDamperHalfCompoundStabilityAnalysis",
    "StraightBevelDiffGearCompoundStabilityAnalysis",
    "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
    "StraightBevelGearCompoundStabilityAnalysis",
    "StraightBevelGearMeshCompoundStabilityAnalysis",
    "StraightBevelGearSetCompoundStabilityAnalysis",
    "StraightBevelPlanetGearCompoundStabilityAnalysis",
    "StraightBevelSunGearCompoundStabilityAnalysis",
    "SynchroniserCompoundStabilityAnalysis",
    "SynchroniserHalfCompoundStabilityAnalysis",
    "SynchroniserPartCompoundStabilityAnalysis",
    "SynchroniserSleeveCompoundStabilityAnalysis",
    "TorqueConverterCompoundStabilityAnalysis",
    "TorqueConverterConnectionCompoundStabilityAnalysis",
    "TorqueConverterPumpCompoundStabilityAnalysis",
    "TorqueConverterTurbineCompoundStabilityAnalysis",
    "UnbalancedMassCompoundStabilityAnalysis",
    "VirtualComponentCompoundStabilityAnalysis",
    "WormGearCompoundStabilityAnalysis",
    "WormGearMeshCompoundStabilityAnalysis",
    "WormGearSetCompoundStabilityAnalysis",
    "ZerolBevelGearCompoundStabilityAnalysis",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
    "ZerolBevelGearSetCompoundStabilityAnalysis",
)
