"""PlanetaryConnectorMultiNodeFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2434
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTOR_MULTI_NODE_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "PlanetaryConnectorMultiNodeFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2432, _2425


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectorMultiNodeFELink",)


Self = TypeVar("Self", bound="PlanetaryConnectorMultiNodeFELink")


class PlanetaryConnectorMultiNodeFELink(_2434.PlanetBasedFELink):
    """PlanetaryConnectorMultiNodeFELink

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTOR_MULTI_NODE_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectorMultiNodeFELink")

    class _Cast_PlanetaryConnectorMultiNodeFELink:
        """Special nested class for casting PlanetaryConnectorMultiNodeFELink to subclasses."""

        def __init__(
            self: "PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink",
            parent: "PlanetaryConnectorMultiNodeFELink",
        ):
            self._parent = parent

        @property
        def planet_based_fe_link(
            self: "PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink",
        ) -> "_2434.PlanetBasedFELink":
            return self._parent._cast(_2434.PlanetBasedFELink)

        @property
        def multi_node_fe_link(
            self: "PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink",
        ) -> "_2432.MultiNodeFELink":
            from mastapy.system_model.fe.links import _2432

            return self._parent._cast(_2432.MultiNodeFELink)

        @property
        def fe_link(
            self: "PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink",
        ) -> "_2425.FELink":
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.FELink)

        @property
        def planetary_connector_multi_node_fe_link(
            self: "PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink",
        ) -> "PlanetaryConnectorMultiNodeFELink":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink",
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
        self: Self, instance_to_wrap: "PlanetaryConnectorMultiNodeFELink.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectorMultiNodeFELink._Cast_PlanetaryConnectorMultiNodeFELink":
        return self._Cast_PlanetaryConnectorMultiNodeFELink(self)
