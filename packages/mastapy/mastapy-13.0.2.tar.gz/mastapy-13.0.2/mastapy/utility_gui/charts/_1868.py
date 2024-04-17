"""PointsForSurface"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINTS_FOR_SURFACE = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "PointsForSurface"
)


__docformat__ = "restructuredtext en"
__all__ = ("PointsForSurface",)


Self = TypeVar("Self", bound="PointsForSurface")


class PointsForSurface(_0.APIBase):
    """PointsForSurface

    This is a mastapy class.
    """

    TYPE = _POINTS_FOR_SURFACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointsForSurface")

    class _Cast_PointsForSurface:
        """Special nested class for casting PointsForSurface to subclasses."""

        def __init__(
            self: "PointsForSurface._Cast_PointsForSurface", parent: "PointsForSurface"
        ):
            self._parent = parent

        @property
        def points_for_surface(
            self: "PointsForSurface._Cast_PointsForSurface",
        ) -> "PointsForSurface":
            return self._parent

        def __getattr__(self: "PointsForSurface._Cast_PointsForSurface", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointsForSurface.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def points(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Points

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PointsForSurface._Cast_PointsForSurface":
        return self._Cast_PointsForSurface(self)
