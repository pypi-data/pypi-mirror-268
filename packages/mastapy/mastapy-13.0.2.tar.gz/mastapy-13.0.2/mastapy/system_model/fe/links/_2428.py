"""GearMeshFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.fe import _2392
from mastapy._internal import constructor
from mastapy.system_model.fe.links import _2430
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "GearMeshFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe.links import _2432, _2425


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshFELink",)


Self = TypeVar("Self", bound="GearMeshFELink")


class GearMeshFELink(_2430.MultiAngleConnectionFELink):
    """GearMeshFELink

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshFELink")

    class _Cast_GearMeshFELink:
        """Special nested class for casting GearMeshFELink to subclasses."""

        def __init__(
            self: "GearMeshFELink._Cast_GearMeshFELink", parent: "GearMeshFELink"
        ):
            self._parent = parent

        @property
        def multi_angle_connection_fe_link(
            self: "GearMeshFELink._Cast_GearMeshFELink",
        ) -> "_2430.MultiAngleConnectionFELink":
            return self._parent._cast(_2430.MultiAngleConnectionFELink)

        @property
        def multi_node_fe_link(
            self: "GearMeshFELink._Cast_GearMeshFELink",
        ) -> "_2432.MultiNodeFELink":
            from mastapy.system_model.fe.links import _2432

            return self._parent._cast(_2432.MultiNodeFELink)

        @property
        def fe_link(self: "GearMeshFELink._Cast_GearMeshFELink") -> "_2425.FELink":
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.FELink)

        @property
        def gear_mesh_fe_link(
            self: "GearMeshFELink._Cast_GearMeshFELink",
        ) -> "GearMeshFELink":
            return self._parent

        def __getattr__(self: "GearMeshFELink._Cast_GearMeshFELink", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reference_fe_substructure_node_for_misalignments(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_FESubstructureNode":
        """ListWithSelectedItem[mastapy.system_model.fe.FESubstructureNode]"""
        temp = self.wrapped.ReferenceFESubstructureNodeForMisalignments

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FESubstructureNode",
        )(temp)

    @reference_fe_substructure_node_for_misalignments.setter
    @enforce_parameter_types
    def reference_fe_substructure_node_for_misalignments(
        self: Self, value: "_2392.FESubstructureNode"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructureNode.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructureNode.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ReferenceFESubstructureNodeForMisalignments = value

    @property
    def use_active_mesh_node_for_reference_fe_substructure_node_for_misalignments(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseActiveMeshNodeForReferenceFESubstructureNodeForMisalignments
        )

        if temp is None:
            return False

        return temp

    @use_active_mesh_node_for_reference_fe_substructure_node_for_misalignments.setter
    @enforce_parameter_types
    def use_active_mesh_node_for_reference_fe_substructure_node_for_misalignments(
        self: Self, value: "bool"
    ):
        self.wrapped.UseActiveMeshNodeForReferenceFESubstructureNodeForMisalignments = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "GearMeshFELink._Cast_GearMeshFELink":
        return self._Cast_GearMeshFELink(self)
