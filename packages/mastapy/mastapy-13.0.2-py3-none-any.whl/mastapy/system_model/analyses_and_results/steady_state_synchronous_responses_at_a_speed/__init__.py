"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3512 import AbstractAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3513 import AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
    from ._3514 import AbstractShaftSteadyStateSynchronousResponseAtASpeed
    from ._3515 import (
        AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3516 import AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3517 import AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3518 import AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3519 import AssemblySteadyStateSynchronousResponseAtASpeed
    from ._3520 import BearingSteadyStateSynchronousResponseAtASpeed
    from ._3521 import BeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3522 import BeltDriveSteadyStateSynchronousResponseAtASpeed
    from ._3523 import BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3524 import BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3525 import BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
    from ._3526 import BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3527 import BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3528 import BevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3529 import BevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3530 import BevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3531 import BoltedJointSteadyStateSynchronousResponseAtASpeed
    from ._3532 import BoltSteadyStateSynchronousResponseAtASpeed
    from ._3533 import ClutchConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3534 import ClutchHalfSteadyStateSynchronousResponseAtASpeed
    from ._3535 import ClutchSteadyStateSynchronousResponseAtASpeed
    from ._3536 import CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3537 import ComponentSteadyStateSynchronousResponseAtASpeed
    from ._3538 import ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3539 import ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3540 import ConceptCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3541 import ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3542 import ConceptGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3543 import ConceptGearSteadyStateSynchronousResponseAtASpeed
    from ._3544 import ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3545 import ConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3546 import ConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3547 import ConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3548 import ConnectorSteadyStateSynchronousResponseAtASpeed
    from ._3549 import CouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3550 import CouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3551 import CouplingSteadyStateSynchronousResponseAtASpeed
    from ._3552 import CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3553 import CVTPulleySteadyStateSynchronousResponseAtASpeed
    from ._3554 import CVTSteadyStateSynchronousResponseAtASpeed
    from ._3555 import CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3556 import (
        CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3557 import (
        CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3558 import CycloidalDiscSteadyStateSynchronousResponseAtASpeed
    from ._3559 import CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3560 import CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3561 import CylindricalGearSteadyStateSynchronousResponseAtASpeed
    from ._3562 import CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3563 import DatumSteadyStateSynchronousResponseAtASpeed
    from ._3564 import ExternalCADModelSteadyStateSynchronousResponseAtASpeed
    from ._3565 import FaceGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3566 import FaceGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3567 import FaceGearSteadyStateSynchronousResponseAtASpeed
    from ._3568 import FEPartSteadyStateSynchronousResponseAtASpeed
    from ._3569 import FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3570 import GearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3571 import GearSetSteadyStateSynchronousResponseAtASpeed
    from ._3572 import GearSteadyStateSynchronousResponseAtASpeed
    from ._3573 import GuideDxfModelSteadyStateSynchronousResponseAtASpeed
    from ._3574 import HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3575 import HypoidGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3576 import HypoidGearSteadyStateSynchronousResponseAtASpeed
    from ._3577 import (
        InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3578 import (
        KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3579 import (
        KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3580 import (
        KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3581 import (
        KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3582 import (
        KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3583 import (
        KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3584 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3585 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3586 import (
        KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3587 import MassDiscSteadyStateSynchronousResponseAtASpeed
    from ._3588 import MeasurementComponentSteadyStateSynchronousResponseAtASpeed
    from ._3589 import MountableComponentSteadyStateSynchronousResponseAtASpeed
    from ._3590 import OilSealSteadyStateSynchronousResponseAtASpeed
    from ._3591 import PartSteadyStateSynchronousResponseAtASpeed
    from ._3592 import (
        PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3593 import PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3594 import PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3595 import PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3596 import PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3597 import PlanetCarrierSteadyStateSynchronousResponseAtASpeed
    from ._3598 import PointLoadSteadyStateSynchronousResponseAtASpeed
    from ._3599 import PowerLoadSteadyStateSynchronousResponseAtASpeed
    from ._3600 import PulleySteadyStateSynchronousResponseAtASpeed
    from ._3601 import RingPinsSteadyStateSynchronousResponseAtASpeed
    from ._3602 import RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3603 import RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3604 import RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3605 import RollingRingSteadyStateSynchronousResponseAtASpeed
    from ._3606 import RootAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3607 import ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3608 import ShaftSteadyStateSynchronousResponseAtASpeed
    from ._3609 import (
        ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3610 import SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3611 import SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3612 import SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3613 import SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3614 import SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3615 import SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
    from ._3616 import SpringDamperSteadyStateSynchronousResponseAtASpeed
    from ._3617 import SteadyStateSynchronousResponseAtASpeed
    from ._3618 import StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3619 import StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3620 import StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
    from ._3621 import StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3622 import StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3623 import StraightBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3624 import StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3625 import StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3626 import SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
    from ._3627 import SynchroniserPartSteadyStateSynchronousResponseAtASpeed
    from ._3628 import SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
    from ._3629 import SynchroniserSteadyStateSynchronousResponseAtASpeed
    from ._3630 import TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3631 import TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
    from ._3632 import TorqueConverterSteadyStateSynchronousResponseAtASpeed
    from ._3633 import TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
    from ._3634 import UnbalancedMassSteadyStateSynchronousResponseAtASpeed
    from ._3635 import VirtualComponentSteadyStateSynchronousResponseAtASpeed
    from ._3636 import WormGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3637 import WormGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3638 import WormGearSteadyStateSynchronousResponseAtASpeed
    from ._3639 import ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3640 import ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3641 import ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3512": ["AbstractAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3513": ["AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed"],
        "_3514": ["AbstractShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3515": [
            "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3516": ["AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3517": ["AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3518": ["AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3519": ["AssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3520": ["BearingSteadyStateSynchronousResponseAtASpeed"],
        "_3521": ["BeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3522": ["BeltDriveSteadyStateSynchronousResponseAtASpeed"],
        "_3523": ["BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3524": ["BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3525": ["BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed"],
        "_3526": ["BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3527": ["BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3528": ["BevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3529": ["BevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3530": ["BevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3531": ["BoltedJointSteadyStateSynchronousResponseAtASpeed"],
        "_3532": ["BoltSteadyStateSynchronousResponseAtASpeed"],
        "_3533": ["ClutchConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3534": ["ClutchHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3535": ["ClutchSteadyStateSynchronousResponseAtASpeed"],
        "_3536": ["CoaxialConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3537": ["ComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3538": ["ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3539": ["ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3540": ["ConceptCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3541": ["ConceptGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3542": ["ConceptGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3543": ["ConceptGearSteadyStateSynchronousResponseAtASpeed"],
        "_3544": ["ConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3545": ["ConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3546": ["ConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3547": ["ConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3548": ["ConnectorSteadyStateSynchronousResponseAtASpeed"],
        "_3549": ["CouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3550": ["CouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3551": ["CouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3552": ["CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3553": ["CVTPulleySteadyStateSynchronousResponseAtASpeed"],
        "_3554": ["CVTSteadyStateSynchronousResponseAtASpeed"],
        "_3555": ["CycloidalAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3556": [
            "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3557": [
            "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3558": ["CycloidalDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3559": ["CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3560": ["CylindricalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3561": ["CylindricalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3562": ["CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3563": ["DatumSteadyStateSynchronousResponseAtASpeed"],
        "_3564": ["ExternalCADModelSteadyStateSynchronousResponseAtASpeed"],
        "_3565": ["FaceGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3566": ["FaceGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3567": ["FaceGearSteadyStateSynchronousResponseAtASpeed"],
        "_3568": ["FEPartSteadyStateSynchronousResponseAtASpeed"],
        "_3569": ["FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3570": ["GearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3571": ["GearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3572": ["GearSteadyStateSynchronousResponseAtASpeed"],
        "_3573": ["GuideDxfModelSteadyStateSynchronousResponseAtASpeed"],
        "_3574": ["HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3575": ["HypoidGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3576": ["HypoidGearSteadyStateSynchronousResponseAtASpeed"],
        "_3577": [
            "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3578": [
            "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3579": [
            "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3580": [
            "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3581": [
            "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3582": [
            "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3583": [
            "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3584": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3585": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3586": [
            "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3587": ["MassDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3588": ["MeasurementComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3589": ["MountableComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3590": ["OilSealSteadyStateSynchronousResponseAtASpeed"],
        "_3591": ["PartSteadyStateSynchronousResponseAtASpeed"],
        "_3592": [
            "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3593": ["PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3594": ["PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3595": ["PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3596": ["PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3597": ["PlanetCarrierSteadyStateSynchronousResponseAtASpeed"],
        "_3598": ["PointLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3599": ["PowerLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3600": ["PulleySteadyStateSynchronousResponseAtASpeed"],
        "_3601": ["RingPinsSteadyStateSynchronousResponseAtASpeed"],
        "_3602": ["RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3603": ["RollingRingAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3604": ["RollingRingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3605": ["RollingRingSteadyStateSynchronousResponseAtASpeed"],
        "_3606": ["RootAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3607": ["ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3608": ["ShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3609": [
            "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3610": ["SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3611": ["SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3612": ["SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3613": ["SpiralBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3614": ["SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3615": ["SpringDamperHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3616": ["SpringDamperSteadyStateSynchronousResponseAtASpeed"],
        "_3617": ["SteadyStateSynchronousResponseAtASpeed"],
        "_3618": ["StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3619": ["StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3620": ["StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed"],
        "_3621": ["StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3622": ["StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3623": ["StraightBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3624": ["StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3625": ["StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3626": ["SynchroniserHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3627": ["SynchroniserPartSteadyStateSynchronousResponseAtASpeed"],
        "_3628": ["SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed"],
        "_3629": ["SynchroniserSteadyStateSynchronousResponseAtASpeed"],
        "_3630": ["TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3631": ["TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed"],
        "_3632": ["TorqueConverterSteadyStateSynchronousResponseAtASpeed"],
        "_3633": ["TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed"],
        "_3634": ["UnbalancedMassSteadyStateSynchronousResponseAtASpeed"],
        "_3635": ["VirtualComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3636": ["WormGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3637": ["WormGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3638": ["WormGearSteadyStateSynchronousResponseAtASpeed"],
        "_3639": ["ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3640": ["ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3641": ["ZerolBevelGearSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
    "AssemblySteadyStateSynchronousResponseAtASpeed",
    "BearingSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointSteadyStateSynchronousResponseAtASpeed",
    "BoltSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfSteadyStateSynchronousResponseAtASpeed",
    "ClutchSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
    "ComponentSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSteadyStateSynchronousResponseAtASpeed",
    "ConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConnectorSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "CouplingSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleySteadyStateSynchronousResponseAtASpeed",
    "CVTSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "DatumSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSteadyStateSynchronousResponseAtASpeed",
    "FEPartSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed",
    "GearMeshSteadyStateSynchronousResponseAtASpeed",
    "GearSetSteadyStateSynchronousResponseAtASpeed",
    "GearSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "MassDiscSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentSteadyStateSynchronousResponseAtASpeed",
    "OilSealSteadyStateSynchronousResponseAtASpeed",
    "PartSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
    "PointLoadSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadSteadyStateSynchronousResponseAtASpeed",
    "PulleySteadyStateSynchronousResponseAtASpeed",
    "RingPinsSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblySteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblySteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed",
    "ShaftSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperSteadyStateSynchronousResponseAtASpeed",
    "SteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetSteadyStateSynchronousResponseAtASpeed",
    "WormGearSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
)
