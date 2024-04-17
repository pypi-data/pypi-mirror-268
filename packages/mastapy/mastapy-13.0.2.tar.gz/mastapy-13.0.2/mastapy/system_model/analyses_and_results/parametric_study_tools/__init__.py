"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4304 import AbstractAssemblyParametricStudyTool
    from ._4305 import AbstractShaftOrHousingParametricStudyTool
    from ._4306 import AbstractShaftParametricStudyTool
    from ._4307 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4308 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4309 import AGMAGleasonConicalGearParametricStudyTool
    from ._4310 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4311 import AssemblyParametricStudyTool
    from ._4312 import BearingParametricStudyTool
    from ._4313 import BeltConnectionParametricStudyTool
    from ._4314 import BeltDriveParametricStudyTool
    from ._4315 import BevelDifferentialGearMeshParametricStudyTool
    from ._4316 import BevelDifferentialGearParametricStudyTool
    from ._4317 import BevelDifferentialGearSetParametricStudyTool
    from ._4318 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4319 import BevelDifferentialSunGearParametricStudyTool
    from ._4320 import BevelGearMeshParametricStudyTool
    from ._4321 import BevelGearParametricStudyTool
    from ._4322 import BevelGearSetParametricStudyTool
    from ._4323 import BoltedJointParametricStudyTool
    from ._4324 import BoltParametricStudyTool
    from ._4325 import ClutchConnectionParametricStudyTool
    from ._4326 import ClutchHalfParametricStudyTool
    from ._4327 import ClutchParametricStudyTool
    from ._4328 import CoaxialConnectionParametricStudyTool
    from ._4329 import ComponentParametricStudyTool
    from ._4330 import ConceptCouplingConnectionParametricStudyTool
    from ._4331 import ConceptCouplingHalfParametricStudyTool
    from ._4332 import ConceptCouplingParametricStudyTool
    from ._4333 import ConceptGearMeshParametricStudyTool
    from ._4334 import ConceptGearParametricStudyTool
    from ._4335 import ConceptGearSetParametricStudyTool
    from ._4336 import ConicalGearMeshParametricStudyTool
    from ._4337 import ConicalGearParametricStudyTool
    from ._4338 import ConicalGearSetParametricStudyTool
    from ._4339 import ConnectionParametricStudyTool
    from ._4340 import ConnectorParametricStudyTool
    from ._4341 import CouplingConnectionParametricStudyTool
    from ._4342 import CouplingHalfParametricStudyTool
    from ._4343 import CouplingParametricStudyTool
    from ._4344 import CVTBeltConnectionParametricStudyTool
    from ._4345 import CVTParametricStudyTool
    from ._4346 import CVTPulleyParametricStudyTool
    from ._4347 import CycloidalAssemblyParametricStudyTool
    from ._4348 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4349 import CycloidalDiscParametricStudyTool
    from ._4350 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4351 import CylindricalGearMeshParametricStudyTool
    from ._4352 import CylindricalGearParametricStudyTool
    from ._4353 import CylindricalGearSetParametricStudyTool
    from ._4354 import CylindricalPlanetGearParametricStudyTool
    from ._4355 import DatumParametricStudyTool
    from ._4356 import DesignOfExperimentsVariableSetter
    from ._4357 import DoeValueSpecificationOption
    from ._4358 import DutyCycleResultsForAllComponents
    from ._4359 import DutyCycleResultsForAllGearSets
    from ._4360 import DutyCycleResultsForRootAssembly
    from ._4361 import DutyCycleResultsForSingleBearing
    from ._4362 import DutyCycleResultsForSingleShaft
    from ._4363 import ExternalCADModelParametricStudyTool
    from ._4364 import FaceGearMeshParametricStudyTool
    from ._4365 import FaceGearParametricStudyTool
    from ._4366 import FaceGearSetParametricStudyTool
    from ._4367 import FEPartParametricStudyTool
    from ._4368 import FlexiblePinAssemblyParametricStudyTool
    from ._4369 import GearMeshParametricStudyTool
    from ._4370 import GearParametricStudyTool
    from ._4371 import GearSetParametricStudyTool
    from ._4372 import GuideDxfModelParametricStudyTool
    from ._4373 import HypoidGearMeshParametricStudyTool
    from ._4374 import HypoidGearParametricStudyTool
    from ._4375 import HypoidGearSetParametricStudyTool
    from ._4376 import InterMountableComponentConnectionParametricStudyTool
    from ._4377 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4378 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4379 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4380 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4381 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4382 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4383 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4384 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4385 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4386 import MassDiscParametricStudyTool
    from ._4387 import MeasurementComponentParametricStudyTool
    from ._4388 import MonteCarloDistribution
    from ._4389 import MountableComponentParametricStudyTool
    from ._4390 import OilSealParametricStudyTool
    from ._4391 import ParametricStudyDimension
    from ._4392 import ParametricStudyDOEResultVariable
    from ._4393 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4394 import ParametricStudyHistogram
    from ._4395 import ParametricStudyStaticLoad
    from ._4396 import ParametricStudyTool
    from ._4397 import ParametricStudyToolOptions
    from ._4398 import ParametricStudyToolResultsForReporting
    from ._4399 import ParametricStudyToolStepResult
    from ._4400 import ParametricStudyVariable
    from ._4401 import PartParametricStudyTool
    from ._4402 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4403 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4404 import PartToPartShearCouplingParametricStudyTool
    from ._4405 import PlanetaryConnectionParametricStudyTool
    from ._4406 import PlanetaryGearSetParametricStudyTool
    from ._4407 import PlanetCarrierParametricStudyTool
    from ._4408 import PointLoadParametricStudyTool
    from ._4409 import PowerLoadParametricStudyTool
    from ._4410 import PulleyParametricStudyTool
    from ._4411 import RingPinsParametricStudyTool
    from ._4412 import RingPinsToDiscConnectionParametricStudyTool
    from ._4413 import RollingRingAssemblyParametricStudyTool
    from ._4414 import RollingRingConnectionParametricStudyTool
    from ._4415 import RollingRingParametricStudyTool
    from ._4416 import RootAssemblyParametricStudyTool
    from ._4417 import ShaftHubConnectionParametricStudyTool
    from ._4418 import ShaftParametricStudyTool
    from ._4419 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4420 import SpecialisedAssemblyParametricStudyTool
    from ._4421 import SpiralBevelGearMeshParametricStudyTool
    from ._4422 import SpiralBevelGearParametricStudyTool
    from ._4423 import SpiralBevelGearSetParametricStudyTool
    from ._4424 import SpringDamperConnectionParametricStudyTool
    from ._4425 import SpringDamperHalfParametricStudyTool
    from ._4426 import SpringDamperParametricStudyTool
    from ._4427 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4428 import StraightBevelDiffGearParametricStudyTool
    from ._4429 import StraightBevelDiffGearSetParametricStudyTool
    from ._4430 import StraightBevelGearMeshParametricStudyTool
    from ._4431 import StraightBevelGearParametricStudyTool
    from ._4432 import StraightBevelGearSetParametricStudyTool
    from ._4433 import StraightBevelPlanetGearParametricStudyTool
    from ._4434 import StraightBevelSunGearParametricStudyTool
    from ._4435 import SynchroniserHalfParametricStudyTool
    from ._4436 import SynchroniserParametricStudyTool
    from ._4437 import SynchroniserPartParametricStudyTool
    from ._4438 import SynchroniserSleeveParametricStudyTool
    from ._4439 import TorqueConverterConnectionParametricStudyTool
    from ._4440 import TorqueConverterParametricStudyTool
    from ._4441 import TorqueConverterPumpParametricStudyTool
    from ._4442 import TorqueConverterTurbineParametricStudyTool
    from ._4443 import UnbalancedMassParametricStudyTool
    from ._4444 import VirtualComponentParametricStudyTool
    from ._4445 import WormGearMeshParametricStudyTool
    from ._4446 import WormGearParametricStudyTool
    from ._4447 import WormGearSetParametricStudyTool
    from ._4448 import ZerolBevelGearMeshParametricStudyTool
    from ._4449 import ZerolBevelGearParametricStudyTool
    from ._4450 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        "_4304": ["AbstractAssemblyParametricStudyTool"],
        "_4305": ["AbstractShaftOrHousingParametricStudyTool"],
        "_4306": ["AbstractShaftParametricStudyTool"],
        "_4307": ["AbstractShaftToMountableComponentConnectionParametricStudyTool"],
        "_4308": ["AGMAGleasonConicalGearMeshParametricStudyTool"],
        "_4309": ["AGMAGleasonConicalGearParametricStudyTool"],
        "_4310": ["AGMAGleasonConicalGearSetParametricStudyTool"],
        "_4311": ["AssemblyParametricStudyTool"],
        "_4312": ["BearingParametricStudyTool"],
        "_4313": ["BeltConnectionParametricStudyTool"],
        "_4314": ["BeltDriveParametricStudyTool"],
        "_4315": ["BevelDifferentialGearMeshParametricStudyTool"],
        "_4316": ["BevelDifferentialGearParametricStudyTool"],
        "_4317": ["BevelDifferentialGearSetParametricStudyTool"],
        "_4318": ["BevelDifferentialPlanetGearParametricStudyTool"],
        "_4319": ["BevelDifferentialSunGearParametricStudyTool"],
        "_4320": ["BevelGearMeshParametricStudyTool"],
        "_4321": ["BevelGearParametricStudyTool"],
        "_4322": ["BevelGearSetParametricStudyTool"],
        "_4323": ["BoltedJointParametricStudyTool"],
        "_4324": ["BoltParametricStudyTool"],
        "_4325": ["ClutchConnectionParametricStudyTool"],
        "_4326": ["ClutchHalfParametricStudyTool"],
        "_4327": ["ClutchParametricStudyTool"],
        "_4328": ["CoaxialConnectionParametricStudyTool"],
        "_4329": ["ComponentParametricStudyTool"],
        "_4330": ["ConceptCouplingConnectionParametricStudyTool"],
        "_4331": ["ConceptCouplingHalfParametricStudyTool"],
        "_4332": ["ConceptCouplingParametricStudyTool"],
        "_4333": ["ConceptGearMeshParametricStudyTool"],
        "_4334": ["ConceptGearParametricStudyTool"],
        "_4335": ["ConceptGearSetParametricStudyTool"],
        "_4336": ["ConicalGearMeshParametricStudyTool"],
        "_4337": ["ConicalGearParametricStudyTool"],
        "_4338": ["ConicalGearSetParametricStudyTool"],
        "_4339": ["ConnectionParametricStudyTool"],
        "_4340": ["ConnectorParametricStudyTool"],
        "_4341": ["CouplingConnectionParametricStudyTool"],
        "_4342": ["CouplingHalfParametricStudyTool"],
        "_4343": ["CouplingParametricStudyTool"],
        "_4344": ["CVTBeltConnectionParametricStudyTool"],
        "_4345": ["CVTParametricStudyTool"],
        "_4346": ["CVTPulleyParametricStudyTool"],
        "_4347": ["CycloidalAssemblyParametricStudyTool"],
        "_4348": ["CycloidalDiscCentralBearingConnectionParametricStudyTool"],
        "_4349": ["CycloidalDiscParametricStudyTool"],
        "_4350": ["CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"],
        "_4351": ["CylindricalGearMeshParametricStudyTool"],
        "_4352": ["CylindricalGearParametricStudyTool"],
        "_4353": ["CylindricalGearSetParametricStudyTool"],
        "_4354": ["CylindricalPlanetGearParametricStudyTool"],
        "_4355": ["DatumParametricStudyTool"],
        "_4356": ["DesignOfExperimentsVariableSetter"],
        "_4357": ["DoeValueSpecificationOption"],
        "_4358": ["DutyCycleResultsForAllComponents"],
        "_4359": ["DutyCycleResultsForAllGearSets"],
        "_4360": ["DutyCycleResultsForRootAssembly"],
        "_4361": ["DutyCycleResultsForSingleBearing"],
        "_4362": ["DutyCycleResultsForSingleShaft"],
        "_4363": ["ExternalCADModelParametricStudyTool"],
        "_4364": ["FaceGearMeshParametricStudyTool"],
        "_4365": ["FaceGearParametricStudyTool"],
        "_4366": ["FaceGearSetParametricStudyTool"],
        "_4367": ["FEPartParametricStudyTool"],
        "_4368": ["FlexiblePinAssemblyParametricStudyTool"],
        "_4369": ["GearMeshParametricStudyTool"],
        "_4370": ["GearParametricStudyTool"],
        "_4371": ["GearSetParametricStudyTool"],
        "_4372": ["GuideDxfModelParametricStudyTool"],
        "_4373": ["HypoidGearMeshParametricStudyTool"],
        "_4374": ["HypoidGearParametricStudyTool"],
        "_4375": ["HypoidGearSetParametricStudyTool"],
        "_4376": ["InterMountableComponentConnectionParametricStudyTool"],
        "_4377": ["KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"],
        "_4378": ["KlingelnbergCycloPalloidConicalGearParametricStudyTool"],
        "_4379": ["KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"],
        "_4380": ["KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"],
        "_4381": ["KlingelnbergCycloPalloidHypoidGearParametricStudyTool"],
        "_4382": ["KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool"],
        "_4383": ["KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool"],
        "_4384": ["KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool"],
        "_4385": ["KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool"],
        "_4386": ["MassDiscParametricStudyTool"],
        "_4387": ["MeasurementComponentParametricStudyTool"],
        "_4388": ["MonteCarloDistribution"],
        "_4389": ["MountableComponentParametricStudyTool"],
        "_4390": ["OilSealParametricStudyTool"],
        "_4391": ["ParametricStudyDimension"],
        "_4392": ["ParametricStudyDOEResultVariable"],
        "_4393": ["ParametricStudyDOEResultVariableForParallelCoordinatesPlot"],
        "_4394": ["ParametricStudyHistogram"],
        "_4395": ["ParametricStudyStaticLoad"],
        "_4396": ["ParametricStudyTool"],
        "_4397": ["ParametricStudyToolOptions"],
        "_4398": ["ParametricStudyToolResultsForReporting"],
        "_4399": ["ParametricStudyToolStepResult"],
        "_4400": ["ParametricStudyVariable"],
        "_4401": ["PartParametricStudyTool"],
        "_4402": ["PartToPartShearCouplingConnectionParametricStudyTool"],
        "_4403": ["PartToPartShearCouplingHalfParametricStudyTool"],
        "_4404": ["PartToPartShearCouplingParametricStudyTool"],
        "_4405": ["PlanetaryConnectionParametricStudyTool"],
        "_4406": ["PlanetaryGearSetParametricStudyTool"],
        "_4407": ["PlanetCarrierParametricStudyTool"],
        "_4408": ["PointLoadParametricStudyTool"],
        "_4409": ["PowerLoadParametricStudyTool"],
        "_4410": ["PulleyParametricStudyTool"],
        "_4411": ["RingPinsParametricStudyTool"],
        "_4412": ["RingPinsToDiscConnectionParametricStudyTool"],
        "_4413": ["RollingRingAssemblyParametricStudyTool"],
        "_4414": ["RollingRingConnectionParametricStudyTool"],
        "_4415": ["RollingRingParametricStudyTool"],
        "_4416": ["RootAssemblyParametricStudyTool"],
        "_4417": ["ShaftHubConnectionParametricStudyTool"],
        "_4418": ["ShaftParametricStudyTool"],
        "_4419": ["ShaftToMountableComponentConnectionParametricStudyTool"],
        "_4420": ["SpecialisedAssemblyParametricStudyTool"],
        "_4421": ["SpiralBevelGearMeshParametricStudyTool"],
        "_4422": ["SpiralBevelGearParametricStudyTool"],
        "_4423": ["SpiralBevelGearSetParametricStudyTool"],
        "_4424": ["SpringDamperConnectionParametricStudyTool"],
        "_4425": ["SpringDamperHalfParametricStudyTool"],
        "_4426": ["SpringDamperParametricStudyTool"],
        "_4427": ["StraightBevelDiffGearMeshParametricStudyTool"],
        "_4428": ["StraightBevelDiffGearParametricStudyTool"],
        "_4429": ["StraightBevelDiffGearSetParametricStudyTool"],
        "_4430": ["StraightBevelGearMeshParametricStudyTool"],
        "_4431": ["StraightBevelGearParametricStudyTool"],
        "_4432": ["StraightBevelGearSetParametricStudyTool"],
        "_4433": ["StraightBevelPlanetGearParametricStudyTool"],
        "_4434": ["StraightBevelSunGearParametricStudyTool"],
        "_4435": ["SynchroniserHalfParametricStudyTool"],
        "_4436": ["SynchroniserParametricStudyTool"],
        "_4437": ["SynchroniserPartParametricStudyTool"],
        "_4438": ["SynchroniserSleeveParametricStudyTool"],
        "_4439": ["TorqueConverterConnectionParametricStudyTool"],
        "_4440": ["TorqueConverterParametricStudyTool"],
        "_4441": ["TorqueConverterPumpParametricStudyTool"],
        "_4442": ["TorqueConverterTurbineParametricStudyTool"],
        "_4443": ["UnbalancedMassParametricStudyTool"],
        "_4444": ["VirtualComponentParametricStudyTool"],
        "_4445": ["WormGearMeshParametricStudyTool"],
        "_4446": ["WormGearParametricStudyTool"],
        "_4447": ["WormGearSetParametricStudyTool"],
        "_4448": ["ZerolBevelGearMeshParametricStudyTool"],
        "_4449": ["ZerolBevelGearParametricStudyTool"],
        "_4450": ["ZerolBevelGearSetParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyParametricStudyTool",
    "AbstractShaftOrHousingParametricStudyTool",
    "AbstractShaftParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
    "AGMAGleasonConicalGearParametricStudyTool",
    "AGMAGleasonConicalGearSetParametricStudyTool",
    "AssemblyParametricStudyTool",
    "BearingParametricStudyTool",
    "BeltConnectionParametricStudyTool",
    "BeltDriveParametricStudyTool",
    "BevelDifferentialGearMeshParametricStudyTool",
    "BevelDifferentialGearParametricStudyTool",
    "BevelDifferentialGearSetParametricStudyTool",
    "BevelDifferentialPlanetGearParametricStudyTool",
    "BevelDifferentialSunGearParametricStudyTool",
    "BevelGearMeshParametricStudyTool",
    "BevelGearParametricStudyTool",
    "BevelGearSetParametricStudyTool",
    "BoltedJointParametricStudyTool",
    "BoltParametricStudyTool",
    "ClutchConnectionParametricStudyTool",
    "ClutchHalfParametricStudyTool",
    "ClutchParametricStudyTool",
    "CoaxialConnectionParametricStudyTool",
    "ComponentParametricStudyTool",
    "ConceptCouplingConnectionParametricStudyTool",
    "ConceptCouplingHalfParametricStudyTool",
    "ConceptCouplingParametricStudyTool",
    "ConceptGearMeshParametricStudyTool",
    "ConceptGearParametricStudyTool",
    "ConceptGearSetParametricStudyTool",
    "ConicalGearMeshParametricStudyTool",
    "ConicalGearParametricStudyTool",
    "ConicalGearSetParametricStudyTool",
    "ConnectionParametricStudyTool",
    "ConnectorParametricStudyTool",
    "CouplingConnectionParametricStudyTool",
    "CouplingHalfParametricStudyTool",
    "CouplingParametricStudyTool",
    "CVTBeltConnectionParametricStudyTool",
    "CVTParametricStudyTool",
    "CVTPulleyParametricStudyTool",
    "CycloidalAssemblyParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionParametricStudyTool",
    "CycloidalDiscParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    "CylindricalGearMeshParametricStudyTool",
    "CylindricalGearParametricStudyTool",
    "CylindricalGearSetParametricStudyTool",
    "CylindricalPlanetGearParametricStudyTool",
    "DatumParametricStudyTool",
    "DesignOfExperimentsVariableSetter",
    "DoeValueSpecificationOption",
    "DutyCycleResultsForAllComponents",
    "DutyCycleResultsForAllGearSets",
    "DutyCycleResultsForRootAssembly",
    "DutyCycleResultsForSingleBearing",
    "DutyCycleResultsForSingleShaft",
    "ExternalCADModelParametricStudyTool",
    "FaceGearMeshParametricStudyTool",
    "FaceGearParametricStudyTool",
    "FaceGearSetParametricStudyTool",
    "FEPartParametricStudyTool",
    "FlexiblePinAssemblyParametricStudyTool",
    "GearMeshParametricStudyTool",
    "GearParametricStudyTool",
    "GearSetParametricStudyTool",
    "GuideDxfModelParametricStudyTool",
    "HypoidGearMeshParametricStudyTool",
    "HypoidGearParametricStudyTool",
    "HypoidGearSetParametricStudyTool",
    "InterMountableComponentConnectionParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool",
    "MassDiscParametricStudyTool",
    "MeasurementComponentParametricStudyTool",
    "MonteCarloDistribution",
    "MountableComponentParametricStudyTool",
    "OilSealParametricStudyTool",
    "ParametricStudyDimension",
    "ParametricStudyDOEResultVariable",
    "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
    "ParametricStudyHistogram",
    "ParametricStudyStaticLoad",
    "ParametricStudyTool",
    "ParametricStudyToolOptions",
    "ParametricStudyToolResultsForReporting",
    "ParametricStudyToolStepResult",
    "ParametricStudyVariable",
    "PartParametricStudyTool",
    "PartToPartShearCouplingConnectionParametricStudyTool",
    "PartToPartShearCouplingHalfParametricStudyTool",
    "PartToPartShearCouplingParametricStudyTool",
    "PlanetaryConnectionParametricStudyTool",
    "PlanetaryGearSetParametricStudyTool",
    "PlanetCarrierParametricStudyTool",
    "PointLoadParametricStudyTool",
    "PowerLoadParametricStudyTool",
    "PulleyParametricStudyTool",
    "RingPinsParametricStudyTool",
    "RingPinsToDiscConnectionParametricStudyTool",
    "RollingRingAssemblyParametricStudyTool",
    "RollingRingConnectionParametricStudyTool",
    "RollingRingParametricStudyTool",
    "RootAssemblyParametricStudyTool",
    "ShaftHubConnectionParametricStudyTool",
    "ShaftParametricStudyTool",
    "ShaftToMountableComponentConnectionParametricStudyTool",
    "SpecialisedAssemblyParametricStudyTool",
    "SpiralBevelGearMeshParametricStudyTool",
    "SpiralBevelGearParametricStudyTool",
    "SpiralBevelGearSetParametricStudyTool",
    "SpringDamperConnectionParametricStudyTool",
    "SpringDamperHalfParametricStudyTool",
    "SpringDamperParametricStudyTool",
    "StraightBevelDiffGearMeshParametricStudyTool",
    "StraightBevelDiffGearParametricStudyTool",
    "StraightBevelDiffGearSetParametricStudyTool",
    "StraightBevelGearMeshParametricStudyTool",
    "StraightBevelGearParametricStudyTool",
    "StraightBevelGearSetParametricStudyTool",
    "StraightBevelPlanetGearParametricStudyTool",
    "StraightBevelSunGearParametricStudyTool",
    "SynchroniserHalfParametricStudyTool",
    "SynchroniserParametricStudyTool",
    "SynchroniserPartParametricStudyTool",
    "SynchroniserSleeveParametricStudyTool",
    "TorqueConverterConnectionParametricStudyTool",
    "TorqueConverterParametricStudyTool",
    "TorqueConverterPumpParametricStudyTool",
    "TorqueConverterTurbineParametricStudyTool",
    "UnbalancedMassParametricStudyTool",
    "VirtualComponentParametricStudyTool",
    "WormGearMeshParametricStudyTool",
    "WormGearParametricStudyTool",
    "WormGearSetParametricStudyTool",
    "ZerolBevelGearMeshParametricStudyTool",
    "ZerolBevelGearParametricStudyTool",
    "ZerolBevelGearSetParametricStudyTool",
)
