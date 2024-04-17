"""MassProperties"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_PROPERTIES = python_net_import("SMT.MastaAPI.MathUtility", "MassProperties")

if TYPE_CHECKING:
    from mastapy.math_utility import _1524


__docformat__ = "restructuredtext en"
__all__ = ("MassProperties",)


Self = TypeVar("Self", bound="MassProperties")


class MassProperties(_0.APIBase):
    """MassProperties

    This is a mastapy class.
    """

    TYPE = _MASS_PROPERTIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassProperties")

    class _Cast_MassProperties:
        """Special nested class for casting MassProperties to subclasses."""

        def __init__(
            self: "MassProperties._Cast_MassProperties", parent: "MassProperties"
        ):
            self._parent = parent

        @property
        def mass_properties(
            self: "MassProperties._Cast_MassProperties",
        ) -> "MassProperties":
            return self._parent

        def __getattr__(self: "MassProperties._Cast_MassProperties", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassProperties.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_of_mass(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreOfMass

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def inertia_tensor_about_centre_of_mass(self: Self) -> "_1524.InertiaTensor":
        """mastapy.math_utility.InertiaTensor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaTensorAboutCentreOfMass

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inertia_tensor_about_origin(self: Self) -> "_1524.InertiaTensor":
        """mastapy.math_utility.InertiaTensor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaTensorAboutOrigin

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "MassProperties._Cast_MassProperties":
        return self._Cast_MassProperties(self)
