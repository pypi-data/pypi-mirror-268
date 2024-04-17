"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1444 import KeyedJointDesign
    from ._1445 import KeyTypes
    from ._1446 import KeywayJointHalfDesign
    from ._1447 import NumberOfKeys
else:
    import_structure = {
        "_1444": ["KeyedJointDesign"],
        "_1445": ["KeyTypes"],
        "_1446": ["KeywayJointHalfDesign"],
        "_1447": ["NumberOfKeys"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)
