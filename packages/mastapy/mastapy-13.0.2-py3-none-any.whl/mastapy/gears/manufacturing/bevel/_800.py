"""HypoidAdvancedLibrary"""

from __future__ import annotations

from typing import TypeVar

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_ADVANCED_LIBRARY = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "HypoidAdvancedLibrary"
)


__docformat__ = "restructuredtext en"
__all__ = ("HypoidAdvancedLibrary",)


Self = TypeVar("Self", bound="HypoidAdvancedLibrary")


class HypoidAdvancedLibrary(_0.APIBase):
    """HypoidAdvancedLibrary

    This is a mastapy class.
    """

    TYPE = _HYPOID_ADVANCED_LIBRARY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidAdvancedLibrary")

    class _Cast_HypoidAdvancedLibrary:
        """Special nested class for casting HypoidAdvancedLibrary to subclasses."""

        def __init__(
            self: "HypoidAdvancedLibrary._Cast_HypoidAdvancedLibrary",
            parent: "HypoidAdvancedLibrary",
        ):
            self._parent = parent

        @property
        def hypoid_advanced_library(
            self: "HypoidAdvancedLibrary._Cast_HypoidAdvancedLibrary",
        ) -> "HypoidAdvancedLibrary":
            return self._parent

        def __getattr__(
            self: "HypoidAdvancedLibrary._Cast_HypoidAdvancedLibrary", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidAdvancedLibrary.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_pinion_meshing_boundary_coast(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerPinionMeshingBoundaryCoast

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def inner_pinion_meshing_boundary_drive(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerPinionMeshingBoundaryDrive

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def outer_pinion_meshing_boundary_coast(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterPinionMeshingBoundaryCoast

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def outer_pinion_meshing_boundary_drive(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterPinionMeshingBoundaryDrive

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def wheel_inner_blade_angle_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInnerBladeAngleConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_blade_angle_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelOuterBladeAngleConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "HypoidAdvancedLibrary._Cast_HypoidAdvancedLibrary":
        return self._Cast_HypoidAdvancedLibrary(self)
