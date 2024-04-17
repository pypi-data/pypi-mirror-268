"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._706 import CurveInLinkedList
    from ._707 import CustomisableEdgeProfile
    from ._708 import CylindricalFormedWheelGrinderDatabase
    from ._709 import CylindricalGearAbstractCutterDesign
    from ._710 import CylindricalGearFormGrindingWheel
    from ._711 import CylindricalGearGrindingWorm
    from ._712 import CylindricalGearHobDesign
    from ._713 import CylindricalGearPlungeShaver
    from ._714 import CylindricalGearPlungeShaverDatabase
    from ._715 import CylindricalGearRackDesign
    from ._716 import CylindricalGearRealCutterDesign
    from ._717 import CylindricalGearShaper
    from ._718 import CylindricalGearShaver
    from ._719 import CylindricalGearShaverDatabase
    from ._720 import CylindricalWormGrinderDatabase
    from ._721 import InvoluteCutterDesign
    from ._722 import MutableCommon
    from ._723 import MutableCurve
    from ._724 import MutableFillet
    from ._725 import RoughCutterCreationSettings
else:
    import_structure = {
        "_706": ["CurveInLinkedList"],
        "_707": ["CustomisableEdgeProfile"],
        "_708": ["CylindricalFormedWheelGrinderDatabase"],
        "_709": ["CylindricalGearAbstractCutterDesign"],
        "_710": ["CylindricalGearFormGrindingWheel"],
        "_711": ["CylindricalGearGrindingWorm"],
        "_712": ["CylindricalGearHobDesign"],
        "_713": ["CylindricalGearPlungeShaver"],
        "_714": ["CylindricalGearPlungeShaverDatabase"],
        "_715": ["CylindricalGearRackDesign"],
        "_716": ["CylindricalGearRealCutterDesign"],
        "_717": ["CylindricalGearShaper"],
        "_718": ["CylindricalGearShaver"],
        "_719": ["CylindricalGearShaverDatabase"],
        "_720": ["CylindricalWormGrinderDatabase"],
        "_721": ["InvoluteCutterDesign"],
        "_722": ["MutableCommon"],
        "_723": ["MutableCurve"],
        "_724": ["MutableFillet"],
        "_725": ["RoughCutterCreationSettings"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CurveInLinkedList",
    "CustomisableEdgeProfile",
    "CylindricalFormedWheelGrinderDatabase",
    "CylindricalGearAbstractCutterDesign",
    "CylindricalGearFormGrindingWheel",
    "CylindricalGearGrindingWorm",
    "CylindricalGearHobDesign",
    "CylindricalGearPlungeShaver",
    "CylindricalGearPlungeShaverDatabase",
    "CylindricalGearRackDesign",
    "CylindricalGearRealCutterDesign",
    "CylindricalGearShaper",
    "CylindricalGearShaver",
    "CylindricalGearShaverDatabase",
    "CylindricalWormGrinderDatabase",
    "InvoluteCutterDesign",
    "MutableCommon",
    "MutableCurve",
    "MutableFillet",
    "RoughCutterCreationSettings",
)
