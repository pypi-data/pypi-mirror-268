"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1831 import Database
    from ._1832 import DatabaseConnectionSettings
    from ._1833 import DatabaseKey
    from ._1834 import DatabaseSettings
    from ._1835 import NamedDatabase
    from ._1836 import NamedDatabaseItem
    from ._1837 import NamedKey
    from ._1838 import SQLDatabase
else:
    import_structure = {
        "_1831": ["Database"],
        "_1832": ["DatabaseConnectionSettings"],
        "_1833": ["DatabaseKey"],
        "_1834": ["DatabaseSettings"],
        "_1835": ["NamedDatabase"],
        "_1836": ["NamedDatabaseItem"],
        "_1837": ["NamedKey"],
        "_1838": ["SQLDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Database",
    "DatabaseConnectionSettings",
    "DatabaseKey",
    "DatabaseSettings",
    "NamedDatabase",
    "NamedDatabaseItem",
    "NamedKey",
    "SQLDatabase",
)
