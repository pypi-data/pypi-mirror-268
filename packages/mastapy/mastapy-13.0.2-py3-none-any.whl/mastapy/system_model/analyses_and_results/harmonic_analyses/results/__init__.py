"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5852 import ConnectedComponentType
    from ._5853 import ExcitationSourceSelection
    from ._5854 import ExcitationSourceSelectionBase
    from ._5855 import ExcitationSourceSelectionGroup
    from ._5856 import HarmonicSelection
    from ._5857 import ModalContributionDisplayMethod
    from ._5858 import ModalContributionFilteringMethod
    from ._5859 import ResultLocationSelectionGroup
    from ._5860 import ResultLocationSelectionGroups
    from ._5861 import ResultNodeSelection
else:
    import_structure = {
        "_5852": ["ConnectedComponentType"],
        "_5853": ["ExcitationSourceSelection"],
        "_5854": ["ExcitationSourceSelectionBase"],
        "_5855": ["ExcitationSourceSelectionGroup"],
        "_5856": ["HarmonicSelection"],
        "_5857": ["ModalContributionDisplayMethod"],
        "_5858": ["ModalContributionFilteringMethod"],
        "_5859": ["ResultLocationSelectionGroup"],
        "_5860": ["ResultLocationSelectionGroups"],
        "_5861": ["ResultNodeSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConnectedComponentType",
    "ExcitationSourceSelection",
    "ExcitationSourceSelectionBase",
    "ExcitationSourceSelectionGroup",
    "HarmonicSelection",
    "ModalContributionDisplayMethod",
    "ModalContributionFilteringMethod",
    "ResultLocationSelectionGroup",
    "ResultLocationSelectionGroups",
    "ResultNodeSelection",
)
