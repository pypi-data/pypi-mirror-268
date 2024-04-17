"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5680 import AbstractAssemblyStaticLoadCaseGroup
    from ._5681 import ComponentStaticLoadCaseGroup
    from ._5682 import ConnectionStaticLoadCaseGroup
    from ._5683 import DesignEntityStaticLoadCaseGroup
    from ._5684 import GearSetStaticLoadCaseGroup
    from ._5685 import PartStaticLoadCaseGroup
else:
    import_structure = {
        "_5680": ["AbstractAssemblyStaticLoadCaseGroup"],
        "_5681": ["ComponentStaticLoadCaseGroup"],
        "_5682": ["ConnectionStaticLoadCaseGroup"],
        "_5683": ["DesignEntityStaticLoadCaseGroup"],
        "_5684": ["GearSetStaticLoadCaseGroup"],
        "_5685": ["PartStaticLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStaticLoadCaseGroup",
    "ComponentStaticLoadCaseGroup",
    "ConnectionStaticLoadCaseGroup",
    "DesignEntityStaticLoadCaseGroup",
    "GearSetStaticLoadCaseGroup",
    "PartStaticLoadCaseGroup",
)
