"""CombinedResistiveTorque"""

from __future__ import annotations

from typing import TypeVar

from mastapy.materials.efficiency import _306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMBINED_RESISTIVE_TORQUE = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "CombinedResistiveTorque"
)


__docformat__ = "restructuredtext en"
__all__ = ("CombinedResistiveTorque",)


Self = TypeVar("Self", bound="CombinedResistiveTorque")


class CombinedResistiveTorque(_306.ResistiveTorque):
    """CombinedResistiveTorque

    This is a mastapy class.
    """

    TYPE = _COMBINED_RESISTIVE_TORQUE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CombinedResistiveTorque")

    class _Cast_CombinedResistiveTorque:
        """Special nested class for casting CombinedResistiveTorque to subclasses."""

        def __init__(
            self: "CombinedResistiveTorque._Cast_CombinedResistiveTorque",
            parent: "CombinedResistiveTorque",
        ):
            self._parent = parent

        @property
        def resistive_torque(
            self: "CombinedResistiveTorque._Cast_CombinedResistiveTorque",
        ) -> "_306.ResistiveTorque":
            return self._parent._cast(_306.ResistiveTorque)

        @property
        def combined_resistive_torque(
            self: "CombinedResistiveTorque._Cast_CombinedResistiveTorque",
        ) -> "CombinedResistiveTorque":
            return self._parent

        def __getattr__(
            self: "CombinedResistiveTorque._Cast_CombinedResistiveTorque", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CombinedResistiveTorque.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CombinedResistiveTorque._Cast_CombinedResistiveTorque":
        return self._Cast_CombinedResistiveTorque(self)
