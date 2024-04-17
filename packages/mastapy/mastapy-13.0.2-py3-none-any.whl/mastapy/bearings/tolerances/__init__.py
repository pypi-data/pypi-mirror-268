"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1908 import BearingConnectionComponent
    from ._1909 import InternalClearanceClass
    from ._1910 import BearingToleranceClass
    from ._1911 import BearingToleranceDefinitionOptions
    from ._1912 import FitType
    from ._1913 import InnerRingTolerance
    from ._1914 import InnerSupportTolerance
    from ._1915 import InterferenceDetail
    from ._1916 import InterferenceTolerance
    from ._1917 import ITDesignation
    from ._1918 import MountingSleeveDiameterDetail
    from ._1919 import OuterRingTolerance
    from ._1920 import OuterSupportTolerance
    from ._1921 import RaceDetail
    from ._1922 import RaceRoundnessAtAngle
    from ._1923 import RadialSpecificationMethod
    from ._1924 import RingTolerance
    from ._1925 import RoundnessSpecification
    from ._1926 import RoundnessSpecificationType
    from ._1927 import SupportDetail
    from ._1928 import SupportMaterialSource
    from ._1929 import SupportTolerance
    from ._1930 import SupportToleranceLocationDesignation
    from ._1931 import ToleranceCombination
    from ._1932 import TypeOfFit
else:
    import_structure = {
        "_1908": ["BearingConnectionComponent"],
        "_1909": ["InternalClearanceClass"],
        "_1910": ["BearingToleranceClass"],
        "_1911": ["BearingToleranceDefinitionOptions"],
        "_1912": ["FitType"],
        "_1913": ["InnerRingTolerance"],
        "_1914": ["InnerSupportTolerance"],
        "_1915": ["InterferenceDetail"],
        "_1916": ["InterferenceTolerance"],
        "_1917": ["ITDesignation"],
        "_1918": ["MountingSleeveDiameterDetail"],
        "_1919": ["OuterRingTolerance"],
        "_1920": ["OuterSupportTolerance"],
        "_1921": ["RaceDetail"],
        "_1922": ["RaceRoundnessAtAngle"],
        "_1923": ["RadialSpecificationMethod"],
        "_1924": ["RingTolerance"],
        "_1925": ["RoundnessSpecification"],
        "_1926": ["RoundnessSpecificationType"],
        "_1927": ["SupportDetail"],
        "_1928": ["SupportMaterialSource"],
        "_1929": ["SupportTolerance"],
        "_1930": ["SupportToleranceLocationDesignation"],
        "_1931": ["ToleranceCombination"],
        "_1932": ["TypeOfFit"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceDetail",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)
