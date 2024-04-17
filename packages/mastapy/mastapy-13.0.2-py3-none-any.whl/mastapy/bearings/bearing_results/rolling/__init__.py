"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1973 import BallBearingAnalysisMethod
    from ._1974 import BallBearingContactCalculation
    from ._1975 import BallBearingRaceContactGeometry
    from ._1976 import DIN7322010Results
    from ._1977 import ForceAtLaminaGroupReportable
    from ._1978 import ForceAtLaminaReportable
    from ._1979 import FrictionModelForGyroscopicMoment
    from ._1980 import InternalClearance
    from ._1981 import ISO14179Settings
    from ._1982 import ISO14179SettingsDatabase
    from ._1983 import ISO14179SettingsPerBearingType
    from ._1984 import ISO153122018Results
    from ._1985 import ISOTR1417912001Results
    from ._1986 import ISOTR141792001Results
    from ._1987 import ISOTR1417922001Results
    from ._1988 import LoadedAbstractSphericalRollerBearingStripLoadResults
    from ._1989 import LoadedAngularContactBallBearingElement
    from ._1990 import LoadedAngularContactBallBearingResults
    from ._1991 import LoadedAngularContactBallBearingRow
    from ._1992 import LoadedAngularContactThrustBallBearingElement
    from ._1993 import LoadedAngularContactThrustBallBearingResults
    from ._1994 import LoadedAngularContactThrustBallBearingRow
    from ._1995 import LoadedAsymmetricSphericalRollerBearingElement
    from ._1996 import LoadedAsymmetricSphericalRollerBearingResults
    from ._1997 import LoadedAsymmetricSphericalRollerBearingRow
    from ._1998 import LoadedAsymmetricSphericalRollerBearingStripLoadResults
    from ._1999 import LoadedAxialThrustCylindricalRollerBearingDutyCycle
    from ._2000 import LoadedAxialThrustCylindricalRollerBearingElement
    from ._2001 import LoadedAxialThrustCylindricalRollerBearingResults
    from ._2002 import LoadedAxialThrustCylindricalRollerBearingRow
    from ._2003 import LoadedAxialThrustNeedleRollerBearingElement
    from ._2004 import LoadedAxialThrustNeedleRollerBearingResults
    from ._2005 import LoadedAxialThrustNeedleRollerBearingRow
    from ._2006 import LoadedBallBearingDutyCycle
    from ._2007 import LoadedBallBearingElement
    from ._2008 import LoadedBallBearingRaceResults
    from ._2009 import LoadedBallBearingResults
    from ._2010 import LoadedBallBearingRow
    from ._2011 import LoadedCrossedRollerBearingElement
    from ._2012 import LoadedCrossedRollerBearingResults
    from ._2013 import LoadedCrossedRollerBearingRow
    from ._2014 import LoadedCylindricalRollerBearingDutyCycle
    from ._2015 import LoadedCylindricalRollerBearingElement
    from ._2016 import LoadedCylindricalRollerBearingResults
    from ._2017 import LoadedCylindricalRollerBearingRow
    from ._2018 import LoadedDeepGrooveBallBearingElement
    from ._2019 import LoadedDeepGrooveBallBearingResults
    from ._2020 import LoadedDeepGrooveBallBearingRow
    from ._2021 import LoadedElement
    from ._2022 import LoadedFourPointContactBallBearingElement
    from ._2023 import LoadedFourPointContactBallBearingRaceResults
    from ._2024 import LoadedFourPointContactBallBearingResults
    from ._2025 import LoadedFourPointContactBallBearingRow
    from ._2026 import LoadedMultiPointContactBallBearingElement
    from ._2027 import LoadedNeedleRollerBearingElement
    from ._2028 import LoadedNeedleRollerBearingResults
    from ._2029 import LoadedNeedleRollerBearingRow
    from ._2030 import LoadedNonBarrelRollerBearingDutyCycle
    from ._2031 import LoadedNonBarrelRollerBearingResults
    from ._2032 import LoadedNonBarrelRollerBearingRow
    from ._2033 import LoadedNonBarrelRollerBearingStripLoadResults
    from ._2034 import LoadedNonBarrelRollerElement
    from ._2035 import LoadedRollerBearingElement
    from ._2036 import LoadedRollerBearingResults
    from ._2037 import LoadedRollerBearingRow
    from ._2038 import LoadedRollerStripLoadResults
    from ._2039 import LoadedRollingBearingRaceResults
    from ._2040 import LoadedRollingBearingResults
    from ._2041 import LoadedRollingBearingRow
    from ._2042 import LoadedSelfAligningBallBearingElement
    from ._2043 import LoadedSelfAligningBallBearingResults
    from ._2044 import LoadedSelfAligningBallBearingRow
    from ._2045 import LoadedSphericalRadialRollerBearingElement
    from ._2046 import LoadedSphericalRollerBearingElement
    from ._2047 import LoadedSphericalRollerRadialBearingResults
    from ._2048 import LoadedSphericalRollerRadialBearingRow
    from ._2049 import LoadedSphericalRollerRadialBearingStripLoadResults
    from ._2050 import LoadedSphericalRollerThrustBearingResults
    from ._2051 import LoadedSphericalRollerThrustBearingRow
    from ._2052 import LoadedSphericalThrustRollerBearingElement
    from ._2053 import LoadedTaperRollerBearingDutyCycle
    from ._2054 import LoadedTaperRollerBearingElement
    from ._2055 import LoadedTaperRollerBearingResults
    from ._2056 import LoadedTaperRollerBearingRow
    from ._2057 import LoadedThreePointContactBallBearingElement
    from ._2058 import LoadedThreePointContactBallBearingResults
    from ._2059 import LoadedThreePointContactBallBearingRow
    from ._2060 import LoadedThrustBallBearingElement
    from ._2061 import LoadedThrustBallBearingResults
    from ._2062 import LoadedThrustBallBearingRow
    from ._2063 import LoadedToroidalRollerBearingElement
    from ._2064 import LoadedToroidalRollerBearingResults
    from ._2065 import LoadedToroidalRollerBearingRow
    from ._2066 import LoadedToroidalRollerBearingStripLoadResults
    from ._2067 import MaximumStaticContactStress
    from ._2068 import MaximumStaticContactStressDutyCycle
    from ._2069 import MaximumStaticContactStressResultsAbstract
    from ._2070 import MaxStripLoadStressObject
    from ._2071 import PermissibleContinuousAxialLoadResults
    from ._2072 import PowerRatingF1EstimationMethod
    from ._2073 import PreloadFactorLookupTable
    from ._2074 import ResultsAtRollerOffset
    from ._2075 import RingForceAndDisplacement
    from ._2076 import RollerAnalysisMethod
    from ._2077 import RollingBearingFrictionCoefficients
    from ._2078 import RollingBearingSpeedResults
    from ._2079 import SMTRibStressResults
    from ._2080 import StressAtPosition
    from ._2081 import ThreePointContactInternalClearance
    from ._2082 import TrackTruncationSafetyFactorResults
