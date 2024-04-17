"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._423 import GeneralLoadFactorCalculationMethod
    from ._424 import Iso10300FinishingMethods
    from ._425 import ISO10300MeshSingleFlankRating
    from ._426 import ISO10300MeshSingleFlankRatingBevelMethodB2
    from ._427 import ISO10300MeshSingleFlankRatingHypoidMethodB2
    from ._428 import ISO10300MeshSingleFlankRatingMethodB1
    from ._429 import ISO10300MeshSingleFlankRatingMethodB2
    from ._430 import ISO10300RateableMesh
    from ._431 import ISO10300RatingMethod
    from ._432 import ISO10300SingleFlankRating
    from ._433 import ISO10300SingleFlankRatingBevelMethodB2
    from ._434 import ISO10300SingleFlankRatingHypoidMethodB2
    from ._435 import ISO10300SingleFlankRatingMethodB1
    from ._436 import ISO10300SingleFlankRatingMethodB2
    from ._437 import MountingConditionsOfPinionAndWheel
    from ._438 import PittingFactorCalculationMethod
    from ._439 import ProfileCrowningSetting
    from ._440 import VerificationOfContactPattern
else:
    import_structure = {
        "_423": ["GeneralLoadFactorCalculationMethod"],
        "_424": ["Iso10300FinishingMethods"],
        "_425": ["ISO10300MeshSingleFlankRating"],
        "_426": ["ISO10300MeshSingleFlankRatingBevelMethodB2"],
        "_427": ["ISO10300MeshSingleFlankRatingHypoidMethodB2"],
        "_428": ["ISO10300MeshSingleFlankRatingMethodB1"],
        "_429": ["ISO10300MeshSingleFlankRatingMethodB2"],
        "_430": ["ISO10300RateableMesh"],
        "_431": ["ISO10300RatingMethod"],
        "_432": ["ISO10300SingleFlankRating"],
        "_433": ["ISO10300SingleFlankRatingBevelMethodB2"],
        "_434": ["ISO10300SingleFlankRatingHypoidMethodB2"],
        "_435": ["ISO10300SingleFlankRatingMethodB1"],
        "_436": ["ISO10300SingleFlankRatingMethodB2"],
        "_437": ["MountingConditionsOfPinionAndWheel"],
        "_438": ["PittingFactorCalculationMethod"],
        "_439": ["ProfileCrowningSetting"],
        "_440": ["VerificationOfContactPattern"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GeneralLoadFactorCalculationMethod",
    "Iso10300FinishingMethods",
    "ISO10300MeshSingleFlankRating",
    "ISO10300MeshSingleFlankRatingBevelMethodB2",
    "ISO10300MeshSingleFlankRatingHypoidMethodB2",
    "ISO10300MeshSingleFlankRatingMethodB1",
    "ISO10300MeshSingleFlankRatingMethodB2",
    "ISO10300RateableMesh",
    "ISO10300RatingMethod",
    "ISO10300SingleFlankRating",
    "ISO10300SingleFlankRatingBevelMethodB2",
    "ISO10300SingleFlankRatingHypoidMethodB2",
    "ISO10300SingleFlankRatingMethodB1",
    "ISO10300SingleFlankRatingMethodB2",
    "MountingConditionsOfPinionAndWheel",
    "PittingFactorCalculationMethod",
    "ProfileCrowningSetting",
    "VerificationOfContactPattern",
)
