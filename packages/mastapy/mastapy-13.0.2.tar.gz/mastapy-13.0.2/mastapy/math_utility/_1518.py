"""FacetedBody"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACETED_BODY = python_net_import("SMT.MastaAPI.MathUtility", "FacetedBody")

if TYPE_CHECKING:
    from mastapy.math_utility import _1519


__docformat__ = "restructuredtext en"
__all__ = ("FacetedBody",)


Self = TypeVar("Self", bound="FacetedBody")


class FacetedBody(_0.APIBase):
    """FacetedBody

    This is a mastapy class.
    """

    TYPE = _FACETED_BODY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FacetedBody")

    class _Cast_FacetedBody:
        """Special nested class for casting FacetedBody to subclasses."""

        def __init__(self: "FacetedBody._Cast_FacetedBody", parent: "FacetedBody"):
            self._parent = parent

        @property
        def faceted_body(self: "FacetedBody._Cast_FacetedBody") -> "FacetedBody":
            return self._parent

        def __getattr__(self: "FacetedBody._Cast_FacetedBody", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FacetedBody.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def surfaces(self: Self) -> "List[_1519.FacetedSurface]":
        """List[mastapy.math_utility.FacetedSurface]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Surfaces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def add_surface(
        self: Self,
        vertices: "List[List[float]]",
        normals: "List[List[float]]",
        facets: "List[List[int]]",
    ):
        """Method does not return.

        Args:
            vertices (List[List[float]])
            normals (List[List[float]])
            facets (List[List[int]])
        """
        vertices = conversion.mp_to_pn_objects_in_list(vertices)
        normals = conversion.mp_to_pn_objects_in_list(normals)
        facets = conversion.mp_to_pn_objects_in_list(facets)
        self.wrapped.AddSurface(vertices, normals, facets)

    @property
    def cast_to(self: Self) -> "FacetedBody._Cast_FacetedBody":
        return self._Cast_FacetedBody(self)
