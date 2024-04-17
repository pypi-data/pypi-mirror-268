"""InitialFill"""

from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling.skf_module import _2103
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INITIAL_FILL = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "InitialFill"
)


__docformat__ = "restructuredtext en"
__all__ = ("InitialFill",)


Self = TypeVar("Self", bound="InitialFill")


class InitialFill(_2103.SKFCalculationResult):
    """InitialFill

    This is a mastapy class.
    """

    TYPE = _INITIAL_FILL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InitialFill")

    class _Cast_InitialFill:
        """Special nested class for casting InitialFill to subclasses."""

        def __init__(self: "InitialFill._Cast_InitialFill", parent: "InitialFill"):
            self._parent = parent

        @property
        def skf_calculation_result(
            self: "InitialFill._Cast_InitialFill",
        ) -> "_2103.SKFCalculationResult":
            return self._parent._cast(_2103.SKFCalculationResult)

        @property
        def initial_fill(self: "InitialFill._Cast_InitialFill") -> "InitialFill":
            return self._parent

        def __getattr__(self: "InitialFill._Cast_InitialFill", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InitialFill.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Ring

        if temp is None:
            return 0.0

        return temp

    @property
    def side(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Side

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "InitialFill._Cast_InitialFill":
        return self._Cast_InitialFill(self)
