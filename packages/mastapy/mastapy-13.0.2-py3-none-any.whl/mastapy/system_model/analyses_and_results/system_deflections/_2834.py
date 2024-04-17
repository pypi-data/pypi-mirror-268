"""SystemDeflectionDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.drawing import _2253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SystemDeflectionDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1858
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("SystemDeflectionDrawStyle",)


Self = TypeVar("Self", bound="SystemDeflectionDrawStyle")


class SystemDeflectionDrawStyle(_2253.ContourDrawStyle):
    """SystemDeflectionDrawStyle

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemDeflectionDrawStyle")

    class _Cast_SystemDeflectionDrawStyle:
        """Special nested class for casting SystemDeflectionDrawStyle to subclasses."""

        def __init__(
            self: "SystemDeflectionDrawStyle._Cast_SystemDeflectionDrawStyle",
            parent: "SystemDeflectionDrawStyle",
        ):
            self._parent = parent

        @property
        def contour_draw_style(
            self: "SystemDeflectionDrawStyle._Cast_SystemDeflectionDrawStyle",
        ) -> "_2253.ContourDrawStyle":
            return self._parent._cast(_2253.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "SystemDeflectionDrawStyle._Cast_SystemDeflectionDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def system_deflection_draw_style(
            self: "SystemDeflectionDrawStyle._Cast_SystemDeflectionDrawStyle",
        ) -> "SystemDeflectionDrawStyle":
            return self._parent

        def __getattr__(
            self: "SystemDeflectionDrawStyle._Cast_SystemDeflectionDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemDeflectionDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_arrows(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowArrows

        if temp is None:
            return False

        return temp

    @show_arrows.setter
    @enforce_parameter_types
    def show_arrows(self: Self, value: "bool"):
        self.wrapped.ShowArrows = bool(value) if value is not None else False

    @property
    def force_arrow_scaling(self: Self) -> "_1858.ScalingDrawStyle":
        """mastapy.utility_gui.ScalingDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceArrowScaling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SystemDeflectionDrawStyle._Cast_SystemDeflectionDrawStyle":
        return self._Cast_SystemDeflectionDrawStyle(self)
