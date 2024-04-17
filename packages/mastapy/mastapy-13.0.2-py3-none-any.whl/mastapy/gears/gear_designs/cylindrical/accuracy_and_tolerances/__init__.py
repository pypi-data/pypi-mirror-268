"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1138 import AGMA2000A88AccuracyGrader
    from ._1139 import AGMA20151A01AccuracyGrader
    from ._1140 import AGMA20151AccuracyGrades
    from ._1141 import AGMAISO13281B14AccuracyGrader
    from ._1142 import CylindricalAccuracyGrader
    from ._1143 import CylindricalAccuracyGraderWithProfileFormAndSlope
    from ._1144 import CylindricalAccuracyGrades
    from ._1145 import CylindricalGearAccuracyTolerances
    from ._1146 import DIN3967SystemOfGearFits
    from ._1147 import ISO132811995AccuracyGrader
    from ._1148 import ISO132812013AccuracyGrader
    from ._1149 import ISO1328AccuracyGraderCommon
    from ._1150 import ISO1328AccuracyGrades
    from ._1151 import OverridableTolerance
else:
    import_structure = {
        "_1138": ["AGMA2000A88AccuracyGrader"],
        "_1139": ["AGMA20151A01AccuracyGrader"],
        "_1140": ["AGMA20151AccuracyGrades"],
        "_1141": ["AGMAISO13281B14AccuracyGrader"],
        "_1142": ["CylindricalAccuracyGrader"],
        "_1143": ["CylindricalAccuracyGraderWithProfileFormAndSlope"],
        "_1144": ["CylindricalAccuracyGrades"],
        "_1145": ["CylindricalGearAccuracyTolerances"],
        "_1146": ["DIN3967SystemOfGearFits"],
        "_1147": ["ISO132811995AccuracyGrader"],
        "_1148": ["ISO132812013AccuracyGrader"],
        "_1149": ["ISO1328AccuracyGraderCommon"],
        "_1150": ["ISO1328AccuracyGrades"],
        "_1151": ["OverridableTolerance"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2000A88AccuracyGrader",
    "AGMA20151A01AccuracyGrader",
    "AGMA20151AccuracyGrades",
    "AGMAISO13281B14AccuracyGrader",
    "CylindricalAccuracyGrader",
    "CylindricalAccuracyGraderWithProfileFormAndSlope",
    "CylindricalAccuracyGrades",
    "CylindricalGearAccuracyTolerances",
    "DIN3967SystemOfGearFits",
    "ISO132811995AccuracyGrader",
    "ISO132812013AccuracyGrader",
    "ISO1328AccuracyGraderCommon",
    "ISO1328AccuracyGrades",
    "OverridableTolerance",
)
