"""ISO6336GeometryManufactured"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical import _1059
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_GEOMETRY_MANUFACTURED = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ISO6336GeometryManufactured"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336GeometryManufactured",)


Self = TypeVar("Self", bound="ISO6336GeometryManufactured")


class ISO6336GeometryManufactured(_1059.ISO6336GeometryBase):
    """ISO6336GeometryManufactured

    This is a mastapy class.
    """

    TYPE = _ISO6336_GEOMETRY_MANUFACTURED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336GeometryManufactured")

    class _Cast_ISO6336GeometryManufactured:
        """Special nested class for casting ISO6336GeometryManufactured to subclasses."""

        def __init__(
            self: "ISO6336GeometryManufactured._Cast_ISO6336GeometryManufactured",
            parent: "ISO6336GeometryManufactured",
        ):
            self._parent = parent

        @property
        def iso6336_geometry_base(
            self: "ISO6336GeometryManufactured._Cast_ISO6336GeometryManufactured",
        ) -> "_1059.ISO6336GeometryBase":
            return self._parent._cast(_1059.ISO6336GeometryBase)

        @property
        def iso6336_geometry_manufactured(
            self: "ISO6336GeometryManufactured._Cast_ISO6336GeometryManufactured",
        ) -> "ISO6336GeometryManufactured":
            return self._parent

        def __getattr__(
            self: "ISO6336GeometryManufactured._Cast_ISO6336GeometryManufactured",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO6336GeometryManufactured.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "ISO6336GeometryManufactured._Cast_ISO6336GeometryManufactured":
        return self._Cast_ISO6336GeometryManufactured(self)
