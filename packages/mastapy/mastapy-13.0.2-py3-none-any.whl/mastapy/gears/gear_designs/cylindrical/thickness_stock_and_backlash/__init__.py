"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1095 import FinishStockSpecification
    from ._1096 import FinishStockType
    from ._1097 import NominalValueSpecification
    from ._1098 import NoValueSpecification
else:
    import_structure = {
        "_1095": ["FinishStockSpecification"],
        "_1096": ["FinishStockType"],
        "_1097": ["NominalValueSpecification"],
        "_1098": ["NoValueSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FinishStockSpecification",
    "FinishStockType",
    "NominalValueSpecification",
    "NoValueSpecification",
)
