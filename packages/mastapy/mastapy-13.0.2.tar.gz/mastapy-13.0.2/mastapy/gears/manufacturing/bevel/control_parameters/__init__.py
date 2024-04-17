"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._820 import ConicalGearManufacturingControlParameters
    from ._821 import ConicalManufacturingSGMControlParameters
    from ._822 import ConicalManufacturingSGTControlParameters
    from ._823 import ConicalManufacturingSMTControlParameters
else:
    import_structure = {
        "_820": ["ConicalGearManufacturingControlParameters"],
        "_821": ["ConicalManufacturingSGMControlParameters"],
        "_822": ["ConicalManufacturingSGTControlParameters"],
        "_823": ["ConicalManufacturingSMTControlParameters"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearManufacturingControlParameters",
    "ConicalManufacturingSGMControlParameters",
    "ConicalManufacturingSGTControlParameters",
    "ConicalManufacturingSMTControlParameters",
)
