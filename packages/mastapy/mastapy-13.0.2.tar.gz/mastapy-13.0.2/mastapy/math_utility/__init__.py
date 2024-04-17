"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1496 import Range
    from ._1497 import AcousticWeighting
    from ._1498 import AlignmentAxis
    from ._1499 import Axis
    from ._1500 import CirclesOnAxis
    from ._1501 import ComplexMatrix
    from ._1502 import ComplexPartDisplayOption
    from ._1503 import ComplexVector
    from ._1504 import ComplexVector3D
    from ._1505 import ComplexVector6D
    from ._1506 import CoordinateSystem3D
    from ._1507 import CoordinateSystemEditor
    from ._1508 import CoordinateSystemForRotation
    from ._1509 import CoordinateSystemForRotationOrigin
    from ._1510 import DataPrecision
    from ._1511 import DegreeOfFreedom
    from ._1512 import DynamicsResponseScalarResult
    from ._1513 import DynamicsResponseScaling
    from ._1514 import Eigenmode
    from ._1515 import Eigenmodes
    from ._1516 import EulerParameters
    from ._1517 import ExtrapolationOptions
    from ._1518 import FacetedBody
    from ._1519 import FacetedSurface
    from ._1520 import FourierSeries
    from ._1521 import GenericMatrix
    from ._1522 import GriddedSurface
    from ._1523 import HarmonicValue
    from ._1524 import InertiaTensor
    from ._1525 import MassProperties
    from ._1526 import MaxMinMean
    from ._1527 import ComplexMagnitudeMethod
    from ._1528 import MultipleFourierSeriesInterpolator
    from ._1529 import Named2DLocation
    from ._1530 import PIDControlUpdateMethod
    from ._1531 import Quaternion
    from ._1532 import RealMatrix
    from ._1533 import RealVector
    from ._1534 import ResultOptionsFor3DVector
    from ._1535 import RotationAxis
    from ._1536 import RoundedOrder
    from ._1537 import SinCurve
    from ._1538 import SquareMatrix
    from ._1539 import StressPoint
    from ._1540 import TransformMatrix3D
    from ._1541 import TranslationRotation
    from ._1542 import Vector2DListAccessor
    from ._1543 import Vector6D
else:
    import_structure = {
        "_1496": ["Range"],
        "_1497": ["AcousticWeighting"],
        "_1498": ["AlignmentAxis"],
        "_1499": ["Axis"],
        "_1500": ["CirclesOnAxis"],
        "_1501": ["ComplexMatrix"],
        "_1502": ["ComplexPartDisplayOption"],
        "_1503": ["ComplexVector"],
        "_1504": ["ComplexVector3D"],
        "_1505": ["ComplexVector6D"],
        "_1506": ["CoordinateSystem3D"],
        "_1507": ["CoordinateSystemEditor"],
        "_1508": ["CoordinateSystemForRotation"],
        "_1509": ["CoordinateSystemForRotationOrigin"],
        "_1510": ["DataPrecision"],
        "_1511": ["DegreeOfFreedom"],
        "_1512": ["DynamicsResponseScalarResult"],
        "_1513": ["DynamicsResponseScaling"],
        "_1514": ["Eigenmode"],
        "_1515": ["Eigenmodes"],
        "_1516": ["EulerParameters"],
        "_1517": ["ExtrapolationOptions"],
        "_1518": ["FacetedBody"],
        "_1519": ["FacetedSurface"],
        "_1520": ["FourierSeries"],
        "_1521": ["GenericMatrix"],
        "_1522": ["GriddedSurface"],
        "_1523": ["HarmonicValue"],
        "_1524": ["InertiaTensor"],
        "_1525": ["MassProperties"],
        "_1526": ["MaxMinMean"],
        "_1527": ["ComplexMagnitudeMethod"],
        "_1528": ["MultipleFourierSeriesInterpolator"],
        "_1529": ["Named2DLocation"],
        "_1530": ["PIDControlUpdateMethod"],
        "_1531": ["Quaternion"],
        "_1532": ["RealMatrix"],
        "_1533": ["RealVector"],
        "_1534": ["ResultOptionsFor3DVector"],
        "_1535": ["RotationAxis"],
        "_1536": ["RoundedOrder"],
        "_1537": ["SinCurve"],
        "_1538": ["SquareMatrix"],
        "_1539": ["StressPoint"],
        "_1540": ["TransformMatrix3D"],
        "_1541": ["TranslationRotation"],
        "_1542": ["Vector2DListAccessor"],
        "_1543": ["Vector6D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)
