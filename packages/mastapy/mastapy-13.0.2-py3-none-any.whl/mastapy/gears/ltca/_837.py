"""GearBendingStiffnessNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_BENDING_STIFFNESS_NODE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearBendingStiffnessNode"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _855
    from mastapy.gears.ltca.conical import _867
    from mastapy.nodal_analysis import _67


__docformat__ = "restructuredtext en"
__all__ = ("GearBendingStiffnessNode",)


Self = TypeVar("Self", bound="GearBendingStiffnessNode")


class GearBendingStiffnessNode(_851.GearStiffnessNode):
    """GearBendingStiffnessNode

    This is a mastapy class.
    """

    TYPE = _GEAR_BENDING_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearBendingStiffnessNode")

    class _Cast_GearBendingStiffnessNode:
        """Special nested class for casting GearBendingStiffnessNode to subclasses."""

        def __init__(
            self: "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode",
            parent: "GearBendingStiffnessNode",
        ):
            self._parent = parent

        @property
        def gear_stiffness_node(
            self: "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode",
        ) -> "_851.GearStiffnessNode":
            return self._parent._cast(_851.GearStiffnessNode)

        @property
        def fe_stiffness_node(
            self: "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode",
        ) -> "_67.FEStiffnessNode":
            from mastapy.nodal_analysis import _67

            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(
            self: "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode",
        ) -> "_855.CylindricalGearBendingStiffnessNode":
            from mastapy.gears.ltca.cylindrical import _855

            return self._parent._cast(_855.CylindricalGearBendingStiffnessNode)

        @property
        def conical_gear_bending_stiffness_node(
            self: "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode",
        ) -> "_867.ConicalGearBendingStiffnessNode":
            from mastapy.gears.ltca.conical import _867

            return self._parent._cast(_867.ConicalGearBendingStiffnessNode)

        @property
        def gear_bending_stiffness_node(
            self: "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode",
        ) -> "GearBendingStiffnessNode":
            return self._parent

        def __getattr__(
            self: "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearBendingStiffnessNode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearBendingStiffnessNode._Cast_GearBendingStiffnessNode":
        return self._Cast_GearBendingStiffnessNode(self)
