"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4451 import AbstractAssemblyCompoundParametricStudyTool
    from ._4452 import AbstractShaftCompoundParametricStudyTool
    from ._4453 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4454 import (
        AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool,
    )
    from ._4455 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4456 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4457 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4458 import AssemblyCompoundParametricStudyTool
    from ._4459 import BearingCompoundParametricStudyTool
    from ._4460 import BeltConnectionCompoundParametricStudyTool
    from ._4461 import BeltDriveCompoundParametricStudyTool
    from ._4462 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4463 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4464 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4465 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4466 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4467 import BevelGearCompoundParametricStudyTool
    from ._4468 import BevelGearMeshCompoundParametricStudyTool
    from ._4469 import BevelGearSetCompoundParametricStudyTool
    from ._4470 import BoltCompoundParametricStudyTool
    from ._4471 import BoltedJointCompoundParametricStudyTool
    from ._4472 import ClutchCompoundParametricStudyTool
    from ._4473 import ClutchConnectionCompoundParametricStudyTool
    from ._4474 import ClutchHalfCompoundParametricStudyTool
    from ._4475 import CoaxialConnectionCompoundParametricStudyTool
    from ._4476 import ComponentCompoundParametricStudyTool
    from ._4477 import ConceptCouplingCompoundParametricStudyTool
    from ._4478 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4479 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4480 import ConceptGearCompoundParametricStudyTool
    from ._4481 import ConceptGearMeshCompoundParametricStudyTool
    from ._4482 import ConceptGearSetCompoundParametricStudyTool
    from ._4483 import ConicalGearCompoundParametricStudyTool
    from ._4484 import ConicalGearMeshCompoundParametricStudyTool
    from ._4485 import ConicalGearSetCompoundParametricStudyTool
    from ._4486 import ConnectionCompoundParametricStudyTool
    from ._4487 import ConnectorCompoundParametricStudyTool
    from ._4488 import CouplingCompoundParametricStudyTool
    from ._4489 import CouplingConnectionCompoundParametricStudyTool
    from ._4490 import CouplingHalfCompoundParametricStudyTool
    from ._4491 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4492 import CVTCompoundParametricStudyTool
    from ._4493 import CVTPulleyCompoundParametricStudyTool
    from ._4494 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4495 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4496 import CycloidalDiscCompoundParametricStudyTool
    from ._4497 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool,
    )
    from ._4498 import CylindricalGearCompoundParametricStudyTool
    from ._4499 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4500 import CylindricalGearSetCompoundParametricStudyTool
    from ._4501 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4502 import DatumCompoundParametricStudyTool
    from ._4503 import ExternalCADModelCompoundParametricStudyTool
    from ._4504 import FaceGearCompoundParametricStudyTool
    from ._4505 import FaceGearMeshCompoundParametricStudyTool
    from ._4506 import FaceGearSetCompoundParametricStudyTool
    from ._4507 import FEPartCompoundParametricStudyTool
    from ._4508 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4509 import GearCompoundParametricStudyTool
    from ._4510 import GearMeshCompoundParametricStudyTool
    from ._4511 import GearSetCompoundParametricStudyTool
    from ._4512 import GuideDxfModelCompoundParametricStudyTool
    from ._4513 import HypoidGearCompoundParametricStudyTool
    from ._4514 import HypoidGearMeshCompoundParametricStudyTool
    from ._4515 import HypoidGearSetCompoundParametricStudyTool
    from ._4516 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4517 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4518 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool,
    )
    from ._4519 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4520 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4521 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4522 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4523 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool,
    )
    from ._4524 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool,
    )
    from ._4525 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool,
    )
    from ._4526 import MassDiscCompoundParametricStudyTool
    from ._4527 import MeasurementComponentCompoundParametricStudyTool
    from ._4528 import MountableComponentCompoundParametricStudyTool
    from ._4529 import OilSealCompoundParametricStudyTool
    from ._4530 import PartCompoundParametricStudyTool
    from ._4531 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4532 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4533 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4534 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4535 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4536 import PlanetCarrierCompoundParametricStudyTool
    from ._4537 import PointLoadCompoundParametricStudyTool
    from ._4538 import PowerLoadCompoundParametricStudyTool
    from ._4539 import PulleyCompoundParametricStudyTool
    from ._4540 import RingPinsCompoundParametricStudyTool
    from ._4541 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4542 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4543 import RollingRingCompoundParametricStudyTool
    from ._4544 import RollingRingConnectionCompoundParametricStudyTool
    from ._4545 import RootAssemblyCompoundParametricStudyTool
    from ._4546 import ShaftCompoundParametricStudyTool
    from ._4547 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4548 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4549 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4550 import SpiralBevelGearCompoundParametricStudyTool
    from ._4551 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4552 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4553 import SpringDamperCompoundParametricStudyTool
    from ._4554 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4555 import SpringDamperHalfCompoundParametricStudyTool
    from ._4556 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4557 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4558 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4559 import StraightBevelGearCompoundParametricStudyTool
    from ._4560 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4561 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4562 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4563 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4564 import SynchroniserCompoundParametricStudyTool
    from ._4565 import SynchroniserHalfCompoundParametricStudyTool
    from ._4566 import SynchroniserPartCompoundParametricStudyTool
    from ._4567 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4568 import TorqueConverterCompoundParametricStudyTool
    from ._4569 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4570 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4571 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4572 import UnbalancedMassCompoundParametricStudyTool
    from ._4573 import VirtualComponentCompoundParametricStudyTool
    from ._4574 import WormGearCompoundParametricStudyTool
    from ._4575 import WormGearMeshCompoundParametricStudyTool
    from ._4576 import WormGearSetCompoundParametricStudyTool
    from ._4577 import ZerolBevelGearCompoundParametricStudyTool
    from ._4578 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4579 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        "_4451": ["AbstractAssemblyCompoundParametricStudyTool"],
        "_4452": ["AbstractShaftCompoundParametricStudyTool"],
        "_4453": ["AbstractShaftOrHousingCompoundParametricStudyTool"],
        "_4454": [
            "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"
        ],
        "_4455": ["AGMAGleasonConicalGearCompoundParametricStudyTool"],
        "_4456": ["AGMAGleasonConicalGearMeshCompoundParametricStudyTool"],
        "_4457": ["AGMAGleasonConicalGearSetCompoundParametricStudyTool"],
        "_4458": ["AssemblyCompoundParametricStudyTool"],
        "_4459": ["BearingCompoundParametricStudyTool"],
        "_4460": ["BeltConnectionCompoundParametricStudyTool"],
        "_4461": ["BeltDriveCompoundParametricStudyTool"],
        "_4462": ["BevelDifferentialGearCompoundParametricStudyTool"],
        "_4463": ["BevelDifferentialGearMeshCompoundParametricStudyTool"],
        "_4464": ["BevelDifferentialGearSetCompoundParametricStudyTool"],
        "_4465": ["BevelDifferentialPlanetGearCompoundParametricStudyTool"],
        "_4466": ["BevelDifferentialSunGearCompoundParametricStudyTool"],
        "_4467": ["BevelGearCompoundParametricStudyTool"],
        "_4468": ["BevelGearMeshCompoundParametricStudyTool"],
        "_4469": ["BevelGearSetCompoundParametricStudyTool"],
        "_4470": ["BoltCompoundParametricStudyTool"],
        "_4471": ["BoltedJointCompoundParametricStudyTool"],
        "_4472": ["ClutchCompoundParametricStudyTool"],
        "_4473": ["ClutchConnectionCompoundParametricStudyTool"],
        "_4474": ["ClutchHalfCompoundParametricStudyTool"],
        "_4475": ["CoaxialConnectionCompoundParametricStudyTool"],
        "_4476": ["ComponentCompoundParametricStudyTool"],
        "_4477": ["ConceptCouplingCompoundParametricStudyTool"],
        "_4478": ["ConceptCouplingConnectionCompoundParametricStudyTool"],
        "_4479": ["ConceptCouplingHalfCompoundParametricStudyTool"],
        "_4480": ["ConceptGearCompoundParametricStudyTool"],
        "_4481": ["ConceptGearMeshCompoundParametricStudyTool"],
        "_4482": ["ConceptGearSetCompoundParametricStudyTool"],
        "_4483": ["ConicalGearCompoundParametricStudyTool"],
        "_4484": ["ConicalGearMeshCompoundParametricStudyTool"],
        "_4485": ["ConicalGearSetCompoundParametricStudyTool"],
        "_4486": ["ConnectionCompoundParametricStudyTool"],
        "_4487": ["ConnectorCompoundParametricStudyTool"],
        "_4488": ["CouplingCompoundParametricStudyTool"],
        "_4489": ["CouplingConnectionCompoundParametricStudyTool"],
        "_4490": ["CouplingHalfCompoundParametricStudyTool"],
        "_4491": ["CVTBeltConnectionCompoundParametricStudyTool"],
        "_4492": ["CVTCompoundParametricStudyTool"],
        "_4493": ["CVTPulleyCompoundParametricStudyTool"],
        "_4494": ["CycloidalAssemblyCompoundParametricStudyTool"],
        "_4495": ["CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"],
        "_4496": ["CycloidalDiscCompoundParametricStudyTool"],
        "_4497": ["CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool"],
        "_4498": ["CylindricalGearCompoundParametricStudyTool"],
        "_4499": ["CylindricalGearMeshCompoundParametricStudyTool"],
        "_4500": ["CylindricalGearSetCompoundParametricStudyTool"],
        "_4501": ["CylindricalPlanetGearCompoundParametricStudyTool"],
        "_4502": ["DatumCompoundParametricStudyTool"],
        "_4503": ["ExternalCADModelCompoundParametricStudyTool"],
        "_4504": ["FaceGearCompoundParametricStudyTool"],
        "_4505": ["FaceGearMeshCompoundParametricStudyTool"],
        "_4506": ["FaceGearSetCompoundParametricStudyTool"],
        "_4507": ["FEPartCompoundParametricStudyTool"],
        "_4508": ["FlexiblePinAssemblyCompoundParametricStudyTool"],
        "_4509": ["GearCompoundParametricStudyTool"],
        "_4510": ["GearMeshCompoundParametricStudyTool"],
        "_4511": ["GearSetCompoundParametricStudyTool"],
        "_4512": ["GuideDxfModelCompoundParametricStudyTool"],
        "_4513": ["HypoidGearCompoundParametricStudyTool"],
        "_4514": ["HypoidGearMeshCompoundParametricStudyTool"],
        "_4515": ["HypoidGearSetCompoundParametricStudyTool"],
        "_4516": ["InterMountableComponentConnectionCompoundParametricStudyTool"],
        "_4517": ["KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"],
        "_4518": ["KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"],
        "_4519": ["KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"],
        "_4520": ["KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"],
        "_4521": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool"],
        "_4522": ["KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"],
        "_4523": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool"],
        "_4524": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool"
        ],
        "_4525": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool"
        ],
        "_4526": ["MassDiscCompoundParametricStudyTool"],
        "_4527": ["MeasurementComponentCompoundParametricStudyTool"],
        "_4528": ["MountableComponentCompoundParametricStudyTool"],
        "_4529": ["OilSealCompoundParametricStudyTool"],
        "_4530": ["PartCompoundParametricStudyTool"],
        "_4531": ["PartToPartShearCouplingCompoundParametricStudyTool"],
        "_4532": ["PartToPartShearCouplingConnectionCompoundParametricStudyTool"],
        "_4533": ["PartToPartShearCouplingHalfCompoundParametricStudyTool"],
        "_4534": ["PlanetaryConnectionCompoundParametricStudyTool"],
        "_4535": ["PlanetaryGearSetCompoundParametricStudyTool"],
        "_4536": ["PlanetCarrierCompoundParametricStudyTool"],
        "_4537": ["PointLoadCompoundParametricStudyTool"],
        "_4538": ["PowerLoadCompoundParametricStudyTool"],
        "_4539": ["PulleyCompoundParametricStudyTool"],
        "_4540": ["RingPinsCompoundParametricStudyTool"],
        "_4541": ["RingPinsToDiscConnectionCompoundParametricStudyTool"],
        "_4542": ["RollingRingAssemblyCompoundParametricStudyTool"],
        "_4543": ["RollingRingCompoundParametricStudyTool"],
        "_4544": ["RollingRingConnectionCompoundParametricStudyTool"],
        "_4545": ["RootAssemblyCompoundParametricStudyTool"],
        "_4546": ["ShaftCompoundParametricStudyTool"],
        "_4547": ["ShaftHubConnectionCompoundParametricStudyTool"],
        "_4548": ["ShaftToMountableComponentConnectionCompoundParametricStudyTool"],
        "_4549": ["SpecialisedAssemblyCompoundParametricStudyTool"],
        "_4550": ["SpiralBevelGearCompoundParametricStudyTool"],
        "_4551": ["SpiralBevelGearMeshCompoundParametricStudyTool"],
        "_4552": ["SpiralBevelGearSetCompoundParametricStudyTool"],
        "_4553": ["SpringDamperCompoundParametricStudyTool"],
        "_4554": ["SpringDamperConnectionCompoundParametricStudyTool"],
        "_4555": ["SpringDamperHalfCompoundParametricStudyTool"],
        "_4556": ["StraightBevelDiffGearCompoundParametricStudyTool"],
        "_4557": ["StraightBevelDiffGearMeshCompoundParametricStudyTool"],
        "_4558": ["StraightBevelDiffGearSetCompoundParametricStudyTool"],
        "_4559": ["StraightBevelGearCompoundParametricStudyTool"],
        "_4560": ["StraightBevelGearMeshCompoundParametricStudyTool"],
        "_4561": ["StraightBevelGearSetCompoundParametricStudyTool"],
        "_4562": ["StraightBevelPlanetGearCompoundParametricStudyTool"],
        "_4563": ["StraightBevelSunGearCompoundParametricStudyTool"],
        "_4564": ["SynchroniserCompoundParametricStudyTool"],
        "_4565": ["SynchroniserHalfCompoundParametricStudyTool"],
        "_4566": ["SynchroniserPartCompoundParametricStudyTool"],
        "_4567": ["SynchroniserSleeveCompoundParametricStudyTool"],
        "_4568": ["TorqueConverterCompoundParametricStudyTool"],
        "_4569": ["TorqueConverterConnectionCompoundParametricStudyTool"],
        "_4570": ["TorqueConverterPumpCompoundParametricStudyTool"],
        "_4571": ["TorqueConverterTurbineCompoundParametricStudyTool"],
        "_4572": ["UnbalancedMassCompoundParametricStudyTool"],
        "_4573": ["VirtualComponentCompoundParametricStudyTool"],
        "_4574": ["WormGearCompoundParametricStudyTool"],
        "_4575": ["WormGearMeshCompoundParametricStudyTool"],
        "_4576": ["WormGearSetCompoundParametricStudyTool"],
        "_4577": ["ZerolBevelGearCompoundParametricStudyTool"],
        "_4578": ["ZerolBevelGearMeshCompoundParametricStudyTool"],
        "_4579": ["ZerolBevelGearSetCompoundParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundParametricStudyTool",
    "AbstractShaftCompoundParametricStudyTool",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "AGMAGleasonConicalGearCompoundParametricStudyTool",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
    "AssemblyCompoundParametricStudyTool",
    "BearingCompoundParametricStudyTool",
    "BeltConnectionCompoundParametricStudyTool",
    "BeltDriveCompoundParametricStudyTool",
    "BevelDifferentialGearCompoundParametricStudyTool",
    "BevelDifferentialGearMeshCompoundParametricStudyTool",
    "BevelDifferentialGearSetCompoundParametricStudyTool",
    "BevelDifferentialPlanetGearCompoundParametricStudyTool",
    "BevelDifferentialSunGearCompoundParametricStudyTool",
    "BevelGearCompoundParametricStudyTool",
    "BevelGearMeshCompoundParametricStudyTool",
    "BevelGearSetCompoundParametricStudyTool",
    "BoltCompoundParametricStudyTool",
    "BoltedJointCompoundParametricStudyTool",
    "ClutchCompoundParametricStudyTool",
    "ClutchConnectionCompoundParametricStudyTool",
    "ClutchHalfCompoundParametricStudyTool",
    "CoaxialConnectionCompoundParametricStudyTool",
    "ComponentCompoundParametricStudyTool",
    "ConceptCouplingCompoundParametricStudyTool",
    "ConceptCouplingConnectionCompoundParametricStudyTool",
    "ConceptCouplingHalfCompoundParametricStudyTool",
    "ConceptGearCompoundParametricStudyTool",
    "ConceptGearMeshCompoundParametricStudyTool",
    "ConceptGearSetCompoundParametricStudyTool",
    "ConicalGearCompoundParametricStudyTool",
    "ConicalGearMeshCompoundParametricStudyTool",
    "ConicalGearSetCompoundParametricStudyTool",
    "ConnectionCompoundParametricStudyTool",
    "ConnectorCompoundParametricStudyTool",
    "CouplingCompoundParametricStudyTool",
    "CouplingConnectionCompoundParametricStudyTool",
    "CouplingHalfCompoundParametricStudyTool",
    "CVTBeltConnectionCompoundParametricStudyTool",
    "CVTCompoundParametricStudyTool",
    "CVTPulleyCompoundParametricStudyTool",
    "CycloidalAssemblyCompoundParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    "CycloidalDiscCompoundParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool",
    "CylindricalGearCompoundParametricStudyTool",
    "CylindricalGearMeshCompoundParametricStudyTool",
    "CylindricalGearSetCompoundParametricStudyTool",
    "CylindricalPlanetGearCompoundParametricStudyTool",
    "DatumCompoundParametricStudyTool",
    "ExternalCADModelCompoundParametricStudyTool",
    "FaceGearCompoundParametricStudyTool",
    "FaceGearMeshCompoundParametricStudyTool",
    "FaceGearSetCompoundParametricStudyTool",
    "FEPartCompoundParametricStudyTool",
    "FlexiblePinAssemblyCompoundParametricStudyTool",
    "GearCompoundParametricStudyTool",
    "GearMeshCompoundParametricStudyTool",
    "GearSetCompoundParametricStudyTool",
    "GuideDxfModelCompoundParametricStudyTool",
    "HypoidGearCompoundParametricStudyTool",
    "HypoidGearMeshCompoundParametricStudyTool",
    "HypoidGearSetCompoundParametricStudyTool",
    "InterMountableComponentConnectionCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool",
    "MassDiscCompoundParametricStudyTool",
    "MeasurementComponentCompoundParametricStudyTool",
    "MountableComponentCompoundParametricStudyTool",
    "OilSealCompoundParametricStudyTool",
    "PartCompoundParametricStudyTool",
    "PartToPartShearCouplingCompoundParametricStudyTool",
    "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    "PartToPartShearCouplingHalfCompoundParametricStudyTool",
    "PlanetaryConnectionCompoundParametricStudyTool",
    "PlanetaryGearSetCompoundParametricStudyTool",
    "PlanetCarrierCompoundParametricStudyTool",
    "PointLoadCompoundParametricStudyTool",
    "PowerLoadCompoundParametricStudyTool",
    "PulleyCompoundParametricStudyTool",
    "RingPinsCompoundParametricStudyTool",
    "RingPinsToDiscConnectionCompoundParametricStudyTool",
    "RollingRingAssemblyCompoundParametricStudyTool",
    "RollingRingCompoundParametricStudyTool",
    "RollingRingConnectionCompoundParametricStudyTool",
    "RootAssemblyCompoundParametricStudyTool",
    "ShaftCompoundParametricStudyTool",
    "ShaftHubConnectionCompoundParametricStudyTool",
    "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "SpecialisedAssemblyCompoundParametricStudyTool",
    "SpiralBevelGearCompoundParametricStudyTool",
    "SpiralBevelGearMeshCompoundParametricStudyTool",
    "SpiralBevelGearSetCompoundParametricStudyTool",
    "SpringDamperCompoundParametricStudyTool",
    "SpringDamperConnectionCompoundParametricStudyTool",
    "SpringDamperHalfCompoundParametricStudyTool",
    "StraightBevelDiffGearCompoundParametricStudyTool",
    "StraightBevelDiffGearMeshCompoundParametricStudyTool",
    "StraightBevelDiffGearSetCompoundParametricStudyTool",
    "StraightBevelGearCompoundParametricStudyTool",
    "StraightBevelGearMeshCompoundParametricStudyTool",
    "StraightBevelGearSetCompoundParametricStudyTool",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
    "StraightBevelSunGearCompoundParametricStudyTool",
    "SynchroniserCompoundParametricStudyTool",
    "SynchroniserHalfCompoundParametricStudyTool",
    "SynchroniserPartCompoundParametricStudyTool",
    "SynchroniserSleeveCompoundParametricStudyTool",
    "TorqueConverterCompoundParametricStudyTool",
    "TorqueConverterConnectionCompoundParametricStudyTool",
    "TorqueConverterPumpCompoundParametricStudyTool",
    "TorqueConverterTurbineCompoundParametricStudyTool",
    "UnbalancedMassCompoundParametricStudyTool",
    "VirtualComponentCompoundParametricStudyTool",
    "WormGearCompoundParametricStudyTool",
    "WormGearMeshCompoundParametricStudyTool",
    "WormGearSetCompoundParametricStudyTool",
    "ZerolBevelGearCompoundParametricStudyTool",
    "ZerolBevelGearMeshCompoundParametricStudyTool",
    "ZerolBevelGearSetCompoundParametricStudyTool",
)
