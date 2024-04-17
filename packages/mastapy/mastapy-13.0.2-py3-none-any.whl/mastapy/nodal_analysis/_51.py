"""BarGeometry"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_GEOMETRY = python_net_import("SMT.MastaAPI.NodalAnalysis", "BarGeometry")


__docformat__ = "restructuredtext en"
__all__ = ("BarGeometry",)


Self = TypeVar("Self", bound="BarGeometry")


class BarGeometry(_0.APIBase):
    """BarGeometry

    This is a mastapy class.
    """

    TYPE = _BAR_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BarGeometry")

    class _Cast_BarGeometry:
        """Special nested class for casting BarGeometry to subclasses."""

        def __init__(self: "BarGeometry._Cast_BarGeometry", parent: "BarGeometry"):
            self._parent = parent

        @property
        def bar_geometry(self: "BarGeometry._Cast_BarGeometry") -> "BarGeometry":
            return self._parent

        def __getattr__(self: "BarGeometry._Cast_BarGeometry", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BarGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cross_sectional_area_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrossSectionalAreaRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_area_moment_of_inertia_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarAreaMomentOfInertiaRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "BarGeometry._Cast_BarGeometry":
        return self._Cast_BarGeometry(self)
