"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._944 import BevelHypoidGearDesignSettingsDatabase
    from ._945 import BevelHypoidGearDesignSettingsItem
    from ._946 import BevelHypoidGearRatingSettingsDatabase
    from ._947 import BevelHypoidGearRatingSettingsItem
    from ._948 import DesignConstraint
    from ._949 import DesignConstraintCollectionDatabase
    from ._950 import DesignConstraintsCollection
    from ._951 import GearDesign
    from ._952 import GearDesignComponent
    from ._953 import GearMeshDesign
    from ._954 import GearSetDesign
    from ._955 import SelectedDesignConstraintsCollection
else:
    import_structure = {
        "_944": ["BevelHypoidGearDesignSettingsDatabase"],
        "_945": ["BevelHypoidGearDesignSettingsItem"],
        "_946": ["BevelHypoidGearRatingSettingsDatabase"],
        "_947": ["BevelHypoidGearRatingSettingsItem"],
        "_948": ["DesignConstraint"],
        "_949": ["DesignConstraintCollectionDatabase"],
        "_950": ["DesignConstraintsCollection"],
        "_951": ["GearDesign"],
        "_952": ["GearDesignComponent"],
        "_953": ["GearMeshDesign"],
        "_954": ["GearSetDesign"],
        "_955": ["SelectedDesignConstraintsCollection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelHypoidGearDesignSettingsDatabase",
    "BevelHypoidGearDesignSettingsItem",
    "BevelHypoidGearRatingSettingsDatabase",
    "BevelHypoidGearRatingSettingsItem",
    "DesignConstraint",
    "DesignConstraintCollectionDatabase",
    "DesignConstraintsCollection",
    "GearDesign",
    "GearDesignComponent",
    "GearMeshDesign",
    "GearSetDesign",
    "SelectedDesignConstraintsCollection",
)
