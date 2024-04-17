"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1576 import DataScalingOptions
    from ._1577 import DataScalingReferenceValues
    from ._1578 import DataScalingReferenceValuesBase
else:
    import_structure = {
        "_1576": ["DataScalingOptions"],
        "_1577": ["DataScalingReferenceValues"],
        "_1578": ["DataScalingReferenceValuesBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DataScalingOptions",
    "DataScalingReferenceValues",
    "DataScalingReferenceValuesBase",
)
