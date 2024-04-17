"""IndependentMASTACreatedCondensationNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_MASTA_CREATED_CONDENSATION_NODE = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "IndependentMASTACreatedCondensationNode"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _205
    from mastapy.system_model.fe import _2392


__docformat__ = "restructuredtext en"
__all__ = ("IndependentMASTACreatedCondensationNode",)


Self = TypeVar("Self", bound="IndependentMASTACreatedCondensationNode")


class IndependentMASTACreatedCondensationNode(_0.APIBase):
    """IndependentMASTACreatedCondensationNode

    This is a mastapy class.
    """

    TYPE = _INDEPENDENT_MASTA_CREATED_CONDENSATION_NODE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_IndependentMASTACreatedCondensationNode"
    )

    class _Cast_IndependentMASTACreatedCondensationNode:
        """Special nested class for casting IndependentMASTACreatedCondensationNode to subclasses."""

        def __init__(
            self: "IndependentMASTACreatedCondensationNode._Cast_IndependentMASTACreatedCondensationNode",
            parent: "IndependentMASTACreatedCondensationNode",
        ):
            self._parent = parent

        @property
        def independent_masta_created_condensation_node(
            self: "IndependentMASTACreatedCondensationNode._Cast_IndependentMASTACreatedCondensationNode",
        ) -> "IndependentMASTACreatedCondensationNode":
            return self._parent

        def __getattr__(
            self: "IndependentMASTACreatedCondensationNode._Cast_IndependentMASTACreatedCondensationNode",
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
        self: Self, instance_to_wrap: "IndependentMASTACreatedCondensationNode.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rigid_coupling_type(self: Self) -> "_205.RigidCouplingType":
        """mastapy.nodal_analysis.dev_tools_analyses.RigidCouplingType"""
        temp = self.wrapped.RigidCouplingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.RigidCouplingType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis.dev_tools_analyses._205", "RigidCouplingType"
        )(value)

    @rigid_coupling_type.setter
    @enforce_parameter_types
    def rigid_coupling_type(self: Self, value: "_205.RigidCouplingType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.RigidCouplingType"
        )
        self.wrapped.RigidCouplingType = value

    @property
    def fe_substructure_node(self: Self) -> "_2392.FESubstructureNode":
        """mastapy.system_model.fe.FESubstructureNode

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESubstructureNode

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def node_position(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.NodePosition

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @node_position.setter
    @enforce_parameter_types
    def node_position(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.NodePosition = value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @property
    def cast_to(
        self: Self,
    ) -> "IndependentMASTACreatedCondensationNode._Cast_IndependentMASTACreatedCondensationNode":
        return self._Cast_IndependentMASTACreatedCondensationNode(self)
