"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1876 import BearingCatalog
    from ._1877 import BasicDynamicLoadRatingCalculationMethod
    from ._1878 import BasicStaticLoadRatingCalculationMethod
    from ._1879 import BearingCageMaterial
    from ._1880 import BearingDampingMatrixOption
    from ._1881 import BearingLoadCaseResultsForPST
    from ._1882 import BearingLoadCaseResultsLightweight
    from ._1883 import BearingMeasurementType
    from ._1884 import BearingModel
    from ._1885 import BearingRow
    from ._1886 import BearingSettings
    from ._1887 import BearingSettingsDatabase
    from ._1888 import BearingSettingsItem
    from ._1889 import BearingStiffnessMatrixOption
    from ._1890 import ExponentAndReductionFactorsInISO16281Calculation
    from ._1891 import FluidFilmTemperatureOptions
    from ._1892 import HybridSteelAll
    from ._1893 import JournalBearingType
    from ._1894 import JournalOilFeedType
    from ._1895 import MountingPointSurfaceFinishes
    from ._1896 import OuterRingMounting
    from ._1897 import RatingLife
    from ._1898 import RollerBearingProfileTypes
    from ._1899 import RollingBearingArrangement
    from ._1900 import RollingBearingDatabase
    from ._1901 import RollingBearingKey
    from ._1902 import RollingBearingRaceType
    from ._1903 import RollingBearingType
    from ._1904 import RotationalDirections
    from ._1905 import SealLocation
    from ._1906 import SKFSettings
    from ._1907 import TiltingPadTypes
else:
    import_structure = {
        "_1876": ["BearingCatalog"],
        "_1877": ["BasicDynamicLoadRatingCalculationMethod"],
        "_1878": ["BasicStaticLoadRatingCalculationMethod"],
        "_1879": ["BearingCageMaterial"],
        "_1880": ["BearingDampingMatrixOption"],
        "_1881": ["BearingLoadCaseResultsForPST"],
        "_1882": ["BearingLoadCaseResultsLightweight"],
        "_1883": ["BearingMeasurementType"],
        "_1884": ["BearingModel"],
        "_1885": ["BearingRow"],
        "_1886": ["BearingSettings"],
        "_1887": ["BearingSettingsDatabase"],
        "_1888": ["BearingSettingsItem"],
        "_1889": ["BearingStiffnessMatrixOption"],
        "_1890": ["ExponentAndReductionFactorsInISO16281Calculation"],
        "_1891": ["FluidFilmTemperatureOptions"],
        "_1892": ["HybridSteelAll"],
        "_1893": ["JournalBearingType"],
        "_1894": ["JournalOilFeedType"],
        "_1895": ["MountingPointSurfaceFinishes"],
        "_1896": ["OuterRingMounting"],
        "_1897": ["RatingLife"],
        "_1898": ["RollerBearingProfileTypes"],
        "_1899": ["RollingBearingArrangement"],
        "_1900": ["RollingBearingDatabase"],
        "_1901": ["RollingBearingKey"],
        "_1902": ["RollingBearingRaceType"],
        "_1903": ["RollingBearingType"],
        "_1904": ["RotationalDirections"],
        "_1905": ["SealLocation"],
        "_1906": ["SKFSettings"],
        "_1907": ["TiltingPadTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingCatalog",
    "BasicDynamicLoadRatingCalculationMethod",
    "BasicStaticLoadRatingCalculationMethod",
    "BearingCageMaterial",
    "BearingDampingMatrixOption",
    "BearingLoadCaseResultsForPST",
    "BearingLoadCaseResultsLightweight",
    "BearingMeasurementType",
    "BearingModel",
    "BearingRow",
    "BearingSettings",
    "BearingSettingsDatabase",
    "BearingSettingsItem",
    "BearingStiffnessMatrixOption",
    "ExponentAndReductionFactorsInISO16281Calculation",
    "FluidFilmTemperatureOptions",
    "HybridSteelAll",
    "JournalBearingType",
    "JournalOilFeedType",
    "MountingPointSurfaceFinishes",
    "OuterRingMounting",
    "RatingLife",
    "RollerBearingProfileTypes",
    "RollingBearingArrangement",
    "RollingBearingDatabase",
    "RollingBearingKey",
    "RollingBearingRaceType",
    "RollingBearingType",
    "RotationalDirections",
    "SealLocation",
    "SKFSettings",
    "TiltingPadTypes",
)
