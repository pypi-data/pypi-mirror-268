"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1249 import AbstractStator
    from ._1250 import AbstractToothAndSlot
    from ._1251 import AirGapPartition
    from ._1252 import CADConductor
    from ._1253 import CADElectricMachineDetail
    from ._1254 import CADMagnetDetails
    from ._1255 import CADMagnetsForLayer
    from ._1256 import CADRotor
    from ._1257 import CADStator
    from ._1258 import CADToothAndSlot
    from ._1259 import Coil
    from ._1260 import CoilPositionInSlot
    from ._1261 import CoolingDuctLayerSpecification
    from ._1262 import CoolingDuctShape
    from ._1263 import CoreLossBuildFactorSpecificationMethod
    from ._1264 import CoreLossCoefficients
    from ._1265 import DoubleLayerWindingSlotPositions
    from ._1266 import DQAxisConvention
    from ._1267 import Eccentricity
    from ._1268 import ElectricMachineDetail
    from ._1269 import ElectricMachineDetailInitialInformation
    from ._1270 import ElectricMachineMechanicalAnalysisMeshingOptions
    from ._1271 import ElectricMachineMeshingOptions
    from ._1272 import ElectricMachineMeshingOptionsBase
    from ._1273 import ElectricMachineSetup
    from ._1274 import ElectricMachineType
    from ._1275 import FillFactorSpecificationMethod
    from ._1276 import FluxBarrierOrWeb
    from ._1277 import FluxBarrierStyle
    from ._1278 import HairpinConductor
    from ._1279 import HarmonicLoadDataControlExcitationOptionForElectricMachineMode
    from ._1280 import IndividualConductorSpecificationSource
    from ._1281 import InteriorPermanentMagnetAndSynchronousReluctanceRotor
    from ._1282 import InteriorPermanentMagnetMachine
    from ._1283 import IronLossCoefficientSpecificationMethod
    from ._1284 import MagnetClearance
    from ._1285 import MagnetConfiguration
    from ._1286 import MagnetData
    from ._1287 import MagnetDesign
    from ._1288 import MagnetForLayer
    from ._1289 import MagnetisationDirection
    from ._1290 import MagnetMaterial
    from ._1291 import MagnetMaterialDatabase
    from ._1292 import MotorRotorSideFaceDetail
    from ._1293 import NonCADElectricMachineDetail
    from ._1294 import NotchShape
    from ._1295 import NotchSpecification
    from ._1296 import PermanentMagnetAssistedSynchronousReluctanceMachine
    from ._1297 import PermanentMagnetRotor
    from ._1298 import Phase
    from ._1299 import RegionID
    from ._1300 import Rotor
    from ._1301 import RotorInternalLayerSpecification
    from ._1302 import RotorSkewSlice
    from ._1303 import RotorType
    from ._1304 import SingleOrDoubleLayerWindings
    from ._1305 import SlotSectionDetail
    from ._1306 import Stator
    from ._1307 import StatorCutOutSpecification
    from ._1308 import StatorRotorMaterial
    from ._1309 import StatorRotorMaterialDatabase
    from ._1310 import SurfacePermanentMagnetMachine
    from ._1311 import SurfacePermanentMagnetRotor
    from ._1312 import SynchronousReluctanceMachine
    from ._1313 import ToothAndSlot
    from ._1314 import ToothSlotStyle
    from ._1315 import ToothTaperSpecification
    from ._1316 import TwoDimensionalFEModelForAnalysis
    from ._1317 import UShapedLayerSpecification
    from ._1318 import VShapedMagnetLayerSpecification
    from ._1319 import WindingConductor
    from ._1320 import WindingConnection
    from ._1321 import WindingMaterial
    from ._1322 import WindingMaterialDatabase
    from ._1323 import Windings
    from ._1324 import WindingsViewer
    from ._1325 import WindingType
    from ._1326 import WireSizeSpecificationMethod
    from ._1327 import WoundFieldSynchronousMachine
