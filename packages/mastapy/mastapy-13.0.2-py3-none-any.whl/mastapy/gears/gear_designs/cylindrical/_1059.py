"""ISO6336GeometryBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_GEOMETRY_BASE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "ISO6336GeometryBase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1058, _1060, _1061


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336GeometryBase",)


Self = TypeVar("Self", bound="ISO6336GeometryBase")


class ISO6336GeometryBase(_0.APIBase):
    """ISO6336GeometryBase

    This is a mastapy class.
    """

    TYPE = _ISO6336_GEOMETRY_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336GeometryBase")

    class _Cast_ISO6336GeometryBase:
        """Special nested class for casting ISO6336GeometryBase to subclasses."""

        def __init__(
            self: "ISO6336GeometryBase._Cast_ISO6336GeometryBase",
            parent: "ISO6336GeometryBase",
        ):
            self._parent = parent

        @property
        def iso6336_geometry(
            self: "ISO6336GeometryBase._Cast_ISO6336GeometryBase",
        ) -> "_1058.ISO6336Geometry":
            from mastapy.gears.gear_designs.cylindrical import _1058

            return self._parent._cast(_1058.ISO6336Geometry)

        @property
        def iso6336_geometry_for_shaped_gears(
            self: "ISO6336GeometryBase._Cast_ISO6336GeometryBase",
        ) -> "_1060.ISO6336GeometryForShapedGears":
            from mastapy.gears.gear_designs.cylindrical import _1060

            return self._parent._cast(_1060.ISO6336GeometryForShapedGears)

        @property
        def iso6336_geometry_manufactured(
            self: "ISO6336GeometryBase._Cast_ISO6336GeometryBase",
        ) -> "_1061.ISO6336GeometryManufactured":
            from mastapy.gears.gear_designs.cylindrical import _1061

            return self._parent._cast(_1061.ISO6336GeometryManufactured)

        @property
        def iso6336_geometry_base(
            self: "ISO6336GeometryBase._Cast_ISO6336GeometryBase",
        ) -> "ISO6336GeometryBase":
            return self._parent

        def __getattr__(
            self: "ISO6336GeometryBase._Cast_ISO6336GeometryBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO6336GeometryBase.TYPE"):
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
    def iso6336_signed_virtual_base_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO6336SignedVirtualBaseDiameter

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
    def iso6336_virtual_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO6336VirtualTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_number_of_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualNumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ISO6336GeometryBase._Cast_ISO6336GeometryBase":
        return self._Cast_ISO6336GeometryBase(self)
