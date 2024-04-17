"""MultiAngleConnectionFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_ANGLE_CONNECTION_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiAngleConnectionFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2428, _2437, _2425


__docformat__ = "restructuredtext en"
__all__ = ("MultiAngleConnectionFELink",)


Self = TypeVar("Self", bound="MultiAngleConnectionFELink")


class MultiAngleConnectionFELink(_2432.MultiNodeFELink):
    """MultiAngleConnectionFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_ANGLE_CONNECTION_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiAngleConnectionFELink")

    class _Cast_MultiAngleConnectionFELink:
        """Special nested class for casting MultiAngleConnectionFELink to subclasses."""

        def __init__(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
            parent: "MultiAngleConnectionFELink",
        ):
            self._parent = parent

        @property
        def multi_node_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2432.MultiNodeFELink":
            return self._parent._cast(_2432.MultiNodeFELink)

        @property
        def fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2425.FELink":
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.FELink)

        @property
        def gear_mesh_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2428.GearMeshFELink":
            from mastapy.system_model.fe.links import _2428

            return self._parent._cast(_2428.GearMeshFELink)

        @property
        def rolling_ring_connection_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "_2437.RollingRingConnectionFELink":
            from mastapy.system_model.fe.links import _2437

            return self._parent._cast(_2437.RollingRingConnectionFELink)

        @property
        def multi_angle_connection_fe_link(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
        ) -> "MultiAngleConnectionFELink":
            return self._parent

        def __getattr__(
            self: "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiAngleConnectionFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink":
        return self._Cast_MultiAngleConnectionFELink(self)
