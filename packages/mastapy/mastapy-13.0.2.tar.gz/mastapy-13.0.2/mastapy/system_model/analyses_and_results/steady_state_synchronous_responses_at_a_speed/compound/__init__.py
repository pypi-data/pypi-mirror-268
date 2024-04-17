"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3642 import AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3643 import AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3644 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3645 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3646 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3647 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3648 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3649 import AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3650 import BearingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3651 import BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3652 import BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3653 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3654 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3655 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3656 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3657 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3658 import BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3659 import BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3660 import BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3661 import BoltCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3662 import BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3663 import ClutchCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3664 import ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3665 import ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3666 import CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3667 import ComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3668 import ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3669 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3670 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3671 import ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3672 import ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3673 import ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3674 import ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3675 import ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3676 import ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3677 import ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3678 import ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3679 import CouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3680 import CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3681 import CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3682 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3683 import CVTCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3684 import CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3685 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3686 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3687 import CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3688 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3689 import CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3690 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3691 import CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3692 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3693 import DatumCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3694 import ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3695 import FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3696 import FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3697 import FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3698 import FEPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3699 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3700 import GearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3701 import GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3702 import GearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3703 import GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3704 import HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3705 import HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3706 import HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3707 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3708 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3709 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3710 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3711 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3712 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3713 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3714 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3715 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3716 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3717 import MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3718 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3719 import MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3720 import OilSealCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3721 import PartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3722 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3723 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3724 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3725 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3726 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3727 import PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3728 import PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3729 import PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3730 import PulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3731 import RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3732 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3733 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3734 import RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3735 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3736 import RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3737 import ShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3738 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3739 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3740 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3741 import SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3742 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3743 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3744 import SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3745 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3746 import SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3747 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3748 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3749 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3750 import StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3751 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3752 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3753 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3754 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3755 import SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3756 import SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3757 import SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3758 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3759 import TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3760 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3761 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3762 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3763 import UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3764 import VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3765 import WormGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3766 import WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3767 import WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3768 import ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3769 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3770 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3642": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3643": ["AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3644": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3645": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3646": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3647": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3648": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3649": ["AssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3650": ["BearingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3651": ["BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3652": ["BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3653": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3654": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3655": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3656": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3657": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3658": ["BevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3659": ["BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3660": ["BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3661": ["BoltCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3662": ["BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3663": ["ClutchCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3664": ["ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3665": ["ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3666": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3667": ["ComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3668": ["ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3669": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3670": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3671": ["ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3672": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3673": ["ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3674": ["ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3675": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3676": ["ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3677": ["ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3678": ["ConnectorCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3679": ["CouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3680": ["CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3681": ["CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3682": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3683": ["CVTCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3684": ["CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3685": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3686": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3687": ["CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3688": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3689": ["CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3690": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3691": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3692": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3693": ["DatumCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3694": ["ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3695": ["FaceGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3696": ["FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3697": ["FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3698": ["FEPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3699": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3700": ["GearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3701": ["GearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3702": ["GearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3703": ["GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3704": ["HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3705": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3706": ["HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3707": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3708": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3709": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3710": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3711": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3712": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3713": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3714": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3715": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3716": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3717": ["MassDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3718": ["MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3719": ["MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3720": ["OilSealCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3721": ["PartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3722": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3723": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3724": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3725": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3726": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3727": ["PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3728": ["PointLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3729": ["PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3730": ["PulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3731": ["RingPinsCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3732": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3733": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3734": ["RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3735": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3736": ["RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3737": ["ShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3738": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3739": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3740": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3741": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3742": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3743": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3744": ["SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3745": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3746": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3747": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3748": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3749": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3750": ["StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3751": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3752": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3753": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3754": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3755": ["SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3756": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3757": ["SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3758": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3759": ["TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3760": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3761": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3762": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3763": ["UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3764": ["VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3765": ["WormGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3766": ["WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3767": ["WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3768": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3769": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3770": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "AssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "DatumCompoundSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "FEPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "MassDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "OilSealCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed",
    "PointLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)
