"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1934 import ProfileDataToUse
    from ._1935 import ProfileSet
    from ._1936 import ProfileToFit
    from ._1937 import RollerBearingConicalProfile
    from ._1938 import RollerBearingCrownedProfile
    from ._1939 import RollerBearingDinLundbergProfile
    from ._1940 import RollerBearingFlatProfile
    from ._1941 import RollerBearingJohnsGoharProfile
    from ._1942 import RollerBearingLundbergProfile
    from ._1943 import RollerBearingProfile
    from ._1944 import RollerBearingUserSpecifiedProfile
    from ._1945 import RollerRaceProfilePoint
    from ._1946 import UserSpecifiedProfilePoint
    from ._1947 import UserSpecifiedRollerRaceProfilePoint
else:
    import_structure = {
        "_1934": ["ProfileDataToUse"],
        "_1935": ["ProfileSet"],
        "_1936": ["ProfileToFit"],
        "_1937": ["RollerBearingConicalProfile"],
        "_1938": ["RollerBearingCrownedProfile"],
        "_1939": ["RollerBearingDinLundbergProfile"],
        "_1940": ["RollerBearingFlatProfile"],
        "_1941": ["RollerBearingJohnsGoharProfile"],
        "_1942": ["RollerBearingLundbergProfile"],
        "_1943": ["RollerBearingProfile"],
        "_1944": ["RollerBearingUserSpecifiedProfile"],
        "_1945": ["RollerRaceProfilePoint"],
        "_1946": ["UserSpecifiedProfilePoint"],
        "_1947": ["UserSpecifiedRollerRaceProfilePoint"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)
