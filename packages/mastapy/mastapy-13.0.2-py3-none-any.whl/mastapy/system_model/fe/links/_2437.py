"""RollingRingConnectionFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2430
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "RollingRingConnectionFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2432, _2425


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingConnectionFELink",)


Self = TypeVar("Self", bound="RollingRingConnectionFELink")


class RollingRingConnectionFELink(_2430.MultiAngleConnectionFELink):
    """RollingRingConnectionFELink

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingConnectionFELink")

    class _Cast_RollingRingConnectionFELink:
        """Special nested class for casting RollingRingConnectionFELink to subclasses."""

        def __init__(
            self: "RollingRingConnectionFELink._Cast_RollingRingConnectionFELink",
            parent: "RollingRingConnectionFELink",
        ):
            self._parent = parent

        @property
        def multi_angle_connection_fe_link(
            self: "RollingRingConnectionFELink._Cast_RollingRingConnectionFELink",
        ) -> "_2430.MultiAngleConnectionFELink":
            return self._parent._cast(_2430.MultiAngleConnectionFELink)

        @property
        def multi_node_fe_link(
            self: "RollingRingConnectionFELink._Cast_RollingRingConnectionFELink",
        ) -> "_2432.MultiNodeFELink":
            from mastapy.system_model.fe.links import _2432

            return self._parent._cast(_2432.MultiNodeFELink)

        @property
        def fe_link(
            self: "RollingRingConnectionFELink._Cast_RollingRingConnectionFELink",
        ) -> "_2425.FELink":
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.FELink)

        @property
        def rolling_ring_connection_fe_link(
            self: "RollingRingConnectionFELink._Cast_RollingRingConnectionFELink",
        ) -> "RollingRingConnectionFELink":
            return self._parent

        def __getattr__(
            self: "RollingRingConnectionFELink._Cast_RollingRingConnectionFELink",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingConnectionFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingConnectionFELink._Cast_RollingRingConnectionFELink":
        return self._Cast_RollingRingConnectionFELink(self)
