"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1817 import NamedTuple1
    from ._1818 import NamedTuple2
    from ._1819 import NamedTuple3
    from ._1820 import NamedTuple4
    from ._1821 import NamedTuple5
    from ._1822 import NamedTuple6
    from ._1823 import NamedTuple7
else:
    import_structure = {
        "_1817": ["NamedTuple1"],
        "_1818": ["NamedTuple2"],
        "_1819": ["NamedTuple3"],
        "_1820": ["NamedTuple4"],
        "_1821": ["NamedTuple5"],
        "_1822": ["NamedTuple6"],
        "_1823": ["NamedTuple7"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "NamedTuple1",
    "NamedTuple2",
    "NamedTuple3",
    "NamedTuple4",
    "NamedTuple5",
    "NamedTuple6",
    "NamedTuple7",
)
