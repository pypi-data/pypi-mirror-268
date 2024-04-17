"""SurfaceToSurfaceContact"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SURFACE_TO_SURFACE_CONTACT = python_net_import(
    "SMT.MastaAPI.MathUtility.StiffnessCalculators", "SurfaceToSurfaceContact"
)


__docformat__ = "restructuredtext en"
__all__ = ("SurfaceToSurfaceContact",)


Self = TypeVar("Self", bound="SurfaceToSurfaceContact")


class SurfaceToSurfaceContact(_0.APIBase):
    """SurfaceToSurfaceContact

    This is a mastapy class.
    """

    TYPE = _SURFACE_TO_SURFACE_CONTACT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SurfaceToSurfaceContact")

    class _Cast_SurfaceToSurfaceContact:
        """Special nested class for casting SurfaceToSurfaceContact to subclasses."""

        def __init__(
            self: "SurfaceToSurfaceContact._Cast_SurfaceToSurfaceContact",
            parent: "SurfaceToSurfaceContact",
        ):
            self._parent = parent

        @property
        def surface_to_surface_contact(
            self: "SurfaceToSurfaceContact._Cast_SurfaceToSurfaceContact",
        ) -> "SurfaceToSurfaceContact":
            return self._parent

        def __getattr__(
            self: "SurfaceToSurfaceContact._Cast_SurfaceToSurfaceContact", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SurfaceToSurfaceContact.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def normal_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_penetration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfacePenetration

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SurfaceToSurfaceContact._Cast_SurfaceToSurfaceContact":
        return self._Cast_SurfaceToSurfaceContact(self)
