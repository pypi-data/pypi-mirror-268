"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5255 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5256 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5257 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5258 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5259 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5260 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5261 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5262 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5263 import BearingCompoundModalAnalysisAtASpeed
    from ._5264 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5265 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5266 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5267 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5268 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5269 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5270 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5271 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5272 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5273 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5274 import BoltCompoundModalAnalysisAtASpeed
    from ._5275 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5276 import ClutchCompoundModalAnalysisAtASpeed
    from ._5277 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5278 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5279 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5280 import ComponentCompoundModalAnalysisAtASpeed
    from ._5281 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5282 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5283 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5284 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5285 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5286 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5287 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5288 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5289 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5290 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5291 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5292 import CouplingCompoundModalAnalysisAtASpeed
    from ._5293 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5294 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5295 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5296 import CVTCompoundModalAnalysisAtASpeed
    from ._5297 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5298 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5299 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5300 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5301 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5302 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5303 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5304 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5305 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5306 import DatumCompoundModalAnalysisAtASpeed
    from ._5307 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5308 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5309 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5310 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5311 import FEPartCompoundModalAnalysisAtASpeed
    from ._5312 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5313 import GearCompoundModalAnalysisAtASpeed
    from ._5314 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5315 import GearSetCompoundModalAnalysisAtASpeed
    from ._5316 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5317 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5318 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5319 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5320 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5321 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5322 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5323 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5324 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5325 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5326 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5327 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed,
    )
    from ._5328 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5329 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5330 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5331 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5332 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5333 import OilSealCompoundModalAnalysisAtASpeed
    from ._5334 import PartCompoundModalAnalysisAtASpeed
    from ._5335 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5336 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5337 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5338 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5339 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5340 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5341 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5342 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5343 import PulleyCompoundModalAnalysisAtASpeed
    from ._5344 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5345 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5346 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5347 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5348 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5349 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5350 import ShaftCompoundModalAnalysisAtASpeed
    from ._5351 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5352 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5353 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5354 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5355 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5356 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5357 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5358 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5359 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5360 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5361 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5362 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5363 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5364 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5365 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5366 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5367 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5368 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5369 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5370 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5371 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5372 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5373 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5374 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5375 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5376 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5377 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5378 import WormGearCompoundModalAnalysisAtASpeed
    from ._5379 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5380 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5381 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5382 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5383 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        "_5255": ["AbstractAssemblyCompoundModalAnalysisAtASpeed"],
        "_5256": ["AbstractShaftCompoundModalAnalysisAtASpeed"],
        "_5257": ["AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"],
        "_5258": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5259": ["AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"],
        "_5260": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5261": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5262": ["AssemblyCompoundModalAnalysisAtASpeed"],
        "_5263": ["BearingCompoundModalAnalysisAtASpeed"],
        "_5264": ["BeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5265": ["BeltDriveCompoundModalAnalysisAtASpeed"],
        "_5266": ["BevelDifferentialGearCompoundModalAnalysisAtASpeed"],
        "_5267": ["BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed"],
        "_5268": ["BevelDifferentialGearSetCompoundModalAnalysisAtASpeed"],
        "_5269": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5270": ["BevelDifferentialSunGearCompoundModalAnalysisAtASpeed"],
        "_5271": ["BevelGearCompoundModalAnalysisAtASpeed"],
        "_5272": ["BevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5273": ["BevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5274": ["BoltCompoundModalAnalysisAtASpeed"],
        "_5275": ["BoltedJointCompoundModalAnalysisAtASpeed"],
        "_5276": ["ClutchCompoundModalAnalysisAtASpeed"],
        "_5277": ["ClutchConnectionCompoundModalAnalysisAtASpeed"],
        "_5278": ["ClutchHalfCompoundModalAnalysisAtASpeed"],
        "_5279": ["CoaxialConnectionCompoundModalAnalysisAtASpeed"],
        "_5280": ["ComponentCompoundModalAnalysisAtASpeed"],
        "_5281": ["ConceptCouplingCompoundModalAnalysisAtASpeed"],
        "_5282": ["ConceptCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5283": ["ConceptCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5284": ["ConceptGearCompoundModalAnalysisAtASpeed"],
        "_5285": ["ConceptGearMeshCompoundModalAnalysisAtASpeed"],
        "_5286": ["ConceptGearSetCompoundModalAnalysisAtASpeed"],
        "_5287": ["ConicalGearCompoundModalAnalysisAtASpeed"],
        "_5288": ["ConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5289": ["ConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5290": ["ConnectionCompoundModalAnalysisAtASpeed"],
        "_5291": ["ConnectorCompoundModalAnalysisAtASpeed"],
        "_5292": ["CouplingCompoundModalAnalysisAtASpeed"],
        "_5293": ["CouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5294": ["CouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5295": ["CVTBeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5296": ["CVTCompoundModalAnalysisAtASpeed"],
        "_5297": ["CVTPulleyCompoundModalAnalysisAtASpeed"],
        "_5298": ["CycloidalAssemblyCompoundModalAnalysisAtASpeed"],
        "_5299": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"],
        "_5300": ["CycloidalDiscCompoundModalAnalysisAtASpeed"],
        "_5301": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5302": ["CylindricalGearCompoundModalAnalysisAtASpeed"],
        "_5303": ["CylindricalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5304": ["CylindricalGearSetCompoundModalAnalysisAtASpeed"],
        "_5305": ["CylindricalPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5306": ["DatumCompoundModalAnalysisAtASpeed"],
        "_5307": ["ExternalCADModelCompoundModalAnalysisAtASpeed"],
        "_5308": ["FaceGearCompoundModalAnalysisAtASpeed"],
        "_5309": ["FaceGearMeshCompoundModalAnalysisAtASpeed"],
        "_5310": ["FaceGearSetCompoundModalAnalysisAtASpeed"],
        "_5311": ["FEPartCompoundModalAnalysisAtASpeed"],
        "_5312": ["FlexiblePinAssemblyCompoundModalAnalysisAtASpeed"],
        "_5313": ["GearCompoundModalAnalysisAtASpeed"],
        "_5314": ["GearMeshCompoundModalAnalysisAtASpeed"],
        "_5315": ["GearSetCompoundModalAnalysisAtASpeed"],
        "_5316": ["GuideDxfModelCompoundModalAnalysisAtASpeed"],
        "_5317": ["HypoidGearCompoundModalAnalysisAtASpeed"],
        "_5318": ["HypoidGearMeshCompoundModalAnalysisAtASpeed"],
        "_5319": ["HypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5320": ["InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5321": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed"],
        "_5322": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5323": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5324": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed"],
        "_5325": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5326": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5327": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ],
        "_5328": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5329": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5330": ["MassDiscCompoundModalAnalysisAtASpeed"],
        "_5331": ["MeasurementComponentCompoundModalAnalysisAtASpeed"],
        "_5332": ["MountableComponentCompoundModalAnalysisAtASpeed"],
        "_5333": ["OilSealCompoundModalAnalysisAtASpeed"],
        "_5334": ["PartCompoundModalAnalysisAtASpeed"],
        "_5335": ["PartToPartShearCouplingCompoundModalAnalysisAtASpeed"],
        "_5336": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5337": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5338": ["PlanetaryConnectionCompoundModalAnalysisAtASpeed"],
        "_5339": ["PlanetaryGearSetCompoundModalAnalysisAtASpeed"],
        "_5340": ["PlanetCarrierCompoundModalAnalysisAtASpeed"],
        "_5341": ["PointLoadCompoundModalAnalysisAtASpeed"],
        "_5342": ["PowerLoadCompoundModalAnalysisAtASpeed"],
        "_5343": ["PulleyCompoundModalAnalysisAtASpeed"],
        "_5344": ["RingPinsCompoundModalAnalysisAtASpeed"],
        "_5345": ["RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed"],
        "_5346": ["RollingRingAssemblyCompoundModalAnalysisAtASpeed"],
        "_5347": ["RollingRingCompoundModalAnalysisAtASpeed"],
        "_5348": ["RollingRingConnectionCompoundModalAnalysisAtASpeed"],
        "_5349": ["RootAssemblyCompoundModalAnalysisAtASpeed"],
        "_5350": ["ShaftCompoundModalAnalysisAtASpeed"],
        "_5351": ["ShaftHubConnectionCompoundModalAnalysisAtASpeed"],
        "_5352": ["ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5353": ["SpecialisedAssemblyCompoundModalAnalysisAtASpeed"],
        "_5354": ["SpiralBevelGearCompoundModalAnalysisAtASpeed"],
        "_5355": ["SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5356": ["SpiralBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5357": ["SpringDamperCompoundModalAnalysisAtASpeed"],
        "_5358": ["SpringDamperConnectionCompoundModalAnalysisAtASpeed"],
        "_5359": ["SpringDamperHalfCompoundModalAnalysisAtASpeed"],
        "_5360": ["StraightBevelDiffGearCompoundModalAnalysisAtASpeed"],
        "_5361": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed"],
        "_5362": ["StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"],
        "_5363": ["StraightBevelGearCompoundModalAnalysisAtASpeed"],
        "_5364": ["StraightBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5365": ["StraightBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5366": ["StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5367": ["StraightBevelSunGearCompoundModalAnalysisAtASpeed"],
        "_5368": ["SynchroniserCompoundModalAnalysisAtASpeed"],
        "_5369": ["SynchroniserHalfCompoundModalAnalysisAtASpeed"],
        "_5370": ["SynchroniserPartCompoundModalAnalysisAtASpeed"],
        "_5371": ["SynchroniserSleeveCompoundModalAnalysisAtASpeed"],
        "_5372": ["TorqueConverterCompoundModalAnalysisAtASpeed"],
        "_5373": ["TorqueConverterConnectionCompoundModalAnalysisAtASpeed"],
        "_5374": ["TorqueConverterPumpCompoundModalAnalysisAtASpeed"],
        "_5375": ["TorqueConverterTurbineCompoundModalAnalysisAtASpeed"],
        "_5376": ["UnbalancedMassCompoundModalAnalysisAtASpeed"],
        "_5377": ["VirtualComponentCompoundModalAnalysisAtASpeed"],
        "_5378": ["WormGearCompoundModalAnalysisAtASpeed"],
        "_5379": ["WormGearMeshCompoundModalAnalysisAtASpeed"],
        "_5380": ["WormGearSetCompoundModalAnalysisAtASpeed"],
        "_5381": ["ZerolBevelGearCompoundModalAnalysisAtASpeed"],
        "_5382": ["ZerolBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5383": ["ZerolBevelGearSetCompoundModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
    "AbstractShaftCompoundModalAnalysisAtASpeed",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    "AssemblyCompoundModalAnalysisAtASpeed",
    "BearingCompoundModalAnalysisAtASpeed",
    "BeltConnectionCompoundModalAnalysisAtASpeed",
    "BeltDriveCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearSetCompoundModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialSunGearCompoundModalAnalysisAtASpeed",
    "BevelGearCompoundModalAnalysisAtASpeed",
    "BevelGearMeshCompoundModalAnalysisAtASpeed",
    "BevelGearSetCompoundModalAnalysisAtASpeed",
    "BoltCompoundModalAnalysisAtASpeed",
    "BoltedJointCompoundModalAnalysisAtASpeed",
    "ClutchCompoundModalAnalysisAtASpeed",
    "ClutchConnectionCompoundModalAnalysisAtASpeed",
    "ClutchHalfCompoundModalAnalysisAtASpeed",
    "CoaxialConnectionCompoundModalAnalysisAtASpeed",
    "ComponentCompoundModalAnalysisAtASpeed",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
    "ConceptCouplingConnectionCompoundModalAnalysisAtASpeed",
    "ConceptCouplingHalfCompoundModalAnalysisAtASpeed",
    "ConceptGearCompoundModalAnalysisAtASpeed",
    "ConceptGearMeshCompoundModalAnalysisAtASpeed",
    "ConceptGearSetCompoundModalAnalysisAtASpeed",
    "ConicalGearCompoundModalAnalysisAtASpeed",
    "ConicalGearMeshCompoundModalAnalysisAtASpeed",
    "ConicalGearSetCompoundModalAnalysisAtASpeed",
    "ConnectionCompoundModalAnalysisAtASpeed",
    "ConnectorCompoundModalAnalysisAtASpeed",
    "CouplingCompoundModalAnalysisAtASpeed",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
    "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
    "CVTCompoundModalAnalysisAtASpeed",
    "CVTPulleyCompoundModalAnalysisAtASpeed",
    "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    "CylindricalGearCompoundModalAnalysisAtASpeed",
    "CylindricalGearMeshCompoundModalAnalysisAtASpeed",
    "CylindricalGearSetCompoundModalAnalysisAtASpeed",
    "CylindricalPlanetGearCompoundModalAnalysisAtASpeed",
    "DatumCompoundModalAnalysisAtASpeed",
    "ExternalCADModelCompoundModalAnalysisAtASpeed",
    "FaceGearCompoundModalAnalysisAtASpeed",
    "FaceGearMeshCompoundModalAnalysisAtASpeed",
    "FaceGearSetCompoundModalAnalysisAtASpeed",
    "FEPartCompoundModalAnalysisAtASpeed",
    "FlexiblePinAssemblyCompoundModalAnalysisAtASpeed",
    "GearCompoundModalAnalysisAtASpeed",
    "GearMeshCompoundModalAnalysisAtASpeed",
    "GearSetCompoundModalAnalysisAtASpeed",
    "GuideDxfModelCompoundModalAnalysisAtASpeed",
    "HypoidGearCompoundModalAnalysisAtASpeed",
    "HypoidGearMeshCompoundModalAnalysisAtASpeed",
    "HypoidGearSetCompoundModalAnalysisAtASpeed",
    "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "MassDiscCompoundModalAnalysisAtASpeed",
    "MeasurementComponentCompoundModalAnalysisAtASpeed",
    "MountableComponentCompoundModalAnalysisAtASpeed",
    "OilSealCompoundModalAnalysisAtASpeed",
    "PartCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    "PlanetaryConnectionCompoundModalAnalysisAtASpeed",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
    "PlanetCarrierCompoundModalAnalysisAtASpeed",
    "PointLoadCompoundModalAnalysisAtASpeed",
    "PowerLoadCompoundModalAnalysisAtASpeed",
    "PulleyCompoundModalAnalysisAtASpeed",
    "RingPinsCompoundModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed",
    "RollingRingAssemblyCompoundModalAnalysisAtASpeed",
    "RollingRingCompoundModalAnalysisAtASpeed",
    "RollingRingConnectionCompoundModalAnalysisAtASpeed",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
    "ShaftCompoundModalAnalysisAtASpeed",
    "ShaftHubConnectionCompoundModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "SpringDamperCompoundModalAnalysisAtASpeed",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelGearCompoundModalAnalysisAtASpeed",
    "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
    "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
    "SynchroniserCompoundModalAnalysisAtASpeed",
    "SynchroniserHalfCompoundModalAnalysisAtASpeed",
    "SynchroniserPartCompoundModalAnalysisAtASpeed",
    "SynchroniserSleeveCompoundModalAnalysisAtASpeed",
    "TorqueConverterCompoundModalAnalysisAtASpeed",
    "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
    "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
    "TorqueConverterTurbineCompoundModalAnalysisAtASpeed",
    "UnbalancedMassCompoundModalAnalysisAtASpeed",
    "VirtualComponentCompoundModalAnalysisAtASpeed",
    "WormGearCompoundModalAnalysisAtASpeed",
    "WormGearMeshCompoundModalAnalysisAtASpeed",
    "WormGearSetCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearMeshCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
)
