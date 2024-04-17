"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4996 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._4997 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._4998 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._4999 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5000 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._5001 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5002 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5003 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._5004 import BearingCompoundModalAnalysisAtAStiffness
    from ._5005 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5006 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._5007 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._5008 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._5009 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._5010 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5011 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._5012 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._5013 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5014 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5015 import BoltCompoundModalAnalysisAtAStiffness
    from ._5016 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._5017 import ClutchCompoundModalAnalysisAtAStiffness
    from ._5018 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._5019 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._5020 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._5021 import ComponentCompoundModalAnalysisAtAStiffness
    from ._5022 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._5023 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5024 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5025 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._5026 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._5027 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._5028 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._5029 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5030 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5031 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._5032 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5033 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5034 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5035 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5036 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5037 import CVTCompoundModalAnalysisAtAStiffness
    from ._5038 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5039 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5040 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5041 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5042 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5043 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5044 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5045 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5046 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5047 import DatumCompoundModalAnalysisAtAStiffness
    from ._5048 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5049 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5050 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5051 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5052 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5053 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5054 import GearCompoundModalAnalysisAtAStiffness
    from ._5055 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5056 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5057 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5058 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5059 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5060 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5061 import (
        InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5062 import (
        KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5063 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5064 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5065 import (
        KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5066 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5067 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5068 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5069 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5070 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5071 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5072 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5073 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5074 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5075 import PartCompoundModalAnalysisAtAStiffness
    from ._5076 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5077 import (
        PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5078 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5079 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5080 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5081 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5082 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5083 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5084 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5085 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5086 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5087 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5088 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5089 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5090 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5091 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5092 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5093 import (
        ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5094 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5095 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5096 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5097 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5098 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5099 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5100 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5101 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5102 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5103 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5104 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5105 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5106 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5107 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5108 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5109 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5110 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5111 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5112 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5113 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5114 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5115 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5116 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5117 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5118 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5119 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5120 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5121 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5122 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5123 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5124 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        "_4996": ["AbstractAssemblyCompoundModalAnalysisAtAStiffness"],
        "_4997": ["AbstractShaftCompoundModalAnalysisAtAStiffness"],
        "_4998": ["AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"],
        "_4999": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5000": ["AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5001": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5002": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5003": ["AssemblyCompoundModalAnalysisAtAStiffness"],
        "_5004": ["BearingCompoundModalAnalysisAtAStiffness"],
        "_5005": ["BeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5006": ["BeltDriveCompoundModalAnalysisAtAStiffness"],
        "_5007": ["BevelDifferentialGearCompoundModalAnalysisAtAStiffness"],
        "_5008": ["BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5009": ["BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"],
        "_5010": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5011": ["BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness"],
        "_5012": ["BevelGearCompoundModalAnalysisAtAStiffness"],
        "_5013": ["BevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5014": ["BevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5015": ["BoltCompoundModalAnalysisAtAStiffness"],
        "_5016": ["BoltedJointCompoundModalAnalysisAtAStiffness"],
        "_5017": ["ClutchCompoundModalAnalysisAtAStiffness"],
        "_5018": ["ClutchConnectionCompoundModalAnalysisAtAStiffness"],
        "_5019": ["ClutchHalfCompoundModalAnalysisAtAStiffness"],
        "_5020": ["CoaxialConnectionCompoundModalAnalysisAtAStiffness"],
        "_5021": ["ComponentCompoundModalAnalysisAtAStiffness"],
        "_5022": ["ConceptCouplingCompoundModalAnalysisAtAStiffness"],
        "_5023": ["ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5024": ["ConceptCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5025": ["ConceptGearCompoundModalAnalysisAtAStiffness"],
        "_5026": ["ConceptGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5027": ["ConceptGearSetCompoundModalAnalysisAtAStiffness"],
        "_5028": ["ConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5029": ["ConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5030": ["ConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5031": ["ConnectionCompoundModalAnalysisAtAStiffness"],
        "_5032": ["ConnectorCompoundModalAnalysisAtAStiffness"],
        "_5033": ["CouplingCompoundModalAnalysisAtAStiffness"],
        "_5034": ["CouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5035": ["CouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5036": ["CVTBeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5037": ["CVTCompoundModalAnalysisAtAStiffness"],
        "_5038": ["CVTPulleyCompoundModalAnalysisAtAStiffness"],
        "_5039": ["CycloidalAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5040": [
            "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5041": ["CycloidalDiscCompoundModalAnalysisAtAStiffness"],
        "_5042": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5043": ["CylindricalGearCompoundModalAnalysisAtAStiffness"],
        "_5044": ["CylindricalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5045": ["CylindricalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5046": ["CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5047": ["DatumCompoundModalAnalysisAtAStiffness"],
        "_5048": ["ExternalCADModelCompoundModalAnalysisAtAStiffness"],
        "_5049": ["FaceGearCompoundModalAnalysisAtAStiffness"],
        "_5050": ["FaceGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5051": ["FaceGearSetCompoundModalAnalysisAtAStiffness"],
        "_5052": ["FEPartCompoundModalAnalysisAtAStiffness"],
        "_5053": ["FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5054": ["GearCompoundModalAnalysisAtAStiffness"],
        "_5055": ["GearMeshCompoundModalAnalysisAtAStiffness"],
        "_5056": ["GearSetCompoundModalAnalysisAtAStiffness"],
        "_5057": ["GuideDxfModelCompoundModalAnalysisAtAStiffness"],
        "_5058": ["HypoidGearCompoundModalAnalysisAtAStiffness"],
        "_5059": ["HypoidGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5060": ["HypoidGearSetCompoundModalAnalysisAtAStiffness"],
        "_5061": ["InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"],
        "_5062": [
            "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5063": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5064": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5065": [
            "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5066": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5067": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5068": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5069": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5070": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5071": ["MassDiscCompoundModalAnalysisAtAStiffness"],
        "_5072": ["MeasurementComponentCompoundModalAnalysisAtAStiffness"],
        "_5073": ["MountableComponentCompoundModalAnalysisAtAStiffness"],
        "_5074": ["OilSealCompoundModalAnalysisAtAStiffness"],
        "_5075": ["PartCompoundModalAnalysisAtAStiffness"],
        "_5076": ["PartToPartShearCouplingCompoundModalAnalysisAtAStiffness"],
        "_5077": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5078": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5079": ["PlanetaryConnectionCompoundModalAnalysisAtAStiffness"],
        "_5080": ["PlanetaryGearSetCompoundModalAnalysisAtAStiffness"],
        "_5081": ["PlanetCarrierCompoundModalAnalysisAtAStiffness"],
        "_5082": ["PointLoadCompoundModalAnalysisAtAStiffness"],
        "_5083": ["PowerLoadCompoundModalAnalysisAtAStiffness"],
        "_5084": ["PulleyCompoundModalAnalysisAtAStiffness"],
        "_5085": ["RingPinsCompoundModalAnalysisAtAStiffness"],
        "_5086": ["RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"],
        "_5087": ["RollingRingAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5088": ["RollingRingCompoundModalAnalysisAtAStiffness"],
        "_5089": ["RollingRingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5090": ["RootAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5091": ["ShaftCompoundModalAnalysisAtAStiffness"],
        "_5092": ["ShaftHubConnectionCompoundModalAnalysisAtAStiffness"],
        "_5093": [
            "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5094": ["SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5095": ["SpiralBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5096": ["SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5097": ["SpiralBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5098": ["SpringDamperCompoundModalAnalysisAtAStiffness"],
        "_5099": ["SpringDamperConnectionCompoundModalAnalysisAtAStiffness"],
        "_5100": ["SpringDamperHalfCompoundModalAnalysisAtAStiffness"],
        "_5101": ["StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"],
        "_5102": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5103": ["StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness"],
        "_5104": ["StraightBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5105": ["StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5106": ["StraightBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5107": ["StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5108": ["StraightBevelSunGearCompoundModalAnalysisAtAStiffness"],
        "_5109": ["SynchroniserCompoundModalAnalysisAtAStiffness"],
        "_5110": ["SynchroniserHalfCompoundModalAnalysisAtAStiffness"],
        "_5111": ["SynchroniserPartCompoundModalAnalysisAtAStiffness"],
        "_5112": ["SynchroniserSleeveCompoundModalAnalysisAtAStiffness"],
        "_5113": ["TorqueConverterCompoundModalAnalysisAtAStiffness"],
        "_5114": ["TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"],
        "_5115": ["TorqueConverterPumpCompoundModalAnalysisAtAStiffness"],
        "_5116": ["TorqueConverterTurbineCompoundModalAnalysisAtAStiffness"],
        "_5117": ["UnbalancedMassCompoundModalAnalysisAtAStiffness"],
        "_5118": ["VirtualComponentCompoundModalAnalysisAtAStiffness"],
        "_5119": ["WormGearCompoundModalAnalysisAtAStiffness"],
        "_5120": ["WormGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5121": ["WormGearSetCompoundModalAnalysisAtAStiffness"],
        "_5122": ["ZerolBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5123": ["ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5124": ["ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
    "AbstractShaftCompoundModalAnalysisAtAStiffness",
    "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness",
    "AssemblyCompoundModalAnalysisAtAStiffness",
    "BearingCompoundModalAnalysisAtAStiffness",
    "BeltConnectionCompoundModalAnalysisAtAStiffness",
    "BeltDriveCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness",
    "BevelGearCompoundModalAnalysisAtAStiffness",
    "BevelGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelGearSetCompoundModalAnalysisAtAStiffness",
    "BoltCompoundModalAnalysisAtAStiffness",
    "BoltedJointCompoundModalAnalysisAtAStiffness",
    "ClutchCompoundModalAnalysisAtAStiffness",
    "ClutchConnectionCompoundModalAnalysisAtAStiffness",
    "ClutchHalfCompoundModalAnalysisAtAStiffness",
    "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
    "ComponentCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingHalfCompoundModalAnalysisAtAStiffness",
    "ConceptGearCompoundModalAnalysisAtAStiffness",
    "ConceptGearMeshCompoundModalAnalysisAtAStiffness",
    "ConceptGearSetCompoundModalAnalysisAtAStiffness",
    "ConicalGearCompoundModalAnalysisAtAStiffness",
    "ConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "ConicalGearSetCompoundModalAnalysisAtAStiffness",
    "ConnectionCompoundModalAnalysisAtAStiffness",
    "ConnectorCompoundModalAnalysisAtAStiffness",
    "CouplingCompoundModalAnalysisAtAStiffness",
    "CouplingConnectionCompoundModalAnalysisAtAStiffness",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
    "CVTCompoundModalAnalysisAtAStiffness",
    "CVTPulleyCompoundModalAnalysisAtAStiffness",
    "CycloidalAssemblyCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CylindricalGearCompoundModalAnalysisAtAStiffness",
    "CylindricalGearMeshCompoundModalAnalysisAtAStiffness",
    "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
    "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
    "DatumCompoundModalAnalysisAtAStiffness",
    "ExternalCADModelCompoundModalAnalysisAtAStiffness",
    "FaceGearCompoundModalAnalysisAtAStiffness",
    "FaceGearMeshCompoundModalAnalysisAtAStiffness",
    "FaceGearSetCompoundModalAnalysisAtAStiffness",
    "FEPartCompoundModalAnalysisAtAStiffness",
    "FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness",
    "GearCompoundModalAnalysisAtAStiffness",
    "GearMeshCompoundModalAnalysisAtAStiffness",
    "GearSetCompoundModalAnalysisAtAStiffness",
    "GuideDxfModelCompoundModalAnalysisAtAStiffness",
    "HypoidGearCompoundModalAnalysisAtAStiffness",
    "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "HypoidGearSetCompoundModalAnalysisAtAStiffness",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "MassDiscCompoundModalAnalysisAtAStiffness",
    "MeasurementComponentCompoundModalAnalysisAtAStiffness",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
    "OilSealCompoundModalAnalysisAtAStiffness",
    "PartCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
    "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
    "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
    "PlanetCarrierCompoundModalAnalysisAtAStiffness",
    "PointLoadCompoundModalAnalysisAtAStiffness",
    "PowerLoadCompoundModalAnalysisAtAStiffness",
    "PulleyCompoundModalAnalysisAtAStiffness",
    "RingPinsCompoundModalAnalysisAtAStiffness",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
    "RollingRingAssemblyCompoundModalAnalysisAtAStiffness",
    "RollingRingCompoundModalAnalysisAtAStiffness",
    "RollingRingConnectionCompoundModalAnalysisAtAStiffness",
    "RootAssemblyCompoundModalAnalysisAtAStiffness",
    "ShaftCompoundModalAnalysisAtAStiffness",
    "ShaftHubConnectionCompoundModalAnalysisAtAStiffness",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "SpringDamperCompoundModalAnalysisAtAStiffness",
    "SpringDamperConnectionCompoundModalAnalysisAtAStiffness",
    "SpringDamperHalfCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
    "SynchroniserCompoundModalAnalysisAtAStiffness",
    "SynchroniserHalfCompoundModalAnalysisAtAStiffness",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
    "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
    "TorqueConverterCompoundModalAnalysisAtAStiffness",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    "TorqueConverterPumpCompoundModalAnalysisAtAStiffness",
    "TorqueConverterTurbineCompoundModalAnalysisAtAStiffness",
    "UnbalancedMassCompoundModalAnalysisAtAStiffness",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
    "WormGearCompoundModalAnalysisAtAStiffness",
    "WormGearMeshCompoundModalAnalysisAtAStiffness",
    "WormGearSetCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)
