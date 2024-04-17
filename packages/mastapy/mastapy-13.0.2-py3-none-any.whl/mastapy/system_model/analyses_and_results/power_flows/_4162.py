"""ToothPassingHarmonic"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_PASSING_HARMONIC = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ToothPassingHarmonic"
)


__docformat__ = "restructuredtext en"
__all__ = ("ToothPassingHarmonic",)


Self = TypeVar("Self", bound="ToothPassingHarmonic")


class ToothPassingHarmonic(_0.APIBase):
    """ToothPassingHarmonic

    This is a mastapy class.
    """

    TYPE = _TOOTH_PASSING_HARMONIC
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothPassingHarmonic")

    class _Cast_ToothPassingHarmonic:
        """Special nested class for casting ToothPassingHarmonic to subclasses."""

        def __init__(
            self: "ToothPassingHarmonic._Cast_ToothPassingHarmonic",
            parent: "ToothPassingHarmonic",
        ):
            self._parent = parent

        @property
        def tooth_passing_harmonic(
            self: "ToothPassingHarmonic._Cast_ToothPassingHarmonic",
        ) -> "ToothPassingHarmonic":
            return self._parent

        def __getattr__(
            self: "ToothPassingHarmonic._Cast_ToothPassingHarmonic", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ToothPassingHarmonic.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicName

        if temp is None:
            return ""

        return temp

    @property
    def order(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Order

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency_at_reference_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingFrequencyAtReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ToothPassingHarmonic._Cast_ToothPassingHarmonic":
        return self._Cast_ToothPassingHarmonic(self)
