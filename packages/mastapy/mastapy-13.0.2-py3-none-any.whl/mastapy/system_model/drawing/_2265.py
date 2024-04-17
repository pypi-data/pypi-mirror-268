"""SteadyStateSynchronousResponseViewable"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.drawing import _2262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "SteadyStateSynchronousResponseViewable"
)


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseViewable",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseViewable")


class SteadyStateSynchronousResponseViewable(_2262.RotorDynamicsViewable):
    """SteadyStateSynchronousResponseViewable

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_VIEWABLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseViewable"
    )

    class _Cast_SteadyStateSynchronousResponseViewable:
        """Special nested class for casting SteadyStateSynchronousResponseViewable to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseViewable._Cast_SteadyStateSynchronousResponseViewable",
            parent: "SteadyStateSynchronousResponseViewable",
        ):
            self._parent = parent

        @property
        def rotor_dynamics_viewable(
            self: "SteadyStateSynchronousResponseViewable._Cast_SteadyStateSynchronousResponseViewable",
        ) -> "_2262.RotorDynamicsViewable":
            return self._parent._cast(_2262.RotorDynamicsViewable)

        @property
        def steady_state_synchronous_response_viewable(
            self: "SteadyStateSynchronousResponseViewable._Cast_SteadyStateSynchronousResponseViewable",
        ) -> "SteadyStateSynchronousResponseViewable":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseViewable._Cast_SteadyStateSynchronousResponseViewable",
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
        self: Self, instance_to_wrap: "SteadyStateSynchronousResponseViewable.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseViewable._Cast_SteadyStateSynchronousResponseViewable":
        return self._Cast_SteadyStateSynchronousResponseViewable(self)
