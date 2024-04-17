"""InertiaTensor"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INERTIA_TENSOR = python_net_import("SMT.MastaAPI.MathUtility", "InertiaTensor")


__docformat__ = "restructuredtext en"
__all__ = ("InertiaTensor",)


Self = TypeVar("Self", bound="InertiaTensor")


class InertiaTensor(_0.APIBase):
    """InertiaTensor

    This is a mastapy class.
    """

    TYPE = _INERTIA_TENSOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InertiaTensor")

    class _Cast_InertiaTensor:
        """Special nested class for casting InertiaTensor to subclasses."""

        def __init__(
            self: "InertiaTensor._Cast_InertiaTensor", parent: "InertiaTensor"
        ):
            self._parent = parent

        @property
        def inertia_tensor(
            self: "InertiaTensor._Cast_InertiaTensor",
        ) -> "InertiaTensor":
            return self._parent

        def __getattr__(self: "InertiaTensor._Cast_InertiaTensor", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InertiaTensor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_axis_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XAxisInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def xy_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XYInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def xz_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XZInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def y_axis_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YAxisInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def yz_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YZInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def z_axis_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZAxisInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "InertiaTensor._Cast_InertiaTensor":
        return self._Cast_InertiaTensor(self)
