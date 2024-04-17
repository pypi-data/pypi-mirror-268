"""CriticalSpeedAnalysisDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.rotor_dynamics import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CriticalSpeedAnalysisDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2253
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("CriticalSpeedAnalysisDrawStyle",)


Self = TypeVar("Self", bound="CriticalSpeedAnalysisDrawStyle")


class CriticalSpeedAnalysisDrawStyle(_4034.RotorDynamicsDrawStyle):
    """CriticalSpeedAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CriticalSpeedAnalysisDrawStyle")

    class _Cast_CriticalSpeedAnalysisDrawStyle:
        """Special nested class for casting CriticalSpeedAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "CriticalSpeedAnalysisDrawStyle._Cast_CriticalSpeedAnalysisDrawStyle",
            parent: "CriticalSpeedAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def rotor_dynamics_draw_style(
            self: "CriticalSpeedAnalysisDrawStyle._Cast_CriticalSpeedAnalysisDrawStyle",
        ) -> "_4034.RotorDynamicsDrawStyle":
            return self._parent._cast(_4034.RotorDynamicsDrawStyle)

        @property
        def contour_draw_style(
            self: "CriticalSpeedAnalysisDrawStyle._Cast_CriticalSpeedAnalysisDrawStyle",
        ) -> "_2253.ContourDrawStyle":
            from mastapy.system_model.drawing import _2253

            return self._parent._cast(_2253.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "CriticalSpeedAnalysisDrawStyle._Cast_CriticalSpeedAnalysisDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def critical_speed_analysis_draw_style(
            self: "CriticalSpeedAnalysisDrawStyle._Cast_CriticalSpeedAnalysisDrawStyle",
        ) -> "CriticalSpeedAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "CriticalSpeedAnalysisDrawStyle._Cast_CriticalSpeedAnalysisDrawStyle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CriticalSpeedAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CriticalSpeedAnalysisDrawStyle._Cast_CriticalSpeedAnalysisDrawStyle":
        return self._Cast_CriticalSpeedAnalysisDrawStyle(self)
