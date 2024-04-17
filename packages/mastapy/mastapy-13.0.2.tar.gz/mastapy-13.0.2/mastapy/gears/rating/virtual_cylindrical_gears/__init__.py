"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._381 import BevelVirtualCylindricalGearISO10300MethodB2
    from ._382 import BevelVirtualCylindricalGearSetISO10300MethodB1
    from ._383 import BevelVirtualCylindricalGearSetISO10300MethodB2
    from ._384 import HypoidVirtualCylindricalGearISO10300MethodB2
    from ._385 import HypoidVirtualCylindricalGearSetISO10300MethodB1
    from ._386 import HypoidVirtualCylindricalGearSetISO10300MethodB2
    from ._387 import KlingelnbergHypoidVirtualCylindricalGear
    from ._388 import KlingelnbergSpiralBevelVirtualCylindricalGear
    from ._389 import KlingelnbergVirtualCylindricalGear
    from ._390 import KlingelnbergVirtualCylindricalGearSet
    from ._391 import VirtualCylindricalGear
    from ._392 import VirtualCylindricalGearBasic
    from ._393 import VirtualCylindricalGearISO10300MethodB1
    from ._394 import VirtualCylindricalGearISO10300MethodB2
    from ._395 import VirtualCylindricalGearSet
    from ._396 import VirtualCylindricalGearSetISO10300MethodB1
    from ._397 import VirtualCylindricalGearSetISO10300MethodB2
else:
    import_structure = {
        "_381": ["BevelVirtualCylindricalGearISO10300MethodB2"],
        "_382": ["BevelVirtualCylindricalGearSetISO10300MethodB1"],
        "_383": ["BevelVirtualCylindricalGearSetISO10300MethodB2"],
        "_384": ["HypoidVirtualCylindricalGearISO10300MethodB2"],
        "_385": ["HypoidVirtualCylindricalGearSetISO10300MethodB1"],
        "_386": ["HypoidVirtualCylindricalGearSetISO10300MethodB2"],
        "_387": ["KlingelnbergHypoidVirtualCylindricalGear"],
        "_388": ["KlingelnbergSpiralBevelVirtualCylindricalGear"],
        "_389": ["KlingelnbergVirtualCylindricalGear"],
        "_390": ["KlingelnbergVirtualCylindricalGearSet"],
        "_391": ["VirtualCylindricalGear"],
        "_392": ["VirtualCylindricalGearBasic"],
        "_393": ["VirtualCylindricalGearISO10300MethodB1"],
        "_394": ["VirtualCylindricalGearISO10300MethodB2"],
        "_395": ["VirtualCylindricalGearSet"],
        "_396": ["VirtualCylindricalGearSetISO10300MethodB1"],
        "_397": ["VirtualCylindricalGearSetISO10300MethodB2"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelVirtualCylindricalGearISO10300MethodB2",
    "BevelVirtualCylindricalGearSetISO10300MethodB1",
    "BevelVirtualCylindricalGearSetISO10300MethodB2",
    "HypoidVirtualCylindricalGearISO10300MethodB2",
    "HypoidVirtualCylindricalGearSetISO10300MethodB1",
    "HypoidVirtualCylindricalGearSetISO10300MethodB2",
    "KlingelnbergHypoidVirtualCylindricalGear",
    "KlingelnbergSpiralBevelVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGearSet",
    "VirtualCylindricalGear",
    "VirtualCylindricalGearBasic",
    "VirtualCylindricalGearISO10300MethodB1",
    "VirtualCylindricalGearISO10300MethodB2",
    "VirtualCylindricalGearSet",
    "VirtualCylindricalGearSetISO10300MethodB1",
    "VirtualCylindricalGearSetISO10300MethodB2",
)
