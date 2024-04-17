"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4040 import AbstractAssemblyPowerFlow
    from ._4041 import AbstractShaftOrHousingPowerFlow
    from ._4042 import AbstractShaftPowerFlow
    from ._4043 import AbstractShaftToMountableComponentConnectionPowerFlow
    from ._4044 import AGMAGleasonConicalGearMeshPowerFlow
    from ._4045 import AGMAGleasonConicalGearPowerFlow
    from ._4046 import AGMAGleasonConicalGearSetPowerFlow
    from ._4047 import AssemblyPowerFlow
    from ._4048 import BearingPowerFlow
    from ._4049 import BeltConnectionPowerFlow
    from ._4050 import BeltDrivePowerFlow
    from ._4051 import BevelDifferentialGearMeshPowerFlow
    from ._4052 import BevelDifferentialGearPowerFlow
    from ._4053 import BevelDifferentialGearSetPowerFlow
    from ._4054 import BevelDifferentialPlanetGearPowerFlow
    from ._4055 import BevelDifferentialSunGearPowerFlow
    from ._4056 import BevelGearMeshPowerFlow
    from ._4057 import BevelGearPowerFlow
    from ._4058 import BevelGearSetPowerFlow
    from ._4059 import BoltedJointPowerFlow
    from ._4060 import BoltPowerFlow
    from ._4061 import ClutchConnectionPowerFlow
    from ._4062 import ClutchHalfPowerFlow
    from ._4063 import ClutchPowerFlow
    from ._4064 import CoaxialConnectionPowerFlow
    from ._4065 import ComponentPowerFlow
    from ._4066 import ConceptCouplingConnectionPowerFlow
    from ._4067 import ConceptCouplingHalfPowerFlow
    from ._4068 import ConceptCouplingPowerFlow
    from ._4069 import ConceptGearMeshPowerFlow
    from ._4070 import ConceptGearPowerFlow
    from ._4071 import ConceptGearSetPowerFlow
    from ._4072 import ConicalGearMeshPowerFlow
    from ._4073 import ConicalGearPowerFlow
    from ._4074 import ConicalGearSetPowerFlow
    from ._4075 import ConnectionPowerFlow
    from ._4076 import ConnectorPowerFlow
    from ._4077 import CouplingConnectionPowerFlow
    from ._4078 import CouplingHalfPowerFlow
    from ._4079 import CouplingPowerFlow
    from ._4080 import CVTBeltConnectionPowerFlow
    from ._4081 import CVTPowerFlow
    from ._4082 import CVTPulleyPowerFlow
    from ._4083 import CycloidalAssemblyPowerFlow
    from ._4084 import CycloidalDiscCentralBearingConnectionPowerFlow
    from ._4085 import CycloidalDiscPlanetaryBearingConnectionPowerFlow
    from ._4086 import CycloidalDiscPowerFlow
    from ._4087 import CylindricalGearGeometricEntityDrawStyle
    from ._4088 import CylindricalGearMeshPowerFlow
    from ._4089 import CylindricalGearPowerFlow
    from ._4090 import CylindricalGearSetPowerFlow
    from ._4091 import CylindricalPlanetGearPowerFlow
    from ._4092 import DatumPowerFlow
    from ._4093 import ExternalCADModelPowerFlow
    from ._4094 import FaceGearMeshPowerFlow
    from ._4095 import FaceGearPowerFlow
    from ._4096 import FaceGearSetPowerFlow
    from ._4097 import FastPowerFlow
    from ._4098 import FastPowerFlowSolution
    from ._4099 import FEPartPowerFlow
    from ._4100 import FlexiblePinAssemblyPowerFlow
    from ._4101 import GearMeshPowerFlow
    from ._4102 import GearPowerFlow
    from ._4103 import GearSetPowerFlow
    from ._4104 import GuideDxfModelPowerFlow
    from ._4105 import HypoidGearMeshPowerFlow
    from ._4106 import HypoidGearPowerFlow
    from ._4107 import HypoidGearSetPowerFlow
    from ._4108 import InterMountableComponentConnectionPowerFlow
    from ._4109 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4110 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4111 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4112 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4113 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4114 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4115 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4116 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4117 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4118 import MassDiscPowerFlow
    from ._4119 import MeasurementComponentPowerFlow
    from ._4120 import MountableComponentPowerFlow
    from ._4121 import OilSealPowerFlow
    from ._4122 import PartPowerFlow
    from ._4123 import PartToPartShearCouplingConnectionPowerFlow
    from ._4124 import PartToPartShearCouplingHalfPowerFlow
    from ._4125 import PartToPartShearCouplingPowerFlow
    from ._4126 import PlanetaryConnectionPowerFlow
    from ._4127 import PlanetaryGearSetPowerFlow
    from ._4128 import PlanetCarrierPowerFlow
    from ._4129 import PointLoadPowerFlow
    from ._4130 import PowerFlow
    from ._4131 import PowerFlowDrawStyle
    from ._4132 import PowerLoadPowerFlow
    from ._4133 import PulleyPowerFlow
    from ._4134 import RingPinsPowerFlow
    from ._4135 import RingPinsToDiscConnectionPowerFlow
    from ._4136 import RollingRingAssemblyPowerFlow
    from ._4137 import RollingRingConnectionPowerFlow
    from ._4138 import RollingRingPowerFlow
    from ._4139 import RootAssemblyPowerFlow
    from ._4140 import ShaftHubConnectionPowerFlow
    from ._4141 import ShaftPowerFlow
    from ._4142 import ShaftToMountableComponentConnectionPowerFlow
    from ._4143 import SpecialisedAssemblyPowerFlow
    from ._4144 import SpiralBevelGearMeshPowerFlow
    from ._4145 import SpiralBevelGearPowerFlow
    from ._4146 import SpiralBevelGearSetPowerFlow
    from ._4147 import SpringDamperConnectionPowerFlow
    from ._4148 import SpringDamperHalfPowerFlow
    from ._4149 import SpringDamperPowerFlow
    from ._4150 import StraightBevelDiffGearMeshPowerFlow
    from ._4151 import StraightBevelDiffGearPowerFlow
    from ._4152 import StraightBevelDiffGearSetPowerFlow
    from ._4153 import StraightBevelGearMeshPowerFlow
    from ._4154 import StraightBevelGearPowerFlow
    from ._4155 import StraightBevelGearSetPowerFlow
    from ._4156 import StraightBevelPlanetGearPowerFlow
    from ._4157 import StraightBevelSunGearPowerFlow
    from ._4158 import SynchroniserHalfPowerFlow
    from ._4159 import SynchroniserPartPowerFlow
    from ._4160 import SynchroniserPowerFlow
    from ._4161 import SynchroniserSleevePowerFlow
    from ._4162 import ToothPassingHarmonic
    from ._4163 import TorqueConverterConnectionPowerFlow
    from ._4164 import TorqueConverterPowerFlow
    from ._4165 import TorqueConverterPumpPowerFlow
    from ._4166 import TorqueConverterTurbinePowerFlow
    from ._4167 import UnbalancedMassPowerFlow
    from ._4168 import VirtualComponentPowerFlow
    from ._4169 import WormGearMeshPowerFlow
    from ._4170 import WormGearPowerFlow
    from ._4171 import WormGearSetPowerFlow
    from ._4172 import ZerolBevelGearMeshPowerFlow
    from ._4173 import ZerolBevelGearPowerFlow
    from ._4174 import ZerolBevelGearSetPowerFlow