else:
    import_structure = {
        "_1973": ["BallBearingAnalysisMethod"],
        "_1974": ["BallBearingContactCalculation"],
        "_1975": ["BallBearingRaceContactGeometry"],
        "_1976": ["DIN7322010Results"],
        "_1977": ["ForceAtLaminaGroupReportable"],
        "_1978": ["ForceAtLaminaReportable"],
        "_1979": ["FrictionModelForGyroscopicMoment"],
        "_1980": ["InternalClearance"],
        "_1981": ["ISO14179Settings"],
        "_1982": ["ISO14179SettingsDatabase"],
        "_1983": ["ISO14179SettingsPerBearingType"],
        "_1984": ["ISO153122018Results"],
        "_1985": ["ISOTR1417912001Results"],
        "_1986": ["ISOTR141792001Results"],
        "_1987": ["ISOTR1417922001Results"],
        "_1988": ["LoadedAbstractSphericalRollerBearingStripLoadResults"],
        "_1989": ["LoadedAngularContactBallBearingElement"],
        "_1990": ["LoadedAngularContactBallBearingResults"],
        "_1991": ["LoadedAngularContactBallBearingRow"],
        "_1992": ["LoadedAngularContactThrustBallBearingElement"],
        "_1993": ["LoadedAngularContactThrustBallBearingResults"],
        "_1994": ["LoadedAngularContactThrustBallBearingRow"],
        "_1995": ["LoadedAsymmetricSphericalRollerBearingElement"],
        "_1996": ["LoadedAsymmetricSphericalRollerBearingResults"],
        "_1997": ["LoadedAsymmetricSphericalRollerBearingRow"],
        "_1998": ["LoadedAsymmetricSphericalRollerBearingStripLoadResults"],
        "_1999": ["LoadedAxialThrustCylindricalRollerBearingDutyCycle"],
        "_2000": ["LoadedAxialThrustCylindricalRollerBearingElement"],
        "_2001": ["LoadedAxialThrustCylindricalRollerBearingResults"],
        "_2002": ["LoadedAxialThrustCylindricalRollerBearingRow"],
        "_2003": ["LoadedAxialThrustNeedleRollerBearingElement"],
        "_2004": ["LoadedAxialThrustNeedleRollerBearingResults"],
        "_2005": ["LoadedAxialThrustNeedleRollerBearingRow"],
        "_2006": ["LoadedBallBearingDutyCycle"],
        "_2007": ["LoadedBallBearingElement"],
        "_2008": ["LoadedBallBearingRaceResults"],
        "_2009": ["LoadedBallBearingResults"],
        "_2010": ["LoadedBallBearingRow"],
        "_2011": ["LoadedCrossedRollerBearingElement"],
        "_2012": ["LoadedCrossedRollerBearingResults"],
        "_2013": ["LoadedCrossedRollerBearingRow"],
        "_2014": ["LoadedCylindricalRollerBearingDutyCycle"],
        "_2015": ["LoadedCylindricalRollerBearingElement"],
        "_2016": ["LoadedCylindricalRollerBearingResults"],
        "_2017": ["LoadedCylindricalRollerBearingRow"],
        "_2018": ["LoadedDeepGrooveBallBearingElement"],
        "_2019": ["LoadedDeepGrooveBallBearingResults"],
        "_2020": ["LoadedDeepGrooveBallBearingRow"],
        "_2021": ["LoadedElement"],
        "_2022": ["LoadedFourPointContactBallBearingElement"],
        "_2023": ["LoadedFourPointContactBallBearingRaceResults"],
        "_2024": ["LoadedFourPointContactBallBearingResults"],
        "_2025": ["LoadedFourPointContactBallBearingRow"],
        "_2026": ["LoadedMultiPointContactBallBearingElement"],
        "_2027": ["LoadedNeedleRollerBearingElement"],
        "_2028": ["LoadedNeedleRollerBearingResults"],
        "_2029": ["LoadedNeedleRollerBearingRow"],
        "_2030": ["LoadedNonBarrelRollerBearingDutyCycle"],
        "_2031": ["LoadedNonBarrelRollerBearingResults"],
        "_2032": ["LoadedNonBarrelRollerBearingRow"],
        "_2033": ["LoadedNonBarrelRollerBearingStripLoadResults"],
        "_2034": ["LoadedNonBarrelRollerElement"],
        "_2035": ["LoadedRollerBearingElement"],
        "_2036": ["LoadedRollerBearingResults"],
        "_2037": ["LoadedRollerBearingRow"],
        "_2038": ["LoadedRollerStripLoadResults"],
        "_2039": ["LoadedRollingBearingRaceResults"],
        "_2040": ["LoadedRollingBearingResults"],
        "_2041": ["LoadedRollingBearingRow"],
        "_2042": ["LoadedSelfAligningBallBearingElement"],
        "_2043": ["LoadedSelfAligningBallBearingResults"],
        "_2044": ["LoadedSelfAligningBallBearingRow"],
        "_2045": ["LoadedSphericalRadialRollerBearingElement"],
        "_2046": ["LoadedSphericalRollerBearingElement"],
        "_2047": ["LoadedSphericalRollerRadialBearingResults"],
        "_2048": ["LoadedSphericalRollerRadialBearingRow"],
        "_2049": ["LoadedSphericalRollerRadialBearingStripLoadResults"],
        "_2050": ["LoadedSphericalRollerThrustBearingResults"],
        "_2051": ["LoadedSphericalRollerThrustBearingRow"],
        "_2052": ["LoadedSphericalThrustRollerBearingElement"],
        "_2053": ["LoadedTaperRollerBearingDutyCycle"],
        "_2054": ["LoadedTaperRollerBearingElement"],
        "_2055": ["LoadedTaperRollerBearingResults"],
        "_2056": ["LoadedTaperRollerBearingRow"],
        "_2057": ["LoadedThreePointContactBallBearingElement"],
        "_2058": ["LoadedThreePointContactBallBearingResults"],
        "_2059": ["LoadedThreePointContactBallBearingRow"],
        "_2060": ["LoadedThrustBallBearingElement"],
        "_2061": ["LoadedThrustBallBearingResults"],
        "_2062": ["LoadedThrustBallBearingRow"],
        "_2063": ["LoadedToroidalRollerBearingElement"],
        "_2064": ["LoadedToroidalRollerBearingResults"],
        "_2065": ["LoadedToroidalRollerBearingRow"],
        "_2066": ["LoadedToroidalRollerBearingStripLoadResults"],
        "_2067": ["MaximumStaticContactStress"],
        "_2068": ["MaximumStaticContactStressDutyCycle"],
        "_2069": ["MaximumStaticContactStressResultsAbstract"],
        "_2070": ["MaxStripLoadStressObject"],
        "_2071": ["PermissibleContinuousAxialLoadResults"],
        "_2072": ["PowerRatingF1EstimationMethod"],
        "_2073": ["PreloadFactorLookupTable"],
        "_2074": ["ResultsAtRollerOffset"],
        "_2075": ["RingForceAndDisplacement"],
        "_2076": ["RollerAnalysisMethod"],
        "_2077": ["RollingBearingFrictionCoefficients"],
        "_2078": ["RollingBearingSpeedResults"],
        "_2079": ["SMTRibStressResults"],
        "_2080": ["StressAtPosition"],
        "_2081": ["ThreePointContactInternalClearance"],
        "_2082": ["TrackTruncationSafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallBearingAnalysisMethod",
    "BallBearingContactCalculation",
    "BallBearingRaceContactGeometry",
    "DIN7322010Results",
    "ForceAtLaminaGroupReportable",
    "ForceAtLaminaReportable",
    "FrictionModelForGyroscopicMoment",
    "InternalClearance",
    "ISO14179Settings",
    "ISO14179SettingsDatabase",
    "ISO14179SettingsPerBearingType",
    "ISO153122018Results",
    "ISOTR1417912001Results",
    "ISOTR141792001Results",
    "ISOTR1417922001Results",
    "LoadedAbstractSphericalRollerBearingStripLoadResults",
    "LoadedAngularContactBallBearingElement",
    "LoadedAngularContactBallBearingResults",
    "LoadedAngularContactBallBearingRow",
    "LoadedAngularContactThrustBallBearingElement",
    "LoadedAngularContactThrustBallBearingResults",
    "LoadedAngularContactThrustBallBearingRow",
    "LoadedAsymmetricSphericalRollerBearingElement",
    "LoadedAsymmetricSphericalRollerBearingResults",
    "LoadedAsymmetricSphericalRollerBearingRow",
    "LoadedAsymmetricSphericalRollerBearingStripLoadResults",
    "LoadedAxialThrustCylindricalRollerBearingDutyCycle",
    "LoadedAxialThrustCylindricalRollerBearingElement",
    "LoadedAxialThrustCylindricalRollerBearingResults",
    "LoadedAxialThrustCylindricalRollerBearingRow",
    "LoadedAxialThrustNeedleRollerBearingElement",
    "LoadedAxialThrustNeedleRollerBearingResults",
    "LoadedAxialThrustNeedleRollerBearingRow",
    "LoadedBallBearingDutyCycle",
    "LoadedBallBearingElement",
    "LoadedBallBearingRaceResults",
    "LoadedBallBearingResults",
    "LoadedBallBearingRow",
    "LoadedCrossedRollerBearingElement",
    "LoadedCrossedRollerBearingResults",
    "LoadedCrossedRollerBearingRow",
    "LoadedCylindricalRollerBearingDutyCycle",
    "LoadedCylindricalRollerBearingElement",
    "LoadedCylindricalRollerBearingResults",
    "LoadedCylindricalRollerBearingRow",
    "LoadedDeepGrooveBallBearingElement",
    "LoadedDeepGrooveBallBearingResults",
    "LoadedDeepGrooveBallBearingRow",
    "LoadedElement",
    "LoadedFourPointContactBallBearingElement",
    "LoadedFourPointContactBallBearingRaceResults",
    "LoadedFourPointContactBallBearingResults",
    "LoadedFourPointContactBallBearingRow",
    "LoadedMultiPointContactBallBearingElement",
    "LoadedNeedleRollerBearingElement",
    "LoadedNeedleRollerBearingResults",
    "LoadedNeedleRollerBearingRow",
    "LoadedNonBarrelRollerBearingDutyCycle",
    "LoadedNonBarrelRollerBearingResults",
    "LoadedNonBarrelRollerBearingRow",
    "LoadedNonBarrelRollerBearingStripLoadResults",
    "LoadedNonBarrelRollerElement",
    "LoadedRollerBearingElement",
    "LoadedRollerBearingResults",
    "LoadedRollerBearingRow",
    "LoadedRollerStripLoadResults",
    "LoadedRollingBearingRaceResults",
    "LoadedRollingBearingResults",
    "LoadedRollingBearingRow",
    "LoadedSelfAligningBallBearingElement",
    "LoadedSelfAligningBallBearingResults",
    "LoadedSelfAligningBallBearingRow",
    "LoadedSphericalRadialRollerBearingElement",
    "LoadedSphericalRollerBearingElement",
    "LoadedSphericalRollerRadialBearingResults",
    "LoadedSphericalRollerRadialBearingRow",
    "LoadedSphericalRollerRadialBearingStripLoadResults",
    "LoadedSphericalRollerThrustBearingResults",
    "LoadedSphericalRollerThrustBearingRow",
    "LoadedSphericalThrustRollerBearingElement",
    "LoadedTaperRollerBearingDutyCycle",
    "LoadedTaperRollerBearingElement",
    "LoadedTaperRollerBearingResults",
    "LoadedTaperRollerBearingRow",
    "LoadedThreePointContactBallBearingElement",
    "LoadedThreePointContactBallBearingResults",
    "LoadedThreePointContactBallBearingRow",
    "LoadedThrustBallBearingElement",
    "LoadedThrustBallBearingResults",
    "LoadedThrustBallBearingRow",
    "LoadedToroidalRollerBearingElement",
    "LoadedToroidalRollerBearingResults",
    "LoadedToroidalRollerBearingRow",
    "LoadedToroidalRollerBearingStripLoadResults",
    "MaximumStaticContactStress",
    "MaximumStaticContactStressDutyCycle",
    "MaximumStaticContactStressResultsAbstract",
    "MaxStripLoadStressObject",
    "PermissibleContinuousAxialLoadResults",
    "PowerRatingF1EstimationMethod",
    "PreloadFactorLookupTable",
    "ResultsAtRollerOffset",
    "RingForceAndDisplacement",
    "RollerAnalysisMethod",
    "RollingBearingFrictionCoefficients",
    "RollingBearingSpeedResults",
    "SMTRibStressResults",
    "StressAtPosition",
    "ThreePointContactInternalClearance",
    "TrackTruncationSafetyFactorResults",
)
