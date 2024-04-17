"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._993 import FaceGearDesign
    from ._994 import FaceGearDiameterFaceWidthSpecificationMethod
    from ._995 import FaceGearMeshDesign
    from ._996 import FaceGearMeshMicroGeometry
    from ._997 import FaceGearMicroGeometry
    from ._998 import FaceGearPinionDesign
    from ._999 import FaceGearSetDesign
    from ._1000 import FaceGearSetMicroGeometry
    from ._1001 import FaceGearWheelDesign
else:
    import_structure = {
        "_993": ["FaceGearDesign"],
        "_994": ["FaceGearDiameterFaceWidthSpecificationMethod"],
        "_995": ["FaceGearMeshDesign"],
        "_996": ["FaceGearMeshMicroGeometry"],
        "_997": ["FaceGearMicroGeometry"],
        "_998": ["FaceGearPinionDesign"],
        "_999": ["FaceGearSetDesign"],
        "_1000": ["FaceGearSetMicroGeometry"],
        "_1001": ["FaceGearWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDesign",
    "FaceGearDiameterFaceWidthSpecificationMethod",
    "FaceGearMeshDesign",
    "FaceGearMeshMicroGeometry",
    "FaceGearMicroGeometry",
    "FaceGearPinionDesign",
    "FaceGearSetDesign",
    "FaceGearSetMicroGeometry",
    "FaceGearWheelDesign",
)
