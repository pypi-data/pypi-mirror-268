"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5125 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5126 import AbstractShaftModalAnalysisAtASpeed
    from ._5127 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5128 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5129 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5130 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5131 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5132 import AssemblyModalAnalysisAtASpeed
    from ._5133 import BearingModalAnalysisAtASpeed
    from ._5134 import BeltConnectionModalAnalysisAtASpeed
    from ._5135 import BeltDriveModalAnalysisAtASpeed
    from ._5136 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5137 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5138 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5139 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5140 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5141 import BevelGearMeshModalAnalysisAtASpeed
    from ._5142 import BevelGearModalAnalysisAtASpeed
    from ._5143 import BevelGearSetModalAnalysisAtASpeed
    from ._5144 import BoltedJointModalAnalysisAtASpeed
    from ._5145 import BoltModalAnalysisAtASpeed
    from ._5146 import ClutchConnectionModalAnalysisAtASpeed
    from ._5147 import ClutchHalfModalAnalysisAtASpeed
    from ._5148 import ClutchModalAnalysisAtASpeed
    from ._5149 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5150 import ComponentModalAnalysisAtASpeed
    from ._5151 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5152 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5153 import ConceptCouplingModalAnalysisAtASpeed
    from ._5154 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5155 import ConceptGearModalAnalysisAtASpeed
    from ._5156 import ConceptGearSetModalAnalysisAtASpeed
    from ._5157 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5158 import ConicalGearModalAnalysisAtASpeed
    from ._5159 import ConicalGearSetModalAnalysisAtASpeed
    from ._5160 import ConnectionModalAnalysisAtASpeed
    from ._5161 import ConnectorModalAnalysisAtASpeed
    from ._5162 import CouplingConnectionModalAnalysisAtASpeed
    from ._5163 import CouplingHalfModalAnalysisAtASpeed
    from ._5164 import CouplingModalAnalysisAtASpeed
    from ._5165 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5166 import CVTModalAnalysisAtASpeed
    from ._5167 import CVTPulleyModalAnalysisAtASpeed
    from ._5168 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5169 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5170 import CycloidalDiscModalAnalysisAtASpeed
    from ._5171 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5172 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5173 import CylindricalGearModalAnalysisAtASpeed
    from ._5174 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5175 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5176 import DatumModalAnalysisAtASpeed
    from ._5177 import ExternalCADModelModalAnalysisAtASpeed
    from ._5178 import FaceGearMeshModalAnalysisAtASpeed
    from ._5179 import FaceGearModalAnalysisAtASpeed
    from ._5180 import FaceGearSetModalAnalysisAtASpeed
    from ._5181 import FEPartModalAnalysisAtASpeed
    from ._5182 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5183 import GearMeshModalAnalysisAtASpeed
    from ._5184 import GearModalAnalysisAtASpeed
    from ._5185 import GearSetModalAnalysisAtASpeed
    from ._5186 import GuideDxfModelModalAnalysisAtASpeed
    from ._5187 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5188 import HypoidGearModalAnalysisAtASpeed
    from ._5189 import HypoidGearSetModalAnalysisAtASpeed
    from ._5190 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5191 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5192 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5193 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5194 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5195 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5196 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5197 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5198 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5199 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5200 import MassDiscModalAnalysisAtASpeed
    from ._5201 import MeasurementComponentModalAnalysisAtASpeed
    from ._5202 import ModalAnalysisAtASpeed
    from ._5203 import MountableComponentModalAnalysisAtASpeed
    from ._5204 import OilSealModalAnalysisAtASpeed
    from ._5205 import PartModalAnalysisAtASpeed
    from ._5206 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5207 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5208 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5209 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5210 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5211 import PlanetCarrierModalAnalysisAtASpeed
    from ._5212 import PointLoadModalAnalysisAtASpeed
    from ._5213 import PowerLoadModalAnalysisAtASpeed
    from ._5214 import PulleyModalAnalysisAtASpeed
    from ._5215 import RingPinsModalAnalysisAtASpeed
    from ._5216 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5217 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5218 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5219 import RollingRingModalAnalysisAtASpeed
    from ._5220 import RootAssemblyModalAnalysisAtASpeed
    from ._5221 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5222 import ShaftModalAnalysisAtASpeed
    from ._5223 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5224 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5225 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5226 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5227 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5228 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5229 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5230 import SpringDamperModalAnalysisAtASpeed
    from ._5231 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5232 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5233 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5234 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5235 import StraightBevelGearModalAnalysisAtASpeed
    from ._5236 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5237 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5238 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5239 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5240 import SynchroniserModalAnalysisAtASpeed
    from ._5241 import SynchroniserPartModalAnalysisAtASpeed
    from ._5242 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5243 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5244 import TorqueConverterModalAnalysisAtASpeed
    from ._5245 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5246 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5247 import UnbalancedMassModalAnalysisAtASpeed
    from ._5248 import VirtualComponentModalAnalysisAtASpeed
    from ._5249 import WormGearMeshModalAnalysisAtASpeed
    from ._5250 import WormGearModalAnalysisAtASpeed
    from ._5251 import WormGearSetModalAnalysisAtASpeed
    from ._5252 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5253 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5254 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        "_5125": ["AbstractAssemblyModalAnalysisAtASpeed"],
        "_5126": ["AbstractShaftModalAnalysisAtASpeed"],
        "_5127": ["AbstractShaftOrHousingModalAnalysisAtASpeed"],
        "_5128": ["AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5129": ["AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"],
        "_5130": ["AGMAGleasonConicalGearModalAnalysisAtASpeed"],
        "_5131": ["AGMAGleasonConicalGearSetModalAnalysisAtASpeed"],
        "_5132": ["AssemblyModalAnalysisAtASpeed"],
        "_5133": ["BearingModalAnalysisAtASpeed"],
        "_5134": ["BeltConnectionModalAnalysisAtASpeed"],
        "_5135": ["BeltDriveModalAnalysisAtASpeed"],
        "_5136": ["BevelDifferentialGearMeshModalAnalysisAtASpeed"],
        "_5137": ["BevelDifferentialGearModalAnalysisAtASpeed"],
        "_5138": ["BevelDifferentialGearSetModalAnalysisAtASpeed"],
        "_5139": ["BevelDifferentialPlanetGearModalAnalysisAtASpeed"],
        "_5140": ["BevelDifferentialSunGearModalAnalysisAtASpeed"],
        "_5141": ["BevelGearMeshModalAnalysisAtASpeed"],
        "_5142": ["BevelGearModalAnalysisAtASpeed"],
        "_5143": ["BevelGearSetModalAnalysisAtASpeed"],
        "_5144": ["BoltedJointModalAnalysisAtASpeed"],
        "_5145": ["BoltModalAnalysisAtASpeed"],
        "_5146": ["ClutchConnectionModalAnalysisAtASpeed"],
        "_5147": ["ClutchHalfModalAnalysisAtASpeed"],
        "_5148": ["ClutchModalAnalysisAtASpeed"],
        "_5149": ["CoaxialConnectionModalAnalysisAtASpeed"],
        "_5150": ["ComponentModalAnalysisAtASpeed"],
        "_5151": ["ConceptCouplingConnectionModalAnalysisAtASpeed"],
        "_5152": ["ConceptCouplingHalfModalAnalysisAtASpeed"],
        "_5153": ["ConceptCouplingModalAnalysisAtASpeed"],
        "_5154": ["ConceptGearMeshModalAnalysisAtASpeed"],
        "_5155": ["ConceptGearModalAnalysisAtASpeed"],
        "_5156": ["ConceptGearSetModalAnalysisAtASpeed"],
        "_5157": ["ConicalGearMeshModalAnalysisAtASpeed"],
        "_5158": ["ConicalGearModalAnalysisAtASpeed"],
        "_5159": ["ConicalGearSetModalAnalysisAtASpeed"],
        "_5160": ["ConnectionModalAnalysisAtASpeed"],
        "_5161": ["ConnectorModalAnalysisAtASpeed"],
        "_5162": ["CouplingConnectionModalAnalysisAtASpeed"],
        "_5163": ["CouplingHalfModalAnalysisAtASpeed"],
        "_5164": ["CouplingModalAnalysisAtASpeed"],
        "_5165": ["CVTBeltConnectionModalAnalysisAtASpeed"],
        "_5166": ["CVTModalAnalysisAtASpeed"],
        "_5167": ["CVTPulleyModalAnalysisAtASpeed"],
        "_5168": ["CycloidalAssemblyModalAnalysisAtASpeed"],
        "_5169": ["CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"],
        "_5170": ["CycloidalDiscModalAnalysisAtASpeed"],
        "_5171": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"],
        "_5172": ["CylindricalGearMeshModalAnalysisAtASpeed"],
        "_5173": ["CylindricalGearModalAnalysisAtASpeed"],
        "_5174": ["CylindricalGearSetModalAnalysisAtASpeed"],
        "_5175": ["CylindricalPlanetGearModalAnalysisAtASpeed"],
        "_5176": ["DatumModalAnalysisAtASpeed"],
        "_5177": ["ExternalCADModelModalAnalysisAtASpeed"],
        "_5178": ["FaceGearMeshModalAnalysisAtASpeed"],
        "_5179": ["FaceGearModalAnalysisAtASpeed"],
        "_5180": ["FaceGearSetModalAnalysisAtASpeed"],
        "_5181": ["FEPartModalAnalysisAtASpeed"],
        "_5182": ["FlexiblePinAssemblyModalAnalysisAtASpeed"],
        "_5183": ["GearMeshModalAnalysisAtASpeed"],
        "_5184": ["GearModalAnalysisAtASpeed"],
        "_5185": ["GearSetModalAnalysisAtASpeed"],
        "_5186": ["GuideDxfModelModalAnalysisAtASpeed"],
        "_5187": ["HypoidGearMeshModalAnalysisAtASpeed"],
        "_5188": ["HypoidGearModalAnalysisAtASpeed"],
        "_5189": ["HypoidGearSetModalAnalysisAtASpeed"],
        "_5190": ["InterMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5191": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"],
        "_5192": ["KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"],
        "_5193": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"],
        "_5194": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"],
        "_5195": ["KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed"],
        "_5196": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed"],
        "_5197": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5198": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed"],
        "_5199": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5200": ["MassDiscModalAnalysisAtASpeed"],
        "_5201": ["MeasurementComponentModalAnalysisAtASpeed"],
        "_5202": ["ModalAnalysisAtASpeed"],
        "_5203": ["MountableComponentModalAnalysisAtASpeed"],
        "_5204": ["OilSealModalAnalysisAtASpeed"],
        "_5205": ["PartModalAnalysisAtASpeed"],
        "_5206": ["PartToPartShearCouplingConnectionModalAnalysisAtASpeed"],
        "_5207": ["PartToPartShearCouplingHalfModalAnalysisAtASpeed"],
        "_5208": ["PartToPartShearCouplingModalAnalysisAtASpeed"],
        "_5209": ["PlanetaryConnectionModalAnalysisAtASpeed"],
        "_5210": ["PlanetaryGearSetModalAnalysisAtASpeed"],
        "_5211": ["PlanetCarrierModalAnalysisAtASpeed"],
        "_5212": ["PointLoadModalAnalysisAtASpeed"],
        "_5213": ["PowerLoadModalAnalysisAtASpeed"],
        "_5214": ["PulleyModalAnalysisAtASpeed"],
        "_5215": ["RingPinsModalAnalysisAtASpeed"],
        "_5216": ["RingPinsToDiscConnectionModalAnalysisAtASpeed"],
        "_5217": ["RollingRingAssemblyModalAnalysisAtASpeed"],
        "_5218": ["RollingRingConnectionModalAnalysisAtASpeed"],
        "_5219": ["RollingRingModalAnalysisAtASpeed"],
        "_5220": ["RootAssemblyModalAnalysisAtASpeed"],
        "_5221": ["ShaftHubConnectionModalAnalysisAtASpeed"],
        "_5222": ["ShaftModalAnalysisAtASpeed"],
        "_5223": ["ShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5224": ["SpecialisedAssemblyModalAnalysisAtASpeed"],
        "_5225": ["SpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5226": ["SpiralBevelGearModalAnalysisAtASpeed"],
        "_5227": ["SpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5228": ["SpringDamperConnectionModalAnalysisAtASpeed"],
        "_5229": ["SpringDamperHalfModalAnalysisAtASpeed"],
        "_5230": ["SpringDamperModalAnalysisAtASpeed"],
        "_5231": ["StraightBevelDiffGearMeshModalAnalysisAtASpeed"],
        "_5232": ["StraightBevelDiffGearModalAnalysisAtASpeed"],
        "_5233": ["StraightBevelDiffGearSetModalAnalysisAtASpeed"],
        "_5234": ["StraightBevelGearMeshModalAnalysisAtASpeed"],
        "_5235": ["StraightBevelGearModalAnalysisAtASpeed"],
        "_5236": ["StraightBevelGearSetModalAnalysisAtASpeed"],
        "_5237": ["StraightBevelPlanetGearModalAnalysisAtASpeed"],
        "_5238": ["StraightBevelSunGearModalAnalysisAtASpeed"],
        "_5239": ["SynchroniserHalfModalAnalysisAtASpeed"],
        "_5240": ["SynchroniserModalAnalysisAtASpeed"],
        "_5241": ["SynchroniserPartModalAnalysisAtASpeed"],
        "_5242": ["SynchroniserSleeveModalAnalysisAtASpeed"],
        "_5243": ["TorqueConverterConnectionModalAnalysisAtASpeed"],
        "_5244": ["TorqueConverterModalAnalysisAtASpeed"],
        "_5245": ["TorqueConverterPumpModalAnalysisAtASpeed"],
        "_5246": ["TorqueConverterTurbineModalAnalysisAtASpeed"],
        "_5247": ["UnbalancedMassModalAnalysisAtASpeed"],
        "_5248": ["VirtualComponentModalAnalysisAtASpeed"],
        "_5249": ["WormGearMeshModalAnalysisAtASpeed"],
        "_5250": ["WormGearModalAnalysisAtASpeed"],
        "_5251": ["WormGearSetModalAnalysisAtASpeed"],
        "_5252": ["ZerolBevelGearMeshModalAnalysisAtASpeed"],
        "_5253": ["ZerolBevelGearModalAnalysisAtASpeed"],
        "_5254": ["ZerolBevelGearSetModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyModalAnalysisAtASpeed",
    "AbstractShaftModalAnalysisAtASpeed",
    "AbstractShaftOrHousingModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
    "AssemblyModalAnalysisAtASpeed",
    "BearingModalAnalysisAtASpeed",
    "BeltConnectionModalAnalysisAtASpeed",
    "BeltDriveModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshModalAnalysisAtASpeed",
    "BevelDifferentialGearModalAnalysisAtASpeed",
    "BevelDifferentialGearSetModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
    "BevelDifferentialSunGearModalAnalysisAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
    "BevelGearModalAnalysisAtASpeed",
    "BevelGearSetModalAnalysisAtASpeed",
    "BoltedJointModalAnalysisAtASpeed",
    "BoltModalAnalysisAtASpeed",
    "ClutchConnectionModalAnalysisAtASpeed",
    "ClutchHalfModalAnalysisAtASpeed",
    "ClutchModalAnalysisAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
    "ComponentModalAnalysisAtASpeed",
    "ConceptCouplingConnectionModalAnalysisAtASpeed",
    "ConceptCouplingHalfModalAnalysisAtASpeed",
    "ConceptCouplingModalAnalysisAtASpeed",
    "ConceptGearMeshModalAnalysisAtASpeed",
    "ConceptGearModalAnalysisAtASpeed",
    "ConceptGearSetModalAnalysisAtASpeed",
    "ConicalGearMeshModalAnalysisAtASpeed",
    "ConicalGearModalAnalysisAtASpeed",
    "ConicalGearSetModalAnalysisAtASpeed",
    "ConnectionModalAnalysisAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
    "CouplingHalfModalAnalysisAtASpeed",
    "CouplingModalAnalysisAtASpeed",
    "CVTBeltConnectionModalAnalysisAtASpeed",
    "CVTModalAnalysisAtASpeed",
    "CVTPulleyModalAnalysisAtASpeed",
    "CycloidalAssemblyModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    "CycloidalDiscModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    "CylindricalGearMeshModalAnalysisAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
    "CylindricalGearSetModalAnalysisAtASpeed",
    "CylindricalPlanetGearModalAnalysisAtASpeed",
    "DatumModalAnalysisAtASpeed",
    "ExternalCADModelModalAnalysisAtASpeed",
    "FaceGearMeshModalAnalysisAtASpeed",
    "FaceGearModalAnalysisAtASpeed",
    "FaceGearSetModalAnalysisAtASpeed",
    "FEPartModalAnalysisAtASpeed",
    "FlexiblePinAssemblyModalAnalysisAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
    "GearModalAnalysisAtASpeed",
    "GearSetModalAnalysisAtASpeed",
    "GuideDxfModelModalAnalysisAtASpeed",
    "HypoidGearMeshModalAnalysisAtASpeed",
    "HypoidGearModalAnalysisAtASpeed",
    "HypoidGearSetModalAnalysisAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    "MassDiscModalAnalysisAtASpeed",
    "MeasurementComponentModalAnalysisAtASpeed",
    "ModalAnalysisAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
    "OilSealModalAnalysisAtASpeed",
    "PartModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
    "PartToPartShearCouplingModalAnalysisAtASpeed",
    "PlanetaryConnectionModalAnalysisAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
    "PlanetCarrierModalAnalysisAtASpeed",
    "PointLoadModalAnalysisAtASpeed",
    "PowerLoadModalAnalysisAtASpeed",
    "PulleyModalAnalysisAtASpeed",
    "RingPinsModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionModalAnalysisAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
    "RollingRingConnectionModalAnalysisAtASpeed",
    "RollingRingModalAnalysisAtASpeed",
    "RootAssemblyModalAnalysisAtASpeed",
    "ShaftHubConnectionModalAnalysisAtASpeed",
    "ShaftModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
    "SpiralBevelGearModalAnalysisAtASpeed",
    "SpiralBevelGearSetModalAnalysisAtASpeed",
    "SpringDamperConnectionModalAnalysisAtASpeed",
    "SpringDamperHalfModalAnalysisAtASpeed",
    "SpringDamperModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshModalAnalysisAtASpeed",
    "StraightBevelDiffGearModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
    "StraightBevelGearMeshModalAnalysisAtASpeed",
    "StraightBevelGearModalAnalysisAtASpeed",
    "StraightBevelGearSetModalAnalysisAtASpeed",
    "StraightBevelPlanetGearModalAnalysisAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
    "SynchroniserHalfModalAnalysisAtASpeed",
    "SynchroniserModalAnalysisAtASpeed",
    "SynchroniserPartModalAnalysisAtASpeed",
    "SynchroniserSleeveModalAnalysisAtASpeed",
    "TorqueConverterConnectionModalAnalysisAtASpeed",
    "TorqueConverterModalAnalysisAtASpeed",
    "TorqueConverterPumpModalAnalysisAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
    "UnbalancedMassModalAnalysisAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
    "WormGearModalAnalysisAtASpeed",
    "WormGearSetModalAnalysisAtASpeed",
    "ZerolBevelGearMeshModalAnalysisAtASpeed",
    "ZerolBevelGearModalAnalysisAtASpeed",
    "ZerolBevelGearSetModalAnalysisAtASpeed",
)
