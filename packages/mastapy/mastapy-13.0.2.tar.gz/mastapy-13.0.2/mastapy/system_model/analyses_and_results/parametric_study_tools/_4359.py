"""DutyCycleResultsForAllGearSets"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_ALL_GEAR_SETS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "DutyCycleResultsForAllGearSets",
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1233


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycleResultsForAllGearSets",)


Self = TypeVar("Self", bound="DutyCycleResultsForAllGearSets")


class DutyCycleResultsForAllGearSets(_0.APIBase):
    """DutyCycleResultsForAllGearSets

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_RESULTS_FOR_ALL_GEAR_SETS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycleResultsForAllGearSets")

    class _Cast_DutyCycleResultsForAllGearSets:
        """Special nested class for casting DutyCycleResultsForAllGearSets to subclasses."""

        def __init__(
            self: "DutyCycleResultsForAllGearSets._Cast_DutyCycleResultsForAllGearSets",
            parent: "DutyCycleResultsForAllGearSets",
        ):
            self._parent = parent

        @property
        def duty_cycle_results_for_all_gear_sets(
            self: "DutyCycleResultsForAllGearSets._Cast_DutyCycleResultsForAllGearSets",
        ) -> "DutyCycleResultsForAllGearSets":
            return self._parent

        def __getattr__(
            self: "DutyCycleResultsForAllGearSets._Cast_DutyCycleResultsForAllGearSets",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCycleResultsForAllGearSets.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_results(self: Self) -> "_1233.GearSetGroupDutyCycle":
        """mastapy.gears.analysis.GearSetGroupDutyCycle

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
    ) -> "DutyCycleResultsForAllGearSets._Cast_DutyCycleResultsForAllGearSets":
        return self._Cast_DutyCycleResultsForAllGearSets(self)
