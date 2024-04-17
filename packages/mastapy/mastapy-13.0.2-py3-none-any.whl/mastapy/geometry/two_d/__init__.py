"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._313 import CADFace
    from ._314 import CADFaceGroup
    from ._315 import InternalExternalType
else:
    import_structure = {
        "_313": ["CADFace"],
        "_314": ["CADFaceGroup"],
        "_315": ["InternalExternalType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CADFace",
    "CADFaceGroup",
    "InternalExternalType",
)
