"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1841 import EnumWithSelectedValue
    from ._1843 import DeletableCollectionMember
    from ._1844 import DutyCyclePropertySummary
    from ._1845 import DutyCyclePropertySummaryForce
    from ._1846 import DutyCyclePropertySummaryPercentage
    from ._1847 import DutyCyclePropertySummarySmallAngle
    from ._1848 import DutyCyclePropertySummaryStress
    from ._1849 import DutyCyclePropertySummaryVeryShortLength
    from ._1850 import EnumWithBoolean
    from ._1851 import NamedRangeWithOverridableMinAndMax
    from ._1852 import TypedObjectsWithOption
else:
    import_structure = {
        "_1841": ["EnumWithSelectedValue"],
        "_1843": ["DeletableCollectionMember"],
        "_1844": ["DutyCyclePropertySummary"],
        "_1845": ["DutyCyclePropertySummaryForce"],
        "_1846": ["DutyCyclePropertySummaryPercentage"],
        "_1847": ["DutyCyclePropertySummarySmallAngle"],
        "_1848": ["DutyCyclePropertySummaryStress"],
        "_1849": ["DutyCyclePropertySummaryVeryShortLength"],
        "_1850": ["EnumWithBoolean"],
        "_1851": ["NamedRangeWithOverridableMinAndMax"],
        "_1852": ["TypedObjectsWithOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "EnumWithSelectedValue",
    "DeletableCollectionMember",
    "DutyCyclePropertySummary",
    "DutyCyclePropertySummaryForce",
    "DutyCyclePropertySummaryPercentage",
    "DutyCyclePropertySummarySmallAngle",
    "DutyCyclePropertySummaryStress",
    "DutyCyclePropertySummaryVeryShortLength",
    "EnumWithBoolean",
    "NamedRangeWithOverridableMinAndMax",
    "TypedObjectsWithOption",
)
