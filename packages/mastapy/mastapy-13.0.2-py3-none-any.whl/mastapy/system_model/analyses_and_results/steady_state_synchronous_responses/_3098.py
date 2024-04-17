"""SteadyStateSynchronousResponseDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.rotor_dynamics import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SteadyStateSynchronousResponseDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2253
    from mastapy.geometry import _311


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseDrawStyle",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseDrawStyle")


class SteadyStateSynchronousResponseDrawStyle(_4034.RotorDynamicsDrawStyle):
    """SteadyStateSynchronousResponseDrawStyle

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_DRAW_STYLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseDrawStyle"
    )

    class _Cast_SteadyStateSynchronousResponseDrawStyle:
        """Special nested class for casting SteadyStateSynchronousResponseDrawStyle to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseDrawStyle._Cast_SteadyStateSynchronousResponseDrawStyle",
            parent: "SteadyStateSynchronousResponseDrawStyle",
        ):
            self._parent = parent

        @property
        def rotor_dynamics_draw_style(
            self: "SteadyStateSynchronousResponseDrawStyle._Cast_SteadyStateSynchronousResponseDrawStyle",
        ) -> "_4034.RotorDynamicsDrawStyle":
            return self._parent._cast(_4034.RotorDynamicsDrawStyle)

        @property
        def contour_draw_style(
            self: "SteadyStateSynchronousResponseDrawStyle._Cast_SteadyStateSynchronousResponseDrawStyle",
        ) -> "_2253.ContourDrawStyle":
            from mastapy.system_model.drawing import _2253

            return self._parent._cast(_2253.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "SteadyStateSynchronousResponseDrawStyle._Cast_SteadyStateSynchronousResponseDrawStyle",
        ) -> "_311.DrawStyleBase":
            from mastapy.geometry import _311

            return self._parent._cast(_311.DrawStyleBase)

        @property
        def steady_state_synchronous_response_draw_style(
            self: "SteadyStateSynchronousResponseDrawStyle._Cast_SteadyStateSynchronousResponseDrawStyle",
        ) -> "SteadyStateSynchronousResponseDrawStyle":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseDrawStyle._Cast_SteadyStateSynchronousResponseDrawStyle",
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
        self: Self, instance_to_wrap: "SteadyStateSynchronousResponseDrawStyle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseDrawStyle._Cast_SteadyStateSynchronousResponseDrawStyle":
        return self._Cast_SteadyStateSynchronousResponseDrawStyle(self)
