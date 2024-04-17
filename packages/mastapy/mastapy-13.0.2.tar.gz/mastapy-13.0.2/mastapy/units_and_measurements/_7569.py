"""MeasurementTypeExtensions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_TYPE_EXTENSIONS = python_net_import(
    "SMT.MastaAPIUtility.UnitsAndMeasurements", "MeasurementTypeExtensions"
)

if TYPE_CHECKING:
    from mastapy.units_and_measurements import _7568


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementTypeExtensions",)


Self = TypeVar("Self", bound="MeasurementTypeExtensions")


class MeasurementTypeExtensions:
    """MeasurementTypeExtensions

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_TYPE_EXTENSIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementTypeExtensions")

    class _Cast_MeasurementTypeExtensions:
        """Special nested class for casting MeasurementTypeExtensions to subclasses."""

        def __init__(
            self: "MeasurementTypeExtensions._Cast_MeasurementTypeExtensions",
            parent: "MeasurementTypeExtensions",
        ):
            self._parent = parent

        @property
        def measurement_type_extensions(
            self: "MeasurementTypeExtensions._Cast_MeasurementTypeExtensions",
        ) -> "MeasurementTypeExtensions":
            return self._parent

        def __getattr__(
            self: "MeasurementTypeExtensions._Cast_MeasurementTypeExtensions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeasurementTypeExtensions.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    @enforce_parameter_types
    def is_unmeasurable(measurement_type: "_7568.MeasurementType") -> "bool":
        """bool

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        measurement_type = conversion.mp_to_pn_enum(
            measurement_type, "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType"
        )
        method_result = MeasurementTypeExtensions.TYPE.IsUnmeasurable(measurement_type)
        return method_result

    @staticmethod
    @enforce_parameter_types
    def is_valid(measurement_type: "_7568.MeasurementType") -> "bool":
        """bool

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        measurement_type = conversion.mp_to_pn_enum(
            measurement_type, "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType"
        )
        method_result = MeasurementTypeExtensions.TYPE.IsValid(measurement_type)
        return method_result

    @staticmethod
    @enforce_parameter_types
    def is_angle(measurement_type: "_7568.MeasurementType") -> "bool":
        """bool

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        measurement_type = conversion.mp_to_pn_enum(
            measurement_type, "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType"
        )
        method_result = MeasurementTypeExtensions.TYPE.IsAngle(measurement_type)
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "MeasurementTypeExtensions._Cast_MeasurementTypeExtensions":
        return self._Cast_MeasurementTypeExtensions(self)
