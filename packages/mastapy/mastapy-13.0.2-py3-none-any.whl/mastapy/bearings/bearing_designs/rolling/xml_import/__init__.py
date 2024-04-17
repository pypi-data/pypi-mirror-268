"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2183 import AbstractXmlVariableAssignment
    from ._2184 import BearingImportFile
    from ._2185 import RollingBearingImporter
    from ._2186 import XmlBearingTypeMapping
    from ._2187 import XMLVariableAssignment
else:
    import_structure = {
        "_2183": ["AbstractXmlVariableAssignment"],
        "_2184": ["BearingImportFile"],
        "_2185": ["RollingBearingImporter"],
        "_2186": ["XmlBearingTypeMapping"],
        "_2187": ["XMLVariableAssignment"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractXmlVariableAssignment",
    "BearingImportFile",
    "RollingBearingImporter",
    "XmlBearingTypeMapping",
    "XMLVariableAssignment",
)
