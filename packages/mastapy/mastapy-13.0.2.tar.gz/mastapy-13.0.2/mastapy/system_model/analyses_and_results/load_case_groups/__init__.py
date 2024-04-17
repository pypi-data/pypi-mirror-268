"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5666 import AbstractDesignStateLoadCaseGroup
    from ._5667 import AbstractLoadCaseGroup
    from ._5668 import AbstractStaticLoadCaseGroup
    from ._5669 import ClutchEngagementStatus
    from ._5670 import ConceptSynchroGearEngagementStatus
    from ._5671 import DesignState
    from ._5672 import DutyCycle
    from ._5673 import GenericClutchEngagementStatus
    from ._5674 import LoadCaseGroupHistograms
    from ._5675 import SubGroupInSingleDesignState
    from ._5676 import SystemOptimisationGearSet
    from ._5677 import SystemOptimiserGearSetOptimisation
    from ._5678 import SystemOptimiserTargets
    from ._5679 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        "_5666": ["AbstractDesignStateLoadCaseGroup"],
        "_5667": ["AbstractLoadCaseGroup"],
        "_5668": ["AbstractStaticLoadCaseGroup"],
        "_5669": ["ClutchEngagementStatus"],
        "_5670": ["ConceptSynchroGearEngagementStatus"],
        "_5671": ["DesignState"],
        "_5672": ["DutyCycle"],
        "_5673": ["GenericClutchEngagementStatus"],
        "_5674": ["LoadCaseGroupHistograms"],
        "_5675": ["SubGroupInSingleDesignState"],
        "_5676": ["SystemOptimisationGearSet"],
        "_5677": ["SystemOptimiserGearSetOptimisation"],
        "_5678": ["SystemOptimiserTargets"],
        "_5679": ["TimeSeriesLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractDesignStateLoadCaseGroup",
    "AbstractLoadCaseGroup",
    "AbstractStaticLoadCaseGroup",
    "ClutchEngagementStatus",
    "ConceptSynchroGearEngagementStatus",
    "DesignState",
    "DutyCycle",
    "GenericClutchEngagementStatus",
    "LoadCaseGroupHistograms",
    "SubGroupInSingleDesignState",
    "SystemOptimisationGearSet",
    "SystemOptimiserGearSetOptimisation",
    "SystemOptimiserTargets",
    "TimeSeriesLoadCaseGroup",
)
