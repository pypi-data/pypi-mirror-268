"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7149 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7150 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7151 import (
        AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7152 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7153 import (
        AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7154 import (
        AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7155 import (
        AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7156 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7157 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import (
        BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7161 import (
        BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7162 import (
        BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7163 import (
        BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7164 import (
        BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7165 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7166 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7167 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7168 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7169 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7170 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7171 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7172 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7173 import (
        CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7174 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7175 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7176 import (
        ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7177 import (
        ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7178 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7179 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7180 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7181 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7182 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7183 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7184 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7185 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7186 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7187 import (
        CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7188 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7189 import (
        CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7190 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7191 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7192 import (
        CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7193 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7194 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7195 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7196 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import (
        CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7198 import (
        CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7199 import (
        CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7200 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7201 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7203 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7204 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7205 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7206 import (
        FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7207 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7208 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7209 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7210 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7211 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7212 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7213 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7214 import (
        InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7215 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7216 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7217 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7218 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7219 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7220 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7221 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7222 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7223 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7224 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7225 import (
        MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7226 import (
        MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7227 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7228 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7229 import (
        PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7230 import (
        PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7231 import (
        PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7232 import (
        PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7233 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7234 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7235 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7236 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7237 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7238 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7239 import (
        RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7240 import (
        RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7241 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7242 import (
        RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7243 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7244 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7245 import (
        ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7246 import (
        ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7247 import (
        SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7248 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7249 import (
        SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7250 import (
        SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7251 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7252 import (
        SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7253 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7254 import (
        StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7255 import (
        StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7256 import (
        StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7257 import (
        StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7258 import (
        StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7259 import (
        StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7260 import (
        StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7261 import (
        StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7262 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7263 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7264 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7265 import (
        SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7266 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7267 import (
        TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7268 import (
        TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7269 import (
        TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7270 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7271 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7272 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7273 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7274 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7275 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7276 import (
        ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7277 import (
        ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
else:
    import_structure = {
        "_7149": ["AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7150": ["AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7151": [
            "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7152": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7153": [
            "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7154": [
            "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7155": [
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7156": ["AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7157": ["BearingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7158": ["BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7159": ["BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7160": [
            "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7161": [
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7162": [
            "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7163": [
            "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7164": [
            "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7165": ["BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7166": ["BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7167": ["BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7168": ["BoltCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7169": ["BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7170": ["ClutchCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7171": ["ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7172": ["ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7173": ["CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7174": ["ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7175": ["ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7176": [
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7177": [
            "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7178": ["ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7179": ["ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7180": ["ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7181": ["ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7182": ["ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7183": ["ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7184": ["ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7185": ["ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7186": ["CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7187": [
            "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7188": ["CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7189": ["CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7190": ["CVTCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7191": ["CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7192": ["CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7193": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7194": ["CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7195": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7196": ["CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7197": [
            "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7198": [
            "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7199": [
            "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7200": ["DatumCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7201": ["ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7202": ["FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7203": ["FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7204": ["FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7205": ["FEPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7206": [
            "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7207": ["GearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7208": ["GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7209": ["GearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7210": ["GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7211": ["HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7212": ["HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7213": ["HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7214": [
            "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7215": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7216": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7217": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7218": [
            "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7219": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7220": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7221": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7222": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7223": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7224": ["MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7225": [
            "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7226": [
            "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7227": ["OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7228": ["PartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7229": [
            "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7230": [
            "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7231": [
            "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7232": [
            "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7233": ["PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7234": ["PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7235": ["PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7236": ["PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7237": ["PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7238": ["RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7239": [
            "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7240": [
            "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7241": ["RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7242": [
            "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7243": ["RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7244": ["ShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7245": [
            "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7246": [
            "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7247": [
            "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7248": ["SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7249": [
            "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7250": [
            "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7251": ["SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7252": [
            "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7253": ["SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7254": [
            "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7255": [
            "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7256": [
            "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7257": ["StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7258": [
            "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7259": [
            "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7260": [
            "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7261": [
            "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7262": ["SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7263": ["SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7264": ["SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7265": [
            "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7266": ["TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7267": [
            "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7268": [
            "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7269": [
            "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7270": ["UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7271": ["VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7272": ["WormGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7273": ["WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7274": ["WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7275": ["ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7276": [
            "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7277": ["ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BearingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "DatumCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FEPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)
