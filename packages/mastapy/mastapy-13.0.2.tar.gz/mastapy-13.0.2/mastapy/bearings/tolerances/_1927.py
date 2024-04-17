"""SupportDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings.tolerances import _1915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPPORT_DETAIL = python_net_import("SMT.MastaAPI.Bearings.Tolerances", "SupportDetail")

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1928, _1923, _1908


__docformat__ = "restructuredtext en"
__all__ = ("SupportDetail",)


Self = TypeVar("Self", bound="SupportDetail")


class SupportDetail(_1915.InterferenceDetail):
    """SupportDetail

    This is a mastapy class.
    """

    TYPE = _SUPPORT_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SupportDetail")

    class _Cast_SupportDetail:
        """Special nested class for casting SupportDetail to subclasses."""

        def __init__(
            self: "SupportDetail._Cast_SupportDetail", parent: "SupportDetail"
        ):
            self._parent = parent

        @property
        def interference_detail(
            self: "SupportDetail._Cast_SupportDetail",
        ) -> "_1915.InterferenceDetail":
            return self._parent._cast(_1915.InterferenceDetail)

        @property
        def bearing_connection_component(
            self: "SupportDetail._Cast_SupportDetail",
        ) -> "_1908.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1908

            return self._parent._cast(_1908.BearingConnectionComponent)

        @property
        def support_detail(
            self: "SupportDetail._Cast_SupportDetail",
        ) -> "SupportDetail":
            return self._parent

        def __getattr__(self: "SupportDetail._Cast_SupportDetail", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SupportDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_radial_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngleOfRadialError

        if temp is None:
            return 0.0

        return temp

    @angle_of_radial_error.setter
    @enforce_parameter_types
    def angle_of_radial_error(self: Self, value: "float"):
        self.wrapped.AngleOfRadialError = float(value) if value is not None else 0.0

    @property
    def material_source(self: Self) -> "_1928.SupportMaterialSource":
        """mastapy.bearings.tolerances.SupportMaterialSource

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.SupportMaterialSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.tolerances._1928", "SupportMaterialSource"
        )(value)

    @property
    def radial_error_magnitude(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialErrorMagnitude

        if temp is None:
            return 0.0

        return temp

    @radial_error_magnitude.setter
    @enforce_parameter_types
    def radial_error_magnitude(self: Self, value: "float"):
        self.wrapped.RadialErrorMagnitude = float(value) if value is not None else 0.0

    @property
    def radial_specification_method(self: Self) -> "_1923.RadialSpecificationMethod":
        """mastapy.bearings.tolerances.RadialSpecificationMethod"""
        temp = self.wrapped.RadialSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.RadialSpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.tolerances._1923", "RadialSpecificationMethod"
        )(value)

    @radial_specification_method.setter
    @enforce_parameter_types
    def radial_specification_method(
        self: Self, value: "_1923.RadialSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.Tolerances.RadialSpecificationMethod"
        )
        self.wrapped.RadialSpecificationMethod = value

    @property
    def theta_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThetaX

        if temp is None:
            return 0.0

        return temp

    @theta_x.setter
    @enforce_parameter_types
    def theta_x(self: Self, value: "float"):
        self.wrapped.ThetaX = float(value) if value is not None else 0.0

    @property
    def theta_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThetaY

        if temp is None:
            return 0.0

        return temp

    @theta_y.setter
    @enforce_parameter_types
    def theta_y(self: Self, value: "float"):
        self.wrapped.ThetaY = float(value) if value is not None else 0.0

    @property
    def x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.X

        if temp is None:
            return 0.0

        return temp

    @x.setter
    @enforce_parameter_types
    def x(self: Self, value: "float"):
        self.wrapped.X = float(value) if value is not None else 0.0

    @property
    def y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Y

        if temp is None:
            return 0.0

        return temp

    @y.setter
    @enforce_parameter_types
    def y(self: Self, value: "float"):
        self.wrapped.Y = float(value) if value is not None else 0.0

    @property
    def z(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Z

        if temp is None:
            return 0.0

        return temp

    @z.setter
    @enforce_parameter_types
    def z(self: Self, value: "float"):
        self.wrapped.Z = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "SupportDetail._Cast_SupportDetail":
        return self._Cast_SupportDetail(self)
