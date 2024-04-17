"""DutyCycleResultsForSingleBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_SINGLE_BEARING = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "DutyCycleResultsForSingleBearing",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1955


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycleResultsForSingleBearing",)


Self = TypeVar("Self", bound="DutyCycleResultsForSingleBearing")


class DutyCycleResultsForSingleBearing(_0.APIBase):
    """DutyCycleResultsForSingleBearing

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_RESULTS_FOR_SINGLE_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycleResultsForSingleBearing")

    class _Cast_DutyCycleResultsForSingleBearing:
        """Special nested class for casting DutyCycleResultsForSingleBearing to subclasses."""

        def __init__(
            self: "DutyCycleResultsForSingleBearing._Cast_DutyCycleResultsForSingleBearing",
            parent: "DutyCycleResultsForSingleBearing",
        ):
            self._parent = parent

        @property
        def duty_cycle_results_for_single_bearing(
            self: "DutyCycleResultsForSingleBearing._Cast_DutyCycleResultsForSingleBearing",
        ) -> "DutyCycleResultsForSingleBearing":
            return self._parent

        def __getattr__(
            self: "DutyCycleResultsForSingleBearing._Cast_DutyCycleResultsForSingleBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCycleResultsForSingleBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_results(self: Self) -> "_1955.LoadedBearingDutyCycle":
        """mastapy.bearings.bearing_results.LoadedBearingDutyCycle

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
    ) -> "DutyCycleResultsForSingleBearing._Cast_DutyCycleResultsForSingleBearing":
        return self._Cast_DutyCycleResultsForSingleBearing(self)
