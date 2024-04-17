"""IndependentResistiveTorque"""

from __future__ import annotations

from typing import TypeVar

from mastapy.materials.efficiency import _306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_RESISTIVE_TORQUE = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "IndependentResistiveTorque"
)


__docformat__ = "restructuredtext en"
__all__ = ("IndependentResistiveTorque",)


Self = TypeVar("Self", bound="IndependentResistiveTorque")


class IndependentResistiveTorque(_306.ResistiveTorque):
    """IndependentResistiveTorque

    This is a mastapy class.
    """

    TYPE = _INDEPENDENT_RESISTIVE_TORQUE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IndependentResistiveTorque")

    class _Cast_IndependentResistiveTorque:
        """Special nested class for casting IndependentResistiveTorque to subclasses."""

        def __init__(
            self: "IndependentResistiveTorque._Cast_IndependentResistiveTorque",
            parent: "IndependentResistiveTorque",
        ):
            self._parent = parent

        @property
        def resistive_torque(
            self: "IndependentResistiveTorque._Cast_IndependentResistiveTorque",
        ) -> "_306.ResistiveTorque":
            return self._parent._cast(_306.ResistiveTorque)

        @property
        def independent_resistive_torque(
            self: "IndependentResistiveTorque._Cast_IndependentResistiveTorque",
        ) -> "IndependentResistiveTorque":
            return self._parent

        def __getattr__(
            self: "IndependentResistiveTorque._Cast_IndependentResistiveTorque",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "IndependentResistiveTorque.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_dependent_resistive_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDependentResistiveTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_dependent_resistive_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedDependentResistiveTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "IndependentResistiveTorque._Cast_IndependentResistiveTorque":
        return self._Cast_IndependentResistiveTorque(self)
