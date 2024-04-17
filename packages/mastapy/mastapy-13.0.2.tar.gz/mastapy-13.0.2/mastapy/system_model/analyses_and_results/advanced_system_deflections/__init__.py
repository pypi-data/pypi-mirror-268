"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7278 import AbstractAssemblyAdvancedSystemDeflection
    from ._7279 import AbstractShaftAdvancedSystemDeflection
    from ._7280 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7281 import (
        AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection,
    )
    from ._7282 import AdvancedSystemDeflection
    from ._7283 import AdvancedSystemDeflectionOptions
    from ._7284 import AdvancedSystemDeflectionSubAnalysis
    from ._7285 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7286 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7287 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7288 import AssemblyAdvancedSystemDeflection
    from ._7289 import BearingAdvancedSystemDeflection
    from ._7290 import BeltConnectionAdvancedSystemDeflection
    from ._7291 import BeltDriveAdvancedSystemDeflection
    from ._7292 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7293 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7294 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7295 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7296 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7297 import BevelGearAdvancedSystemDeflection
    from ._7298 import BevelGearMeshAdvancedSystemDeflection
    from ._7299 import BevelGearSetAdvancedSystemDeflection
    from ._7300 import BoltAdvancedSystemDeflection
    from ._7301 import BoltedJointAdvancedSystemDeflection
    from ._7302 import ClutchAdvancedSystemDeflection
    from ._7303 import ClutchConnectionAdvancedSystemDeflection
    from ._7304 import ClutchHalfAdvancedSystemDeflection
    from ._7305 import CoaxialConnectionAdvancedSystemDeflection
    from ._7306 import ComponentAdvancedSystemDeflection
    from ._7307 import ConceptCouplingAdvancedSystemDeflection
    from ._7308 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7309 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7310 import ConceptGearAdvancedSystemDeflection
    from ._7311 import ConceptGearMeshAdvancedSystemDeflection
    from ._7312 import ConceptGearSetAdvancedSystemDeflection
    from ._7313 import ConicalGearAdvancedSystemDeflection
    from ._7314 import ConicalGearMeshAdvancedSystemDeflection
    from ._7315 import ConicalGearSetAdvancedSystemDeflection
    from ._7316 import ConnectionAdvancedSystemDeflection
    from ._7317 import ConnectorAdvancedSystemDeflection
    from ._7318 import ContactChartPerToothPass
    from ._7319 import CouplingAdvancedSystemDeflection
    from ._7320 import CouplingConnectionAdvancedSystemDeflection
    from ._7321 import CouplingHalfAdvancedSystemDeflection
    from ._7322 import CVTAdvancedSystemDeflection
    from ._7323 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7324 import CVTPulleyAdvancedSystemDeflection
    from ._7325 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7326 import CycloidalDiscAdvancedSystemDeflection
    from ._7327 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7328 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7329 import CylindricalGearAdvancedSystemDeflection
    from ._7330 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7331 import CylindricalGearSetAdvancedSystemDeflection
    from ._7332 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7333 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7334 import DatumAdvancedSystemDeflection
    from ._7335 import ExternalCADModelAdvancedSystemDeflection
    from ._7336 import FaceGearAdvancedSystemDeflection
    from ._7337 import FaceGearMeshAdvancedSystemDeflection
    from ._7338 import FaceGearSetAdvancedSystemDeflection
    from ._7339 import FEPartAdvancedSystemDeflection
    from ._7340 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7341 import GearAdvancedSystemDeflection
    from ._7342 import GearMeshAdvancedSystemDeflection
    from ._7343 import GearSetAdvancedSystemDeflection
    from ._7344 import GuideDxfModelAdvancedSystemDeflection
    from ._7345 import HypoidGearAdvancedSystemDeflection
    from ._7346 import HypoidGearMeshAdvancedSystemDeflection
    from ._7347 import HypoidGearSetAdvancedSystemDeflection
    from ._7348 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7349 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7350 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7351 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7352 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7353 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7354 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7355 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7356 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection,
    )
    from ._7357 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection,
    )
    from ._7358 import UseLtcaInAsdOption
    from ._7359 import MassDiscAdvancedSystemDeflection
    from ._7360 import MeasurementComponentAdvancedSystemDeflection
    from ._7361 import MountableComponentAdvancedSystemDeflection
    from ._7362 import OilSealAdvancedSystemDeflection
    from ._7363 import PartAdvancedSystemDeflection
    from ._7364 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7365 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7366 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7367 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7368 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7369 import PlanetCarrierAdvancedSystemDeflection
    from ._7370 import PointLoadAdvancedSystemDeflection
    from ._7371 import PowerLoadAdvancedSystemDeflection
    from ._7372 import PulleyAdvancedSystemDeflection
    from ._7373 import RingPinsAdvancedSystemDeflection
    from ._7374 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7375 import RollingRingAdvancedSystemDeflection
    from ._7376 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7377 import RollingRingConnectionAdvancedSystemDeflection
    from ._7378 import RootAssemblyAdvancedSystemDeflection
    from ._7379 import ShaftAdvancedSystemDeflection
    from ._7380 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7381 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7382 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7383 import SpiralBevelGearAdvancedSystemDeflection
    from ._7384 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7385 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7386 import SpringDamperAdvancedSystemDeflection
    from ._7387 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7388 import SpringDamperHalfAdvancedSystemDeflection
    from ._7389 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7390 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7391 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7392 import StraightBevelGearAdvancedSystemDeflection
    from ._7393 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7394 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7395 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7396 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7397 import SynchroniserAdvancedSystemDeflection
    from ._7398 import SynchroniserHalfAdvancedSystemDeflection
    from ._7399 import SynchroniserPartAdvancedSystemDeflection
    from ._7400 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7401 import TorqueConverterAdvancedSystemDeflection
    from ._7402 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7403 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7404 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7405 import TransmissionErrorToOtherPowerLoad
    from ._7406 import UnbalancedMassAdvancedSystemDeflection
    from ._7407 import VirtualComponentAdvancedSystemDeflection
    from ._7408 import WormGearAdvancedSystemDeflection
    from ._7409 import WormGearMeshAdvancedSystemDeflection
    from ._7410 import WormGearSetAdvancedSystemDeflection
    from ._7411 import ZerolBevelGearAdvancedSystemDeflection
    from ._7412 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7413 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        "_7278": ["AbstractAssemblyAdvancedSystemDeflection"],
        "_7279": ["AbstractShaftAdvancedSystemDeflection"],
        "_7280": ["AbstractShaftOrHousingAdvancedSystemDeflection"],
        "_7281": [
            "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ],
        "_7282": ["AdvancedSystemDeflection"],
        "_7283": ["AdvancedSystemDeflectionOptions"],
        "_7284": ["AdvancedSystemDeflectionSubAnalysis"],
        "_7285": ["AGMAGleasonConicalGearAdvancedSystemDeflection"],
        "_7286": ["AGMAGleasonConicalGearMeshAdvancedSystemDeflection"],
        "_7287": ["AGMAGleasonConicalGearSetAdvancedSystemDeflection"],
        "_7288": ["AssemblyAdvancedSystemDeflection"],
        "_7289": ["BearingAdvancedSystemDeflection"],
        "_7290": ["BeltConnectionAdvancedSystemDeflection"],
        "_7291": ["BeltDriveAdvancedSystemDeflection"],
        "_7292": ["BevelDifferentialGearAdvancedSystemDeflection"],
        "_7293": ["BevelDifferentialGearMeshAdvancedSystemDeflection"],
        "_7294": ["BevelDifferentialGearSetAdvancedSystemDeflection"],
        "_7295": ["BevelDifferentialPlanetGearAdvancedSystemDeflection"],
        "_7296": ["BevelDifferentialSunGearAdvancedSystemDeflection"],
        "_7297": ["BevelGearAdvancedSystemDeflection"],
        "_7298": ["BevelGearMeshAdvancedSystemDeflection"],
        "_7299": ["BevelGearSetAdvancedSystemDeflection"],
        "_7300": ["BoltAdvancedSystemDeflection"],
        "_7301": ["BoltedJointAdvancedSystemDeflection"],
        "_7302": ["ClutchAdvancedSystemDeflection"],
        "_7303": ["ClutchConnectionAdvancedSystemDeflection"],
        "_7304": ["ClutchHalfAdvancedSystemDeflection"],
        "_7305": ["CoaxialConnectionAdvancedSystemDeflection"],
        "_7306": ["ComponentAdvancedSystemDeflection"],
        "_7307": ["ConceptCouplingAdvancedSystemDeflection"],
        "_7308": ["ConceptCouplingConnectionAdvancedSystemDeflection"],
        "_7309": ["ConceptCouplingHalfAdvancedSystemDeflection"],
        "_7310": ["ConceptGearAdvancedSystemDeflection"],
        "_7311": ["ConceptGearMeshAdvancedSystemDeflection"],
        "_7312": ["ConceptGearSetAdvancedSystemDeflection"],
        "_7313": ["ConicalGearAdvancedSystemDeflection"],
        "_7314": ["ConicalGearMeshAdvancedSystemDeflection"],
        "_7315": ["ConicalGearSetAdvancedSystemDeflection"],
        "_7316": ["ConnectionAdvancedSystemDeflection"],
        "_7317": ["ConnectorAdvancedSystemDeflection"],
        "_7318": ["ContactChartPerToothPass"],
        "_7319": ["CouplingAdvancedSystemDeflection"],
        "_7320": ["CouplingConnectionAdvancedSystemDeflection"],
        "_7321": ["CouplingHalfAdvancedSystemDeflection"],
        "_7322": ["CVTAdvancedSystemDeflection"],
        "_7323": ["CVTBeltConnectionAdvancedSystemDeflection"],
        "_7324": ["CVTPulleyAdvancedSystemDeflection"],
        "_7325": ["CycloidalAssemblyAdvancedSystemDeflection"],
        "_7326": ["CycloidalDiscAdvancedSystemDeflection"],
        "_7327": ["CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"],
        "_7328": ["CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection"],
        "_7329": ["CylindricalGearAdvancedSystemDeflection"],
        "_7330": ["CylindricalGearMeshAdvancedSystemDeflection"],
        "_7331": ["CylindricalGearSetAdvancedSystemDeflection"],
        "_7332": ["CylindricalMeshedGearAdvancedSystemDeflection"],
        "_7333": ["CylindricalPlanetGearAdvancedSystemDeflection"],
        "_7334": ["DatumAdvancedSystemDeflection"],
        "_7335": ["ExternalCADModelAdvancedSystemDeflection"],
        "_7336": ["FaceGearAdvancedSystemDeflection"],
        "_7337": ["FaceGearMeshAdvancedSystemDeflection"],
        "_7338": ["FaceGearSetAdvancedSystemDeflection"],
        "_7339": ["FEPartAdvancedSystemDeflection"],
        "_7340": ["FlexiblePinAssemblyAdvancedSystemDeflection"],
        "_7341": ["GearAdvancedSystemDeflection"],
        "_7342": ["GearMeshAdvancedSystemDeflection"],
        "_7343": ["GearSetAdvancedSystemDeflection"],
        "_7344": ["GuideDxfModelAdvancedSystemDeflection"],
        "_7345": ["HypoidGearAdvancedSystemDeflection"],
        "_7346": ["HypoidGearMeshAdvancedSystemDeflection"],
        "_7347": ["HypoidGearSetAdvancedSystemDeflection"],
        "_7348": ["InterMountableComponentConnectionAdvancedSystemDeflection"],
        "_7349": ["KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"],
        "_7350": ["KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"],
        "_7351": ["KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"],
        "_7352": ["KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection"],
        "_7353": ["KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection"],
        "_7354": ["KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection"],
        "_7355": ["KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection"],
        "_7356": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ],
        "_7357": ["KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"],
        "_7358": ["UseLtcaInAsdOption"],
        "_7359": ["MassDiscAdvancedSystemDeflection"],
        "_7360": ["MeasurementComponentAdvancedSystemDeflection"],
        "_7361": ["MountableComponentAdvancedSystemDeflection"],
        "_7362": ["OilSealAdvancedSystemDeflection"],
        "_7363": ["PartAdvancedSystemDeflection"],
        "_7364": ["PartToPartShearCouplingAdvancedSystemDeflection"],
        "_7365": ["PartToPartShearCouplingConnectionAdvancedSystemDeflection"],
        "_7366": ["PartToPartShearCouplingHalfAdvancedSystemDeflection"],
        "_7367": ["PlanetaryConnectionAdvancedSystemDeflection"],
        "_7368": ["PlanetaryGearSetAdvancedSystemDeflection"],
        "_7369": ["PlanetCarrierAdvancedSystemDeflection"],
        "_7370": ["PointLoadAdvancedSystemDeflection"],
        "_7371": ["PowerLoadAdvancedSystemDeflection"],
        "_7372": ["PulleyAdvancedSystemDeflection"],
        "_7373": ["RingPinsAdvancedSystemDeflection"],
        "_7374": ["RingPinsToDiscConnectionAdvancedSystemDeflection"],
        "_7375": ["RollingRingAdvancedSystemDeflection"],
        "_7376": ["RollingRingAssemblyAdvancedSystemDeflection"],
        "_7377": ["RollingRingConnectionAdvancedSystemDeflection"],
        "_7378": ["RootAssemblyAdvancedSystemDeflection"],
        "_7379": ["ShaftAdvancedSystemDeflection"],
        "_7380": ["ShaftHubConnectionAdvancedSystemDeflection"],
        "_7381": ["ShaftToMountableComponentConnectionAdvancedSystemDeflection"],
        "_7382": ["SpecialisedAssemblyAdvancedSystemDeflection"],
        "_7383": ["SpiralBevelGearAdvancedSystemDeflection"],
        "_7384": ["SpiralBevelGearMeshAdvancedSystemDeflection"],
        "_7385": ["SpiralBevelGearSetAdvancedSystemDeflection"],
        "_7386": ["SpringDamperAdvancedSystemDeflection"],
        "_7387": ["SpringDamperConnectionAdvancedSystemDeflection"],
        "_7388": ["SpringDamperHalfAdvancedSystemDeflection"],
        "_7389": ["StraightBevelDiffGearAdvancedSystemDeflection"],
        "_7390": ["StraightBevelDiffGearMeshAdvancedSystemDeflection"],
        "_7391": ["StraightBevelDiffGearSetAdvancedSystemDeflection"],
        "_7392": ["StraightBevelGearAdvancedSystemDeflection"],
        "_7393": ["StraightBevelGearMeshAdvancedSystemDeflection"],
        "_7394": ["StraightBevelGearSetAdvancedSystemDeflection"],
        "_7395": ["StraightBevelPlanetGearAdvancedSystemDeflection"],
        "_7396": ["StraightBevelSunGearAdvancedSystemDeflection"],
        "_7397": ["SynchroniserAdvancedSystemDeflection"],
        "_7398": ["SynchroniserHalfAdvancedSystemDeflection"],
        "_7399": ["SynchroniserPartAdvancedSystemDeflection"],
        "_7400": ["SynchroniserSleeveAdvancedSystemDeflection"],
        "_7401": ["TorqueConverterAdvancedSystemDeflection"],
        "_7402": ["TorqueConverterConnectionAdvancedSystemDeflection"],
        "_7403": ["TorqueConverterPumpAdvancedSystemDeflection"],
        "_7404": ["TorqueConverterTurbineAdvancedSystemDeflection"],
        "_7405": ["TransmissionErrorToOtherPowerLoad"],
        "_7406": ["UnbalancedMassAdvancedSystemDeflection"],
        "_7407": ["VirtualComponentAdvancedSystemDeflection"],
        "_7408": ["WormGearAdvancedSystemDeflection"],
        "_7409": ["WormGearMeshAdvancedSystemDeflection"],
        "_7410": ["WormGearSetAdvancedSystemDeflection"],
        "_7411": ["ZerolBevelGearAdvancedSystemDeflection"],
        "_7412": ["ZerolBevelGearMeshAdvancedSystemDeflection"],
        "_7413": ["ZerolBevelGearSetAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedSystemDeflection",
    "AbstractShaftAdvancedSystemDeflection",
    "AbstractShaftOrHousingAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "AdvancedSystemDeflection",
    "AdvancedSystemDeflectionOptions",
    "AdvancedSystemDeflectionSubAnalysis",
    "AGMAGleasonConicalGearAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
    "AssemblyAdvancedSystemDeflection",
    "BearingAdvancedSystemDeflection",
    "BeltConnectionAdvancedSystemDeflection",
    "BeltDriveAdvancedSystemDeflection",
    "BevelDifferentialGearAdvancedSystemDeflection",
    "BevelDifferentialGearMeshAdvancedSystemDeflection",
    "BevelDifferentialGearSetAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearAdvancedSystemDeflection",
    "BevelDifferentialSunGearAdvancedSystemDeflection",
    "BevelGearAdvancedSystemDeflection",
    "BevelGearMeshAdvancedSystemDeflection",
    "BevelGearSetAdvancedSystemDeflection",
    "BoltAdvancedSystemDeflection",
    "BoltedJointAdvancedSystemDeflection",
    "ClutchAdvancedSystemDeflection",
    "ClutchConnectionAdvancedSystemDeflection",
    "ClutchHalfAdvancedSystemDeflection",
    "CoaxialConnectionAdvancedSystemDeflection",
    "ComponentAdvancedSystemDeflection",
    "ConceptCouplingAdvancedSystemDeflection",
    "ConceptCouplingConnectionAdvancedSystemDeflection",
    "ConceptCouplingHalfAdvancedSystemDeflection",
    "ConceptGearAdvancedSystemDeflection",
    "ConceptGearMeshAdvancedSystemDeflection",
    "ConceptGearSetAdvancedSystemDeflection",
    "ConicalGearAdvancedSystemDeflection",
    "ConicalGearMeshAdvancedSystemDeflection",
    "ConicalGearSetAdvancedSystemDeflection",
    "ConnectionAdvancedSystemDeflection",
    "ConnectorAdvancedSystemDeflection",
    "ContactChartPerToothPass",
    "CouplingAdvancedSystemDeflection",
    "CouplingConnectionAdvancedSystemDeflection",
    "CouplingHalfAdvancedSystemDeflection",
    "CVTAdvancedSystemDeflection",
    "CVTBeltConnectionAdvancedSystemDeflection",
    "CVTPulleyAdvancedSystemDeflection",
    "CycloidalAssemblyAdvancedSystemDeflection",
    "CycloidalDiscAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection",
    "CylindricalGearAdvancedSystemDeflection",
    "CylindricalGearMeshAdvancedSystemDeflection",
    "CylindricalGearSetAdvancedSystemDeflection",
    "CylindricalMeshedGearAdvancedSystemDeflection",
    "CylindricalPlanetGearAdvancedSystemDeflection",
    "DatumAdvancedSystemDeflection",
    "ExternalCADModelAdvancedSystemDeflection",
    "FaceGearAdvancedSystemDeflection",
    "FaceGearMeshAdvancedSystemDeflection",
    "FaceGearSetAdvancedSystemDeflection",
    "FEPartAdvancedSystemDeflection",
    "FlexiblePinAssemblyAdvancedSystemDeflection",
    "GearAdvancedSystemDeflection",
    "GearMeshAdvancedSystemDeflection",
    "GearSetAdvancedSystemDeflection",
    "GuideDxfModelAdvancedSystemDeflection",
    "HypoidGearAdvancedSystemDeflection",
    "HypoidGearMeshAdvancedSystemDeflection",
    "HypoidGearSetAdvancedSystemDeflection",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    "UseLtcaInAsdOption",
    "MassDiscAdvancedSystemDeflection",
    "MeasurementComponentAdvancedSystemDeflection",
    "MountableComponentAdvancedSystemDeflection",
    "OilSealAdvancedSystemDeflection",
    "PartAdvancedSystemDeflection",
    "PartToPartShearCouplingAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfAdvancedSystemDeflection",
    "PlanetaryConnectionAdvancedSystemDeflection",
    "PlanetaryGearSetAdvancedSystemDeflection",
    "PlanetCarrierAdvancedSystemDeflection",
    "PointLoadAdvancedSystemDeflection",
    "PowerLoadAdvancedSystemDeflection",
    "PulleyAdvancedSystemDeflection",
    "RingPinsAdvancedSystemDeflection",
    "RingPinsToDiscConnectionAdvancedSystemDeflection",
    "RollingRingAdvancedSystemDeflection",
    "RollingRingAssemblyAdvancedSystemDeflection",
    "RollingRingConnectionAdvancedSystemDeflection",
    "RootAssemblyAdvancedSystemDeflection",
    "ShaftAdvancedSystemDeflection",
    "ShaftHubConnectionAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "SpecialisedAssemblyAdvancedSystemDeflection",
    "SpiralBevelGearAdvancedSystemDeflection",
    "SpiralBevelGearMeshAdvancedSystemDeflection",
    "SpiralBevelGearSetAdvancedSystemDeflection",
    "SpringDamperAdvancedSystemDeflection",
    "SpringDamperConnectionAdvancedSystemDeflection",
    "SpringDamperHalfAdvancedSystemDeflection",
    "StraightBevelDiffGearAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshAdvancedSystemDeflection",
    "StraightBevelDiffGearSetAdvancedSystemDeflection",
    "StraightBevelGearAdvancedSystemDeflection",
    "StraightBevelGearMeshAdvancedSystemDeflection",
    "StraightBevelGearSetAdvancedSystemDeflection",
    "StraightBevelPlanetGearAdvancedSystemDeflection",
    "StraightBevelSunGearAdvancedSystemDeflection",
    "SynchroniserAdvancedSystemDeflection",
    "SynchroniserHalfAdvancedSystemDeflection",
    "SynchroniserPartAdvancedSystemDeflection",
    "SynchroniserSleeveAdvancedSystemDeflection",
    "TorqueConverterAdvancedSystemDeflection",
    "TorqueConverterConnectionAdvancedSystemDeflection",
    "TorqueConverterPumpAdvancedSystemDeflection",
    "TorqueConverterTurbineAdvancedSystemDeflection",
    "TransmissionErrorToOtherPowerLoad",
    "UnbalancedMassAdvancedSystemDeflection",
    "VirtualComponentAdvancedSystemDeflection",
    "WormGearAdvancedSystemDeflection",
    "WormGearMeshAdvancedSystemDeflection",
    "WormGearSetAdvancedSystemDeflection",
    "ZerolBevelGearAdvancedSystemDeflection",
    "ZerolBevelGearMeshAdvancedSystemDeflection",
    "ZerolBevelGearSetAdvancedSystemDeflection",
)
