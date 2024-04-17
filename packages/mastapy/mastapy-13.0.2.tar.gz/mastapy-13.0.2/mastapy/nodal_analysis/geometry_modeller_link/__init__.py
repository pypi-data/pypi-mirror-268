"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._155 import BaseGeometryModellerDimension
    from ._156 import GeometryModellerAngleDimension
    from ._157 import GeometryModellerCountDimension
    from ._158 import GeometryModellerDesignInformation
    from ._159 import GeometryModellerDimension
    from ._160 import GeometryModellerDimensions
    from ._161 import GeometryModellerDimensionType
    from ._162 import GeometryModellerLengthDimension
    from ._163 import GeometryModellerSettings
    from ._164 import GeometryModellerUnitlessDimension
    from ._165 import MeshRequest
    from ._166 import MeshRequestResult
    from ._167 import RepositionComponentDetails
else:
    import_structure = {
        "_155": ["BaseGeometryModellerDimension"],
        "_156": ["GeometryModellerAngleDimension"],
        "_157": ["GeometryModellerCountDimension"],
        "_158": ["GeometryModellerDesignInformation"],
        "_159": ["GeometryModellerDimension"],
        "_160": ["GeometryModellerDimensions"],
        "_161": ["GeometryModellerDimensionType"],
        "_162": ["GeometryModellerLengthDimension"],
        "_163": ["GeometryModellerSettings"],
        "_164": ["GeometryModellerUnitlessDimension"],
        "_165": ["MeshRequest"],
        "_166": ["MeshRequestResult"],
        "_167": ["RepositionComponentDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BaseGeometryModellerDimension",
    "GeometryModellerAngleDimension",
    "GeometryModellerCountDimension",
    "GeometryModellerDesignInformation",
    "GeometryModellerDimension",
    "GeometryModellerDimensions",
    "GeometryModellerDimensionType",
    "GeometryModellerLengthDimension",
    "GeometryModellerSettings",
    "GeometryModellerUnitlessDimension",
    "MeshRequest",
    "MeshRequestResult",
    "RepositionComponentDetails",
)
