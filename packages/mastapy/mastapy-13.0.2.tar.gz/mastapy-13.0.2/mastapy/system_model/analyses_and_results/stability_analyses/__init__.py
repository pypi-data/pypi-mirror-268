"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3771 import AbstractAssemblyStabilityAnalysis
    from ._3772 import AbstractShaftOrHousingStabilityAnalysis
    from ._3773 import AbstractShaftStabilityAnalysis
    from ._3774 import AbstractShaftToMountableComponentConnectionStabilityAnalysis
    from ._3775 import AGMAGleasonConicalGearMeshStabilityAnalysis
    from ._3776 import AGMAGleasonConicalGearSetStabilityAnalysis
    from ._3777 import AGMAGleasonConicalGearStabilityAnalysis
    from ._3778 import AssemblyStabilityAnalysis
    from ._3779 import BearingStabilityAnalysis
    from ._3780 import BeltConnectionStabilityAnalysis
    from ._3781 import BeltDriveStabilityAnalysis
    from ._3782 import BevelDifferentialGearMeshStabilityAnalysis
    from ._3783 import BevelDifferentialGearSetStabilityAnalysis
    from ._3784 import BevelDifferentialGearStabilityAnalysis
    from ._3785 import BevelDifferentialPlanetGearStabilityAnalysis
    from ._3786 import BevelDifferentialSunGearStabilityAnalysis
    from ._3787 import BevelGearMeshStabilityAnalysis
    from ._3788 import BevelGearSetStabilityAnalysis
    from ._3789 import BevelGearStabilityAnalysis
    from ._3790 import BoltedJointStabilityAnalysis
    from ._3791 import BoltStabilityAnalysis
    from ._3792 import ClutchConnectionStabilityAnalysis
    from ._3793 import ClutchHalfStabilityAnalysis
    from ._3794 import ClutchStabilityAnalysis
    from ._3795 import CoaxialConnectionStabilityAnalysis
    from ._3796 import ComponentStabilityAnalysis
    from ._3797 import ConceptCouplingConnectionStabilityAnalysis
    from ._3798 import ConceptCouplingHalfStabilityAnalysis
    from ._3799 import ConceptCouplingStabilityAnalysis
    from ._3800 import ConceptGearMeshStabilityAnalysis
    from ._3801 import ConceptGearSetStabilityAnalysis
    from ._3802 import ConceptGearStabilityAnalysis
    from ._3803 import ConicalGearMeshStabilityAnalysis
    from ._3804 import ConicalGearSetStabilityAnalysis
    from ._3805 import ConicalGearStabilityAnalysis
    from ._3806 import ConnectionStabilityAnalysis
    from ._3807 import ConnectorStabilityAnalysis
    from ._3808 import CouplingConnectionStabilityAnalysis
    from ._3809 import CouplingHalfStabilityAnalysis
    from ._3810 import CouplingStabilityAnalysis
    from ._3811 import CriticalSpeed
    from ._3812 import CVTBeltConnectionStabilityAnalysis
    from ._3813 import CVTPulleyStabilityAnalysis
    from ._3814 import CVTStabilityAnalysis
    from ._3815 import CycloidalAssemblyStabilityAnalysis
    from ._3816 import CycloidalDiscCentralBearingConnectionStabilityAnalysis
    from ._3817 import CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
    from ._3818 import CycloidalDiscStabilityAnalysis
    from ._3819 import CylindricalGearMeshStabilityAnalysis
    from ._3820 import CylindricalGearSetStabilityAnalysis
    from ._3821 import CylindricalGearStabilityAnalysis
    from ._3822 import CylindricalPlanetGearStabilityAnalysis
    from ._3823 import DatumStabilityAnalysis
    from ._3824 import DynamicModelForStabilityAnalysis
    from ._3825 import ExternalCADModelStabilityAnalysis
    from ._3826 import FaceGearMeshStabilityAnalysis
    from ._3827 import FaceGearSetStabilityAnalysis
    from ._3828 import FaceGearStabilityAnalysis
    from ._3829 import FEPartStabilityAnalysis
    from ._3830 import FlexiblePinAssemblyStabilityAnalysis
    from ._3831 import GearMeshStabilityAnalysis
    from ._3832 import GearSetStabilityAnalysis
    from ._3833 import GearStabilityAnalysis
    from ._3834 import GuideDxfModelStabilityAnalysis
    from ._3835 import HypoidGearMeshStabilityAnalysis
    from ._3836 import HypoidGearSetStabilityAnalysis
    from ._3837 import HypoidGearStabilityAnalysis
    from ._3838 import InterMountableComponentConnectionStabilityAnalysis
    from ._3839 import KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
    from ._3840 import KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
    from ._3841 import KlingelnbergCycloPalloidConicalGearStabilityAnalysis
    from ._3842 import KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
    from ._3843 import KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
    from ._3844 import KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
    from ._3845 import KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
    from ._3846 import KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
    from ._3847 import KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
    from ._3848 import MassDiscStabilityAnalysis
    from ._3849 import MeasurementComponentStabilityAnalysis
    from ._3850 import MountableComponentStabilityAnalysis
    from ._3851 import OilSealStabilityAnalysis
    from ._3852 import PartStabilityAnalysis
    from ._3853 import PartToPartShearCouplingConnectionStabilityAnalysis
    from ._3854 import PartToPartShearCouplingHalfStabilityAnalysis
    from ._3855 import PartToPartShearCouplingStabilityAnalysis
    from ._3856 import PlanetaryConnectionStabilityAnalysis
    from ._3857 import PlanetaryGearSetStabilityAnalysis
    from ._3858 import PlanetCarrierStabilityAnalysis
    from ._3859 import PointLoadStabilityAnalysis
    from ._3860 import PowerLoadStabilityAnalysis
    from ._3861 import PulleyStabilityAnalysis
    from ._3862 import RingPinsStabilityAnalysis
    from ._3863 import RingPinsToDiscConnectionStabilityAnalysis
    from ._3864 import RollingRingAssemblyStabilityAnalysis
    from ._3865 import RollingRingConnectionStabilityAnalysis
    from ._3866 import RollingRingStabilityAnalysis
    from ._3867 import RootAssemblyStabilityAnalysis
    from ._3868 import ShaftHubConnectionStabilityAnalysis
    from ._3869 import ShaftStabilityAnalysis
    from ._3870 import ShaftToMountableComponentConnectionStabilityAnalysis
    from ._3871 import SpecialisedAssemblyStabilityAnalysis
    from ._3872 import SpiralBevelGearMeshStabilityAnalysis
    from ._3873 import SpiralBevelGearSetStabilityAnalysis
    from ._3874 import SpiralBevelGearStabilityAnalysis
    from ._3875 import SpringDamperConnectionStabilityAnalysis
    from ._3876 import SpringDamperHalfStabilityAnalysis
    from ._3877 import SpringDamperStabilityAnalysis
    from ._3878 import StabilityAnalysis
    from ._3879 import StabilityAnalysisDrawStyle
    from ._3880 import StabilityAnalysisOptions
    from ._3881 import StraightBevelDiffGearMeshStabilityAnalysis
    from ._3882 import StraightBevelDiffGearSetStabilityAnalysis
    from ._3883 import StraightBevelDiffGearStabilityAnalysis
    from ._3884 import StraightBevelGearMeshStabilityAnalysis
    from ._3885 import StraightBevelGearSetStabilityAnalysis
    from ._3886 import StraightBevelGearStabilityAnalysis
    from ._3887 import StraightBevelPlanetGearStabilityAnalysis
    from ._3888 import StraightBevelSunGearStabilityAnalysis
    from ._3889 import SynchroniserHalfStabilityAnalysis
    from ._3890 import SynchroniserPartStabilityAnalysis
    from ._3891 import SynchroniserSleeveStabilityAnalysis
    from ._3892 import SynchroniserStabilityAnalysis
    from ._3893 import TorqueConverterConnectionStabilityAnalysis
    from ._3894 import TorqueConverterPumpStabilityAnalysis
    from ._3895 import TorqueConverterStabilityAnalysis
    from ._3896 import TorqueConverterTurbineStabilityAnalysis
    from ._3897 import UnbalancedMassStabilityAnalysis
    from ._3898 import VirtualComponentStabilityAnalysis
    from ._3899 import WormGearMeshStabilityAnalysis
    from ._3900 import WormGearSetStabilityAnalysis
    from ._3901 import WormGearStabilityAnalysis
    from ._3902 import ZerolBevelGearMeshStabilityAnalysis
    from ._3903 import ZerolBevelGearSetStabilityAnalysis
    from ._3904 import ZerolBevelGearStabilityAnalysis
