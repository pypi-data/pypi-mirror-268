"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._824 import BasicConicalGearMachineSettings
    from ._825 import BasicConicalGearMachineSettingsFormate
    from ._826 import BasicConicalGearMachineSettingsGenerated
    from ._827 import CradleStyleConicalMachineSettingsGenerated
else:
    import_structure = {
        "_824": ["BasicConicalGearMachineSettings"],
        "_825": ["BasicConicalGearMachineSettingsFormate"],
        "_826": ["BasicConicalGearMachineSettingsGenerated"],
        "_827": ["CradleStyleConicalMachineSettingsGenerated"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicConicalGearMachineSettings",
    "BasicConicalGearMachineSettingsFormate",
    "BasicConicalGearMachineSettingsGenerated",
    "CradleStyleConicalMachineSettingsGenerated",
)
