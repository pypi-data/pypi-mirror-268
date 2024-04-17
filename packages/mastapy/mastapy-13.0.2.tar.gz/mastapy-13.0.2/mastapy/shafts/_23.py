"""ShaftKey"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.shafts import _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_KEY = python_net_import("SMT.MastaAPI.Shafts", "ShaftKey")

if TYPE_CHECKING:
    from mastapy.shafts import _45


__docformat__ = "restructuredtext en"
__all__ = ("ShaftKey",)


Self = TypeVar("Self", bound="ShaftKey")


class ShaftKey(_21.ShaftFeature):
    """ShaftKey

    This is a mastapy class.
    """

    TYPE = _SHAFT_KEY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftKey")

    class _Cast_ShaftKey:
        """Special nested class for casting ShaftKey to subclasses."""

        def __init__(self: "ShaftKey._Cast_ShaftKey", parent: "ShaftKey"):
            self._parent = parent

        @property
        def shaft_feature(self: "ShaftKey._Cast_ShaftKey") -> "_21.ShaftFeature":
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_key(self: "ShaftKey._Cast_ShaftKey") -> "ShaftKey":
            return self._parent

        def __getattr__(self: "ShaftKey._Cast_ShaftKey", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftKey.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Depth

        if temp is None:
            return 0.0

        return temp

    @depth.setter
    @enforce_parameter_types
    def depth(self: Self, value: "float"):
        self.wrapped.Depth = float(value) if value is not None else 0.0

    @property
    def fillet_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FilletRadius

        if temp is None:
            return 0.0

        return temp

    @fillet_radius.setter
    @enforce_parameter_types
    def fillet_radius(self: Self, value: "float"):
        self.wrapped.FilletRadius = float(value) if value is not None else 0.0

    @property
    def number_of_keys(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfKeys

        if temp is None:
            return 0

        return temp

    @number_of_keys.setter
    @enforce_parameter_types
    def number_of_keys(self: Self, value: "int"):
        self.wrapped.NumberOfKeys = int(value) if value is not None else 0

    @property
    def surface_finish(self: Self) -> "_45.SurfaceFinishes":
        """mastapy.shafts.SurfaceFinishes"""
        temp = self.wrapped.SurfaceFinish

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Shafts.SurfaceFinishes")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.shafts._45", "SurfaceFinishes")(
            value
        )

    @surface_finish.setter
    @enforce_parameter_types
    def surface_finish(self: Self, value: "_45.SurfaceFinishes"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Shafts.SurfaceFinishes")
        self.wrapped.SurfaceFinish = value

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ShaftKey._Cast_ShaftKey":
        return self._Cast_ShaftKey(self)
