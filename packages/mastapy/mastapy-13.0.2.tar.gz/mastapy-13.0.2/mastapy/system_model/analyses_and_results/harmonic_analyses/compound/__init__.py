"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5887 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5888 import AbstractShaftCompoundHarmonicAnalysis
    from ._5889 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5890 import (
        AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis,
    )
    from ._5891 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5892 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5893 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5894 import AssemblyCompoundHarmonicAnalysis
    from ._5895 import BearingCompoundHarmonicAnalysis
    from ._5896 import BeltConnectionCompoundHarmonicAnalysis
    from ._5897 import BeltDriveCompoundHarmonicAnalysis
    from ._5898 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5899 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5900 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5901 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5902 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5903 import BevelGearCompoundHarmonicAnalysis
    from ._5904 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5905 import BevelGearSetCompoundHarmonicAnalysis
    from ._5906 import BoltCompoundHarmonicAnalysis
    from ._5907 import BoltedJointCompoundHarmonicAnalysis
    from ._5908 import ClutchCompoundHarmonicAnalysis
    from ._5909 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5910 import ClutchHalfCompoundHarmonicAnalysis
    from ._5911 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5912 import ComponentCompoundHarmonicAnalysis
    from ._5913 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5914 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5915 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5916 import ConceptGearCompoundHarmonicAnalysis
    from ._5917 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5918 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5919 import ConicalGearCompoundHarmonicAnalysis
    from ._5920 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5921 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5922 import ConnectionCompoundHarmonicAnalysis
    from ._5923 import ConnectorCompoundHarmonicAnalysis
    from ._5924 import CouplingCompoundHarmonicAnalysis
    from ._5925 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5926 import CouplingHalfCompoundHarmonicAnalysis
    from ._5927 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5928 import CVTCompoundHarmonicAnalysis
    from ._5929 import CVTPulleyCompoundHarmonicAnalysis
    from ._5930 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5931 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5932 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5933 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5934 import CylindricalGearCompoundHarmonicAnalysis
    from ._5935 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5936 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5937 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5938 import DatumCompoundHarmonicAnalysis
    from ._5939 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5940 import FaceGearCompoundHarmonicAnalysis
    from ._5941 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5942 import FaceGearSetCompoundHarmonicAnalysis
    from ._5943 import FEPartCompoundHarmonicAnalysis
    from ._5944 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5945 import GearCompoundHarmonicAnalysis
    from ._5946 import GearMeshCompoundHarmonicAnalysis
    from ._5947 import GearSetCompoundHarmonicAnalysis
    from ._5948 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5949 import HypoidGearCompoundHarmonicAnalysis
    from ._5950 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5951 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5952 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5953 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5954 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5955 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5956 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5957 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5958 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5959 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5960 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis,
    )
    from ._5961 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis,
    )
    from ._5962 import MassDiscCompoundHarmonicAnalysis
    from ._5963 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5964 import MountableComponentCompoundHarmonicAnalysis
    from ._5965 import OilSealCompoundHarmonicAnalysis
    from ._5966 import PartCompoundHarmonicAnalysis
    from ._5967 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5968 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5969 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5970 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5971 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5972 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5973 import PointLoadCompoundHarmonicAnalysis
    from ._5974 import PowerLoadCompoundHarmonicAnalysis
    from ._5975 import PulleyCompoundHarmonicAnalysis
    from ._5976 import RingPinsCompoundHarmonicAnalysis
    from ._5977 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5978 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5979 import RollingRingCompoundHarmonicAnalysis
    from ._5980 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5981 import RootAssemblyCompoundHarmonicAnalysis
    from ._5982 import ShaftCompoundHarmonicAnalysis
    from ._5983 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._5984 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5985 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._5986 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._5987 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._5988 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._5989 import SpringDamperCompoundHarmonicAnalysis
    from ._5990 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._5991 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._5992 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._5993 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._5994 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._5995 import StraightBevelGearCompoundHarmonicAnalysis
    from ._5996 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._5997 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._5998 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._5999 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._6000 import SynchroniserCompoundHarmonicAnalysis
    from ._6001 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._6002 import SynchroniserPartCompoundHarmonicAnalysis
    from ._6003 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._6004 import TorqueConverterCompoundHarmonicAnalysis
    from ._6005 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._6006 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._6007 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._6008 import UnbalancedMassCompoundHarmonicAnalysis
    from ._6009 import VirtualComponentCompoundHarmonicAnalysis
    from ._6010 import WormGearCompoundHarmonicAnalysis
    from ._6011 import WormGearMeshCompoundHarmonicAnalysis
    from ._6012 import WormGearSetCompoundHarmonicAnalysis
    from ._6013 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._6014 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._6015 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        "_5887": ["AbstractAssemblyCompoundHarmonicAnalysis"],
        "_5888": ["AbstractShaftCompoundHarmonicAnalysis"],
        "_5889": ["AbstractShaftOrHousingCompoundHarmonicAnalysis"],
        "_5890": [
            "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ],
        "_5891": ["AGMAGleasonConicalGearCompoundHarmonicAnalysis"],
        "_5892": ["AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"],
        "_5893": ["AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"],
        "_5894": ["AssemblyCompoundHarmonicAnalysis"],
        "_5895": ["BearingCompoundHarmonicAnalysis"],
        "_5896": ["BeltConnectionCompoundHarmonicAnalysis"],
        "_5897": ["BeltDriveCompoundHarmonicAnalysis"],
        "_5898": ["BevelDifferentialGearCompoundHarmonicAnalysis"],
        "_5899": ["BevelDifferentialGearMeshCompoundHarmonicAnalysis"],
        "_5900": ["BevelDifferentialGearSetCompoundHarmonicAnalysis"],
        "_5901": ["BevelDifferentialPlanetGearCompoundHarmonicAnalysis"],
        "_5902": ["BevelDifferentialSunGearCompoundHarmonicAnalysis"],
        "_5903": ["BevelGearCompoundHarmonicAnalysis"],
        "_5904": ["BevelGearMeshCompoundHarmonicAnalysis"],
        "_5905": ["BevelGearSetCompoundHarmonicAnalysis"],
        "_5906": ["BoltCompoundHarmonicAnalysis"],
        "_5907": ["BoltedJointCompoundHarmonicAnalysis"],
        "_5908": ["ClutchCompoundHarmonicAnalysis"],
        "_5909": ["ClutchConnectionCompoundHarmonicAnalysis"],
        "_5910": ["ClutchHalfCompoundHarmonicAnalysis"],
        "_5911": ["CoaxialConnectionCompoundHarmonicAnalysis"],
        "_5912": ["ComponentCompoundHarmonicAnalysis"],
        "_5913": ["ConceptCouplingCompoundHarmonicAnalysis"],
        "_5914": ["ConceptCouplingConnectionCompoundHarmonicAnalysis"],
        "_5915": ["ConceptCouplingHalfCompoundHarmonicAnalysis"],
        "_5916": ["ConceptGearCompoundHarmonicAnalysis"],
        "_5917": ["ConceptGearMeshCompoundHarmonicAnalysis"],
        "_5918": ["ConceptGearSetCompoundHarmonicAnalysis"],
        "_5919": ["ConicalGearCompoundHarmonicAnalysis"],
        "_5920": ["ConicalGearMeshCompoundHarmonicAnalysis"],
        "_5921": ["ConicalGearSetCompoundHarmonicAnalysis"],
        "_5922": ["ConnectionCompoundHarmonicAnalysis"],
        "_5923": ["ConnectorCompoundHarmonicAnalysis"],
        "_5924": ["CouplingCompoundHarmonicAnalysis"],
        "_5925": ["CouplingConnectionCompoundHarmonicAnalysis"],
        "_5926": ["CouplingHalfCompoundHarmonicAnalysis"],
        "_5927": ["CVTBeltConnectionCompoundHarmonicAnalysis"],
        "_5928": ["CVTCompoundHarmonicAnalysis"],
        "_5929": ["CVTPulleyCompoundHarmonicAnalysis"],
        "_5930": ["CycloidalAssemblyCompoundHarmonicAnalysis"],
        "_5931": ["CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"],
        "_5932": ["CycloidalDiscCompoundHarmonicAnalysis"],
        "_5933": ["CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis"],
        "_5934": ["CylindricalGearCompoundHarmonicAnalysis"],
        "_5935": ["CylindricalGearMeshCompoundHarmonicAnalysis"],
        "_5936": ["CylindricalGearSetCompoundHarmonicAnalysis"],
        "_5937": ["CylindricalPlanetGearCompoundHarmonicAnalysis"],
        "_5938": ["DatumCompoundHarmonicAnalysis"],
        "_5939": ["ExternalCADModelCompoundHarmonicAnalysis"],
        "_5940": ["FaceGearCompoundHarmonicAnalysis"],
        "_5941": ["FaceGearMeshCompoundHarmonicAnalysis"],
        "_5942": ["FaceGearSetCompoundHarmonicAnalysis"],
        "_5943": ["FEPartCompoundHarmonicAnalysis"],
        "_5944": ["FlexiblePinAssemblyCompoundHarmonicAnalysis"],
        "_5945": ["GearCompoundHarmonicAnalysis"],
        "_5946": ["GearMeshCompoundHarmonicAnalysis"],
        "_5947": ["GearSetCompoundHarmonicAnalysis"],
        "_5948": ["GuideDxfModelCompoundHarmonicAnalysis"],
        "_5949": ["HypoidGearCompoundHarmonicAnalysis"],
        "_5950": ["HypoidGearMeshCompoundHarmonicAnalysis"],
        "_5951": ["HypoidGearSetCompoundHarmonicAnalysis"],
        "_5952": ["InterMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5953": ["KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"],
        "_5954": ["KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"],
        "_5955": ["KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"],
        "_5956": ["KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"],
        "_5957": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"],
        "_5958": ["KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis"],
        "_5959": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"],
        "_5960": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ],
        "_5961": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5962": ["MassDiscCompoundHarmonicAnalysis"],
        "_5963": ["MeasurementComponentCompoundHarmonicAnalysis"],
        "_5964": ["MountableComponentCompoundHarmonicAnalysis"],
        "_5965": ["OilSealCompoundHarmonicAnalysis"],
        "_5966": ["PartCompoundHarmonicAnalysis"],
        "_5967": ["PartToPartShearCouplingCompoundHarmonicAnalysis"],
        "_5968": ["PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"],
        "_5969": ["PartToPartShearCouplingHalfCompoundHarmonicAnalysis"],
        "_5970": ["PlanetaryConnectionCompoundHarmonicAnalysis"],
        "_5971": ["PlanetaryGearSetCompoundHarmonicAnalysis"],
        "_5972": ["PlanetCarrierCompoundHarmonicAnalysis"],
        "_5973": ["PointLoadCompoundHarmonicAnalysis"],
        "_5974": ["PowerLoadCompoundHarmonicAnalysis"],
        "_5975": ["PulleyCompoundHarmonicAnalysis"],
        "_5976": ["RingPinsCompoundHarmonicAnalysis"],
        "_5977": ["RingPinsToDiscConnectionCompoundHarmonicAnalysis"],
        "_5978": ["RollingRingAssemblyCompoundHarmonicAnalysis"],
        "_5979": ["RollingRingCompoundHarmonicAnalysis"],
        "_5980": ["RollingRingConnectionCompoundHarmonicAnalysis"],
        "_5981": ["RootAssemblyCompoundHarmonicAnalysis"],
        "_5982": ["ShaftCompoundHarmonicAnalysis"],
        "_5983": ["ShaftHubConnectionCompoundHarmonicAnalysis"],
        "_5984": ["ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5985": ["SpecialisedAssemblyCompoundHarmonicAnalysis"],
        "_5986": ["SpiralBevelGearCompoundHarmonicAnalysis"],
        "_5987": ["SpiralBevelGearMeshCompoundHarmonicAnalysis"],
        "_5988": ["SpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5989": ["SpringDamperCompoundHarmonicAnalysis"],
        "_5990": ["SpringDamperConnectionCompoundHarmonicAnalysis"],
        "_5991": ["SpringDamperHalfCompoundHarmonicAnalysis"],
        "_5992": ["StraightBevelDiffGearCompoundHarmonicAnalysis"],
        "_5993": ["StraightBevelDiffGearMeshCompoundHarmonicAnalysis"],
        "_5994": ["StraightBevelDiffGearSetCompoundHarmonicAnalysis"],
        "_5995": ["StraightBevelGearCompoundHarmonicAnalysis"],
        "_5996": ["StraightBevelGearMeshCompoundHarmonicAnalysis"],
        "_5997": ["StraightBevelGearSetCompoundHarmonicAnalysis"],
        "_5998": ["StraightBevelPlanetGearCompoundHarmonicAnalysis"],
        "_5999": ["StraightBevelSunGearCompoundHarmonicAnalysis"],
        "_6000": ["SynchroniserCompoundHarmonicAnalysis"],
        "_6001": ["SynchroniserHalfCompoundHarmonicAnalysis"],
        "_6002": ["SynchroniserPartCompoundHarmonicAnalysis"],
        "_6003": ["SynchroniserSleeveCompoundHarmonicAnalysis"],
        "_6004": ["TorqueConverterCompoundHarmonicAnalysis"],
        "_6005": ["TorqueConverterConnectionCompoundHarmonicAnalysis"],
        "_6006": ["TorqueConverterPumpCompoundHarmonicAnalysis"],
        "_6007": ["TorqueConverterTurbineCompoundHarmonicAnalysis"],
        "_6008": ["UnbalancedMassCompoundHarmonicAnalysis"],
        "_6009": ["VirtualComponentCompoundHarmonicAnalysis"],
        "_6010": ["WormGearCompoundHarmonicAnalysis"],
        "_6011": ["WormGearMeshCompoundHarmonicAnalysis"],
        "_6012": ["WormGearSetCompoundHarmonicAnalysis"],
        "_6013": ["ZerolBevelGearCompoundHarmonicAnalysis"],
        "_6014": ["ZerolBevelGearMeshCompoundHarmonicAnalysis"],
        "_6015": ["ZerolBevelGearSetCompoundHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundHarmonicAnalysis",
    "AbstractShaftCompoundHarmonicAnalysis",
    "AbstractShaftOrHousingCompoundHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
    "AssemblyCompoundHarmonicAnalysis",
    "BearingCompoundHarmonicAnalysis",
    "BeltConnectionCompoundHarmonicAnalysis",
    "BeltDriveCompoundHarmonicAnalysis",
    "BevelDifferentialGearCompoundHarmonicAnalysis",
    "BevelDifferentialGearMeshCompoundHarmonicAnalysis",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
    "BevelDifferentialSunGearCompoundHarmonicAnalysis",
    "BevelGearCompoundHarmonicAnalysis",
    "BevelGearMeshCompoundHarmonicAnalysis",
    "BevelGearSetCompoundHarmonicAnalysis",
    "BoltCompoundHarmonicAnalysis",
    "BoltedJointCompoundHarmonicAnalysis",
    "ClutchCompoundHarmonicAnalysis",
    "ClutchConnectionCompoundHarmonicAnalysis",
    "ClutchHalfCompoundHarmonicAnalysis",
    "CoaxialConnectionCompoundHarmonicAnalysis",
    "ComponentCompoundHarmonicAnalysis",
    "ConceptCouplingCompoundHarmonicAnalysis",
    "ConceptCouplingConnectionCompoundHarmonicAnalysis",
    "ConceptCouplingHalfCompoundHarmonicAnalysis",
    "ConceptGearCompoundHarmonicAnalysis",
    "ConceptGearMeshCompoundHarmonicAnalysis",
    "ConceptGearSetCompoundHarmonicAnalysis",
    "ConicalGearCompoundHarmonicAnalysis",
    "ConicalGearMeshCompoundHarmonicAnalysis",
    "ConicalGearSetCompoundHarmonicAnalysis",
    "ConnectionCompoundHarmonicAnalysis",
    "ConnectorCompoundHarmonicAnalysis",
    "CouplingCompoundHarmonicAnalysis",
    "CouplingConnectionCompoundHarmonicAnalysis",
    "CouplingHalfCompoundHarmonicAnalysis",
    "CVTBeltConnectionCompoundHarmonicAnalysis",
    "CVTCompoundHarmonicAnalysis",
    "CVTPulleyCompoundHarmonicAnalysis",
    "CycloidalAssemblyCompoundHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    "CycloidalDiscCompoundHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis",
    "CylindricalGearCompoundHarmonicAnalysis",
    "CylindricalGearMeshCompoundHarmonicAnalysis",
    "CylindricalGearSetCompoundHarmonicAnalysis",
    "CylindricalPlanetGearCompoundHarmonicAnalysis",
    "DatumCompoundHarmonicAnalysis",
    "ExternalCADModelCompoundHarmonicAnalysis",
    "FaceGearCompoundHarmonicAnalysis",
    "FaceGearMeshCompoundHarmonicAnalysis",
    "FaceGearSetCompoundHarmonicAnalysis",
    "FEPartCompoundHarmonicAnalysis",
    "FlexiblePinAssemblyCompoundHarmonicAnalysis",
    "GearCompoundHarmonicAnalysis",
    "GearMeshCompoundHarmonicAnalysis",
    "GearSetCompoundHarmonicAnalysis",
    "GuideDxfModelCompoundHarmonicAnalysis",
    "HypoidGearCompoundHarmonicAnalysis",
    "HypoidGearMeshCompoundHarmonicAnalysis",
    "HypoidGearSetCompoundHarmonicAnalysis",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    "MassDiscCompoundHarmonicAnalysis",
    "MeasurementComponentCompoundHarmonicAnalysis",
    "MountableComponentCompoundHarmonicAnalysis",
    "OilSealCompoundHarmonicAnalysis",
    "PartCompoundHarmonicAnalysis",
    "PartToPartShearCouplingCompoundHarmonicAnalysis",
    "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
    "PartToPartShearCouplingHalfCompoundHarmonicAnalysis",
    "PlanetaryConnectionCompoundHarmonicAnalysis",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
    "PlanetCarrierCompoundHarmonicAnalysis",
    "PointLoadCompoundHarmonicAnalysis",
    "PowerLoadCompoundHarmonicAnalysis",
    "PulleyCompoundHarmonicAnalysis",
    "RingPinsCompoundHarmonicAnalysis",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
    "RollingRingAssemblyCompoundHarmonicAnalysis",
    "RollingRingCompoundHarmonicAnalysis",
    "RollingRingConnectionCompoundHarmonicAnalysis",
    "RootAssemblyCompoundHarmonicAnalysis",
    "ShaftCompoundHarmonicAnalysis",
    "ShaftHubConnectionCompoundHarmonicAnalysis",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "SpecialisedAssemblyCompoundHarmonicAnalysis",
    "SpiralBevelGearCompoundHarmonicAnalysis",
    "SpiralBevelGearMeshCompoundHarmonicAnalysis",
    "SpiralBevelGearSetCompoundHarmonicAnalysis",
    "SpringDamperCompoundHarmonicAnalysis",
    "SpringDamperConnectionCompoundHarmonicAnalysis",
    "SpringDamperHalfCompoundHarmonicAnalysis",
    "StraightBevelDiffGearCompoundHarmonicAnalysis",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
    "StraightBevelGearCompoundHarmonicAnalysis",
    "StraightBevelGearMeshCompoundHarmonicAnalysis",
    "StraightBevelGearSetCompoundHarmonicAnalysis",
    "StraightBevelPlanetGearCompoundHarmonicAnalysis",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
    "SynchroniserCompoundHarmonicAnalysis",
    "SynchroniserHalfCompoundHarmonicAnalysis",
    "SynchroniserPartCompoundHarmonicAnalysis",
    "SynchroniserSleeveCompoundHarmonicAnalysis",
    "TorqueConverterCompoundHarmonicAnalysis",
    "TorqueConverterConnectionCompoundHarmonicAnalysis",
    "TorqueConverterPumpCompoundHarmonicAnalysis",
    "TorqueConverterTurbineCompoundHarmonicAnalysis",
    "UnbalancedMassCompoundHarmonicAnalysis",
    "VirtualComponentCompoundHarmonicAnalysis",
    "WormGearCompoundHarmonicAnalysis",
    "WormGearMeshCompoundHarmonicAnalysis",
    "WormGearSetCompoundHarmonicAnalysis",
    "ZerolBevelGearCompoundHarmonicAnalysis",
    "ZerolBevelGearMeshCompoundHarmonicAnalysis",
    "ZerolBevelGearSetCompoundHarmonicAnalysis",
)
