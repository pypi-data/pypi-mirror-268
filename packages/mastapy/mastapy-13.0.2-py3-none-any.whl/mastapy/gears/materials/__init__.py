"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._586 import AGMACylindricalGearMaterial
    from ._587 import BevelGearAbstractMaterialDatabase
    from ._588 import BevelGearISOMaterial
    from ._589 import BevelGearISOMaterialDatabase
    from ._590 import BevelGearMaterial
    from ._591 import BevelGearMaterialDatabase
    from ._592 import CylindricalGearAGMAMaterialDatabase
    from ._593 import CylindricalGearISOMaterialDatabase
    from ._594 import CylindricalGearMaterial
    from ._595 import CylindricalGearMaterialDatabase
    from ._596 import CylindricalGearPlasticMaterialDatabase
    from ._597 import GearMaterial
    from ._598 import GearMaterialDatabase
    from ._599 import GearMaterialExpertSystemFactorSettings
    from ._600 import ISOCylindricalGearMaterial
    from ._601 import ISOTR1417912001CoefficientOfFrictionConstants
    from ._602 import ISOTR1417912001CoefficientOfFrictionConstantsDatabase
    from ._603 import KlingelnbergConicalGearMaterialDatabase
    from ._604 import KlingelnbergCycloPalloidConicalGearMaterial
    from ._605 import ManufactureRating
    from ._606 import PlasticCylindricalGearMaterial
    from ._607 import PlasticSNCurve
    from ._608 import RatingMethods
    from ._609 import RawMaterial
    from ._610 import RawMaterialDatabase
    from ._611 import SNCurveDefinition
else:
    import_structure = {
        "_586": ["AGMACylindricalGearMaterial"],
        "_587": ["BevelGearAbstractMaterialDatabase"],
        "_588": ["BevelGearISOMaterial"],
        "_589": ["BevelGearISOMaterialDatabase"],
        "_590": ["BevelGearMaterial"],
        "_591": ["BevelGearMaterialDatabase"],
        "_592": ["CylindricalGearAGMAMaterialDatabase"],
        "_593": ["CylindricalGearISOMaterialDatabase"],
        "_594": ["CylindricalGearMaterial"],
        "_595": ["CylindricalGearMaterialDatabase"],
        "_596": ["CylindricalGearPlasticMaterialDatabase"],
        "_597": ["GearMaterial"],
        "_598": ["GearMaterialDatabase"],
        "_599": ["GearMaterialExpertSystemFactorSettings"],
        "_600": ["ISOCylindricalGearMaterial"],
        "_601": ["ISOTR1417912001CoefficientOfFrictionConstants"],
        "_602": ["ISOTR1417912001CoefficientOfFrictionConstantsDatabase"],
        "_603": ["KlingelnbergConicalGearMaterialDatabase"],
        "_604": ["KlingelnbergCycloPalloidConicalGearMaterial"],
        "_605": ["ManufactureRating"],
        "_606": ["PlasticCylindricalGearMaterial"],
        "_607": ["PlasticSNCurve"],
        "_608": ["RatingMethods"],
        "_609": ["RawMaterial"],
        "_610": ["RawMaterialDatabase"],
        "_611": ["SNCurveDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMACylindricalGearMaterial",
    "BevelGearAbstractMaterialDatabase",
    "BevelGearISOMaterial",
    "BevelGearISOMaterialDatabase",
    "BevelGearMaterial",
    "BevelGearMaterialDatabase",
    "CylindricalGearAGMAMaterialDatabase",
    "CylindricalGearISOMaterialDatabase",
    "CylindricalGearMaterial",
    "CylindricalGearMaterialDatabase",
    "CylindricalGearPlasticMaterialDatabase",
    "GearMaterial",
    "GearMaterialDatabase",
    "GearMaterialExpertSystemFactorSettings",
    "ISOCylindricalGearMaterial",
    "ISOTR1417912001CoefficientOfFrictionConstants",
    "ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
    "KlingelnbergConicalGearMaterialDatabase",
    "KlingelnbergCycloPalloidConicalGearMaterial",
    "ManufactureRating",
    "PlasticCylindricalGearMaterial",
    "PlasticSNCurve",
    "RatingMethods",
    "RawMaterial",
    "RawMaterialDatabase",
    "SNCurveDefinition",
)
