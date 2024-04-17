"""RotorDynamicsDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.drawing import _2253
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_DYNAMICS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.RotorDynamics",
    "RotorDynamicsDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3098,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import _3879
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6592
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("RotorDynamicsDrawStyle",)


Self = TypeVar("Self", bound="RotorDynamicsDrawStyle")


class RotorDynamicsDrawStyle(_2253.ContourDrawStyle):
    """RotorDynamicsDrawStyle

    This is a mastapy class.
    """

    TYPE = _ROTOR_DYNAMICS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RotorDynamicsDrawStyle")

    class _Cast_RotorDynamicsDrawStyle:
        """Special nested class for casting RotorDynamicsDrawStyle to subclasses."""

        def __init__(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle",
            parent: "RotorDynamicsDrawStyle",
        ):
            self._parent = parent

        @property
        def contour_draw_style(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle",
        ) -> "_2253.ContourDrawStyle":
            return self._parent._cast(_2253.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def steady_state_synchronous_response_draw_style(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle",
        ) -> "_3098.SteadyStateSynchronousResponseDrawStyle":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(_3098.SteadyStateSynchronousResponseDrawStyle)

        @property
        def stability_analysis_draw_style(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle",
        ) -> "_3879.StabilityAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.StabilityAnalysisDrawStyle)

        @property
        def critical_speed_analysis_draw_style(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle",
        ) -> "_6592.CriticalSpeedAnalysisDrawStyle":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6592,
            )

            return self._parent._cast(_6592.CriticalSpeedAnalysisDrawStyle)

        @property
        def rotor_dynamics_draw_style(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle",
        ) -> "RotorDynamicsDrawStyle":
            return self._parent

        def __getattr__(
            self: "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RotorDynamicsDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_whirl_orbits(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowWhirlOrbits

        if temp is None:
            return False

        return temp

    @show_whirl_orbits.setter
    @enforce_parameter_types
    def show_whirl_orbits(self: Self, value: "bool"):
        self.wrapped.ShowWhirlOrbits = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "RotorDynamicsDrawStyle._Cast_RotorDynamicsDrawStyle":
        return self._Cast_RotorDynamicsDrawStyle(self)
