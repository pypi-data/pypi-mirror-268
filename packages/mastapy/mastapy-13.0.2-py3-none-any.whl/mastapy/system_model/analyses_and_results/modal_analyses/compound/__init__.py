"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4736 import AbstractAssemblyCompoundModalAnalysis
    from ._4737 import AbstractShaftCompoundModalAnalysis
    from ._4738 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4739 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4740 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4741 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4742 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4743 import AssemblyCompoundModalAnalysis
    from ._4744 import BearingCompoundModalAnalysis
    from ._4745 import BeltConnectionCompoundModalAnalysis
    from ._4746 import BeltDriveCompoundModalAnalysis
    from ._4747 import BevelDifferentialGearCompoundModalAnalysis
    from ._4748 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4749 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4750 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4751 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4752 import BevelGearCompoundModalAnalysis
    from ._4753 import BevelGearMeshCompoundModalAnalysis
    from ._4754 import BevelGearSetCompoundModalAnalysis
    from ._4755 import BoltCompoundModalAnalysis
    from ._4756 import BoltedJointCompoundModalAnalysis
    from ._4757 import ClutchCompoundModalAnalysis
    from ._4758 import ClutchConnectionCompoundModalAnalysis
    from ._4759 import ClutchHalfCompoundModalAnalysis
    from ._4760 import CoaxialConnectionCompoundModalAnalysis
    from ._4761 import ComponentCompoundModalAnalysis
    from ._4762 import ConceptCouplingCompoundModalAnalysis
    from ._4763 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4764 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4765 import ConceptGearCompoundModalAnalysis
    from ._4766 import ConceptGearMeshCompoundModalAnalysis
    from ._4767 import ConceptGearSetCompoundModalAnalysis
    from ._4768 import ConicalGearCompoundModalAnalysis
    from ._4769 import ConicalGearMeshCompoundModalAnalysis
    from ._4770 import ConicalGearSetCompoundModalAnalysis
    from ._4771 import ConnectionCompoundModalAnalysis
    from ._4772 import ConnectorCompoundModalAnalysis
    from ._4773 import CouplingCompoundModalAnalysis
    from ._4774 import CouplingConnectionCompoundModalAnalysis
    from ._4775 import CouplingHalfCompoundModalAnalysis
    from ._4776 import CVTBeltConnectionCompoundModalAnalysis
    from ._4777 import CVTCompoundModalAnalysis
    from ._4778 import CVTPulleyCompoundModalAnalysis
    from ._4779 import CycloidalAssemblyCompoundModalAnalysis
    from ._4780 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4781 import CycloidalDiscCompoundModalAnalysis
    from ._4782 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4783 import CylindricalGearCompoundModalAnalysis
    from ._4784 import CylindricalGearMeshCompoundModalAnalysis
    from ._4785 import CylindricalGearSetCompoundModalAnalysis
    from ._4786 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4787 import DatumCompoundModalAnalysis
    from ._4788 import ExternalCADModelCompoundModalAnalysis
    from ._4789 import FaceGearCompoundModalAnalysis
    from ._4790 import FaceGearMeshCompoundModalAnalysis
    from ._4791 import FaceGearSetCompoundModalAnalysis
    from ._4792 import FEPartCompoundModalAnalysis
    from ._4793 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4794 import GearCompoundModalAnalysis
    from ._4795 import GearMeshCompoundModalAnalysis
    from ._4796 import GearSetCompoundModalAnalysis
    from ._4797 import GuideDxfModelCompoundModalAnalysis
    from ._4798 import HypoidGearCompoundModalAnalysis
    from ._4799 import HypoidGearMeshCompoundModalAnalysis
    from ._4800 import HypoidGearSetCompoundModalAnalysis
    from ._4801 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4802 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4803 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4804 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4805 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4806 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4807 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4808 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4809 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4810 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4811 import MassDiscCompoundModalAnalysis
    from ._4812 import MeasurementComponentCompoundModalAnalysis
    from ._4813 import MountableComponentCompoundModalAnalysis
    from ._4814 import OilSealCompoundModalAnalysis
    from ._4815 import PartCompoundModalAnalysis
    from ._4816 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4817 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4818 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4819 import PlanetaryConnectionCompoundModalAnalysis
    from ._4820 import PlanetaryGearSetCompoundModalAnalysis
    from ._4821 import PlanetCarrierCompoundModalAnalysis
    from ._4822 import PointLoadCompoundModalAnalysis
    from ._4823 import PowerLoadCompoundModalAnalysis
    from ._4824 import PulleyCompoundModalAnalysis
    from ._4825 import RingPinsCompoundModalAnalysis
    from ._4826 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4827 import RollingRingAssemblyCompoundModalAnalysis
    from ._4828 import RollingRingCompoundModalAnalysis
    from ._4829 import RollingRingConnectionCompoundModalAnalysis
    from ._4830 import RootAssemblyCompoundModalAnalysis
    from ._4831 import ShaftCompoundModalAnalysis
    from ._4832 import ShaftHubConnectionCompoundModalAnalysis
    from ._4833 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4834 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4835 import SpiralBevelGearCompoundModalAnalysis
    from ._4836 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4837 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4838 import SpringDamperCompoundModalAnalysis
    from ._4839 import SpringDamperConnectionCompoundModalAnalysis
    from ._4840 import SpringDamperHalfCompoundModalAnalysis
    from ._4841 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4842 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4843 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4844 import StraightBevelGearCompoundModalAnalysis
    from ._4845 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4846 import StraightBevelGearSetCompoundModalAnalysis
    from ._4847 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4848 import StraightBevelSunGearCompoundModalAnalysis
    from ._4849 import SynchroniserCompoundModalAnalysis
    from ._4850 import SynchroniserHalfCompoundModalAnalysis
    from ._4851 import SynchroniserPartCompoundModalAnalysis
    from ._4852 import SynchroniserSleeveCompoundModalAnalysis
    from ._4853 import TorqueConverterCompoundModalAnalysis
    from ._4854 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4855 import TorqueConverterPumpCompoundModalAnalysis
    from ._4856 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4857 import UnbalancedMassCompoundModalAnalysis
    from ._4858 import VirtualComponentCompoundModalAnalysis
    from ._4859 import WormGearCompoundModalAnalysis
    from ._4860 import WormGearMeshCompoundModalAnalysis
    from ._4861 import WormGearSetCompoundModalAnalysis
    from ._4862 import ZerolBevelGearCompoundModalAnalysis
    from ._4863 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4864 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        "_4736": ["AbstractAssemblyCompoundModalAnalysis"],
        "_4737": ["AbstractShaftCompoundModalAnalysis"],
        "_4738": ["AbstractShaftOrHousingCompoundModalAnalysis"],
        "_4739": ["AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4740": ["AGMAGleasonConicalGearCompoundModalAnalysis"],
        "_4741": ["AGMAGleasonConicalGearMeshCompoundModalAnalysis"],
        "_4742": ["AGMAGleasonConicalGearSetCompoundModalAnalysis"],
        "_4743": ["AssemblyCompoundModalAnalysis"],
        "_4744": ["BearingCompoundModalAnalysis"],
        "_4745": ["BeltConnectionCompoundModalAnalysis"],
        "_4746": ["BeltDriveCompoundModalAnalysis"],
        "_4747": ["BevelDifferentialGearCompoundModalAnalysis"],
        "_4748": ["BevelDifferentialGearMeshCompoundModalAnalysis"],
        "_4749": ["BevelDifferentialGearSetCompoundModalAnalysis"],
        "_4750": ["BevelDifferentialPlanetGearCompoundModalAnalysis"],
        "_4751": ["BevelDifferentialSunGearCompoundModalAnalysis"],
        "_4752": ["BevelGearCompoundModalAnalysis"],
        "_4753": ["BevelGearMeshCompoundModalAnalysis"],
        "_4754": ["BevelGearSetCompoundModalAnalysis"],
        "_4755": ["BoltCompoundModalAnalysis"],
        "_4756": ["BoltedJointCompoundModalAnalysis"],
        "_4757": ["ClutchCompoundModalAnalysis"],
        "_4758": ["ClutchConnectionCompoundModalAnalysis"],
        "_4759": ["ClutchHalfCompoundModalAnalysis"],
        "_4760": ["CoaxialConnectionCompoundModalAnalysis"],
        "_4761": ["ComponentCompoundModalAnalysis"],
        "_4762": ["ConceptCouplingCompoundModalAnalysis"],
        "_4763": ["ConceptCouplingConnectionCompoundModalAnalysis"],
        "_4764": ["ConceptCouplingHalfCompoundModalAnalysis"],
        "_4765": ["ConceptGearCompoundModalAnalysis"],
        "_4766": ["ConceptGearMeshCompoundModalAnalysis"],
        "_4767": ["ConceptGearSetCompoundModalAnalysis"],
        "_4768": ["ConicalGearCompoundModalAnalysis"],
        "_4769": ["ConicalGearMeshCompoundModalAnalysis"],
        "_4770": ["ConicalGearSetCompoundModalAnalysis"],
        "_4771": ["ConnectionCompoundModalAnalysis"],
        "_4772": ["ConnectorCompoundModalAnalysis"],
        "_4773": ["CouplingCompoundModalAnalysis"],
        "_4774": ["CouplingConnectionCompoundModalAnalysis"],
        "_4775": ["CouplingHalfCompoundModalAnalysis"],
        "_4776": ["CVTBeltConnectionCompoundModalAnalysis"],
        "_4777": ["CVTCompoundModalAnalysis"],
        "_4778": ["CVTPulleyCompoundModalAnalysis"],
        "_4779": ["CycloidalAssemblyCompoundModalAnalysis"],
        "_4780": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"],
        "_4781": ["CycloidalDiscCompoundModalAnalysis"],
        "_4782": ["CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"],
        "_4783": ["CylindricalGearCompoundModalAnalysis"],
        "_4784": ["CylindricalGearMeshCompoundModalAnalysis"],
        "_4785": ["CylindricalGearSetCompoundModalAnalysis"],
        "_4786": ["CylindricalPlanetGearCompoundModalAnalysis"],
        "_4787": ["DatumCompoundModalAnalysis"],
        "_4788": ["ExternalCADModelCompoundModalAnalysis"],
        "_4789": ["FaceGearCompoundModalAnalysis"],
        "_4790": ["FaceGearMeshCompoundModalAnalysis"],
        "_4791": ["FaceGearSetCompoundModalAnalysis"],
        "_4792": ["FEPartCompoundModalAnalysis"],
        "_4793": ["FlexiblePinAssemblyCompoundModalAnalysis"],
        "_4794": ["GearCompoundModalAnalysis"],
        "_4795": ["GearMeshCompoundModalAnalysis"],
        "_4796": ["GearSetCompoundModalAnalysis"],
        "_4797": ["GuideDxfModelCompoundModalAnalysis"],
        "_4798": ["HypoidGearCompoundModalAnalysis"],
        "_4799": ["HypoidGearMeshCompoundModalAnalysis"],
        "_4800": ["HypoidGearSetCompoundModalAnalysis"],
        "_4801": ["InterMountableComponentConnectionCompoundModalAnalysis"],
        "_4802": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"],
        "_4803": ["KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"],
        "_4804": ["KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"],
        "_4805": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"],
        "_4806": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis"],
        "_4807": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"],
        "_4808": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"],
        "_4809": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis"],
        "_4810": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"],
        "_4811": ["MassDiscCompoundModalAnalysis"],
        "_4812": ["MeasurementComponentCompoundModalAnalysis"],
        "_4813": ["MountableComponentCompoundModalAnalysis"],
        "_4814": ["OilSealCompoundModalAnalysis"],
        "_4815": ["PartCompoundModalAnalysis"],
        "_4816": ["PartToPartShearCouplingCompoundModalAnalysis"],
        "_4817": ["PartToPartShearCouplingConnectionCompoundModalAnalysis"],
        "_4818": ["PartToPartShearCouplingHalfCompoundModalAnalysis"],
        "_4819": ["PlanetaryConnectionCompoundModalAnalysis"],
        "_4820": ["PlanetaryGearSetCompoundModalAnalysis"],
        "_4821": ["PlanetCarrierCompoundModalAnalysis"],
        "_4822": ["PointLoadCompoundModalAnalysis"],
        "_4823": ["PowerLoadCompoundModalAnalysis"],
        "_4824": ["PulleyCompoundModalAnalysis"],
        "_4825": ["RingPinsCompoundModalAnalysis"],
        "_4826": ["RingPinsToDiscConnectionCompoundModalAnalysis"],
        "_4827": ["RollingRingAssemblyCompoundModalAnalysis"],
        "_4828": ["RollingRingCompoundModalAnalysis"],
        "_4829": ["RollingRingConnectionCompoundModalAnalysis"],
        "_4830": ["RootAssemblyCompoundModalAnalysis"],
        "_4831": ["ShaftCompoundModalAnalysis"],
        "_4832": ["ShaftHubConnectionCompoundModalAnalysis"],
        "_4833": ["ShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4834": ["SpecialisedAssemblyCompoundModalAnalysis"],
        "_4835": ["SpiralBevelGearCompoundModalAnalysis"],
        "_4836": ["SpiralBevelGearMeshCompoundModalAnalysis"],
        "_4837": ["SpiralBevelGearSetCompoundModalAnalysis"],
        "_4838": ["SpringDamperCompoundModalAnalysis"],
        "_4839": ["SpringDamperConnectionCompoundModalAnalysis"],
        "_4840": ["SpringDamperHalfCompoundModalAnalysis"],
        "_4841": ["StraightBevelDiffGearCompoundModalAnalysis"],
        "_4842": ["StraightBevelDiffGearMeshCompoundModalAnalysis"],
        "_4843": ["StraightBevelDiffGearSetCompoundModalAnalysis"],
        "_4844": ["StraightBevelGearCompoundModalAnalysis"],
        "_4845": ["StraightBevelGearMeshCompoundModalAnalysis"],
        "_4846": ["StraightBevelGearSetCompoundModalAnalysis"],
        "_4847": ["StraightBevelPlanetGearCompoundModalAnalysis"],
        "_4848": ["StraightBevelSunGearCompoundModalAnalysis"],
        "_4849": ["SynchroniserCompoundModalAnalysis"],
        "_4850": ["SynchroniserHalfCompoundModalAnalysis"],
        "_4851": ["SynchroniserPartCompoundModalAnalysis"],
        "_4852": ["SynchroniserSleeveCompoundModalAnalysis"],
        "_4853": ["TorqueConverterCompoundModalAnalysis"],
        "_4854": ["TorqueConverterConnectionCompoundModalAnalysis"],
        "_4855": ["TorqueConverterPumpCompoundModalAnalysis"],
        "_4856": ["TorqueConverterTurbineCompoundModalAnalysis"],
        "_4857": ["UnbalancedMassCompoundModalAnalysis"],
        "_4858": ["VirtualComponentCompoundModalAnalysis"],
        "_4859": ["WormGearCompoundModalAnalysis"],
        "_4860": ["WormGearMeshCompoundModalAnalysis"],
        "_4861": ["WormGearSetCompoundModalAnalysis"],
        "_4862": ["ZerolBevelGearCompoundModalAnalysis"],
        "_4863": ["ZerolBevelGearMeshCompoundModalAnalysis"],
        "_4864": ["ZerolBevelGearSetCompoundModalAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysis",
    "AbstractShaftCompoundModalAnalysis",
    "AbstractShaftOrHousingCompoundModalAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
    "AssemblyCompoundModalAnalysis",
    "BearingCompoundModalAnalysis",
    "BeltConnectionCompoundModalAnalysis",
    "BeltDriveCompoundModalAnalysis",
    "BevelDifferentialGearCompoundModalAnalysis",
    "BevelDifferentialGearMeshCompoundModalAnalysis",
    "BevelDifferentialGearSetCompoundModalAnalysis",
    "BevelDifferentialPlanetGearCompoundModalAnalysis",
    "BevelDifferentialSunGearCompoundModalAnalysis",
    "BevelGearCompoundModalAnalysis",
    "BevelGearMeshCompoundModalAnalysis",
    "BevelGearSetCompoundModalAnalysis",
    "BoltCompoundModalAnalysis",
    "BoltedJointCompoundModalAnalysis",
    "ClutchCompoundModalAnalysis",
    "ClutchConnectionCompoundModalAnalysis",
    "ClutchHalfCompoundModalAnalysis",
    "CoaxialConnectionCompoundModalAnalysis",
    "ComponentCompoundModalAnalysis",
    "ConceptCouplingCompoundModalAnalysis",
    "ConceptCouplingConnectionCompoundModalAnalysis",
    "ConceptCouplingHalfCompoundModalAnalysis",
    "ConceptGearCompoundModalAnalysis",
    "ConceptGearMeshCompoundModalAnalysis",
    "ConceptGearSetCompoundModalAnalysis",
    "ConicalGearCompoundModalAnalysis",
    "ConicalGearMeshCompoundModalAnalysis",
    "ConicalGearSetCompoundModalAnalysis",
    "ConnectionCompoundModalAnalysis",
    "ConnectorCompoundModalAnalysis",
    "CouplingCompoundModalAnalysis",
    "CouplingConnectionCompoundModalAnalysis",
    "CouplingHalfCompoundModalAnalysis",
    "CVTBeltConnectionCompoundModalAnalysis",
    "CVTCompoundModalAnalysis",
    "CVTPulleyCompoundModalAnalysis",
    "CycloidalAssemblyCompoundModalAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
    "CycloidalDiscCompoundModalAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    "CylindricalGearCompoundModalAnalysis",
    "CylindricalGearMeshCompoundModalAnalysis",
    "CylindricalGearSetCompoundModalAnalysis",
    "CylindricalPlanetGearCompoundModalAnalysis",
    "DatumCompoundModalAnalysis",
    "ExternalCADModelCompoundModalAnalysis",
    "FaceGearCompoundModalAnalysis",
    "FaceGearMeshCompoundModalAnalysis",
    "FaceGearSetCompoundModalAnalysis",
    "FEPartCompoundModalAnalysis",
    "FlexiblePinAssemblyCompoundModalAnalysis",
    "GearCompoundModalAnalysis",
    "GearMeshCompoundModalAnalysis",
    "GearSetCompoundModalAnalysis",
    "GuideDxfModelCompoundModalAnalysis",
    "HypoidGearCompoundModalAnalysis",
    "HypoidGearMeshCompoundModalAnalysis",
    "HypoidGearSetCompoundModalAnalysis",
    "InterMountableComponentConnectionCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    "MassDiscCompoundModalAnalysis",
    "MeasurementComponentCompoundModalAnalysis",
    "MountableComponentCompoundModalAnalysis",
    "OilSealCompoundModalAnalysis",
    "PartCompoundModalAnalysis",
    "PartToPartShearCouplingCompoundModalAnalysis",
    "PartToPartShearCouplingConnectionCompoundModalAnalysis",
    "PartToPartShearCouplingHalfCompoundModalAnalysis",
    "PlanetaryConnectionCompoundModalAnalysis",
    "PlanetaryGearSetCompoundModalAnalysis",
    "PlanetCarrierCompoundModalAnalysis",
    "PointLoadCompoundModalAnalysis",
    "PowerLoadCompoundModalAnalysis",
    "PulleyCompoundModalAnalysis",
    "RingPinsCompoundModalAnalysis",
    "RingPinsToDiscConnectionCompoundModalAnalysis",
    "RollingRingAssemblyCompoundModalAnalysis",
    "RollingRingCompoundModalAnalysis",
    "RollingRingConnectionCompoundModalAnalysis",
    "RootAssemblyCompoundModalAnalysis",
    "ShaftCompoundModalAnalysis",
    "ShaftHubConnectionCompoundModalAnalysis",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
    "SpecialisedAssemblyCompoundModalAnalysis",
    "SpiralBevelGearCompoundModalAnalysis",
    "SpiralBevelGearMeshCompoundModalAnalysis",
    "SpiralBevelGearSetCompoundModalAnalysis",
    "SpringDamperCompoundModalAnalysis",
    "SpringDamperConnectionCompoundModalAnalysis",
    "SpringDamperHalfCompoundModalAnalysis",
    "StraightBevelDiffGearCompoundModalAnalysis",
    "StraightBevelDiffGearMeshCompoundModalAnalysis",
    "StraightBevelDiffGearSetCompoundModalAnalysis",
    "StraightBevelGearCompoundModalAnalysis",
    "StraightBevelGearMeshCompoundModalAnalysis",
    "StraightBevelGearSetCompoundModalAnalysis",
    "StraightBevelPlanetGearCompoundModalAnalysis",
    "StraightBevelSunGearCompoundModalAnalysis",
    "SynchroniserCompoundModalAnalysis",
    "SynchroniserHalfCompoundModalAnalysis",
    "SynchroniserPartCompoundModalAnalysis",
    "SynchroniserSleeveCompoundModalAnalysis",
    "TorqueConverterCompoundModalAnalysis",
    "TorqueConverterConnectionCompoundModalAnalysis",
    "TorqueConverterPumpCompoundModalAnalysis",
    "TorqueConverterTurbineCompoundModalAnalysis",
    "UnbalancedMassCompoundModalAnalysis",
    "VirtualComponentCompoundModalAnalysis",
    "WormGearCompoundModalAnalysis",
    "WormGearMeshCompoundModalAnalysis",
    "WormGearSetCompoundModalAnalysis",
    "ZerolBevelGearCompoundModalAnalysis",
    "ZerolBevelGearMeshCompoundModalAnalysis",
    "ZerolBevelGearSetCompoundModalAnalysis",
)
