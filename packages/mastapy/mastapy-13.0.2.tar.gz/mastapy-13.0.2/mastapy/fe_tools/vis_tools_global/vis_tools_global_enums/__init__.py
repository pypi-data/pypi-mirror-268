"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1240 import BeamSectionType
    from ._1241 import ContactPairConstrainedSurfaceType
    from ._1242 import ContactPairReferenceSurfaceType
    from ._1243 import ElementPropertiesShellWallType
else:
    import_structure = {
        "_1240": ["BeamSectionType"],
        "_1241": ["ContactPairConstrainedSurfaceType"],
        "_1242": ["ContactPairReferenceSurfaceType"],
        "_1243": ["ElementPropertiesShellWallType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeamSectionType",
    "ContactPairConstrainedSurfaceType",
    "ContactPairReferenceSurfaceType",
    "ElementPropertiesShellWallType",
)
