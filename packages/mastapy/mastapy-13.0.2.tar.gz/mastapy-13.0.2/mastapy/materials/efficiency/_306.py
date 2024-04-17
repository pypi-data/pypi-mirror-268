"""ResistiveTorque"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESISTIVE_TORQUE = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "ResistiveTorque"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _296, _299


__docformat__ = "restructuredtext en"
__all__ = ("ResistiveTorque",)


Self = TypeVar("Self", bound="ResistiveTorque")


class ResistiveTorque(_0.APIBase):
    """ResistiveTorque

    This is a mastapy class.
    """

    TYPE = _RESISTIVE_TORQUE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResistiveTorque")

    class _Cast_ResistiveTorque:
        """Special nested class for casting ResistiveTorque to subclasses."""

        def __init__(
            self: "ResistiveTorque._Cast_ResistiveTorque", parent: "ResistiveTorque"
        ):
            self._parent = parent

        @property
        def combined_resistive_torque(
            self: "ResistiveTorque._Cast_ResistiveTorque",
        ) -> "_296.CombinedResistiveTorque":
            from mastapy.materials.efficiency import _296

            return self._parent._cast(_296.CombinedResistiveTorque)

        @property
        def independent_resistive_torque(
            self: "ResistiveTorque._Cast_ResistiveTorque",
        ) -> "_299.IndependentResistiveTorque":
            from mastapy.materials.efficiency import _299

            return self._parent._cast(_299.IndependentResistiveTorque)

        @property
        def resistive_torque(
            self: "ResistiveTorque._Cast_ResistiveTorque",
        ) -> "ResistiveTorque":
            return self._parent

        def __getattr__(self: "ResistiveTorque._Cast_ResistiveTorque", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ResistiveTorque.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_resistive_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalResistiveTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ResistiveTorque._Cast_ResistiveTorque":
        return self._Cast_ResistiveTorque(self)
