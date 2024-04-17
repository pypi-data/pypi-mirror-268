"""PowerFlowDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.geometry import _310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_FLOW_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PowerFlowDrawStyle"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4087
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("PowerFlowDrawStyle",)


Self = TypeVar("Self", bound="PowerFlowDrawStyle")


class PowerFlowDrawStyle(_310.DrawStyle):
    """PowerFlowDrawStyle

    This is a mastapy class.
    """

    TYPE = _POWER_FLOW_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerFlowDrawStyle")

    class _Cast_PowerFlowDrawStyle:
        """Special nested class for casting PowerFlowDrawStyle to subclasses."""

        def __init__(
            self: "PowerFlowDrawStyle._Cast_PowerFlowDrawStyle",
            parent: "PowerFlowDrawStyle",
        ):
            self._parent = parent

        @property
        def draw_style(
            self: "PowerFlowDrawStyle._Cast_PowerFlowDrawStyle",
        ) -> "_310.DrawStyle":
            return self._parent._cast(_310.DrawStyle)

        @property
        def draw_style_base(
            self: "PowerFlowDrawStyle._Cast_PowerFlowDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def cylindrical_gear_geometric_entity_draw_style(
            self: "PowerFlowDrawStyle._Cast_PowerFlowDrawStyle",
        ) -> "_4087.CylindricalGearGeometricEntityDrawStyle":
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.CylindricalGearGeometricEntityDrawStyle)

        @property
        def power_flow_draw_style(
            self: "PowerFlowDrawStyle._Cast_PowerFlowDrawStyle",
        ) -> "PowerFlowDrawStyle":
            return self._parent

        def __getattr__(self: "PowerFlowDrawStyle._Cast_PowerFlowDrawStyle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerFlowDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def colour_loaded_flanks(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ColourLoadedFlanks

        if temp is None:
            return False

        return temp

    @colour_loaded_flanks.setter
    @enforce_parameter_types
    def colour_loaded_flanks(self: Self, value: "bool"):
        self.wrapped.ColourLoadedFlanks = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "PowerFlowDrawStyle._Cast_PowerFlowDrawStyle":
        return self._Cast_PowerFlowDrawStyle(self)
