"""FacetedSurface"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACETED_SURFACE = python_net_import("SMT.MastaAPI.MathUtility", "FacetedSurface")


__docformat__ = "restructuredtext en"
__all__ = ("FacetedSurface",)


Self = TypeVar("Self", bound="FacetedSurface")


class FacetedSurface(_0.APIBase):
    """FacetedSurface

    This is a mastapy class.
    """

    TYPE = _FACETED_SURFACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FacetedSurface")

    class _Cast_FacetedSurface:
        """Special nested class for casting FacetedSurface to subclasses."""

        def __init__(
            self: "FacetedSurface._Cast_FacetedSurface", parent: "FacetedSurface"
        ):
            self._parent = parent

        @property
        def faceted_surface(
            self: "FacetedSurface._Cast_FacetedSurface",
        ) -> "FacetedSurface":
            return self._parent

        def __getattr__(self: "FacetedSurface._Cast_FacetedSurface", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FacetedSurface.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def facets(self: Self) -> "List[List[int]]":
        """List[List[int]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Facets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @property
    def normals(self: Self) -> "List[List[float]]":
        """List[List[float]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Normals

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def vertices(self: Self) -> "List[List[float]]":
        """List[List[float]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Vertices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FacetedSurface._Cast_FacetedSurface":
        return self._Cast_FacetedSurface(self)
