"""DutyCycleResultsForSingleShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_SINGLE_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "DutyCycleResultsForSingleShaft",
)

if TYPE_CHECKING:
    from mastapy.shafts import _19


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycleResultsForSingleShaft",)


Self = TypeVar("Self", bound="DutyCycleResultsForSingleShaft")


class DutyCycleResultsForSingleShaft(_0.APIBase):
    """DutyCycleResultsForSingleShaft

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_RESULTS_FOR_SINGLE_SHAFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycleResultsForSingleShaft")

    class _Cast_DutyCycleResultsForSingleShaft:
        """Special nested class for casting DutyCycleResultsForSingleShaft to subclasses."""

        def __init__(
            self: "DutyCycleResultsForSingleShaft._Cast_DutyCycleResultsForSingleShaft",
            parent: "DutyCycleResultsForSingleShaft",
        ):
            self._parent = parent

        @property
        def duty_cycle_results_for_single_shaft(
            self: "DutyCycleResultsForSingleShaft._Cast_DutyCycleResultsForSingleShaft",
        ) -> "DutyCycleResultsForSingleShaft":
            return self._parent

        def __getattr__(
            self: "DutyCycleResultsForSingleShaft._Cast_DutyCycleResultsForSingleShaft",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCycleResultsForSingleShaft.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_results(self: Self) -> "_19.ShaftDamageResults":
        """mastapy.shafts.ShaftDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DutyCycleResultsForSingleShaft._Cast_DutyCycleResultsForSingleShaft":
        return self._Cast_DutyCycleResultsForSingleShaft(self)
