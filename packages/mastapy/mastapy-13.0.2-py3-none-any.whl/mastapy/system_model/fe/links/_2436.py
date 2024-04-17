"""PointLoadFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.fe.links import _2432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "PointLoadFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2425


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadFELink",)


Self = TypeVar("Self", bound="PointLoadFELink")


class PointLoadFELink(_2432.MultiNodeFELink):
    """PointLoadFELink

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadFELink")

    class _Cast_PointLoadFELink:
        """Special nested class for casting PointLoadFELink to subclasses."""

        def __init__(
            self: "PointLoadFELink._Cast_PointLoadFELink", parent: "PointLoadFELink"
        ):
            self._parent = parent

        @property
        def multi_node_fe_link(
            self: "PointLoadFELink._Cast_PointLoadFELink",
        ) -> "_2432.MultiNodeFELink":
            return self._parent._cast(_2432.MultiNodeFELink)

        @property
        def fe_link(self: "PointLoadFELink._Cast_PointLoadFELink") -> "_2425.FELink":
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.FELink)

        @property
        def point_load_fe_link(
            self: "PointLoadFELink._Cast_PointLoadFELink",
        ) -> "PointLoadFELink":
            return self._parent

        def __getattr__(self: "PointLoadFELink._Cast_PointLoadFELink", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PointLoadFELink._Cast_PointLoadFELink":
        return self._Cast_PointLoadFELink(self)
