"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2083 import AdjustedSpeed
    from ._2084 import AdjustmentFactors
    from ._2085 import BearingLoads
    from ._2086 import BearingRatingLife
    from ._2087 import DynamicAxialLoadCarryingCapacity
    from ._2088 import Frequencies
    from ._2089 import FrequencyOfOverRolling
    from ._2090 import Friction
    from ._2091 import FrictionalMoment
    from ._2092 import FrictionSources
    from ._2093 import Grease
    from ._2094 import GreaseLifeAndRelubricationInterval
    from ._2095 import GreaseQuantity
    from ._2096 import InitialFill
    from ._2097 import LifeModel
    from ._2098 import MinimumLoad
    from ._2099 import OperatingViscosity
    from ._2100 import PermissibleAxialLoad
    from ._2101 import RotationalFrequency
    from ._2102 import SKFAuthentication
    from ._2103 import SKFCalculationResult
    from ._2104 import SKFCredentials
    from ._2105 import SKFModuleResults
    from ._2106 import StaticSafetyFactors
    from ._2107 import Viscosities
else:
    import_structure = {
        "_2083": ["AdjustedSpeed"],
        "_2084": ["AdjustmentFactors"],
        "_2085": ["BearingLoads"],
        "_2086": ["BearingRatingLife"],
        "_2087": ["DynamicAxialLoadCarryingCapacity"],
        "_2088": ["Frequencies"],
        "_2089": ["FrequencyOfOverRolling"],
        "_2090": ["Friction"],
        "_2091": ["FrictionalMoment"],
        "_2092": ["FrictionSources"],
        "_2093": ["Grease"],
        "_2094": ["GreaseLifeAndRelubricationInterval"],
        "_2095": ["GreaseQuantity"],
        "_2096": ["InitialFill"],
        "_2097": ["LifeModel"],
        "_2098": ["MinimumLoad"],
        "_2099": ["OperatingViscosity"],
        "_2100": ["PermissibleAxialLoad"],
        "_2101": ["RotationalFrequency"],
        "_2102": ["SKFAuthentication"],
        "_2103": ["SKFCalculationResult"],
        "_2104": ["SKFCredentials"],
        "_2105": ["SKFModuleResults"],
        "_2106": ["StaticSafetyFactors"],
        "_2107": ["Viscosities"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdjustedSpeed",
    "AdjustmentFactors",
    "BearingLoads",
    "BearingRatingLife",
    "DynamicAxialLoadCarryingCapacity",
    "Frequencies",
    "FrequencyOfOverRolling",
    "Friction",
    "FrictionalMoment",
    "FrictionSources",
    "Grease",
    "GreaseLifeAndRelubricationInterval",
    "GreaseQuantity",
    "InitialFill",
    "LifeModel",
    "MinimumLoad",
    "OperatingViscosity",
    "PermissibleAxialLoad",
    "RotationalFrequency",
    "SKFAuthentication",
    "SKFCalculationResult",
    "SKFCredentials",
    "SKFModuleResults",
    "StaticSafetyFactors",
    "Viscosities",
)
