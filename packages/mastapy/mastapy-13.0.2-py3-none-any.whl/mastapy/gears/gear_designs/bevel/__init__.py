"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1185 import AGMAGleasonConicalGearGeometryMethods
    from ._1186 import BevelGearDesign
    from ._1187 import BevelGearMeshDesign
    from ._1188 import BevelGearSetDesign
    from ._1189 import BevelMeshedGearDesign
    from ._1190 import DrivenMachineCharacteristicGleason
    from ._1191 import EdgeRadiusType
    from ._1192 import FinishingMethods
    from ._1193 import MachineCharacteristicAGMAKlingelnberg
    from ._1194 import PrimeMoverCharacteristicGleason
    from ._1195 import ToothProportionsInputMethod
    from ._1196 import ToothThicknessSpecificationMethod
    from ._1197 import WheelFinishCutterPointWidthRestrictionMethod
else:
    import_structure = {
        "_1185": ["AGMAGleasonConicalGearGeometryMethods"],
        "_1186": ["BevelGearDesign"],
        "_1187": ["BevelGearMeshDesign"],
        "_1188": ["BevelGearSetDesign"],
        "_1189": ["BevelMeshedGearDesign"],
        "_1190": ["DrivenMachineCharacteristicGleason"],
        "_1191": ["EdgeRadiusType"],
        "_1192": ["FinishingMethods"],
        "_1193": ["MachineCharacteristicAGMAKlingelnberg"],
        "_1194": ["PrimeMoverCharacteristicGleason"],
        "_1195": ["ToothProportionsInputMethod"],
        "_1196": ["ToothThicknessSpecificationMethod"],
        "_1197": ["WheelFinishCutterPointWidthRestrictionMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearGeometryMethods",
    "BevelGearDesign",
    "BevelGearMeshDesign",
    "BevelGearSetDesign",
    "BevelMeshedGearDesign",
    "DrivenMachineCharacteristicGleason",
    "EdgeRadiusType",
    "FinishingMethods",
    "MachineCharacteristicAGMAKlingelnberg",
    "PrimeMoverCharacteristicGleason",
    "ToothProportionsInputMethod",
    "ToothThicknessSpecificationMethod",
    "WheelFinishCutterPointWidthRestrictionMethod",
)
