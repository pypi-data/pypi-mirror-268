"""StabilityAnalysisDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.rotor_dynamics import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StabilityAnalysisDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2253
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("StabilityAnalysisDrawStyle",)


Self = TypeVar("Self", bound="StabilityAnalysisDrawStyle")


class StabilityAnalysisDrawStyle(_4034.RotorDynamicsDrawStyle):
    """StabilityAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StabilityAnalysisDrawStyle")

    class _Cast_StabilityAnalysisDrawStyle:
        """Special nested class for casting StabilityAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle",
            parent: "StabilityAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def rotor_dynamics_draw_style(
            self: "StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle",
        ) -> "_4034.RotorDynamicsDrawStyle":
            return self._parent._cast(_4034.RotorDynamicsDrawStyle)

        @property
        def contour_draw_style(
            self: "StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle",
        ) -> "_2253.ContourDrawStyle":
            from mastapy.system_model.drawing import _2253

            return self._parent._cast(_2253.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def stability_analysis_draw_style(
            self: "StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle",
        ) -> "StabilityAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StabilityAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StabilityAnalysisDrawStyle._Cast_StabilityAnalysisDrawStyle":
        return self._Cast_StabilityAnalysisDrawStyle(self)
