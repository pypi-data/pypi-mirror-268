"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7414 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7415 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7416 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7417 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7418 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7419 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7420 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7421 import AssemblyCompoundAdvancedSystemDeflection
    from ._7422 import BearingCompoundAdvancedSystemDeflection
    from ._7423 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7424 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7425 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7426 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7427 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7428 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7429 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7430 import BevelGearCompoundAdvancedSystemDeflection
    from ._7431 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7432 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7433 import BoltCompoundAdvancedSystemDeflection
    from ._7434 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7435 import ClutchCompoundAdvancedSystemDeflection
    from ._7436 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7437 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7438 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7439 import ComponentCompoundAdvancedSystemDeflection
    from ._7440 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7441 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7442 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7443 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7444 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7445 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7446 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7447 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7448 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7449 import ConnectionCompoundAdvancedSystemDeflection
    from ._7450 import ConnectorCompoundAdvancedSystemDeflection
    from ._7451 import CouplingCompoundAdvancedSystemDeflection
    from ._7452 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7453 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7454 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7455 import CVTCompoundAdvancedSystemDeflection
    from ._7456 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7457 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7458 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7459 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7460 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7461 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7462 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7463 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7464 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7465 import DatumCompoundAdvancedSystemDeflection
    from ._7466 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7467 import FaceGearCompoundAdvancedSystemDeflection
    from ._7468 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7469 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7470 import FEPartCompoundAdvancedSystemDeflection
    from ._7471 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7472 import GearCompoundAdvancedSystemDeflection
    from ._7473 import GearMeshCompoundAdvancedSystemDeflection
    from ._7474 import GearSetCompoundAdvancedSystemDeflection
    from ._7475 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7476 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7477 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7478 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7479 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7480 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection,
    )
    from ._7481 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7482 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7483 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection,
    )
    from ._7484 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7485 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7486 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection,
    )
    from ._7487 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7488 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7489 import MassDiscCompoundAdvancedSystemDeflection
    from ._7490 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7491 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7492 import OilSealCompoundAdvancedSystemDeflection
    from ._7493 import PartCompoundAdvancedSystemDeflection
    from ._7494 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7495 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7496 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7497 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7498 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7499 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7500 import PointLoadCompoundAdvancedSystemDeflection
    from ._7501 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7502 import PulleyCompoundAdvancedSystemDeflection
    from ._7503 import RingPinsCompoundAdvancedSystemDeflection
    from ._7504 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7505 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7506 import RollingRingCompoundAdvancedSystemDeflection
    from ._7507 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7508 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7509 import ShaftCompoundAdvancedSystemDeflection
    from ._7510 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7511 import (
        ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7512 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7513 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7514 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7515 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7516 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7517 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7518 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7519 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7520 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7521 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7522 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7523 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7524 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7525 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7526 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7527 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7528 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7529 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7530 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7531 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7532 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7533 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7534 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7535 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7536 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7537 import WormGearCompoundAdvancedSystemDeflection
    from ._7538 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7539 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7540 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7541 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7542 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        "_7414": ["AbstractAssemblyCompoundAdvancedSystemDeflection"],
        "_7415": ["AbstractShaftCompoundAdvancedSystemDeflection"],
        "_7416": ["AbstractShaftOrHousingCompoundAdvancedSystemDeflection"],
        "_7417": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7418": ["AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"],
        "_7419": ["AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7420": ["AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7421": ["AssemblyCompoundAdvancedSystemDeflection"],
        "_7422": ["BearingCompoundAdvancedSystemDeflection"],
        "_7423": ["BeltConnectionCompoundAdvancedSystemDeflection"],
        "_7424": ["BeltDriveCompoundAdvancedSystemDeflection"],
        "_7425": ["BevelDifferentialGearCompoundAdvancedSystemDeflection"],
        "_7426": ["BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"],
        "_7427": ["BevelDifferentialGearSetCompoundAdvancedSystemDeflection"],
        "_7428": ["BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection"],
        "_7429": ["BevelDifferentialSunGearCompoundAdvancedSystemDeflection"],
        "_7430": ["BevelGearCompoundAdvancedSystemDeflection"],
        "_7431": ["BevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7432": ["BevelGearSetCompoundAdvancedSystemDeflection"],
        "_7433": ["BoltCompoundAdvancedSystemDeflection"],
        "_7434": ["BoltedJointCompoundAdvancedSystemDeflection"],
        "_7435": ["ClutchCompoundAdvancedSystemDeflection"],
        "_7436": ["ClutchConnectionCompoundAdvancedSystemDeflection"],
        "_7437": ["ClutchHalfCompoundAdvancedSystemDeflection"],
        "_7438": ["CoaxialConnectionCompoundAdvancedSystemDeflection"],
        "_7439": ["ComponentCompoundAdvancedSystemDeflection"],
        "_7440": ["ConceptCouplingCompoundAdvancedSystemDeflection"],
        "_7441": ["ConceptCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7442": ["ConceptCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7443": ["ConceptGearCompoundAdvancedSystemDeflection"],
        "_7444": ["ConceptGearMeshCompoundAdvancedSystemDeflection"],
        "_7445": ["ConceptGearSetCompoundAdvancedSystemDeflection"],
        "_7446": ["ConicalGearCompoundAdvancedSystemDeflection"],
        "_7447": ["ConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7448": ["ConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7449": ["ConnectionCompoundAdvancedSystemDeflection"],
        "_7450": ["ConnectorCompoundAdvancedSystemDeflection"],
        "_7451": ["CouplingCompoundAdvancedSystemDeflection"],
        "_7452": ["CouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7453": ["CouplingHalfCompoundAdvancedSystemDeflection"],
        "_7454": ["CVTBeltConnectionCompoundAdvancedSystemDeflection"],
        "_7455": ["CVTCompoundAdvancedSystemDeflection"],
        "_7456": ["CVTPulleyCompoundAdvancedSystemDeflection"],
        "_7457": ["CycloidalAssemblyCompoundAdvancedSystemDeflection"],
        "_7458": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7459": ["CycloidalDiscCompoundAdvancedSystemDeflection"],
        "_7460": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7461": ["CylindricalGearCompoundAdvancedSystemDeflection"],
        "_7462": ["CylindricalGearMeshCompoundAdvancedSystemDeflection"],
        "_7463": ["CylindricalGearSetCompoundAdvancedSystemDeflection"],
        "_7464": ["CylindricalPlanetGearCompoundAdvancedSystemDeflection"],
        "_7465": ["DatumCompoundAdvancedSystemDeflection"],
        "_7466": ["ExternalCADModelCompoundAdvancedSystemDeflection"],
        "_7467": ["FaceGearCompoundAdvancedSystemDeflection"],
        "_7468": ["FaceGearMeshCompoundAdvancedSystemDeflection"],
        "_7469": ["FaceGearSetCompoundAdvancedSystemDeflection"],
        "_7470": ["FEPartCompoundAdvancedSystemDeflection"],
        "_7471": ["FlexiblePinAssemblyCompoundAdvancedSystemDeflection"],
        "_7472": ["GearCompoundAdvancedSystemDeflection"],
        "_7473": ["GearMeshCompoundAdvancedSystemDeflection"],
        "_7474": ["GearSetCompoundAdvancedSystemDeflection"],
        "_7475": ["GuideDxfModelCompoundAdvancedSystemDeflection"],
        "_7476": ["HypoidGearCompoundAdvancedSystemDeflection"],
        "_7477": ["HypoidGearMeshCompoundAdvancedSystemDeflection"],
        "_7478": ["HypoidGearSetCompoundAdvancedSystemDeflection"],
        "_7479": ["InterMountableComponentConnectionCompoundAdvancedSystemDeflection"],
        "_7480": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ],
        "_7481": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7482": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7483": ["KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"],
        "_7484": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7485": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7486": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
        ],
        "_7487": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7488": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7489": ["MassDiscCompoundAdvancedSystemDeflection"],
        "_7490": ["MeasurementComponentCompoundAdvancedSystemDeflection"],
        "_7491": ["MountableComponentCompoundAdvancedSystemDeflection"],
        "_7492": ["OilSealCompoundAdvancedSystemDeflection"],
        "_7493": ["PartCompoundAdvancedSystemDeflection"],
        "_7494": ["PartToPartShearCouplingCompoundAdvancedSystemDeflection"],
        "_7495": ["PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7496": ["PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7497": ["PlanetaryConnectionCompoundAdvancedSystemDeflection"],
        "_7498": ["PlanetaryGearSetCompoundAdvancedSystemDeflection"],
        "_7499": ["PlanetCarrierCompoundAdvancedSystemDeflection"],
        "_7500": ["PointLoadCompoundAdvancedSystemDeflection"],
        "_7501": ["PowerLoadCompoundAdvancedSystemDeflection"],
        "_7502": ["PulleyCompoundAdvancedSystemDeflection"],
        "_7503": ["RingPinsCompoundAdvancedSystemDeflection"],
        "_7504": ["RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"],
        "_7505": ["RollingRingAssemblyCompoundAdvancedSystemDeflection"],
        "_7506": ["RollingRingCompoundAdvancedSystemDeflection"],
        "_7507": ["RollingRingConnectionCompoundAdvancedSystemDeflection"],
        "_7508": ["RootAssemblyCompoundAdvancedSystemDeflection"],
        "_7509": ["ShaftCompoundAdvancedSystemDeflection"],
        "_7510": ["ShaftHubConnectionCompoundAdvancedSystemDeflection"],
        "_7511": [
            "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7512": ["SpecialisedAssemblyCompoundAdvancedSystemDeflection"],
        "_7513": ["SpiralBevelGearCompoundAdvancedSystemDeflection"],
        "_7514": ["SpiralBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7515": ["SpiralBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7516": ["SpringDamperCompoundAdvancedSystemDeflection"],
        "_7517": ["SpringDamperConnectionCompoundAdvancedSystemDeflection"],
        "_7518": ["SpringDamperHalfCompoundAdvancedSystemDeflection"],
        "_7519": ["StraightBevelDiffGearCompoundAdvancedSystemDeflection"],
        "_7520": ["StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"],
        "_7521": ["StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"],
        "_7522": ["StraightBevelGearCompoundAdvancedSystemDeflection"],
        "_7523": ["StraightBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7524": ["StraightBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7525": ["StraightBevelPlanetGearCompoundAdvancedSystemDeflection"],
        "_7526": ["StraightBevelSunGearCompoundAdvancedSystemDeflection"],
        "_7527": ["SynchroniserCompoundAdvancedSystemDeflection"],
        "_7528": ["SynchroniserHalfCompoundAdvancedSystemDeflection"],
        "_7529": ["SynchroniserPartCompoundAdvancedSystemDeflection"],
        "_7530": ["SynchroniserSleeveCompoundAdvancedSystemDeflection"],
        "_7531": ["TorqueConverterCompoundAdvancedSystemDeflection"],
        "_7532": ["TorqueConverterConnectionCompoundAdvancedSystemDeflection"],
        "_7533": ["TorqueConverterPumpCompoundAdvancedSystemDeflection"],
        "_7534": ["TorqueConverterTurbineCompoundAdvancedSystemDeflection"],
        "_7535": ["UnbalancedMassCompoundAdvancedSystemDeflection"],
        "_7536": ["VirtualComponentCompoundAdvancedSystemDeflection"],
        "_7537": ["WormGearCompoundAdvancedSystemDeflection"],
        "_7538": ["WormGearMeshCompoundAdvancedSystemDeflection"],
        "_7539": ["WormGearSetCompoundAdvancedSystemDeflection"],
        "_7540": ["ZerolBevelGearCompoundAdvancedSystemDeflection"],
        "_7541": ["ZerolBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7542": ["ZerolBevelGearSetCompoundAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedSystemDeflection",
    "AbstractShaftCompoundAdvancedSystemDeflection",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    "AssemblyCompoundAdvancedSystemDeflection",
    "BearingCompoundAdvancedSystemDeflection",
    "BeltConnectionCompoundAdvancedSystemDeflection",
    "BeltDriveCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
    "BevelGearCompoundAdvancedSystemDeflection",
    "BevelGearMeshCompoundAdvancedSystemDeflection",
    "BevelGearSetCompoundAdvancedSystemDeflection",
    "BoltCompoundAdvancedSystemDeflection",
    "BoltedJointCompoundAdvancedSystemDeflection",
    "ClutchCompoundAdvancedSystemDeflection",
    "ClutchConnectionCompoundAdvancedSystemDeflection",
    "ClutchHalfCompoundAdvancedSystemDeflection",
    "CoaxialConnectionCompoundAdvancedSystemDeflection",
    "ComponentCompoundAdvancedSystemDeflection",
    "ConceptCouplingCompoundAdvancedSystemDeflection",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
    "ConceptGearCompoundAdvancedSystemDeflection",
    "ConceptGearMeshCompoundAdvancedSystemDeflection",
    "ConceptGearSetCompoundAdvancedSystemDeflection",
    "ConicalGearCompoundAdvancedSystemDeflection",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
    "ConnectionCompoundAdvancedSystemDeflection",
    "ConnectorCompoundAdvancedSystemDeflection",
    "CouplingCompoundAdvancedSystemDeflection",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
    "CouplingHalfCompoundAdvancedSystemDeflection",
    "CVTBeltConnectionCompoundAdvancedSystemDeflection",
    "CVTCompoundAdvancedSystemDeflection",
    "CVTPulleyCompoundAdvancedSystemDeflection",
    "CycloidalAssemblyCompoundAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    "CycloidalDiscCompoundAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
    "CylindricalGearCompoundAdvancedSystemDeflection",
    "CylindricalGearMeshCompoundAdvancedSystemDeflection",
    "CylindricalGearSetCompoundAdvancedSystemDeflection",
    "CylindricalPlanetGearCompoundAdvancedSystemDeflection",
    "DatumCompoundAdvancedSystemDeflection",
    "ExternalCADModelCompoundAdvancedSystemDeflection",
    "FaceGearCompoundAdvancedSystemDeflection",
    "FaceGearMeshCompoundAdvancedSystemDeflection",
    "FaceGearSetCompoundAdvancedSystemDeflection",
    "FEPartCompoundAdvancedSystemDeflection",
    "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
    "GearCompoundAdvancedSystemDeflection",
    "GearMeshCompoundAdvancedSystemDeflection",
    "GearSetCompoundAdvancedSystemDeflection",
    "GuideDxfModelCompoundAdvancedSystemDeflection",
    "HypoidGearCompoundAdvancedSystemDeflection",
    "HypoidGearMeshCompoundAdvancedSystemDeflection",
    "HypoidGearSetCompoundAdvancedSystemDeflection",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "MassDiscCompoundAdvancedSystemDeflection",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
    "MountableComponentCompoundAdvancedSystemDeflection",
    "OilSealCompoundAdvancedSystemDeflection",
    "PartCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection",
    "PlanetaryConnectionCompoundAdvancedSystemDeflection",
    "PlanetaryGearSetCompoundAdvancedSystemDeflection",
    "PlanetCarrierCompoundAdvancedSystemDeflection",
    "PointLoadCompoundAdvancedSystemDeflection",
    "PowerLoadCompoundAdvancedSystemDeflection",
    "PulleyCompoundAdvancedSystemDeflection",
    "RingPinsCompoundAdvancedSystemDeflection",
    "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
    "RollingRingAssemblyCompoundAdvancedSystemDeflection",
    "RollingRingCompoundAdvancedSystemDeflection",
    "RollingRingConnectionCompoundAdvancedSystemDeflection",
    "RootAssemblyCompoundAdvancedSystemDeflection",
    "ShaftCompoundAdvancedSystemDeflection",
    "ShaftHubConnectionCompoundAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
    "SpiralBevelGearCompoundAdvancedSystemDeflection",
    "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "SpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "SpringDamperCompoundAdvancedSystemDeflection",
    "SpringDamperConnectionCompoundAdvancedSystemDeflection",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelGearCompoundAdvancedSystemDeflection",
    "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
    "SynchroniserCompoundAdvancedSystemDeflection",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
    "SynchroniserPartCompoundAdvancedSystemDeflection",
    "SynchroniserSleeveCompoundAdvancedSystemDeflection",
    "TorqueConverterCompoundAdvancedSystemDeflection",
    "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
    "TorqueConverterPumpCompoundAdvancedSystemDeflection",
    "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
    "UnbalancedMassCompoundAdvancedSystemDeflection",
    "VirtualComponentCompoundAdvancedSystemDeflection",
    "WormGearCompoundAdvancedSystemDeflection",
    "WormGearMeshCompoundAdvancedSystemDeflection",
    "WormGearSetCompoundAdvancedSystemDeflection",
    "ZerolBevelGearCompoundAdvancedSystemDeflection",
    "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
    "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
)
