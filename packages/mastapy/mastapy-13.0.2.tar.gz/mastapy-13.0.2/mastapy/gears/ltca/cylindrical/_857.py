"""CylindricalGearContactStiffnessNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.ltca import _839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_CONTACT_STIFFNESS_NODE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearContactStiffnessNode"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _851
    from mastapy.nodal_analysis import _67


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearContactStiffnessNode",)


Self = TypeVar("Self", bound="CylindricalGearContactStiffnessNode")


class CylindricalGearContactStiffnessNode(_839.GearContactStiffnessNode):
    """CylindricalGearContactStiffnessNode

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_CONTACT_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearContactStiffnessNode")

    class _Cast_CylindricalGearContactStiffnessNode:
        """Special nested class for casting CylindricalGearContactStiffnessNode to subclasses."""

        def __init__(
            self: "CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode",
            parent: "CylindricalGearContactStiffnessNode",
        ):
            self._parent = parent

        @property
        def gear_contact_stiffness_node(
            self: "CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode",
        ) -> "_839.GearContactStiffnessNode":
            return self._parent._cast(_839.GearContactStiffnessNode)

        @property
        def gear_stiffness_node(
            self: "CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode",
        ) -> "_851.GearStiffnessNode":
            from mastapy.gears.ltca import _851

            return self._parent._cast(_851.GearStiffnessNode)

        @property
        def fe_stiffness_node(
            self: "CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode",
        ) -> "_67.FEStiffnessNode":
            from mastapy.nodal_analysis import _67

            return self._parent._cast(_67.FEStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(
            self: "CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode",
        ) -> "CylindricalGearContactStiffnessNode":
            return self._parent

        def __getattr__(
            self: "CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode",
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
        self: Self, instance_to_wrap: "CylindricalGearContactStiffnessNode.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearContactStiffnessNode._Cast_CylindricalGearContactStiffnessNode"
    ):
        return self._Cast_CylindricalGearContactStiffnessNode(self)
