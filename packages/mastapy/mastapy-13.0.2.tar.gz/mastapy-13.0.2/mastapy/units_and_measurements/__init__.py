"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7568 import MeasurementType
    from ._7569 import MeasurementTypeExtensions
else:
    import_structure = {
        "_7568": ["MeasurementType"],
        "_7569": ["MeasurementTypeExtensions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "MeasurementType",
    "MeasurementTypeExtensions",
)
