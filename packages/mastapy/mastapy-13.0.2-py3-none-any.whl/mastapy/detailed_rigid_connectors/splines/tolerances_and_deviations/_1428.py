"""FitAndTolerance"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.detailed_rigid_connectors.splines import _1419, _1425
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FIT_AND_TOLERANCE = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.TolerancesAndDeviations",
    "FitAndTolerance",
)


__docformat__ = "restructuredtext en"
__all__ = ("FitAndTolerance",)


Self = TypeVar("Self", bound="FitAndTolerance")


class FitAndTolerance(_0.APIBase):
    """FitAndTolerance

    This is a mastapy class.
    """

    TYPE = _FIT_AND_TOLERANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FitAndTolerance")

    class _Cast_FitAndTolerance:
        """Special nested class for casting FitAndTolerance to subclasses."""

        def __init__(
            self: "FitAndTolerance._Cast_FitAndTolerance", parent: "FitAndTolerance"
        ):
            self._parent = parent

        @property
        def fit_and_tolerance(
            self: "FitAndTolerance._Cast_FitAndTolerance",
        ) -> "FitAndTolerance":
            return self._parent

        def __getattr__(self: "FitAndTolerance._Cast_FitAndTolerance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FitAndTolerance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fit_class(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_SplineFitClassType":
        """EnumWithSelectedValue[mastapy.detailed_rigid_connectors.splines.SplineFitClassType]"""
        temp = self.wrapped.FitClass

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_SplineFitClassType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @fit_class.setter
    @enforce_parameter_types
    def fit_class(self: Self, value: "_1419.SplineFitClassType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_SplineFitClassType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FitClass = value

    @property
    def tolerance_class(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_SplineToleranceClassTypes":
        """EnumWithSelectedValue[mastapy.detailed_rigid_connectors.splines.SplineToleranceClassTypes]"""
        temp = self.wrapped.ToleranceClass

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_SplineToleranceClassTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @tolerance_class.setter
    @enforce_parameter_types
    def tolerance_class(self: Self, value: "_1425.SplineToleranceClassTypes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_SplineToleranceClassTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToleranceClass = value

    @property
    def cast_to(self: Self) -> "FitAndTolerance._Cast_FitAndTolerance":
        return self._Cast_FitAndTolerance(self)
