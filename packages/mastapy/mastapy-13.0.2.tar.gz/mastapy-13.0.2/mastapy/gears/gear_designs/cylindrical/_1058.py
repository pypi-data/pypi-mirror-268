"""ISO6336Geometry"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical import _1059
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ISO6336Geometry"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336Geometry",)


Self = TypeVar("Self", bound="ISO6336Geometry")


class ISO6336Geometry(_1059.ISO6336GeometryBase):
    """ISO6336Geometry

    This is a mastapy class.
    """

    TYPE = _ISO6336_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336Geometry")

    class _Cast_ISO6336Geometry:
        """Special nested class for casting ISO6336Geometry to subclasses."""

        def __init__(
            self: "ISO6336Geometry._Cast_ISO6336Geometry", parent: "ISO6336Geometry"
        ):
            self._parent = parent

        @property
        def iso6336_geometry_base(
            self: "ISO6336Geometry._Cast_ISO6336Geometry",
        ) -> "_1059.ISO6336GeometryBase":
            return self._parent._cast(_1059.ISO6336GeometryBase)

        @property
        def iso6336_geometry(
            self: "ISO6336Geometry._Cast_ISO6336Geometry",
        ) -> "ISO6336Geometry":
            return self._parent

        def __getattr__(self: "ISO6336Geometry._Cast_ISO6336Geometry", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO6336Geometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso6336_root_fillet_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO6336RootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def iso6336_tooth_root_chord(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO6336ToothRootChord

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ISO6336Geometry._Cast_ISO6336Geometry":
        return self._Cast_ISO6336Geometry(self)
