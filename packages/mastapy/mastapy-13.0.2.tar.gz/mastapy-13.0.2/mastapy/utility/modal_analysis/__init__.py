"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1803 import DesignEntityExcitationDescription
else:
    import_structure = {
        "_1803": ["DesignEntityExcitationDescription"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("DesignEntityExcitationDescription",)
