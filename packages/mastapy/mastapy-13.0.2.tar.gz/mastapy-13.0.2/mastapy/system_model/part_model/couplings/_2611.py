"""SynchroniserCone"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_CONE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserCone"
)


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserCone",)


Self = TypeVar("Self", bound="SynchroniserCone")


class SynchroniserCone(_0.APIBase):
    """SynchroniserCone

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_CONE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserCone")

    class _Cast_SynchroniserCone:
        """Special nested class for casting SynchroniserCone to subclasses."""

        def __init__(
            self: "SynchroniserCone._Cast_SynchroniserCone", parent: "SynchroniserCone"
        ):
            self._parent = parent

        @property
        def synchroniser_cone(
            self: "SynchroniserCone._Cast_SynchroniserCone",
        ) -> "SynchroniserCone":
            return self._parent

        def __getattr__(self: "SynchroniserCone._Cast_SynchroniserCone", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserCone.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "float"):
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def coefficient_dynamic_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientDynamicFriction

        if temp is None:
            return 0.0

        return temp

    @coefficient_dynamic_friction.setter
    @enforce_parameter_types
    def coefficient_dynamic_friction(self: Self, value: "float"):
        self.wrapped.CoefficientDynamicFriction = (
            float(value) if value is not None else 0.0
        )

    @property
    def diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "float"):
        self.wrapped.Diameter = float(value) if value is not None else 0.0

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "SynchroniserCone._Cast_SynchroniserCone":
        return self._Cast_SynchroniserCone(self)
