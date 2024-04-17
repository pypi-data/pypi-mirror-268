"""NamedDiscPhase"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DISC_PHASE = python_net_import("SMT.MastaAPI.Cycloidal", "NamedDiscPhase")


__docformat__ = "restructuredtext en"
__all__ = ("NamedDiscPhase",)


Self = TypeVar("Self", bound="NamedDiscPhase")


class NamedDiscPhase(_0.APIBase):
    """NamedDiscPhase

    This is a mastapy class.
    """

    TYPE = _NAMED_DISC_PHASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedDiscPhase")

    class _Cast_NamedDiscPhase:
        """Special nested class for casting NamedDiscPhase to subclasses."""

        def __init__(
            self: "NamedDiscPhase._Cast_NamedDiscPhase", parent: "NamedDiscPhase"
        ):
            self._parent = parent

        @property
        def named_disc_phase(
            self: "NamedDiscPhase._Cast_NamedDiscPhase",
        ) -> "NamedDiscPhase":
            return self._parent

        def __getattr__(self: "NamedDiscPhase._Cast_NamedDiscPhase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedDiscPhase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def disc_phase_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiscPhaseAngle

        if temp is None:
            return 0.0

        return temp

    @disc_phase_angle.setter
    @enforce_parameter_types
    def disc_phase_angle(self: Self, value: "float"):
        self.wrapped.DiscPhaseAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "NamedDiscPhase._Cast_NamedDiscPhase":
        return self._Cast_NamedDiscPhase(self)
