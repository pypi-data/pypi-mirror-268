"""SingleNodeFELink"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.fe.links import _2425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_NODE_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "SingleNodeFELink"
)


__docformat__ = "restructuredtext en"
__all__ = ("SingleNodeFELink",)


Self = TypeVar("Self", bound="SingleNodeFELink")


class SingleNodeFELink(_2425.FELink):
    """SingleNodeFELink

    This is a mastapy class.
    """

    TYPE = _SINGLE_NODE_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SingleNodeFELink")

    class _Cast_SingleNodeFELink:
        """Special nested class for casting SingleNodeFELink to subclasses."""

        def __init__(
            self: "SingleNodeFELink._Cast_SingleNodeFELink", parent: "SingleNodeFELink"
        ):
            self._parent = parent

        @property
        def fe_link(self: "SingleNodeFELink._Cast_SingleNodeFELink") -> "_2425.FELink":
            return self._parent._cast(_2425.FELink)

        @property
        def single_node_fe_link(
            self: "SingleNodeFELink._Cast_SingleNodeFELink",
        ) -> "SingleNodeFELink":
            return self._parent

        def __getattr__(self: "SingleNodeFELink._Cast_SingleNodeFELink", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SingleNodeFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SingleNodeFELink._Cast_SingleNodeFELink":
        return self._Cast_SingleNodeFELink(self)
