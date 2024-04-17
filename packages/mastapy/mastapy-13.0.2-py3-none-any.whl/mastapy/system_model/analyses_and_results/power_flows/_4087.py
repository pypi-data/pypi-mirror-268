"""CylindricalGearGeometricEntityDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.power_flows import _4131
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_GEOMETRIC_ENTITY_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CylindricalGearGeometricEntityDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.geometry import _310, _311


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearGeometricEntityDrawStyle",)


Self = TypeVar("Self", bound="CylindricalGearGeometricEntityDrawStyle")


class CylindricalGearGeometricEntityDrawStyle(_4131.PowerFlowDrawStyle):
    """CylindricalGearGeometricEntityDrawStyle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_GEOMETRIC_ENTITY_DRAW_STYLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearGeometricEntityDrawStyle"
    )

    class _Cast_CylindricalGearGeometricEntityDrawStyle:
        """Special nested class for casting CylindricalGearGeometricEntityDrawStyle to subclasses."""

        def __init__(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
            parent: "CylindricalGearGeometricEntityDrawStyle",
        ):
            self._parent = parent

        @property
        def power_flow_draw_style(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "_4131.PowerFlowDrawStyle":
            return self._parent._cast(_4131.PowerFlowDrawStyle)

        @property
        def draw_style(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "_310.DrawStyle":
            from mastapy.geometry import _310

            return self._parent._cast(_310.DrawStyle)

        @property
        def draw_style_base(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def cylindrical_gear_geometric_entity_draw_style(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "CylindricalGearGeometricEntityDrawStyle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CylindricalGearGeometricEntityDrawStyle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle":
        return self._Cast_CylindricalGearGeometricEntityDrawStyle(self)
