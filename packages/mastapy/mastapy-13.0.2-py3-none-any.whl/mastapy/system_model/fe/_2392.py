"""FESubstructureNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.nodal_analysis import _67
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_NODE = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureNode"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_vectors import _1571


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureNode",)


Self = TypeVar("Self", bound="FESubstructureNode")


class FESubstructureNode(_67.FEStiffnessNode):
    """FESubstructureNode

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FESubstructureNode")

    class _Cast_FESubstructureNode:
        """Special nested class for casting FESubstructureNode to subclasses."""

        def __init__(
            self: "FESubstructureNode._Cast_FESubstructureNode",
            parent: "FESubstructureNode",
        ):
            self._parent = parent

        @property
        def fe_stiffness_node(
            self: "FESubstructureNode._Cast_FESubstructureNode",
        ) -> "_67.FEStiffnessNode":
            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def fe_substructure_node(
            self: "FESubstructureNode._Cast_FESubstructureNode",
        ) -> "FESubstructureNode":
            return self._parent

        def __getattr__(self: "FESubstructureNode._Cast_FESubstructureNode", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FESubstructureNode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def external_id(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ExternalID

        if temp is None:
            return 0

        return temp

    @external_id.setter
    @enforce_parameter_types
    def external_id(self: Self, value: "int"):
        self.wrapped.ExternalID = int(value) if value is not None else 0

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def override_default_name(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDefaultName

        if temp is None:
            return False

        return temp

    @override_default_name.setter
    @enforce_parameter_types
    def override_default_name(self: Self, value: "bool"):
        self.wrapped.OverrideDefaultName = bool(value) if value is not None else False

    @property
    def force_due_to_gravity_in_local_coordinate_system(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceDueToGravityInLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_due_to_gravity_in_local_coordinate_system_with_gravity_in_fex_direction(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ForceDueToGravityInLocalCoordinateSystemWithGravityInFEXDirection
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_due_to_gravity_in_local_coordinate_system_with_gravity_in_fey_direction(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ForceDueToGravityInLocalCoordinateSystemWithGravityInFEYDirection
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_due_to_gravity_in_local_coordinate_system_with_gravity_in_fez_direction(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ForceDueToGravityInLocalCoordinateSystemWithGravityInFEZDirection
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def position_in_world_coordinate_system(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionInWorldCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FESubstructureNode._Cast_FESubstructureNode":
        return self._Cast_FESubstructureNode(self)
