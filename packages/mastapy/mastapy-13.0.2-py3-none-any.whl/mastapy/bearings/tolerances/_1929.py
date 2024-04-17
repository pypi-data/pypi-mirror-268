"""SupportTolerance"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.bearings.tolerances import _1917, _1930, _1916
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPPORT_TOLERANCE = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "SupportTolerance"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1914, _1920, _1908


__docformat__ = "restructuredtext en"
__all__ = ("SupportTolerance",)


Self = TypeVar("Self", bound="SupportTolerance")


class SupportTolerance(_1916.InterferenceTolerance):
    """SupportTolerance

    This is a mastapy class.
    """

    TYPE = _SUPPORT_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SupportTolerance")

    class _Cast_SupportTolerance:
        """Special nested class for casting SupportTolerance to subclasses."""

        def __init__(
            self: "SupportTolerance._Cast_SupportTolerance", parent: "SupportTolerance"
        ):
            self._parent = parent

        @property
        def interference_tolerance(
            self: "SupportTolerance._Cast_SupportTolerance",
        ) -> "_1916.InterferenceTolerance":
            return self._parent._cast(_1916.InterferenceTolerance)

        @property
        def bearing_connection_component(
            self: "SupportTolerance._Cast_SupportTolerance",
        ) -> "_1908.BearingConnectionComponent":
            from mastapy.bearings.tolerances import _1908

            return self._parent._cast(_1908.BearingConnectionComponent)

        @property
        def inner_support_tolerance(
            self: "SupportTolerance._Cast_SupportTolerance",
        ) -> "_1914.InnerSupportTolerance":
            from mastapy.bearings.tolerances import _1914

            return self._parent._cast(_1914.InnerSupportTolerance)

        @property
        def outer_support_tolerance(
            self: "SupportTolerance._Cast_SupportTolerance",
        ) -> "_1920.OuterSupportTolerance":
            from mastapy.bearings.tolerances import _1920

            return self._parent._cast(_1920.OuterSupportTolerance)

        @property
        def support_tolerance(
            self: "SupportTolerance._Cast_SupportTolerance",
        ) -> "SupportTolerance":
            return self._parent

        def __getattr__(self: "SupportTolerance._Cast_SupportTolerance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SupportTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tolerance_band_designation(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ITDesignation":
        """EnumWithSelectedValue[mastapy.bearings.tolerances.ITDesignation]"""
        temp = self.wrapped.ToleranceBandDesignation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @tolerance_band_designation.setter
    @enforce_parameter_types
    def tolerance_band_designation(self: Self, value: "_1917.ITDesignation"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToleranceBandDesignation = value

    @property
    def tolerance_deviation_class(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation":
        """EnumWithSelectedValue[mastapy.bearings.tolerances.SupportToleranceLocationDesignation]"""
        temp = self.wrapped.ToleranceDeviationClass

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @tolerance_deviation_class.setter
    @enforce_parameter_types
    def tolerance_deviation_class(
        self: Self, value: "_1930.SupportToleranceLocationDesignation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_SupportToleranceLocationDesignation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToleranceDeviationClass = value

    @property
    def cast_to(self: Self) -> "SupportTolerance._Cast_SupportTolerance":
        return self._Cast_SupportTolerance(self)
