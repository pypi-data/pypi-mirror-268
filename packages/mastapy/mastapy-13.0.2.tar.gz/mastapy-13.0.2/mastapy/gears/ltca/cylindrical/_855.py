"""CylindricalGearBendingStiffnessNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BENDING_STIFFNESS_NODE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearBendingStiffnessNode"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _851
    from mastapy.nodal_analysis import _67


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearBendingStiffnessNode",)


Self = TypeVar("Self", bound="CylindricalGearBendingStiffnessNode")


class CylindricalGearBendingStiffnessNode(_837.GearBendingStiffnessNode):
    """CylindricalGearBendingStiffnessNode

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BENDING_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearBendingStiffnessNode")

    class _Cast_CylindricalGearBendingStiffnessNode:
        """Special nested class for casting CylindricalGearBendingStiffnessNode to subclasses."""

        def __init__(
            self: "CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode",
            parent: "CylindricalGearBendingStiffnessNode",
        ):
            self._parent = parent

        @property
        def gear_bending_stiffness_node(
            self: "CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode",
        ) -> "_837.GearBendingStiffnessNode":
            return self._parent._cast(_837.GearBendingStiffnessNode)

        @property
        def gear_stiffness_node(
            self: "CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode",
        ) -> "_851.GearStiffnessNode":
            from mastapy.gears.ltca import _851

            return self._parent._cast(_851.GearStiffnessNode)

        @property
        def fe_stiffness_node(
            self: "CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode",
        ) -> "_67.FEStiffnessNode":
            from mastapy.nodal_analysis import _67

            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(
            self: "CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode",
        ) -> "CylindricalGearBendingStiffnessNode":
            return self._parent

        def __getattr__(
            self: "CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode",
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
        self: Self, instance_to_wrap: "CylindricalGearBendingStiffnessNode.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearBendingStiffnessNode._Cast_CylindricalGearBendingStiffnessNode"
    ):
        return self._Cast_CylindricalGearBendingStiffnessNode(self)
