"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2188 import AxialFeedJournalBearing
    from ._2189 import AxialGrooveJournalBearing
    from ._2190 import AxialHoleJournalBearing
    from ._2191 import CircumferentialFeedJournalBearing
    from ._2192 import CylindricalHousingJournalBearing
    from ._2193 import MachineryEncasedJournalBearing
    from ._2194 import PadFluidFilmBearing
    from ._2195 import PedestalJournalBearing
    from ._2196 import PlainGreaseFilledJournalBearing
    from ._2197 import PlainGreaseFilledJournalBearingHousingType
    from ._2198 import PlainJournalBearing
    from ._2199 import PlainJournalHousing
    from ._2200 import PlainOilFedJournalBearing
    from ._2201 import TiltingPadJournalBearing
    from ._2202 import TiltingPadThrustBearing
else:
    import_structure = {
        "_2188": ["AxialFeedJournalBearing"],
        "_2189": ["AxialGrooveJournalBearing"],
        "_2190": ["AxialHoleJournalBearing"],
        "_2191": ["CircumferentialFeedJournalBearing"],
        "_2192": ["CylindricalHousingJournalBearing"],
        "_2193": ["MachineryEncasedJournalBearing"],
        "_2194": ["PadFluidFilmBearing"],
        "_2195": ["PedestalJournalBearing"],
        "_2196": ["PlainGreaseFilledJournalBearing"],
        "_2197": ["PlainGreaseFilledJournalBearingHousingType"],
        "_2198": ["PlainJournalBearing"],
        "_2199": ["PlainJournalHousing"],
        "_2200": ["PlainOilFedJournalBearing"],
        "_2201": ["TiltingPadJournalBearing"],
        "_2202": ["TiltingPadThrustBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialFeedJournalBearing",
    "AxialGrooveJournalBearing",
    "AxialHoleJournalBearing",
    "CircumferentialFeedJournalBearing",
    "CylindricalHousingJournalBearing",
    "MachineryEncasedJournalBearing",
    "PadFluidFilmBearing",
    "PedestalJournalBearing",
    "PlainGreaseFilledJournalBearing",
    "PlainGreaseFilledJournalBearingHousingType",
    "PlainJournalBearing",
    "PlainJournalHousing",
    "PlainOilFedJournalBearing",
    "TiltingPadJournalBearing",
    "TiltingPadThrustBearing",
)