else:
    import_structure = {
        "_1249": ["AbstractStator"],
        "_1250": ["AbstractToothAndSlot"],
        "_1251": ["AirGapPartition"],
        "_1252": ["CADConductor"],
        "_1253": ["CADElectricMachineDetail"],
        "_1254": ["CADMagnetDetails"],
        "_1255": ["CADMagnetsForLayer"],
        "_1256": ["CADRotor"],
        "_1257": ["CADStator"],
        "_1258": ["CADToothAndSlot"],
        "_1259": ["Coil"],
        "_1260": ["CoilPositionInSlot"],
        "_1261": ["CoolingDuctLayerSpecification"],
        "_1262": ["CoolingDuctShape"],
        "_1263": ["CoreLossBuildFactorSpecificationMethod"],
        "_1264": ["CoreLossCoefficients"],
        "_1265": ["DoubleLayerWindingSlotPositions"],
        "_1266": ["DQAxisConvention"],
        "_1267": ["Eccentricity"],
        "_1268": ["ElectricMachineDetail"],
        "_1269": ["ElectricMachineDetailInitialInformation"],
        "_1270": ["ElectricMachineMechanicalAnalysisMeshingOptions"],
        "_1271": ["ElectricMachineMeshingOptions"],
        "_1272": ["ElectricMachineMeshingOptionsBase"],
        "_1273": ["ElectricMachineSetup"],
        "_1274": ["ElectricMachineType"],
        "_1275": ["FillFactorSpecificationMethod"],
        "_1276": ["FluxBarrierOrWeb"],
        "_1277": ["FluxBarrierStyle"],
        "_1278": ["HairpinConductor"],
        "_1279": ["HarmonicLoadDataControlExcitationOptionForElectricMachineMode"],
        "_1280": ["IndividualConductorSpecificationSource"],
        "_1281": ["InteriorPermanentMagnetAndSynchronousReluctanceRotor"],
        "_1282": ["InteriorPermanentMagnetMachine"],
        "_1283": ["IronLossCoefficientSpecificationMethod"],
        "_1284": ["MagnetClearance"],
        "_1285": ["MagnetConfiguration"],
        "_1286": ["MagnetData"],
        "_1287": ["MagnetDesign"],
        "_1288": ["MagnetForLayer"],
        "_1289": ["MagnetisationDirection"],
        "_1290": ["MagnetMaterial"],
        "_1291": ["MagnetMaterialDatabase"],
        "_1292": ["MotorRotorSideFaceDetail"],
        "_1293": ["NonCADElectricMachineDetail"],
        "_1294": ["NotchShape"],
        "_1295": ["NotchSpecification"],
        "_1296": ["PermanentMagnetAssistedSynchronousReluctanceMachine"],
        "_1297": ["PermanentMagnetRotor"],
        "_1298": ["Phase"],
        "_1299": ["RegionID"],
        "_1300": ["Rotor"],
        "_1301": ["RotorInternalLayerSpecification"],
        "_1302": ["RotorSkewSlice"],
        "_1303": ["RotorType"],
        "_1304": ["SingleOrDoubleLayerWindings"],
        "_1305": ["SlotSectionDetail"],
        "_1306": ["Stator"],
        "_1307": ["StatorCutOutSpecification"],
        "_1308": ["StatorRotorMaterial"],
        "_1309": ["StatorRotorMaterialDatabase"],
        "_1310": ["SurfacePermanentMagnetMachine"],
        "_1311": ["SurfacePermanentMagnetRotor"],
        "_1312": ["SynchronousReluctanceMachine"],
        "_1313": ["ToothAndSlot"],
        "_1314": ["ToothSlotStyle"],
        "_1315": ["ToothTaperSpecification"],
        "_1316": ["TwoDimensionalFEModelForAnalysis"],
        "_1317": ["UShapedLayerSpecification"],
        "_1318": ["VShapedMagnetLayerSpecification"],
        "_1319": ["WindingConductor"],
        "_1320": ["WindingConnection"],
        "_1321": ["WindingMaterial"],
        "_1322": ["WindingMaterialDatabase"],
        "_1323": ["Windings"],
        "_1324": ["WindingsViewer"],
        "_1325": ["WindingType"],
        "_1326": ["WireSizeSpecificationMethod"],
        "_1327": ["WoundFieldSynchronousMachine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStator",
    "AbstractToothAndSlot",
    "AirGapPartition",
    "CADConductor",
    "CADElectricMachineDetail",
    "CADMagnetDetails",
    "CADMagnetsForLayer",
    "CADRotor",
    "CADStator",
    "CADToothAndSlot",
    "Coil",
    "CoilPositionInSlot",
    "CoolingDuctLayerSpecification",
    "CoolingDuctShape",
    "CoreLossBuildFactorSpecificationMethod",
    "CoreLossCoefficients",
    "DoubleLayerWindingSlotPositions",
    "DQAxisConvention",
    "Eccentricity",
    "ElectricMachineDetail",
    "ElectricMachineDetailInitialInformation",
    "ElectricMachineMechanicalAnalysisMeshingOptions",
    "ElectricMachineMeshingOptions",
    "ElectricMachineMeshingOptionsBase",
    "ElectricMachineSetup",
    "ElectricMachineType",
    "FillFactorSpecificationMethod",
    "FluxBarrierOrWeb",
    "FluxBarrierStyle",
    "HairpinConductor",
    "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    "IndividualConductorSpecificationSource",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
    "InteriorPermanentMagnetMachine",
    "IronLossCoefficientSpecificationMethod",
    "MagnetClearance",
    "MagnetConfiguration",
    "MagnetData",
    "MagnetDesign",
    "MagnetForLayer",
    "MagnetisationDirection",
    "MagnetMaterial",
    "MagnetMaterialDatabase",
    "MotorRotorSideFaceDetail",
    "NonCADElectricMachineDetail",
    "NotchShape",
    "NotchSpecification",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
    "PermanentMagnetRotor",
    "Phase",
    "RegionID",
    "Rotor",
    "RotorInternalLayerSpecification",
    "RotorSkewSlice",
    "RotorType",
    "SingleOrDoubleLayerWindings",
    "SlotSectionDetail",
    "Stator",
    "StatorCutOutSpecification",
    "StatorRotorMaterial",
    "StatorRotorMaterialDatabase",
    "SurfacePermanentMagnetMachine",
    "SurfacePermanentMagnetRotor",
    "SynchronousReluctanceMachine",
    "ToothAndSlot",
    "ToothSlotStyle",
    "ToothTaperSpecification",
    "TwoDimensionalFEModelForAnalysis",
    "UShapedLayerSpecification",
    "VShapedMagnetLayerSpecification",
    "WindingConductor",
    "WindingConnection",
    "WindingMaterial",
    "WindingMaterialDatabase",
    "Windings",
    "WindingsViewer",
    "WindingType",
    "WireSizeSpecificationMethod",
    "WoundFieldSynchronousMachine",
)
