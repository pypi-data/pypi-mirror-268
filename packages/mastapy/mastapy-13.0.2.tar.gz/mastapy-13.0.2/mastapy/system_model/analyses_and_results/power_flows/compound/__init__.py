"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4175 import AbstractAssemblyCompoundPowerFlow
    from ._4176 import AbstractShaftCompoundPowerFlow
    from ._4177 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4178 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4179 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4180 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4181 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4182 import AssemblyCompoundPowerFlow
    from ._4183 import BearingCompoundPowerFlow
    from ._4184 import BeltConnectionCompoundPowerFlow
    from ._4185 import BeltDriveCompoundPowerFlow
    from ._4186 import BevelDifferentialGearCompoundPowerFlow
    from ._4187 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4188 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4189 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4190 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4191 import BevelGearCompoundPowerFlow
    from ._4192 import BevelGearMeshCompoundPowerFlow
    from ._4193 import BevelGearSetCompoundPowerFlow
    from ._4194 import BoltCompoundPowerFlow
    from ._4195 import BoltedJointCompoundPowerFlow
    from ._4196 import ClutchCompoundPowerFlow
    from ._4197 import ClutchConnectionCompoundPowerFlow
    from ._4198 import ClutchHalfCompoundPowerFlow
    from ._4199 import CoaxialConnectionCompoundPowerFlow
    from ._4200 import ComponentCompoundPowerFlow
    from ._4201 import ConceptCouplingCompoundPowerFlow
    from ._4202 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4203 import ConceptCouplingHalfCompoundPowerFlow
    from ._4204 import ConceptGearCompoundPowerFlow
    from ._4205 import ConceptGearMeshCompoundPowerFlow
    from ._4206 import ConceptGearSetCompoundPowerFlow
    from ._4207 import ConicalGearCompoundPowerFlow
    from ._4208 import ConicalGearMeshCompoundPowerFlow
    from ._4209 import ConicalGearSetCompoundPowerFlow
    from ._4210 import ConnectionCompoundPowerFlow
    from ._4211 import ConnectorCompoundPowerFlow
    from ._4212 import CouplingCompoundPowerFlow
    from ._4213 import CouplingConnectionCompoundPowerFlow
    from ._4214 import CouplingHalfCompoundPowerFlow
    from ._4215 import CVTBeltConnectionCompoundPowerFlow
    from ._4216 import CVTCompoundPowerFlow
    from ._4217 import CVTPulleyCompoundPowerFlow
    from ._4218 import CycloidalAssemblyCompoundPowerFlow
    from ._4219 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4220 import CycloidalDiscCompoundPowerFlow
    from ._4221 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4222 import CylindricalGearCompoundPowerFlow
    from ._4223 import CylindricalGearMeshCompoundPowerFlow
    from ._4224 import CylindricalGearSetCompoundPowerFlow
    from ._4225 import CylindricalPlanetGearCompoundPowerFlow
    from ._4226 import DatumCompoundPowerFlow
    from ._4227 import ExternalCADModelCompoundPowerFlow
    from ._4228 import FaceGearCompoundPowerFlow
    from ._4229 import FaceGearMeshCompoundPowerFlow
    from ._4230 import FaceGearSetCompoundPowerFlow
    from ._4231 import FEPartCompoundPowerFlow
    from ._4232 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4233 import GearCompoundPowerFlow
    from ._4234 import GearMeshCompoundPowerFlow
    from ._4235 import GearSetCompoundPowerFlow
    from ._4236 import GuideDxfModelCompoundPowerFlow
    from ._4237 import HypoidGearCompoundPowerFlow
    from ._4238 import HypoidGearMeshCompoundPowerFlow
    from ._4239 import HypoidGearSetCompoundPowerFlow
    from ._4240 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4241 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4242 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4243 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4244 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4245 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4246 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4247 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4248 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4249 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4250 import MassDiscCompoundPowerFlow
    from ._4251 import MeasurementComponentCompoundPowerFlow
    from ._4252 import MountableComponentCompoundPowerFlow
    from ._4253 import OilSealCompoundPowerFlow
    from ._4254 import PartCompoundPowerFlow
    from ._4255 import PartToPartShearCouplingCompoundPowerFlow
    from ._4256 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4257 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4258 import PlanetaryConnectionCompoundPowerFlow
    from ._4259 import PlanetaryGearSetCompoundPowerFlow
    from ._4260 import PlanetCarrierCompoundPowerFlow
    from ._4261 import PointLoadCompoundPowerFlow
    from ._4262 import PowerLoadCompoundPowerFlow
    from ._4263 import PulleyCompoundPowerFlow
    from ._4264 import RingPinsCompoundPowerFlow
    from ._4265 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4266 import RollingRingAssemblyCompoundPowerFlow
    from ._4267 import RollingRingCompoundPowerFlow
    from ._4268 import RollingRingConnectionCompoundPowerFlow
    from ._4269 import RootAssemblyCompoundPowerFlow
    from ._4270 import ShaftCompoundPowerFlow
    from ._4271 import ShaftHubConnectionCompoundPowerFlow
    from ._4272 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4273 import SpecialisedAssemblyCompoundPowerFlow
    from ._4274 import SpiralBevelGearCompoundPowerFlow
    from ._4275 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4276 import SpiralBevelGearSetCompoundPowerFlow
    from ._4277 import SpringDamperCompoundPowerFlow
    from ._4278 import SpringDamperConnectionCompoundPowerFlow
    from ._4279 import SpringDamperHalfCompoundPowerFlow
    from ._4280 import StraightBevelDiffGearCompoundPowerFlow
    from ._4281 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4282 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4283 import StraightBevelGearCompoundPowerFlow
    from ._4284 import StraightBevelGearMeshCompoundPowerFlow
    from ._4285 import StraightBevelGearSetCompoundPowerFlow
    from ._4286 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4287 import StraightBevelSunGearCompoundPowerFlow
    from ._4288 import SynchroniserCompoundPowerFlow
    from ._4289 import SynchroniserHalfCompoundPowerFlow
    from ._4290 import SynchroniserPartCompoundPowerFlow
    from ._4291 import SynchroniserSleeveCompoundPowerFlow
    from ._4292 import TorqueConverterCompoundPowerFlow
    from ._4293 import TorqueConverterConnectionCompoundPowerFlow
    from ._4294 import TorqueConverterPumpCompoundPowerFlow
    from ._4295 import TorqueConverterTurbineCompoundPowerFlow
    from ._4296 import UnbalancedMassCompoundPowerFlow
    from ._4297 import VirtualComponentCompoundPowerFlow
    from ._4298 import WormGearCompoundPowerFlow
    from ._4299 import WormGearMeshCompoundPowerFlow
    from ._4300 import WormGearSetCompoundPowerFlow
    from ._4301 import ZerolBevelGearCompoundPowerFlow
    from ._4302 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4303 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        "_4175": ["AbstractAssemblyCompoundPowerFlow"],
        "_4176": ["AbstractShaftCompoundPowerFlow"],
        "_4177": ["AbstractShaftOrHousingCompoundPowerFlow"],
        "_4178": ["AbstractShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4179": ["AGMAGleasonConicalGearCompoundPowerFlow"],
        "_4180": ["AGMAGleasonConicalGearMeshCompoundPowerFlow"],
        "_4181": ["AGMAGleasonConicalGearSetCompoundPowerFlow"],
        "_4182": ["AssemblyCompoundPowerFlow"],
        "_4183": ["BearingCompoundPowerFlow"],
        "_4184": ["BeltConnectionCompoundPowerFlow"],
        "_4185": ["BeltDriveCompoundPowerFlow"],
        "_4186": ["BevelDifferentialGearCompoundPowerFlow"],
        "_4187": ["BevelDifferentialGearMeshCompoundPowerFlow"],
        "_4188": ["BevelDifferentialGearSetCompoundPowerFlow"],
        "_4189": ["BevelDifferentialPlanetGearCompoundPowerFlow"],
        "_4190": ["BevelDifferentialSunGearCompoundPowerFlow"],
        "_4191": ["BevelGearCompoundPowerFlow"],
        "_4192": ["BevelGearMeshCompoundPowerFlow"],
        "_4193": ["BevelGearSetCompoundPowerFlow"],
        "_4194": ["BoltCompoundPowerFlow"],
        "_4195": ["BoltedJointCompoundPowerFlow"],
        "_4196": ["ClutchCompoundPowerFlow"],
        "_4197": ["ClutchConnectionCompoundPowerFlow"],
        "_4198": ["ClutchHalfCompoundPowerFlow"],
        "_4199": ["CoaxialConnectionCompoundPowerFlow"],
        "_4200": ["ComponentCompoundPowerFlow"],
        "_4201": ["ConceptCouplingCompoundPowerFlow"],
        "_4202": ["ConceptCouplingConnectionCompoundPowerFlow"],
        "_4203": ["ConceptCouplingHalfCompoundPowerFlow"],
        "_4204": ["ConceptGearCompoundPowerFlow"],
        "_4205": ["ConceptGearMeshCompoundPowerFlow"],
        "_4206": ["ConceptGearSetCompoundPowerFlow"],
        "_4207": ["ConicalGearCompoundPowerFlow"],
        "_4208": ["ConicalGearMeshCompoundPowerFlow"],
        "_4209": ["ConicalGearSetCompoundPowerFlow"],
        "_4210": ["ConnectionCompoundPowerFlow"],
        "_4211": ["ConnectorCompoundPowerFlow"],
        "_4212": ["CouplingCompoundPowerFlow"],
        "_4213": ["CouplingConnectionCompoundPowerFlow"],
        "_4214": ["CouplingHalfCompoundPowerFlow"],
        "_4215": ["CVTBeltConnectionCompoundPowerFlow"],
        "_4216": ["CVTCompoundPowerFlow"],
        "_4217": ["CVTPulleyCompoundPowerFlow"],
        "_4218": ["CycloidalAssemblyCompoundPowerFlow"],
        "_4219": ["CycloidalDiscCentralBearingConnectionCompoundPowerFlow"],
        "_4220": ["CycloidalDiscCompoundPowerFlow"],
        "_4221": ["CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow"],
        "_4222": ["CylindricalGearCompoundPowerFlow"],
        "_4223": ["CylindricalGearMeshCompoundPowerFlow"],
        "_4224": ["CylindricalGearSetCompoundPowerFlow"],
        "_4225": ["CylindricalPlanetGearCompoundPowerFlow"],
        "_4226": ["DatumCompoundPowerFlow"],
        "_4227": ["ExternalCADModelCompoundPowerFlow"],
        "_4228": ["FaceGearCompoundPowerFlow"],
        "_4229": ["FaceGearMeshCompoundPowerFlow"],
        "_4230": ["FaceGearSetCompoundPowerFlow"],
        "_4231": ["FEPartCompoundPowerFlow"],
        "_4232": ["FlexiblePinAssemblyCompoundPowerFlow"],
        "_4233": ["GearCompoundPowerFlow"],
        "_4234": ["GearMeshCompoundPowerFlow"],
        "_4235": ["GearSetCompoundPowerFlow"],
        "_4236": ["GuideDxfModelCompoundPowerFlow"],
        "_4237": ["HypoidGearCompoundPowerFlow"],
        "_4238": ["HypoidGearMeshCompoundPowerFlow"],
        "_4239": ["HypoidGearSetCompoundPowerFlow"],
        "_4240": ["InterMountableComponentConnectionCompoundPowerFlow"],
        "_4241": ["KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"],
        "_4242": ["KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow"],
        "_4243": ["KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"],
        "_4244": ["KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"],
        "_4245": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"],
        "_4246": ["KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow"],
        "_4247": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow"],
        "_4248": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"],
        "_4249": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"],
        "_4250": ["MassDiscCompoundPowerFlow"],
        "_4251": ["MeasurementComponentCompoundPowerFlow"],
        "_4252": ["MountableComponentCompoundPowerFlow"],
        "_4253": ["OilSealCompoundPowerFlow"],
        "_4254": ["PartCompoundPowerFlow"],
        "_4255": ["PartToPartShearCouplingCompoundPowerFlow"],
        "_4256": ["PartToPartShearCouplingConnectionCompoundPowerFlow"],
        "_4257": ["PartToPartShearCouplingHalfCompoundPowerFlow"],
        "_4258": ["PlanetaryConnectionCompoundPowerFlow"],
        "_4259": ["PlanetaryGearSetCompoundPowerFlow"],
        "_4260": ["PlanetCarrierCompoundPowerFlow"],
        "_4261": ["PointLoadCompoundPowerFlow"],
        "_4262": ["PowerLoadCompoundPowerFlow"],
        "_4263": ["PulleyCompoundPowerFlow"],
        "_4264": ["RingPinsCompoundPowerFlow"],
        "_4265": ["RingPinsToDiscConnectionCompoundPowerFlow"],
        "_4266": ["RollingRingAssemblyCompoundPowerFlow"],
        "_4267": ["RollingRingCompoundPowerFlow"],
        "_4268": ["RollingRingConnectionCompoundPowerFlow"],
        "_4269": ["RootAssemblyCompoundPowerFlow"],
        "_4270": ["ShaftCompoundPowerFlow"],
        "_4271": ["ShaftHubConnectionCompoundPowerFlow"],
        "_4272": ["ShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4273": ["SpecialisedAssemblyCompoundPowerFlow"],
        "_4274": ["SpiralBevelGearCompoundPowerFlow"],
        "_4275": ["SpiralBevelGearMeshCompoundPowerFlow"],
        "_4276": ["SpiralBevelGearSetCompoundPowerFlow"],
        "_4277": ["SpringDamperCompoundPowerFlow"],
        "_4278": ["SpringDamperConnectionCompoundPowerFlow"],
        "_4279": ["SpringDamperHalfCompoundPowerFlow"],
        "_4280": ["StraightBevelDiffGearCompoundPowerFlow"],
        "_4281": ["StraightBevelDiffGearMeshCompoundPowerFlow"],
        "_4282": ["StraightBevelDiffGearSetCompoundPowerFlow"],
        "_4283": ["StraightBevelGearCompoundPowerFlow"],
        "_4284": ["StraightBevelGearMeshCompoundPowerFlow"],
        "_4285": ["StraightBevelGearSetCompoundPowerFlow"],
        "_4286": ["StraightBevelPlanetGearCompoundPowerFlow"],
        "_4287": ["StraightBevelSunGearCompoundPowerFlow"],
        "_4288": ["SynchroniserCompoundPowerFlow"],
        "_4289": ["SynchroniserHalfCompoundPowerFlow"],
        "_4290": ["SynchroniserPartCompoundPowerFlow"],
        "_4291": ["SynchroniserSleeveCompoundPowerFlow"],
        "_4292": ["TorqueConverterCompoundPowerFlow"],
        "_4293": ["TorqueConverterConnectionCompoundPowerFlow"],
        "_4294": ["TorqueConverterPumpCompoundPowerFlow"],
        "_4295": ["TorqueConverterTurbineCompoundPowerFlow"],
        "_4296": ["UnbalancedMassCompoundPowerFlow"],
        "_4297": ["VirtualComponentCompoundPowerFlow"],
        "_4298": ["WormGearCompoundPowerFlow"],
        "_4299": ["WormGearMeshCompoundPowerFlow"],
        "_4300": ["WormGearSetCompoundPowerFlow"],
        "_4301": ["ZerolBevelGearCompoundPowerFlow"],
        "_4302": ["ZerolBevelGearMeshCompoundPowerFlow"],
        "_4303": ["ZerolBevelGearSetCompoundPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundPowerFlow",
    "AbstractShaftCompoundPowerFlow",
    "AbstractShaftOrHousingCompoundPowerFlow",
    "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    "AGMAGleasonConicalGearCompoundPowerFlow",
    "AGMAGleasonConicalGearMeshCompoundPowerFlow",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
    "AssemblyCompoundPowerFlow",
    "BearingCompoundPowerFlow",
    "BeltConnectionCompoundPowerFlow",
    "BeltDriveCompoundPowerFlow",
    "BevelDifferentialGearCompoundPowerFlow",
    "BevelDifferentialGearMeshCompoundPowerFlow",
    "BevelDifferentialGearSetCompoundPowerFlow",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
    "BevelDifferentialSunGearCompoundPowerFlow",
    "BevelGearCompoundPowerFlow",
    "BevelGearMeshCompoundPowerFlow",
    "BevelGearSetCompoundPowerFlow",
    "BoltCompoundPowerFlow",
    "BoltedJointCompoundPowerFlow",
    "ClutchCompoundPowerFlow",
    "ClutchConnectionCompoundPowerFlow",
    "ClutchHalfCompoundPowerFlow",
    "CoaxialConnectionCompoundPowerFlow",
    "ComponentCompoundPowerFlow",
    "ConceptCouplingCompoundPowerFlow",
    "ConceptCouplingConnectionCompoundPowerFlow",
    "ConceptCouplingHalfCompoundPowerFlow",
    "ConceptGearCompoundPowerFlow",
    "ConceptGearMeshCompoundPowerFlow",
    "ConceptGearSetCompoundPowerFlow",
    "ConicalGearCompoundPowerFlow",
    "ConicalGearMeshCompoundPowerFlow",
    "ConicalGearSetCompoundPowerFlow",
    "ConnectionCompoundPowerFlow",
    "ConnectorCompoundPowerFlow",
    "CouplingCompoundPowerFlow",
    "CouplingConnectionCompoundPowerFlow",
    "CouplingHalfCompoundPowerFlow",
    "CVTBeltConnectionCompoundPowerFlow",
    "CVTCompoundPowerFlow",
    "CVTPulleyCompoundPowerFlow",
    "CycloidalAssemblyCompoundPowerFlow",
    "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
    "CycloidalDiscCompoundPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow",
    "CylindricalGearCompoundPowerFlow",
    "CylindricalGearMeshCompoundPowerFlow",
    "CylindricalGearSetCompoundPowerFlow",
    "CylindricalPlanetGearCompoundPowerFlow",
    "DatumCompoundPowerFlow",
    "ExternalCADModelCompoundPowerFlow",
    "FaceGearCompoundPowerFlow",
    "FaceGearMeshCompoundPowerFlow",
    "FaceGearSetCompoundPowerFlow",
    "FEPartCompoundPowerFlow",
    "FlexiblePinAssemblyCompoundPowerFlow",
    "GearCompoundPowerFlow",
    "GearMeshCompoundPowerFlow",
    "GearSetCompoundPowerFlow",
    "GuideDxfModelCompoundPowerFlow",
    "HypoidGearCompoundPowerFlow",
    "HypoidGearMeshCompoundPowerFlow",
    "HypoidGearSetCompoundPowerFlow",
    "InterMountableComponentConnectionCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    "MassDiscCompoundPowerFlow",
    "MeasurementComponentCompoundPowerFlow",
    "MountableComponentCompoundPowerFlow",
    "OilSealCompoundPowerFlow",
    "PartCompoundPowerFlow",
    "PartToPartShearCouplingCompoundPowerFlow",
    "PartToPartShearCouplingConnectionCompoundPowerFlow",
    "PartToPartShearCouplingHalfCompoundPowerFlow",
    "PlanetaryConnectionCompoundPowerFlow",
    "PlanetaryGearSetCompoundPowerFlow",
    "PlanetCarrierCompoundPowerFlow",
    "PointLoadCompoundPowerFlow",
    "PowerLoadCompoundPowerFlow",
    "PulleyCompoundPowerFlow",
    "RingPinsCompoundPowerFlow",
    "RingPinsToDiscConnectionCompoundPowerFlow",
    "RollingRingAssemblyCompoundPowerFlow",
    "RollingRingCompoundPowerFlow",
    "RollingRingConnectionCompoundPowerFlow",
    "RootAssemblyCompoundPowerFlow",
    "ShaftCompoundPowerFlow",
    "ShaftHubConnectionCompoundPowerFlow",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
    "SpecialisedAssemblyCompoundPowerFlow",
    "SpiralBevelGearCompoundPowerFlow",
    "SpiralBevelGearMeshCompoundPowerFlow",
    "SpiralBevelGearSetCompoundPowerFlow",
    "SpringDamperCompoundPowerFlow",
    "SpringDamperConnectionCompoundPowerFlow",
    "SpringDamperHalfCompoundPowerFlow",
    "StraightBevelDiffGearCompoundPowerFlow",
    "StraightBevelDiffGearMeshCompoundPowerFlow",
    "StraightBevelDiffGearSetCompoundPowerFlow",
    "StraightBevelGearCompoundPowerFlow",
    "StraightBevelGearMeshCompoundPowerFlow",
    "StraightBevelGearSetCompoundPowerFlow",
    "StraightBevelPlanetGearCompoundPowerFlow",
    "StraightBevelSunGearCompoundPowerFlow",
    "SynchroniserCompoundPowerFlow",
    "SynchroniserHalfCompoundPowerFlow",
    "SynchroniserPartCompoundPowerFlow",
    "SynchroniserSleeveCompoundPowerFlow",
    "TorqueConverterCompoundPowerFlow",
    "TorqueConverterConnectionCompoundPowerFlow",
    "TorqueConverterPumpCompoundPowerFlow",
    "TorqueConverterTurbineCompoundPowerFlow",
    "UnbalancedMassCompoundPowerFlow",
    "VirtualComponentCompoundPowerFlow",
    "WormGearCompoundPowerFlow",
    "WormGearMeshCompoundPowerFlow",
    "WormGearSetCompoundPowerFlow",
    "ZerolBevelGearCompoundPowerFlow",
    "ZerolBevelGearMeshCompoundPowerFlow",
    "ZerolBevelGearSetCompoundPowerFlow",
)
