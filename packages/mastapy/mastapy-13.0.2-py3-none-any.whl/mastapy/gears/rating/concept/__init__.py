"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._551 import ConceptGearDutyCycleRating
    from ._552 import ConceptGearMeshDutyCycleRating
    from ._553 import ConceptGearMeshRating
    from ._554 import ConceptGearRating
    from ._555 import ConceptGearSetDutyCycleRating
    from ._556 import ConceptGearSetRating
else:
    import_structure = {
        "_551": ["ConceptGearDutyCycleRating"],
        "_552": ["ConceptGearMeshDutyCycleRating"],
        "_553": ["ConceptGearMeshRating"],
        "_554": ["ConceptGearRating"],
        "_555": ["ConceptGearSetDutyCycleRating"],
        "_556": ["ConceptGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDutyCycleRating",
    "ConceptGearMeshDutyCycleRating",
    "ConceptGearMeshRating",
    "ConceptGearRating",
    "ConceptGearSetDutyCycleRating",
    "ConceptGearSetRating",
)
