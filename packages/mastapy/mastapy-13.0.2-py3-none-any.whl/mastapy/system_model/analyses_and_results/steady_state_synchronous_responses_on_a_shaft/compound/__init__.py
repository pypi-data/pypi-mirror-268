"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3383 import AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3384 import AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3385 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3386 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3387 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3388 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3389 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3390 import AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3391 import BearingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3392 import BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3393 import BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3394 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3395 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3396 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3397 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3398 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3399 import BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3400 import BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3401 import BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3402 import BoltCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3403 import BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3404 import ClutchCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3405 import ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3406 import ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3407 import CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3408 import ComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3409 import ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3410 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3411 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3412 import ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3413 import ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3414 import ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3415 import ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3416 import ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3417 import ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3418 import ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3419 import ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3420 import CouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3421 import CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3422 import CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3423 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3424 import CVTCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3425 import CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3426 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3427 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3428 import CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3429 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3430 import CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3431 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3432 import CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3433 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3434 import DatumCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3435 import ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3436 import FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3437 import FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3438 import FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3439 import FEPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3440 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3441 import GearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3442 import GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3443 import GearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3444 import GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3445 import HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3446 import HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3447 import HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3448 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3449 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3450 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3451 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3452 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3453 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3454 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3455 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3456 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3457 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3458 import MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3459 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3460 import MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3461 import OilSealCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3462 import PartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3463 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3464 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3465 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3466 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3467 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3468 import PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3469 import PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3470 import PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3471 import PulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3472 import RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3473 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3474 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3475 import RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3476 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3477 import RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3478 import ShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3479 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3480 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3481 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3482 import SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3483 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3484 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3485 import SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3486 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3487 import SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3488 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3489 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3490 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3491 import StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3492 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3493 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3494 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3495 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3496 import SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3497 import SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3498 import SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3499 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3500 import TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3501 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3502 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3503 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3504 import UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3505 import VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3506 import WormGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3507 import WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3508 import WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3509 import ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3510 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3511 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        "_3383": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3384": ["AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3385": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3386": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3387": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3388": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3389": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3390": ["AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3391": ["BearingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3392": ["BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3393": ["BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3394": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3395": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3396": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3397": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3398": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3399": ["BevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3400": ["BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3401": ["BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3402": ["BoltCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3403": ["BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3404": ["ClutchCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3405": ["ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3406": ["ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3407": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3408": ["ComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3409": ["ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3410": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3411": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3412": ["ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3413": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3414": ["ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3415": ["ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3416": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3417": ["ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3418": ["ConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3419": ["ConnectorCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3420": ["CouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3421": ["CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3422": ["CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3423": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3424": ["CVTCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3425": ["CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3426": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3427": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3428": ["CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3429": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3430": ["CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3431": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3432": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3433": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3434": ["DatumCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3435": ["ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3436": ["FaceGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3437": ["FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3438": ["FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3439": ["FEPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3440": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3441": ["GearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3442": ["GearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3443": ["GearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3444": ["GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3445": ["HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3446": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3447": ["HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3448": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3449": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3450": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3451": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3452": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3453": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3454": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3455": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3456": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3457": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3458": ["MassDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3459": ["MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3460": ["MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3461": ["OilSealCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3462": ["PartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3463": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3464": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3465": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3466": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3467": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3468": ["PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3469": ["PointLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3470": ["PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3471": ["PulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3472": ["RingPinsCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3473": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3474": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3475": ["RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3476": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3477": ["RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3478": ["ShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3479": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3480": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3481": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3482": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3483": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3484": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3485": ["SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3486": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3487": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3488": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3489": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3490": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3491": ["StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3492": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3493": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3494": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3495": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3496": ["SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3497": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3498": ["SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3499": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3500": ["TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3501": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3502": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3503": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3504": ["UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3505": ["VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3506": ["WormGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3507": ["WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3508": ["WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3509": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3510": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3511": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "BearingCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "FEPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "MassDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "OilSealCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft",
    "PointLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft",
    "VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)