else:
    import_structure = {
        "_3771": ["AbstractAssemblyStabilityAnalysis"],
        "_3772": ["AbstractShaftOrHousingStabilityAnalysis"],
        "_3773": ["AbstractShaftStabilityAnalysis"],
        "_3774": ["AbstractShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3775": ["AGMAGleasonConicalGearMeshStabilityAnalysis"],
        "_3776": ["AGMAGleasonConicalGearSetStabilityAnalysis"],
        "_3777": ["AGMAGleasonConicalGearStabilityAnalysis"],
        "_3778": ["AssemblyStabilityAnalysis"],
        "_3779": ["BearingStabilityAnalysis"],
        "_3780": ["BeltConnectionStabilityAnalysis"],
        "_3781": ["BeltDriveStabilityAnalysis"],
        "_3782": ["BevelDifferentialGearMeshStabilityAnalysis"],
        "_3783": ["BevelDifferentialGearSetStabilityAnalysis"],
        "_3784": ["BevelDifferentialGearStabilityAnalysis"],
        "_3785": ["BevelDifferentialPlanetGearStabilityAnalysis"],
        "_3786": ["BevelDifferentialSunGearStabilityAnalysis"],
        "_3787": ["BevelGearMeshStabilityAnalysis"],
        "_3788": ["BevelGearSetStabilityAnalysis"],
        "_3789": ["BevelGearStabilityAnalysis"],
        "_3790": ["BoltedJointStabilityAnalysis"],
        "_3791": ["BoltStabilityAnalysis"],
        "_3792": ["ClutchConnectionStabilityAnalysis"],
        "_3793": ["ClutchHalfStabilityAnalysis"],
        "_3794": ["ClutchStabilityAnalysis"],
        "_3795": ["CoaxialConnectionStabilityAnalysis"],
        "_3796": ["ComponentStabilityAnalysis"],
        "_3797": ["ConceptCouplingConnectionStabilityAnalysis"],
        "_3798": ["ConceptCouplingHalfStabilityAnalysis"],
        "_3799": ["ConceptCouplingStabilityAnalysis"],
        "_3800": ["ConceptGearMeshStabilityAnalysis"],
        "_3801": ["ConceptGearSetStabilityAnalysis"],
        "_3802": ["ConceptGearStabilityAnalysis"],
        "_3803": ["ConicalGearMeshStabilityAnalysis"],
        "_3804": ["ConicalGearSetStabilityAnalysis"],
        "_3805": ["ConicalGearStabilityAnalysis"],
        "_3806": ["ConnectionStabilityAnalysis"],
        "_3807": ["ConnectorStabilityAnalysis"],
        "_3808": ["CouplingConnectionStabilityAnalysis"],
        "_3809": ["CouplingHalfStabilityAnalysis"],
        "_3810": ["CouplingStabilityAnalysis"],
        "_3811": ["CriticalSpeed"],
        "_3812": ["CVTBeltConnectionStabilityAnalysis"],
        "_3813": ["CVTPulleyStabilityAnalysis"],
        "_3814": ["CVTStabilityAnalysis"],
        "_3815": ["CycloidalAssemblyStabilityAnalysis"],
        "_3816": ["CycloidalDiscCentralBearingConnectionStabilityAnalysis"],
        "_3817": ["CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis"],
        "_3818": ["CycloidalDiscStabilityAnalysis"],
        "_3819": ["CylindricalGearMeshStabilityAnalysis"],
        "_3820": ["CylindricalGearSetStabilityAnalysis"],
        "_3821": ["CylindricalGearStabilityAnalysis"],
        "_3822": ["CylindricalPlanetGearStabilityAnalysis"],
        "_3823": ["DatumStabilityAnalysis"],
        "_3824": ["DynamicModelForStabilityAnalysis"],
        "_3825": ["ExternalCADModelStabilityAnalysis"],
        "_3826": ["FaceGearMeshStabilityAnalysis"],
        "_3827": ["FaceGearSetStabilityAnalysis"],
        "_3828": ["FaceGearStabilityAnalysis"],
        "_3829": ["FEPartStabilityAnalysis"],
        "_3830": ["FlexiblePinAssemblyStabilityAnalysis"],
        "_3831": ["GearMeshStabilityAnalysis"],
        "_3832": ["GearSetStabilityAnalysis"],
        "_3833": ["GearStabilityAnalysis"],
        "_3834": ["GuideDxfModelStabilityAnalysis"],
        "_3835": ["HypoidGearMeshStabilityAnalysis"],
        "_3836": ["HypoidGearSetStabilityAnalysis"],
        "_3837": ["HypoidGearStabilityAnalysis"],
        "_3838": ["InterMountableComponentConnectionStabilityAnalysis"],
        "_3839": ["KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis"],
        "_3840": ["KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"],
        "_3841": ["KlingelnbergCycloPalloidConicalGearStabilityAnalysis"],
        "_3842": ["KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis"],
        "_3843": ["KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis"],
        "_3844": ["KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"],
        "_3845": ["KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"],
        "_3846": ["KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"],
        "_3847": ["KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis"],
        "_3848": ["MassDiscStabilityAnalysis"],
        "_3849": ["MeasurementComponentStabilityAnalysis"],
        "_3850": ["MountableComponentStabilityAnalysis"],
        "_3851": ["OilSealStabilityAnalysis"],
        "_3852": ["PartStabilityAnalysis"],
        "_3853": ["PartToPartShearCouplingConnectionStabilityAnalysis"],
        "_3854": ["PartToPartShearCouplingHalfStabilityAnalysis"],
        "_3855": ["PartToPartShearCouplingStabilityAnalysis"],
        "_3856": ["PlanetaryConnectionStabilityAnalysis"],
        "_3857": ["PlanetaryGearSetStabilityAnalysis"],
        "_3858": ["PlanetCarrierStabilityAnalysis"],
        "_3859": ["PointLoadStabilityAnalysis"],
        "_3860": ["PowerLoadStabilityAnalysis"],
        "_3861": ["PulleyStabilityAnalysis"],
        "_3862": ["RingPinsStabilityAnalysis"],
        "_3863": ["RingPinsToDiscConnectionStabilityAnalysis"],
        "_3864": ["RollingRingAssemblyStabilityAnalysis"],
        "_3865": ["RollingRingConnectionStabilityAnalysis"],
        "_3866": ["RollingRingStabilityAnalysis"],
        "_3867": ["RootAssemblyStabilityAnalysis"],
        "_3868": ["ShaftHubConnectionStabilityAnalysis"],
        "_3869": ["ShaftStabilityAnalysis"],
        "_3870": ["ShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3871": ["SpecialisedAssemblyStabilityAnalysis"],
        "_3872": ["SpiralBevelGearMeshStabilityAnalysis"],
        "_3873": ["SpiralBevelGearSetStabilityAnalysis"],
        "_3874": ["SpiralBevelGearStabilityAnalysis"],
        "_3875": ["SpringDamperConnectionStabilityAnalysis"],
        "_3876": ["SpringDamperHalfStabilityAnalysis"],
        "_3877": ["SpringDamperStabilityAnalysis"],
        "_3878": ["StabilityAnalysis"],
        "_3879": ["StabilityAnalysisDrawStyle"],
        "_3880": ["StabilityAnalysisOptions"],
        "_3881": ["StraightBevelDiffGearMeshStabilityAnalysis"],
        "_3882": ["StraightBevelDiffGearSetStabilityAnalysis"],
        "_3883": ["StraightBevelDiffGearStabilityAnalysis"],
        "_3884": ["StraightBevelGearMeshStabilityAnalysis"],
        "_3885": ["StraightBevelGearSetStabilityAnalysis"],
        "_3886": ["StraightBevelGearStabilityAnalysis"],
        "_3887": ["StraightBevelPlanetGearStabilityAnalysis"],
        "_3888": ["StraightBevelSunGearStabilityAnalysis"],
        "_3889": ["SynchroniserHalfStabilityAnalysis"],
        "_3890": ["SynchroniserPartStabilityAnalysis"],
        "_3891": ["SynchroniserSleeveStabilityAnalysis"],
        "_3892": ["SynchroniserStabilityAnalysis"],
        "_3893": ["TorqueConverterConnectionStabilityAnalysis"],
        "_3894": ["TorqueConverterPumpStabilityAnalysis"],
        "_3895": ["TorqueConverterStabilityAnalysis"],
        "_3896": ["TorqueConverterTurbineStabilityAnalysis"],
        "_3897": ["UnbalancedMassStabilityAnalysis"],
        "_3898": ["VirtualComponentStabilityAnalysis"],
        "_3899": ["WormGearMeshStabilityAnalysis"],
        "_3900": ["WormGearSetStabilityAnalysis"],
        "_3901": ["WormGearStabilityAnalysis"],
        "_3902": ["ZerolBevelGearMeshStabilityAnalysis"],
        "_3903": ["ZerolBevelGearSetStabilityAnalysis"],
        "_3904": ["ZerolBevelGearStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStabilityAnalysis",
    "AbstractShaftOrHousingStabilityAnalysis",
    "AbstractShaftStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
    "AGMAGleasonConicalGearStabilityAnalysis",
    "AssemblyStabilityAnalysis",
    "BearingStabilityAnalysis",
    "BeltConnectionStabilityAnalysis",
    "BeltDriveStabilityAnalysis",
    "BevelDifferentialGearMeshStabilityAnalysis",
    "BevelDifferentialGearSetStabilityAnalysis",
    "BevelDifferentialGearStabilityAnalysis",
    "BevelDifferentialPlanetGearStabilityAnalysis",
    "BevelDifferentialSunGearStabilityAnalysis",
    "BevelGearMeshStabilityAnalysis",
    "BevelGearSetStabilityAnalysis",
    "BevelGearStabilityAnalysis",
    "BoltedJointStabilityAnalysis",
    "BoltStabilityAnalysis",
    "ClutchConnectionStabilityAnalysis",
    "ClutchHalfStabilityAnalysis",
    "ClutchStabilityAnalysis",
    "CoaxialConnectionStabilityAnalysis",
    "ComponentStabilityAnalysis",
    "ConceptCouplingConnectionStabilityAnalysis",
    "ConceptCouplingHalfStabilityAnalysis",
    "ConceptCouplingStabilityAnalysis",
    "ConceptGearMeshStabilityAnalysis",
    "ConceptGearSetStabilityAnalysis",
    "ConceptGearStabilityAnalysis",
    "ConicalGearMeshStabilityAnalysis",
    "ConicalGearSetStabilityAnalysis",
    "ConicalGearStabilityAnalysis",
    "ConnectionStabilityAnalysis",
    "ConnectorStabilityAnalysis",
    "CouplingConnectionStabilityAnalysis",
    "CouplingHalfStabilityAnalysis",
    "CouplingStabilityAnalysis",
    "CriticalSpeed",
    "CVTBeltConnectionStabilityAnalysis",
    "CVTPulleyStabilityAnalysis",
    "CVTStabilityAnalysis",
    "CycloidalAssemblyStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
    "CycloidalDiscStabilityAnalysis",
    "CylindricalGearMeshStabilityAnalysis",
    "CylindricalGearSetStabilityAnalysis",
    "CylindricalGearStabilityAnalysis",
    "CylindricalPlanetGearStabilityAnalysis",
    "DatumStabilityAnalysis",
    "DynamicModelForStabilityAnalysis",
    "ExternalCADModelStabilityAnalysis",
    "FaceGearMeshStabilityAnalysis",
    "FaceGearSetStabilityAnalysis",
    "FaceGearStabilityAnalysis",
    "FEPartStabilityAnalysis",
    "FlexiblePinAssemblyStabilityAnalysis",
    "GearMeshStabilityAnalysis",
    "GearSetStabilityAnalysis",
    "GearStabilityAnalysis",
    "GuideDxfModelStabilityAnalysis",
    "HypoidGearMeshStabilityAnalysis",
    "HypoidGearSetStabilityAnalysis",
    "HypoidGearStabilityAnalysis",
    "InterMountableComponentConnectionStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
    "MassDiscStabilityAnalysis",
    "MeasurementComponentStabilityAnalysis",
    "MountableComponentStabilityAnalysis",
    "OilSealStabilityAnalysis",
    "PartStabilityAnalysis",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
    "PartToPartShearCouplingHalfStabilityAnalysis",
    "PartToPartShearCouplingStabilityAnalysis",
    "PlanetaryConnectionStabilityAnalysis",
    "PlanetaryGearSetStabilityAnalysis",
    "PlanetCarrierStabilityAnalysis",
    "PointLoadStabilityAnalysis",
    "PowerLoadStabilityAnalysis",
    "PulleyStabilityAnalysis",
    "RingPinsStabilityAnalysis",
    "RingPinsToDiscConnectionStabilityAnalysis",
    "RollingRingAssemblyStabilityAnalysis",
    "RollingRingConnectionStabilityAnalysis",
    "RollingRingStabilityAnalysis",
    "RootAssemblyStabilityAnalysis",
    "ShaftHubConnectionStabilityAnalysis",
    "ShaftStabilityAnalysis",
    "ShaftToMountableComponentConnectionStabilityAnalysis",
    "SpecialisedAssemblyStabilityAnalysis",
    "SpiralBevelGearMeshStabilityAnalysis",
    "SpiralBevelGearSetStabilityAnalysis",
    "SpiralBevelGearStabilityAnalysis",
    "SpringDamperConnectionStabilityAnalysis",
    "SpringDamperHalfStabilityAnalysis",
    "SpringDamperStabilityAnalysis",
    "StabilityAnalysis",
    "StabilityAnalysisDrawStyle",
    "StabilityAnalysisOptions",
    "StraightBevelDiffGearMeshStabilityAnalysis",
    "StraightBevelDiffGearSetStabilityAnalysis",
    "StraightBevelDiffGearStabilityAnalysis",
    "StraightBevelGearMeshStabilityAnalysis",
    "StraightBevelGearSetStabilityAnalysis",
    "StraightBevelGearStabilityAnalysis",
    "StraightBevelPlanetGearStabilityAnalysis",
    "StraightBevelSunGearStabilityAnalysis",
    "SynchroniserHalfStabilityAnalysis",
    "SynchroniserPartStabilityAnalysis",
    "SynchroniserSleeveStabilityAnalysis",
    "SynchroniserStabilityAnalysis",
    "TorqueConverterConnectionStabilityAnalysis",
    "TorqueConverterPumpStabilityAnalysis",
    "TorqueConverterStabilityAnalysis",
    "TorqueConverterTurbineStabilityAnalysis",
    "UnbalancedMassStabilityAnalysis",
    "VirtualComponentStabilityAnalysis",
    "WormGearMeshStabilityAnalysis",
    "WormGearSetStabilityAnalysis",
    "WormGearStabilityAnalysis",
    "ZerolBevelGearMeshStabilityAnalysis",
    "ZerolBevelGearSetStabilityAnalysis",
    "ZerolBevelGearStabilityAnalysis",
)
