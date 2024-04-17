"""FEEntityGroupWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FEEntityGroupWithSelection"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2382, _2408


__docformat__ = "restructuredtext en"
__all__ = ("FEEntityGroupWithSelection",)


Self = TypeVar("Self", bound="FEEntityGroupWithSelection")
TGroup = TypeVar("TGroup")
TGroupContents = TypeVar("TGroupContents")


class FEEntityGroupWithSelection(_0.APIBase, Generic[TGroup, TGroupContents]):
    """FEEntityGroupWithSelection

    This is a mastapy class.

    Generic Types:
        TGroup
        TGroupContents
    """

    TYPE = _FE_ENTITY_GROUP_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEEntityGroupWithSelection")

    class _Cast_FEEntityGroupWithSelection:
        """Special nested class for casting FEEntityGroupWithSelection to subclasses."""

        def __init__(
            self: "FEEntityGroupWithSelection._Cast_FEEntityGroupWithSelection",
            parent: "FEEntityGroupWithSelection",
        ):
            self._parent = parent

        @property
        def element_face_group_with_selection(
            self: "FEEntityGroupWithSelection._Cast_FEEntityGroupWithSelection",
        ) -> "_2382.ElementFaceGroupWithSelection":
            from mastapy.system_model.fe import _2382

            return self._parent._cast(_2382.ElementFaceGroupWithSelection)

        @property
        def node_group_with_selection(
            self: "FEEntityGroupWithSelection._Cast_FEEntityGroupWithSelection",
        ) -> "_2408.NodeGroupWithSelection":
            from mastapy.system_model.fe import _2408

            return self._parent._cast(_2408.NodeGroupWithSelection)

        @property
        def fe_entity_group_with_selection(
            self: "FEEntityGroupWithSelection._Cast_FEEntityGroupWithSelection",
        ) -> "FEEntityGroupWithSelection":
            return self._parent

        def __getattr__(
            self: "FEEntityGroupWithSelection._Cast_FEEntityGroupWithSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEEntityGroupWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def group(self: Self) -> "TGroup":
        """TGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Group

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def add_selection_to_group(self: Self):
        """Method does not return."""
        self.wrapped.AddSelectionToGroup()

    def delete_group(self: Self):
        """Method does not return."""
        self.wrapped.DeleteGroup()

    def select_items(self: Self):
        """Method does not return."""
        self.wrapped.SelectItems()

    @property
    def cast_to(
        self: Self,
    ) -> "FEEntityGroupWithSelection._Cast_FEEntityGroupWithSelection":
        return self._Cast_FEEntityGroupWithSelection(self)
