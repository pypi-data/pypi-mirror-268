"""ConicalGearBendingStiffnessNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_BENDING_STIFFNESS_NODE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalGearBendingStiffnessNode"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _851
    from mastapy.nodal_analysis import _67


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearBendingStiffnessNode",)


Self = TypeVar("Self", bound="ConicalGearBendingStiffnessNode")


class ConicalGearBendingStiffnessNode(_837.GearBendingStiffnessNode):
    """ConicalGearBendingStiffnessNode

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_BENDING_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearBendingStiffnessNode")

    class _Cast_ConicalGearBendingStiffnessNode:
        """Special nested class for casting ConicalGearBendingStiffnessNode to subclasses."""

        def __init__(
            self: "ConicalGearBendingStiffnessNode._Cast_ConicalGearBendingStiffnessNode",
            parent: "ConicalGearBendingStiffnessNode",
        ):
            self._parent = parent

        @property
        def gear_bending_stiffness_node(
            self: "ConicalGearBendingStiffnessNode._Cast_ConicalGearBendingStiffnessNode",
        ) -> "_837.GearBendingStiffnessNode":
            return self._parent._cast(_837.GearBendingStiffnessNode)

        @property
        def gear_stiffness_node(
            self: "ConicalGearBendingStiffnessNode._Cast_ConicalGearBendingStiffnessNode",
        ) -> "_851.GearStiffnessNode":
            from mastapy.gears.ltca import _851

            return self._parent._cast(_851.GearStiffnessNode)

        @property
        def fe_stiffness_node(
            self: "ConicalGearBendingStiffnessNode._Cast_ConicalGearBendingStiffnessNode",
        ) -> "_67.FEStiffnessNode":
            from mastapy.nodal_analysis import _67

            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def conical_gear_bending_stiffness_node(
            self: "ConicalGearBendingStiffnessNode._Cast_ConicalGearBendingStiffnessNode",
        ) -> "ConicalGearBendingStiffnessNode":
            return self._parent

        def __getattr__(
            self: "ConicalGearBendingStiffnessNode._Cast_ConicalGearBendingStiffnessNode",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearBendingStiffnessNode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearBendingStiffnessNode._Cast_ConicalGearBendingStiffnessNode":
        return self._Cast_ConicalGearBendingStiffnessNode(self)
