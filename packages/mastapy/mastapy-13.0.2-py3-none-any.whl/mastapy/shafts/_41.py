"""ShaftSurfaceFinishSection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.shafts import _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SURFACE_FINISH_SECTION = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftSurfaceFinishSection"
)

if TYPE_CHECKING:
    from mastapy.shafts import _42


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSurfaceFinishSection",)


Self = TypeVar("Self", bound="ShaftSurfaceFinishSection")


class ShaftSurfaceFinishSection(_21.ShaftFeature):
    """ShaftSurfaceFinishSection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SURFACE_FINISH_SECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSurfaceFinishSection")

    class _Cast_ShaftSurfaceFinishSection:
        """Special nested class for casting ShaftSurfaceFinishSection to subclasses."""

        def __init__(
            self: "ShaftSurfaceFinishSection._Cast_ShaftSurfaceFinishSection",
            parent: "ShaftSurfaceFinishSection",
        ):
            self._parent = parent

        @property
        def shaft_feature(
            self: "ShaftSurfaceFinishSection._Cast_ShaftSurfaceFinishSection",
        ) -> "_21.ShaftFeature":
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_surface_finish_section(
            self: "ShaftSurfaceFinishSection._Cast_ShaftSurfaceFinishSection",
        ) -> "ShaftSurfaceFinishSection":
            return self._parent

        def __getattr__(
            self: "ShaftSurfaceFinishSection._Cast_ShaftSurfaceFinishSection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSurfaceFinishSection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def surface_roughness(self: Self) -> "_42.ShaftSurfaceRoughness":
        """mastapy.shafts.ShaftSurfaceRoughness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def add_new_surface_finish_section(self: Self):
        """Method does not return."""
        self.wrapped.AddNewSurfaceFinishSection()

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSurfaceFinishSection._Cast_ShaftSurfaceFinishSection":
        return self._Cast_ShaftSurfaceFinishSection(self)
