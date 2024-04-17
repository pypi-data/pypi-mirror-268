"""GearNURBSSurface"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears import _323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_NURBS_SURFACE = python_net_import("SMT.MastaAPI.Gears", "GearNURBSSurface")


__docformat__ = "restructuredtext en"
__all__ = ("GearNURBSSurface",)


Self = TypeVar("Self", bound="GearNURBSSurface")


class GearNURBSSurface(_323.ConicalGearToothSurface):
    """GearNURBSSurface

    This is a mastapy class.
    """

    TYPE = _GEAR_NURBS_SURFACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearNURBSSurface")

    class _Cast_GearNURBSSurface:
        """Special nested class for casting GearNURBSSurface to subclasses."""

        def __init__(
            self: "GearNURBSSurface._Cast_GearNURBSSurface", parent: "GearNURBSSurface"
        ):
            self._parent = parent

        @property
        def conical_gear_tooth_surface(
            self: "GearNURBSSurface._Cast_GearNURBSSurface",
        ) -> "_323.ConicalGearToothSurface":
            return self._parent._cast(_323.ConicalGearToothSurface)

        @property
        def gear_nurbs_surface(
            self: "GearNURBSSurface._Cast_GearNURBSSurface",
        ) -> "GearNURBSSurface":
            return self._parent

        def __getattr__(self: "GearNURBSSurface._Cast_GearNURBSSurface", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearNURBSSurface.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearNURBSSurface._Cast_GearNURBSSurface":
        return self._Cast_GearNURBSSurface(self)
