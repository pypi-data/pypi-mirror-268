"""FELinkWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_LINK_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "FELinkWithSelection"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2425


__docformat__ = "restructuredtext en"
__all__ = ("FELinkWithSelection",)


Self = TypeVar("Self", bound="FELinkWithSelection")


class FELinkWithSelection(_0.APIBase):
    """FELinkWithSelection

    This is a mastapy class.
    """

    TYPE = _FE_LINK_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FELinkWithSelection")

    class _Cast_FELinkWithSelection:
        """Special nested class for casting FELinkWithSelection to subclasses."""

        def __init__(
            self: "FELinkWithSelection._Cast_FELinkWithSelection",
            parent: "FELinkWithSelection",
        ):
            self._parent = parent

        @property
        def fe_link_with_selection(
            self: "FELinkWithSelection._Cast_FELinkWithSelection",
        ) -> "FELinkWithSelection":
            return self._parent

        def __getattr__(
            self: "FELinkWithSelection._Cast_FELinkWithSelection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FELinkWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def link(self: Self) -> "_2425.FELink":
        """mastapy.system_model.fe.links.FELink

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Link

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def add_selected_nodes(self: Self):
        """Method does not return."""
        self.wrapped.AddSelectedNodes()

    def delete_all_nodes(self: Self):
        """Method does not return."""
        self.wrapped.DeleteAllNodes()

    def select_component(self: Self):
        """Method does not return."""
        self.wrapped.SelectComponent()

    @property
    def cast_to(self: Self) -> "FELinkWithSelection._Cast_FELinkWithSelection":
        return self._Cast_FELinkWithSelection(self)
