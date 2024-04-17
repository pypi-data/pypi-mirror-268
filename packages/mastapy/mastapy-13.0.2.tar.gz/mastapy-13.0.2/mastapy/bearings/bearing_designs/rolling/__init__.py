"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2142 import AngularContactBallBearing
    from ._2143 import AngularContactThrustBallBearing
    from ._2144 import AsymmetricSphericalRollerBearing
    from ._2145 import AxialThrustCylindricalRollerBearing
    from ._2146 import AxialThrustNeedleRollerBearing
    from ._2147 import BallBearing
    from ._2148 import BallBearingShoulderDefinition
    from ._2149 import BarrelRollerBearing
    from ._2150 import BearingProtection
    from ._2151 import BearingProtectionDetailsModifier
    from ._2152 import BearingProtectionLevel
    from ._2153 import BearingTypeExtraInformation
    from ._2154 import CageBridgeShape
    from ._2155 import CrossedRollerBearing
    from ._2156 import CylindricalRollerBearing
    from ._2157 import DeepGrooveBallBearing
    from ._2158 import DiameterSeries
    from ._2159 import FatigueLoadLimitCalculationMethodEnum
    from ._2160 import FourPointContactAngleDefinition
    from ._2161 import FourPointContactBallBearing
    from ._2162 import GeometricConstants
    from ._2163 import GeometricConstantsForRollingFrictionalMoments
    from ._2164 import GeometricConstantsForSlidingFrictionalMoments
    from ._2165 import HeightSeries
    from ._2166 import MultiPointContactBallBearing
    from ._2167 import NeedleRollerBearing
    from ._2168 import NonBarrelRollerBearing
    from ._2169 import RollerBearing
    from ._2170 import RollerEndShape
    from ._2171 import RollerRibDetail
    from ._2172 import RollingBearing
    from ._2173 import SelfAligningBallBearing
    from ._2174 import SKFSealFrictionalMomentConstants
    from ._2175 import SleeveType
    from ._2176 import SphericalRollerBearing
    from ._2177 import SphericalRollerThrustBearing
    from ._2178 import TaperRollerBearing
    from ._2179 import ThreePointContactBallBearing
    from ._2180 import ThrustBallBearing
    from ._2181 import ToroidalRollerBearing
    from ._2182 import WidthSeries
else:
    import_structure = {
        "_2142": ["AngularContactBallBearing"],
        "_2143": ["AngularContactThrustBallBearing"],
        "_2144": ["AsymmetricSphericalRollerBearing"],
        "_2145": ["AxialThrustCylindricalRollerBearing"],
        "_2146": ["AxialThrustNeedleRollerBearing"],
        "_2147": ["BallBearing"],
        "_2148": ["BallBearingShoulderDefinition"],
        "_2149": ["BarrelRollerBearing"],
        "_2150": ["BearingProtection"],
        "_2151": ["BearingProtectionDetailsModifier"],
        "_2152": ["BearingProtectionLevel"],
        "_2153": ["BearingTypeExtraInformation"],
        "_2154": ["CageBridgeShape"],
        "_2155": ["CrossedRollerBearing"],
        "_2156": ["CylindricalRollerBearing"],
        "_2157": ["DeepGrooveBallBearing"],
        "_2158": ["DiameterSeries"],
        "_2159": ["FatigueLoadLimitCalculationMethodEnum"],
        "_2160": ["FourPointContactAngleDefinition"],
        "_2161": ["FourPointContactBallBearing"],
        "_2162": ["GeometricConstants"],
        "_2163": ["GeometricConstantsForRollingFrictionalMoments"],
        "_2164": ["GeometricConstantsForSlidingFrictionalMoments"],
        "_2165": ["HeightSeries"],
        "_2166": ["MultiPointContactBallBearing"],
        "_2167": ["NeedleRollerBearing"],
        "_2168": ["NonBarrelRollerBearing"],
        "_2169": ["RollerBearing"],
        "_2170": ["RollerEndShape"],
        "_2171": ["RollerRibDetail"],
        "_2172": ["RollingBearing"],
        "_2173": ["SelfAligningBallBearing"],
        "_2174": ["SKFSealFrictionalMomentConstants"],
        "_2175": ["SleeveType"],
        "_2176": ["SphericalRollerBearing"],
        "_2177": ["SphericalRollerThrustBearing"],
        "_2178": ["TaperRollerBearing"],
        "_2179": ["ThreePointContactBallBearing"],
        "_2180": ["ThrustBallBearing"],
        "_2181": ["ToroidalRollerBearing"],
        "_2182": ["WidthSeries"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)
