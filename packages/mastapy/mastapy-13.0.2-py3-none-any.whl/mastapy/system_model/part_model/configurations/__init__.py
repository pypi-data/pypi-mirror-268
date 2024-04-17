"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2619 import ActiveFESubstructureSelection
    from ._2620 import ActiveFESubstructureSelectionGroup
    from ._2621 import ActiveShaftDesignSelection
    from ._2622 import ActiveShaftDesignSelectionGroup
    from ._2623 import BearingDetailConfiguration
    from ._2624 import BearingDetailSelection
    from ._2625 import PartDetailConfiguration
    from ._2626 import PartDetailSelection
else:
    import_structure = {
        "_2619": ["ActiveFESubstructureSelection"],
        "_2620": ["ActiveFESubstructureSelectionGroup"],
        "_2621": ["ActiveShaftDesignSelection"],
        "_2622": ["ActiveShaftDesignSelectionGroup"],
        "_2623": ["BearingDetailConfiguration"],
        "_2624": ["BearingDetailSelection"],
        "_2625": ["PartDetailConfiguration"],
        "_2626": ["PartDetailSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveFESubstructureSelection",
    "ActiveFESubstructureSelectionGroup",
    "ActiveShaftDesignSelection",
    "ActiveShaftDesignSelectionGroup",
    "BearingDetailConfiguration",
    "BearingDetailSelection",
    "PartDetailConfiguration",
    "PartDetailSelection",
)
