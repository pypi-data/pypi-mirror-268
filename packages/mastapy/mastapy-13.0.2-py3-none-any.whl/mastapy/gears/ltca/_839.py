"""GearContactStiffnessNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CONTACT_STIFFNESS_NODE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearContactStiffnessNode"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _857
    from mastapy.gears.ltca.conical import _869
    from mastapy.nodal_analysis import _67


__docformat__ = "restructuredtext en"
__all__ = ("GearContactStiffnessNode",)


Self = TypeVar("Self", bound="GearContactStiffnessNode")


class GearContactStiffnessNode(_851.GearStiffnessNode):
    """GearContactStiffnessNode

    This is a mastapy class.
    """

    TYPE = _GEAR_CONTACT_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearContactStiffnessNode")

    class _Cast_GearContactStiffnessNode:
        """Special nested class for casting GearContactStiffnessNode to subclasses."""

        def __init__(
            self: "GearContactStiffnessNode._Cast_GearContactStiffnessNode",
            parent: "GearContactStiffnessNode",
        ):
            self._parent = parent

        @property
        def gear_stiffness_node(
            self: "GearContactStiffnessNode._Cast_GearContactStiffnessNode",
        ) -> "_851.GearStiffnessNode":
            return self._parent._cast(_851.GearStiffnessNode)

        @property
        def fe_stiffness_node(
            self: "GearContactStiffnessNode._Cast_GearContactStiffnessNode",
        ) -> "_67.FEStiffnessNode":
            from mastapy.nodal_analysis import _67

            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(
            self: "GearContactStiffnessNode._Cast_GearContactStiffnessNode",
        ) -> "_857.CylindricalGearContactStiffnessNode":
            from mastapy.gears.ltca.cylindrical import _857

            return self._parent._cast(_857.CylindricalGearContactStiffnessNode)

        @property
        def conical_gear_contact_stiffness_node(
            self: "GearContactStiffnessNode._Cast_GearContactStiffnessNode",
        ) -> "_869.ConicalGearContactStiffnessNode":
            from mastapy.gears.ltca.conical import _869

            return self._parent._cast(_869.ConicalGearContactStiffnessNode)

        @property
        def gear_contact_stiffness_node(
            self: "GearContactStiffnessNode._Cast_GearContactStiffnessNode",
        ) -> "GearContactStiffnessNode":
            return self._parent

        def __getattr__(
            self: "GearContactStiffnessNode._Cast_GearContactStiffnessNode", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearContactStiffnessNode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearContactStiffnessNode._Cast_GearContactStiffnessNode":
        return self._Cast_GearContactStiffnessNode(self)
