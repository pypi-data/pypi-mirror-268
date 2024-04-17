"""GearStiffnessNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis import _67
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_STIFFNESS_NODE = python_net_import("SMT.MastaAPI.Gears.LTCA", "GearStiffnessNode")

if TYPE_CHECKING:
    from mastapy.gears.ltca import _837, _839
    from mastapy.gears.ltca.cylindrical import _855, _857
    from mastapy.gears.ltca.conical import _867, _869


__docformat__ = "restructuredtext en"
__all__ = ("GearStiffnessNode",)


Self = TypeVar("Self", bound="GearStiffnessNode")


class GearStiffnessNode(_67.FEStiffnessNode):
    """GearStiffnessNode

    This is a mastapy class.
    """

    TYPE = _GEAR_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearStiffnessNode")

    class _Cast_GearStiffnessNode:
        """Special nested class for casting GearStiffnessNode to subclasses."""

        def __init__(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
            parent: "GearStiffnessNode",
        ):
            self._parent = parent

        @property
        def fe_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "_67.FEStiffnessNode":
            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def gear_bending_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "_837.GearBendingStiffnessNode":
            from mastapy.gears.ltca import _837

            return self._parent._cast(_837.GearBendingStiffnessNode)

        @property
        def gear_contact_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "_839.GearContactStiffnessNode":
            from mastapy.gears.ltca import _839

            return self._parent._cast(_839.GearContactStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "_855.CylindricalGearBendingStiffnessNode":
            from mastapy.gears.ltca.cylindrical import _855

            return self._parent._cast(_855.CylindricalGearBendingStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "_857.CylindricalGearContactStiffnessNode":
            from mastapy.gears.ltca.cylindrical import _857

            return self._parent._cast(_857.CylindricalGearContactStiffnessNode)

        @property
        def conical_gear_bending_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "_867.ConicalGearBendingStiffnessNode":
            from mastapy.gears.ltca.conical import _867

            return self._parent._cast(_867.ConicalGearBendingStiffnessNode)

        @property
        def conical_gear_contact_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "_869.ConicalGearContactStiffnessNode":
            from mastapy.gears.ltca.conical import _869

            return self._parent._cast(_869.ConicalGearContactStiffnessNode)

        @property
        def gear_stiffness_node(
            self: "GearStiffnessNode._Cast_GearStiffnessNode",
        ) -> "GearStiffnessNode":
            return self._parent

        def __getattr__(self: "GearStiffnessNode._Cast_GearStiffnessNode", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearStiffnessNode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearStiffnessNode._Cast_GearStiffnessNode":
        return self._Cast_GearStiffnessNode(self)
