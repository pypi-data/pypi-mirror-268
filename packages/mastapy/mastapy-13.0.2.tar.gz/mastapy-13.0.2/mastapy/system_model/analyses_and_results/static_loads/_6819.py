"""AdditionalAccelerationOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADDITIONAL_ACCELERATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AdditionalAccelerationOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("AdditionalAccelerationOptions",)


Self = TypeVar("Self", bound="AdditionalAccelerationOptions")


class AdditionalAccelerationOptions(
    _1593.IndependentReportablePropertiesBase["AdditionalAccelerationOptions"]
):
    """AdditionalAccelerationOptions

    This is a mastapy class.
    """

    TYPE = _ADDITIONAL_ACCELERATION_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdditionalAccelerationOptions")

    class _Cast_AdditionalAccelerationOptions:
        """Special nested class for casting AdditionalAccelerationOptions to subclasses."""

        def __init__(
            self: "AdditionalAccelerationOptions._Cast_AdditionalAccelerationOptions",
            parent: "AdditionalAccelerationOptions",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "AdditionalAccelerationOptions._Cast_AdditionalAccelerationOptions",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def additional_acceleration_options(
            self: "AdditionalAccelerationOptions._Cast_AdditionalAccelerationOptions",
        ) -> "AdditionalAccelerationOptions":
            return self._parent

        def __getattr__(
            self: "AdditionalAccelerationOptions._Cast_AdditionalAccelerationOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AdditionalAccelerationOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_additional_acceleration(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAdditionalAcceleration

        if temp is None:
            return False

        return temp

    @include_additional_acceleration.setter
    @enforce_parameter_types
    def include_additional_acceleration(self: Self, value: "bool"):
        self.wrapped.IncludeAdditionalAcceleration = (
            bool(value) if value is not None else False
        )

    @property
    def magnitude(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Magnitude

        if temp is None:
            return 0.0

        return temp

    @magnitude.setter
    @enforce_parameter_types
    def magnitude(self: Self, value: "float"):
        self.wrapped.Magnitude = float(value) if value is not None else 0.0

    @property
    def specify_direction_and_magnitude(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyDirectionAndMagnitude

        if temp is None:
            return False

        return temp

    @specify_direction_and_magnitude.setter
    @enforce_parameter_types
    def specify_direction_and_magnitude(self: Self, value: "bool"):
        self.wrapped.SpecifyDirectionAndMagnitude = (
            bool(value) if value is not None else False
        )

    @property
    def acceleration_vector(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.AccelerationVector

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @acceleration_vector.setter
    @enforce_parameter_types
    def acceleration_vector(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.AccelerationVector = value

    @property
    def orientation(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.Orientation = value

    @property
    def cast_to(
        self: Self,
    ) -> "AdditionalAccelerationOptions._Cast_AdditionalAccelerationOptions":
        return self._Cast_AdditionalAccelerationOptions(self)
