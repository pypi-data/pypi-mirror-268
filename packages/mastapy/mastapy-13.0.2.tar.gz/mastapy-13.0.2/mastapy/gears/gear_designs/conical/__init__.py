"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1156 import ActiveConicalFlank
    from ._1157 import BacklashDistributionRule
    from ._1158 import ConicalFlanks
    from ._1159 import ConicalGearCutter
    from ._1160 import ConicalGearDesign
    from ._1161 import ConicalGearMeshDesign
    from ._1162 import ConicalGearSetDesign
    from ._1163 import ConicalMachineSettingCalculationMethods
    from ._1164 import ConicalManufactureMethods
    from ._1165 import ConicalMeshedGearDesign
    from ._1166 import ConicalMeshMisalignments
    from ._1167 import CutterBladeType
    from ._1168 import CutterGaugeLengths
    from ._1169 import DummyConicalGearCutter
    from ._1170 import FrontEndTypes
    from ._1171 import GleasonSafetyRequirements
    from ._1172 import KIMoSBevelHypoidSingleLoadCaseResultsData
    from ._1173 import KIMoSBevelHypoidSingleRotationAngleResult
    from ._1174 import KlingelnbergFinishingMethods
    from ._1175 import LoadDistributionFactorMethods
    from ._1176 import TopremEntryType
    from ._1177 import TopremLetter
else:
    import_structure = {
        "_1156": ["ActiveConicalFlank"],
        "_1157": ["BacklashDistributionRule"],
        "_1158": ["ConicalFlanks"],
        "_1159": ["ConicalGearCutter"],
        "_1160": ["ConicalGearDesign"],
        "_1161": ["ConicalGearMeshDesign"],
        "_1162": ["ConicalGearSetDesign"],
        "_1163": ["ConicalMachineSettingCalculationMethods"],
        "_1164": ["ConicalManufactureMethods"],
        "_1165": ["ConicalMeshedGearDesign"],
        "_1166": ["ConicalMeshMisalignments"],
        "_1167": ["CutterBladeType"],
        "_1168": ["CutterGaugeLengths"],
        "_1169": ["DummyConicalGearCutter"],
        "_1170": ["FrontEndTypes"],
        "_1171": ["GleasonSafetyRequirements"],
        "_1172": ["KIMoSBevelHypoidSingleLoadCaseResultsData"],
        "_1173": ["KIMoSBevelHypoidSingleRotationAngleResult"],
        "_1174": ["KlingelnbergFinishingMethods"],
        "_1175": ["LoadDistributionFactorMethods"],
        "_1176": ["TopremEntryType"],
        "_1177": ["TopremLetter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveConicalFlank",
    "BacklashDistributionRule",
    "ConicalFlanks",
    "ConicalGearCutter",
    "ConicalGearDesign",
    "ConicalGearMeshDesign",
    "ConicalGearSetDesign",
    "ConicalMachineSettingCalculationMethods",
    "ConicalManufactureMethods",
    "ConicalMeshedGearDesign",
    "ConicalMeshMisalignments",
    "CutterBladeType",
    "CutterGaugeLengths",
    "DummyConicalGearCutter",
    "FrontEndTypes",
    "GleasonSafetyRequirements",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
    "KIMoSBevelHypoidSingleRotationAngleResult",
    "KlingelnbergFinishingMethods",
    "LoadDistributionFactorMethods",
    "TopremEntryType",
    "TopremLetter",
)