else:
    import_structure = {
        "_4040": ["AbstractAssemblyPowerFlow"],
        "_4041": ["AbstractShaftOrHousingPowerFlow"],
        "_4042": ["AbstractShaftPowerFlow"],
        "_4043": ["AbstractShaftToMountableComponentConnectionPowerFlow"],
        "_4044": ["AGMAGleasonConicalGearMeshPowerFlow"],
        "_4045": ["AGMAGleasonConicalGearPowerFlow"],
        "_4046": ["AGMAGleasonConicalGearSetPowerFlow"],
        "_4047": ["AssemblyPowerFlow"],
        "_4048": ["BearingPowerFlow"],
        "_4049": ["BeltConnectionPowerFlow"],
        "_4050": ["BeltDrivePowerFlow"],
        "_4051": ["BevelDifferentialGearMeshPowerFlow"],
        "_4052": ["BevelDifferentialGearPowerFlow"],
        "_4053": ["BevelDifferentialGearSetPowerFlow"],
        "_4054": ["BevelDifferentialPlanetGearPowerFlow"],
        "_4055": ["BevelDifferentialSunGearPowerFlow"],
        "_4056": ["BevelGearMeshPowerFlow"],
        "_4057": ["BevelGearPowerFlow"],
        "_4058": ["BevelGearSetPowerFlow"],
        "_4059": ["BoltedJointPowerFlow"],
        "_4060": ["BoltPowerFlow"],
        "_4061": ["ClutchConnectionPowerFlow"],
        "_4062": ["ClutchHalfPowerFlow"],
        "_4063": ["ClutchPowerFlow"],
        "_4064": ["CoaxialConnectionPowerFlow"],
        "_4065": ["ComponentPowerFlow"],
        "_4066": ["ConceptCouplingConnectionPowerFlow"],
        "_4067": ["ConceptCouplingHalfPowerFlow"],
        "_4068": ["ConceptCouplingPowerFlow"],
        "_4069": ["ConceptGearMeshPowerFlow"],
        "_4070": ["ConceptGearPowerFlow"],
        "_4071": ["ConceptGearSetPowerFlow"],
        "_4072": ["ConicalGearMeshPowerFlow"],
        "_4073": ["ConicalGearPowerFlow"],
        "_4074": ["ConicalGearSetPowerFlow"],
        "_4075": ["ConnectionPowerFlow"],
        "_4076": ["ConnectorPowerFlow"],
        "_4077": ["CouplingConnectionPowerFlow"],
        "_4078": ["CouplingHalfPowerFlow"],
        "_4079": ["CouplingPowerFlow"],
        "_4080": ["CVTBeltConnectionPowerFlow"],
        "_4081": ["CVTPowerFlow"],
        "_4082": ["CVTPulleyPowerFlow"],
        "_4083": ["CycloidalAssemblyPowerFlow"],
        "_4084": ["CycloidalDiscCentralBearingConnectionPowerFlow"],
        "_4085": ["CycloidalDiscPlanetaryBearingConnectionPowerFlow"],
        "_4086": ["CycloidalDiscPowerFlow"],
        "_4087": ["CylindricalGearGeometricEntityDrawStyle"],
        "_4088": ["CylindricalGearMeshPowerFlow"],
        "_4089": ["CylindricalGearPowerFlow"],
        "_4090": ["CylindricalGearSetPowerFlow"],
        "_4091": ["CylindricalPlanetGearPowerFlow"],
        "_4092": ["DatumPowerFlow"],
        "_4093": ["ExternalCADModelPowerFlow"],
        "_4094": ["FaceGearMeshPowerFlow"],
        "_4095": ["FaceGearPowerFlow"],
        "_4096": ["FaceGearSetPowerFlow"],
        "_4097": ["FastPowerFlow"],
        "_4098": ["FastPowerFlowSolution"],
        "_4099": ["FEPartPowerFlow"],
        "_4100": ["FlexiblePinAssemblyPowerFlow"],
        "_4101": ["GearMeshPowerFlow"],
        "_4102": ["GearPowerFlow"],
        "_4103": ["GearSetPowerFlow"],
        "_4104": ["GuideDxfModelPowerFlow"],
        "_4105": ["HypoidGearMeshPowerFlow"],
        "_4106": ["HypoidGearPowerFlow"],
        "_4107": ["HypoidGearSetPowerFlow"],
        "_4108": ["InterMountableComponentConnectionPowerFlow"],
        "_4109": ["KlingelnbergCycloPalloidConicalGearMeshPowerFlow"],
        "_4110": ["KlingelnbergCycloPalloidConicalGearPowerFlow"],
        "_4111": ["KlingelnbergCycloPalloidConicalGearSetPowerFlow"],
        "_4112": ["KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"],
        "_4113": ["KlingelnbergCycloPalloidHypoidGearPowerFlow"],
        "_4114": ["KlingelnbergCycloPalloidHypoidGearSetPowerFlow"],
        "_4115": ["KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow"],
        "_4116": ["KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"],
        "_4117": ["KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"],
        "_4118": ["MassDiscPowerFlow"],
        "_4119": ["MeasurementComponentPowerFlow"],
        "_4120": ["MountableComponentPowerFlow"],
        "_4121": ["OilSealPowerFlow"],
        "_4122": ["PartPowerFlow"],
        "_4123": ["PartToPartShearCouplingConnectionPowerFlow"],
        "_4124": ["PartToPartShearCouplingHalfPowerFlow"],
        "_4125": ["PartToPartShearCouplingPowerFlow"],
        "_4126": ["PlanetaryConnectionPowerFlow"],
        "_4127": ["PlanetaryGearSetPowerFlow"],
        "_4128": ["PlanetCarrierPowerFlow"],
        "_4129": ["PointLoadPowerFlow"],
        "_4130": ["PowerFlow"],
        "_4131": ["PowerFlowDrawStyle"],
        "_4132": ["PowerLoadPowerFlow"],
        "_4133": ["PulleyPowerFlow"],
        "_4134": ["RingPinsPowerFlow"],
        "_4135": ["RingPinsToDiscConnectionPowerFlow"],
        "_4136": ["RollingRingAssemblyPowerFlow"],
        "_4137": ["RollingRingConnectionPowerFlow"],
        "_4138": ["RollingRingPowerFlow"],
        "_4139": ["RootAssemblyPowerFlow"],
        "_4140": ["ShaftHubConnectionPowerFlow"],
        "_4141": ["ShaftPowerFlow"],
        "_4142": ["ShaftToMountableComponentConnectionPowerFlow"],
        "_4143": ["SpecialisedAssemblyPowerFlow"],
        "_4144": ["SpiralBevelGearMeshPowerFlow"],
        "_4145": ["SpiralBevelGearPowerFlow"],
        "_4146": ["SpiralBevelGearSetPowerFlow"],
        "_4147": ["SpringDamperConnectionPowerFlow"],
        "_4148": ["SpringDamperHalfPowerFlow"],
        "_4149": ["SpringDamperPowerFlow"],
        "_4150": ["StraightBevelDiffGearMeshPowerFlow"],
        "_4151": ["StraightBevelDiffGearPowerFlow"],
        "_4152": ["StraightBevelDiffGearSetPowerFlow"],
        "_4153": ["StraightBevelGearMeshPowerFlow"],
        "_4154": ["StraightBevelGearPowerFlow"],
        "_4155": ["StraightBevelGearSetPowerFlow"],
        "_4156": ["StraightBevelPlanetGearPowerFlow"],
        "_4157": ["StraightBevelSunGearPowerFlow"],
        "_4158": ["SynchroniserHalfPowerFlow"],
        "_4159": ["SynchroniserPartPowerFlow"],
        "_4160": ["SynchroniserPowerFlow"],
        "_4161": ["SynchroniserSleevePowerFlow"],
        "_4162": ["ToothPassingHarmonic"],
        "_4163": ["TorqueConverterConnectionPowerFlow"],
        "_4164": ["TorqueConverterPowerFlow"],
        "_4165": ["TorqueConverterPumpPowerFlow"],
        "_4166": ["TorqueConverterTurbinePowerFlow"],
        "_4167": ["UnbalancedMassPowerFlow"],
        "_4168": ["VirtualComponentPowerFlow"],
        "_4169": ["WormGearMeshPowerFlow"],
        "_4170": ["WormGearPowerFlow"],
        "_4171": ["WormGearSetPowerFlow"],
        "_4172": ["ZerolBevelGearMeshPowerFlow"],
        "_4173": ["ZerolBevelGearPowerFlow"],
        "_4174": ["ZerolBevelGearSetPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyPowerFlow",
    "AbstractShaftOrHousingPowerFlow",
    "AbstractShaftPowerFlow",
    "AbstractShaftToMountableComponentConnectionPowerFlow",
    "AGMAGleasonConicalGearMeshPowerFlow",
    "AGMAGleasonConicalGearPowerFlow",
    "AGMAGleasonConicalGearSetPowerFlow",
    "AssemblyPowerFlow",
    "BearingPowerFlow",
    "BeltConnectionPowerFlow",
    "BeltDrivePowerFlow",
    "BevelDifferentialGearMeshPowerFlow",
    "BevelDifferentialGearPowerFlow",
    "BevelDifferentialGearSetPowerFlow",
    "BevelDifferentialPlanetGearPowerFlow",
    "BevelDifferentialSunGearPowerFlow",
    "BevelGearMeshPowerFlow",
    "BevelGearPowerFlow",
    "BevelGearSetPowerFlow",
    "BoltedJointPowerFlow",
    "BoltPowerFlow",
    "ClutchConnectionPowerFlow",
    "ClutchHalfPowerFlow",
    "ClutchPowerFlow",
    "CoaxialConnectionPowerFlow",
    "ComponentPowerFlow",
    "ConceptCouplingConnectionPowerFlow",
    "ConceptCouplingHalfPowerFlow",
    "ConceptCouplingPowerFlow",
    "ConceptGearMeshPowerFlow",
    "ConceptGearPowerFlow",
    "ConceptGearSetPowerFlow",
    "ConicalGearMeshPowerFlow",
    "ConicalGearPowerFlow",
    "ConicalGearSetPowerFlow",
    "ConnectionPowerFlow",
    "ConnectorPowerFlow",
    "CouplingConnectionPowerFlow",
    "CouplingHalfPowerFlow",
    "CouplingPowerFlow",
    "CVTBeltConnectionPowerFlow",
    "CVTPowerFlow",
    "CVTPulleyPowerFlow",
    "CycloidalAssemblyPowerFlow",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
    "CycloidalDiscPowerFlow",
    "CylindricalGearGeometricEntityDrawStyle",
    "CylindricalGearMeshPowerFlow",
    "CylindricalGearPowerFlow",
    "CylindricalGearSetPowerFlow",
    "CylindricalPlanetGearPowerFlow",
    "DatumPowerFlow",
    "ExternalCADModelPowerFlow",
    "FaceGearMeshPowerFlow",
    "FaceGearPowerFlow",
    "FaceGearSetPowerFlow",
    "FastPowerFlow",
    "FastPowerFlowSolution",
    "FEPartPowerFlow",
    "FlexiblePinAssemblyPowerFlow",
    "GearMeshPowerFlow",
    "GearPowerFlow",
    "GearSetPowerFlow",
    "GuideDxfModelPowerFlow",
    "HypoidGearMeshPowerFlow",
    "HypoidGearPowerFlow",
    "HypoidGearSetPowerFlow",
    "InterMountableComponentConnectionPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
    "MassDiscPowerFlow",
    "MeasurementComponentPowerFlow",
    "MountableComponentPowerFlow",
    "OilSealPowerFlow",
    "PartPowerFlow",
    "PartToPartShearCouplingConnectionPowerFlow",
    "PartToPartShearCouplingHalfPowerFlow",
    "PartToPartShearCouplingPowerFlow",
    "PlanetaryConnectionPowerFlow",
    "PlanetaryGearSetPowerFlow",
    "PlanetCarrierPowerFlow",
    "PointLoadPowerFlow",
    "PowerFlow",
    "PowerFlowDrawStyle",
    "PowerLoadPowerFlow",
    "PulleyPowerFlow",
    "RingPinsPowerFlow",
    "RingPinsToDiscConnectionPowerFlow",
    "RollingRingAssemblyPowerFlow",
    "RollingRingConnectionPowerFlow",
    "RollingRingPowerFlow",
    "RootAssemblyPowerFlow",
    "ShaftHubConnectionPowerFlow",
    "ShaftPowerFlow",
    "ShaftToMountableComponentConnectionPowerFlow",
    "SpecialisedAssemblyPowerFlow",
    "SpiralBevelGearMeshPowerFlow",
    "SpiralBevelGearPowerFlow",
    "SpiralBevelGearSetPowerFlow",
    "SpringDamperConnectionPowerFlow",
    "SpringDamperHalfPowerFlow",
    "SpringDamperPowerFlow",
    "StraightBevelDiffGearMeshPowerFlow",
    "StraightBevelDiffGearPowerFlow",
    "StraightBevelDiffGearSetPowerFlow",
    "StraightBevelGearMeshPowerFlow",
    "StraightBevelGearPowerFlow",
    "StraightBevelGearSetPowerFlow",
    "StraightBevelPlanetGearPowerFlow",
    "StraightBevelSunGearPowerFlow",
    "SynchroniserHalfPowerFlow",
    "SynchroniserPartPowerFlow",
    "SynchroniserPowerFlow",
    "SynchroniserSleevePowerFlow",
    "ToothPassingHarmonic",
    "TorqueConverterConnectionPowerFlow",
    "TorqueConverterPowerFlow",
    "TorqueConverterPumpPowerFlow",
    "TorqueConverterTurbinePowerFlow",
    "UnbalancedMassPowerFlow",
    "VirtualComponentPowerFlow",
    "WormGearMeshPowerFlow",
    "WormGearPowerFlow",
    "WormGearSetPowerFlow",
    "ZerolBevelGearMeshPowerFlow",
    "ZerolBevelGearPowerFlow",
    "ZerolBevelGearSetPowerFlow",
)
