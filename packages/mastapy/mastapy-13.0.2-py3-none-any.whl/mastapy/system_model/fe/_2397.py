"""FESubstructureWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.fe import _2367
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureWithSelection"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2390, _2382, _2408, _2398, _2399, _2400, _2401


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureWithSelection",)


Self = TypeVar("Self", bound="FESubstructureWithSelection")


class FESubstructureWithSelection(_2367.BaseFEWithSelection):
    """FESubstructureWithSelection

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FESubstructureWithSelection")

    class _Cast_FESubstructureWithSelection:
        """Special nested class for casting FESubstructureWithSelection to subclasses."""

        def __init__(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
            parent: "FESubstructureWithSelection",
        ):
            self._parent = parent

        @property
        def base_fe_with_selection(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
        ) -> "_2367.BaseFEWithSelection":
            return self._parent._cast(_2367.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_components(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
        ) -> "_2398.FESubstructureWithSelectionComponents":
            from mastapy.system_model.fe import _2398

            return self._parent._cast(_2398.FESubstructureWithSelectionComponents)

        @property
        def fe_substructure_with_selection_for_harmonic_analysis(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
        ) -> "_2399.FESubstructureWithSelectionForHarmonicAnalysis":
            from mastapy.system_model.fe import _2399

            return self._parent._cast(
                _2399.FESubstructureWithSelectionForHarmonicAnalysis
            )

        @property
        def fe_substructure_with_selection_for_modal_analysis(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
        ) -> "_2400.FESubstructureWithSelectionForModalAnalysis":
            from mastapy.system_model.fe import _2400

            return self._parent._cast(_2400.FESubstructureWithSelectionForModalAnalysis)

        @property
        def fe_substructure_with_selection_for_static_analysis(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
        ) -> "_2401.FESubstructureWithSelectionForStaticAnalysis":
            from mastapy.system_model.fe import _2401

            return self._parent._cast(
                _2401.FESubstructureWithSelectionForStaticAnalysis
            )

        @property
        def fe_substructure_with_selection(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
        ) -> "FESubstructureWithSelection":
            return self._parent

        def __getattr__(
            self: "FESubstructureWithSelection._Cast_FESubstructureWithSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FESubstructureWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_nodes(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedNodes

        if temp is None:
            return ""

        return temp

    @property
    def fe_substructure(self: Self) -> "_2390.FESubstructure":
        """mastapy.system_model.fe.FESubstructure

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESubstructure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def element_face_groups(self: Self) -> "List[_2382.ElementFaceGroupWithSelection]":
        """List[mastapy.system_model.fe.ElementFaceGroupWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementFaceGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def node_groups(self: Self) -> "List[_2408.NodeGroupWithSelection]":
        """List[mastapy.system_model.fe.NodeGroupWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def create_condensation_node_connected_to_current_selection(self: Self):
        """Method does not return."""
        self.wrapped.CreateCondensationNodeConnectedToCurrentSelection()

    def create_element_face_group(self: Self):
        """Method does not return."""
        self.wrapped.CreateElementFaceGroup()

    def create_node_group(self: Self):
        """Method does not return."""
        self.wrapped.CreateNodeGroup()

    def ground_selected_faces(self: Self):
        """Method does not return."""
        self.wrapped.GroundSelectedFaces()

    def remove_grounding_on_selected_faces(self: Self):
        """Method does not return."""
        self.wrapped.RemoveGroundingOnSelectedFaces()

    @property
    def cast_to(
        self: Self,
    ) -> "FESubstructureWithSelection._Cast_FESubstructureWithSelection":
        return self._Cast_FESubstructureWithSelection(self)
