"""DiagonalNonLinearStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIAGONAL_NON_LINEAR_STIFFNESS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "DiagonalNonLinearStiffness"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542


__docformat__ = "restructuredtext en"
__all__ = ("DiagonalNonLinearStiffness",)


Self = TypeVar("Self", bound="DiagonalNonLinearStiffness")


class DiagonalNonLinearStiffness(_0.APIBase):
    """DiagonalNonLinearStiffness

    This is a mastapy class.
    """

    TYPE = _DIAGONAL_NON_LINEAR_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DiagonalNonLinearStiffness")

    class _Cast_DiagonalNonLinearStiffness:
        """Special nested class for casting DiagonalNonLinearStiffness to subclasses."""

        def __init__(
            self: "DiagonalNonLinearStiffness._Cast_DiagonalNonLinearStiffness",
            parent: "DiagonalNonLinearStiffness",
        ):
            self._parent = parent

        @property
        def diagonal_non_linear_stiffness(
            self: "DiagonalNonLinearStiffness._Cast_DiagonalNonLinearStiffness",
        ) -> "DiagonalNonLinearStiffness":
            return self._parent

        def __getattr__(
            self: "DiagonalNonLinearStiffness._Cast_DiagonalNonLinearStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DiagonalNonLinearStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def theta_x_stiffness(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ThetaXStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @theta_x_stiffness.setter
    @enforce_parameter_types
    def theta_x_stiffness(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.ThetaXStiffness = value.wrapped

    @property
    def theta_y_stiffness(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ThetaYStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @theta_y_stiffness.setter
    @enforce_parameter_types
    def theta_y_stiffness(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.ThetaYStiffness = value.wrapped

    @property
    def theta_z_stiffness(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ThetaZStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @theta_z_stiffness.setter
    @enforce_parameter_types
    def theta_z_stiffness(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.ThetaZStiffness = value.wrapped

    @property
    def x_stiffness(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.XStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @x_stiffness.setter
    @enforce_parameter_types
    def x_stiffness(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.XStiffness = value.wrapped

    @property
    def y_stiffness(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.YStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @y_stiffness.setter
    @enforce_parameter_types
    def y_stiffness(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.YStiffness = value.wrapped

    @property
    def z_stiffness(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ZStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @z_stiffness.setter
    @enforce_parameter_types
    def z_stiffness(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.ZStiffness = value.wrapped

    @property
    def cast_to(
        self: Self,
    ) -> "DiagonalNonLinearStiffness._Cast_DiagonalNonLinearStiffness":
        return self._Cast_DiagonalNonLinearStiffness(self)
