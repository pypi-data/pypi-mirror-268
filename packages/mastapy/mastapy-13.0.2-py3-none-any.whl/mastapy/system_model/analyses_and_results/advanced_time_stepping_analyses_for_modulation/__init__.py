"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7014 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7015 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7016 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._7017 import (
        AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7018 import AdvancedTimeSteppingAnalysisForModulation
    from ._7019 import AtsamExcitationsOrOthers
    from ._7020 import AtsamNaturalFrequencyViewOption
    from ._7021 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._7022 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7023 import (
        AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7024 import (
        AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7025 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7026 import ATSAMResultsVsLargeTimeStepSettings
    from ._7027 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._7028 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7029 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._7030 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._7031 import (
        BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7032 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7033 import (
        BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7034 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7035 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7036 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7037 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7038 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._7039 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._7040 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7042 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7043 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7045 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import (
        ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7047 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7050 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7052 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7053 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7054 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7055 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7056 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7057 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7058 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7060 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import (
        CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7065 import (
        CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7066 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7070 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7071 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7073 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7074 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7075 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7076 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7077 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7078 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7079 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7080 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7081 import (
        HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7082 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7083 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7084 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7085 import (
        InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7086 import (
        KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7087 import (
        KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7088 import (
        KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7089 import (
        KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7090 import (
        KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7091 import (
        KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7092 import (
        KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7093 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7094 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7095 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7099 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7100 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7101 import (
        PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7102 import (
        PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7103 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7104 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7105 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7106 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7107 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7108 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7109 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7110 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7111 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7112 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7113 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7115 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7116 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import (
        ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7118 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7119 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7120 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7121 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import (
        StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7127 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7128 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7130 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7131 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7136 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7137 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7138 import (
        TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7139 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7140 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7141 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7142 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7143 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7144 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7145 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7146 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7147 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7148 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        "_7014": ["AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7015": ["AbstractShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7016": ["AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"],
        "_7017": [
            "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7018": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_7019": ["AtsamExcitationsOrOthers"],
        "_7020": ["AtsamNaturalFrequencyViewOption"],
        "_7021": ["AdvancedTimeSteppingAnalysisForModulationOptions"],
        "_7022": ["AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7023": [
            "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7024": ["AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7025": ["AssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7026": ["ATSAMResultsVsLargeTimeStepSettings"],
        "_7027": ["BearingAdvancedTimeSteppingAnalysisForModulation"],
        "_7028": ["BeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7029": ["BeltDriveAdvancedTimeSteppingAnalysisForModulation"],
        "_7030": ["BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7031": ["BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7032": ["BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7033": [
            "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7034": ["BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7035": ["BevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7036": ["BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7037": ["BevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7038": ["BoltAdvancedTimeSteppingAnalysisForModulation"],
        "_7039": ["BoltedJointAdvancedTimeSteppingAnalysisForModulation"],
        "_7040": ["ClutchAdvancedTimeSteppingAnalysisForModulation"],
        "_7041": ["ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7042": ["ClutchHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7043": ["CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7044": ["ComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7045": ["ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7046": ["ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7047": ["ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7048": ["ConceptGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7049": ["ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7050": ["ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7051": ["ConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7052": ["ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7053": ["ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7054": ["ConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7055": ["ConnectorAdvancedTimeSteppingAnalysisForModulation"],
        "_7056": ["CouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7057": ["CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7058": ["CouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7059": ["CVTAdvancedTimeSteppingAnalysisForModulation"],
        "_7060": ["CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7061": ["CVTPulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7062": ["CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7063": ["CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7064": [
            "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7065": [
            "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7066": ["CylindricalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7067": ["CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7068": ["CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7069": ["CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7070": ["DatumAdvancedTimeSteppingAnalysisForModulation"],
        "_7071": ["ExternalCADModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7072": ["FaceGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7073": ["FaceGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7074": ["FaceGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7075": ["FEPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7076": ["FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7077": ["GearAdvancedTimeSteppingAnalysisForModulation"],
        "_7078": ["GearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7079": ["GearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7080": ["GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7081": [
            "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7082": ["HypoidGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7083": ["HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7084": ["HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7085": [
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7086": [
            "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7087": [
            "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7088": [
            "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7089": [
            "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7090": [
            "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7091": [
            "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7092": [
            "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7093": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7094": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7095": ["MassDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7096": ["MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7097": ["MountableComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7098": ["OilSealAdvancedTimeSteppingAnalysisForModulation"],
        "_7099": ["PartAdvancedTimeSteppingAnalysisForModulation"],
        "_7100": ["PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7101": [
            "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7102": [
            "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7103": ["PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7104": ["PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7105": ["PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"],
        "_7106": ["PointLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7107": ["PowerLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7108": ["PulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7109": ["RingPinsAdvancedTimeSteppingAnalysisForModulation"],
        "_7110": ["RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7111": ["RollingRingAdvancedTimeSteppingAnalysisForModulation"],
        "_7112": ["RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7113": ["RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7114": ["RootAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7115": ["ShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7116": ["ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7117": [
            "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7118": ["SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7119": ["SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7120": ["SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7121": ["SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7122": ["SpringDamperAdvancedTimeSteppingAnalysisForModulation"],
        "_7123": ["SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7124": ["SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7125": ["StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7126": ["StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7127": ["StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7128": ["StraightBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7129": ["StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7130": ["StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7131": ["StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7132": ["StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7133": ["SynchroniserAdvancedTimeSteppingAnalysisForModulation"],
        "_7134": ["SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7135": ["SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7136": ["SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"],
        "_7137": ["TorqueConverterAdvancedTimeSteppingAnalysisForModulation"],
        "_7138": ["TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7139": ["TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation"],
        "_7140": ["TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation"],
        "_7141": ["UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"],
        "_7142": ["VirtualComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7143": ["WormGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7144": ["WormGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7145": ["WormGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7146": ["ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7147": ["ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7148": ["ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "AdvancedTimeSteppingAnalysisForModulation",
    "AtsamExcitationsOrOthers",
    "AtsamNaturalFrequencyViewOption",
    "AdvancedTimeSteppingAnalysisForModulationOptions",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ATSAMResultsVsLargeTimeStepSettings",
    "BearingAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BoltAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointAdvancedTimeSteppingAnalysisForModulation",
    "ClutchAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ComponentAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorAdvancedTimeSteppingAnalysisForModulation",
    "CouplingAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "CVTAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "DatumAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
    "FEPartAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "GearAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshAdvancedTimeSteppingAnalysisForModulation",
    "GearSetAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    "OilSealAdvancedTimeSteppingAnalysisForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
    "PulleyAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ShaftAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
    "WormGearAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)
