"""GearSetOptimisationResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List
from datetime import datetime

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISATION_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears", "GearSetOptimisationResults"
)

if TYPE_CHECKING:
    from mastapy.gears import _333


__docformat__ = "restructuredtext en"
__all__ = ("GearSetOptimisationResults",)


Self = TypeVar("Self", bound="GearSetOptimisationResults")


class GearSetOptimisationResults(_0.APIBase):
    """GearSetOptimisationResults

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISATION_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetOptimisationResults")

    class _Cast_GearSetOptimisationResults:
        """Special nested class for casting GearSetOptimisationResults to subclasses."""

        def __init__(
            self: "GearSetOptimisationResults._Cast_GearSetOptimisationResults",
            parent: "GearSetOptimisationResults",
        ):
            self._parent = parent

        @property
        def gear_set_optimisation_results(
            self: "GearSetOptimisationResults._Cast_GearSetOptimisationResults",
        ) -> "GearSetOptimisationResults":
            return self._parent

        def __getattr__(
            self: "GearSetOptimisationResults._Cast_GearSetOptimisationResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetOptimisationResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def optimiser_settings_report_table(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OptimiserSettingsReportTable

        if temp is None:
            return ""

        return temp

    @property
    def report(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Report

        if temp is None:
            return ""

        return temp

    @property
    def results(self: Self) -> "List[_333.GearSetOptimisationResult]":
        """List[mastapy.gears.GearSetOptimisationResult]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def run_time(self: Self) -> "datetime":
        """datetime

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunTime

        if temp is None:
            return None

        value = conversion.pn_to_mp_datetime(temp)

        if value is None:
            return None

        return value

    def delete_all_results(self: Self):
        """Method does not return."""
        self.wrapped.DeleteAllResults()

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetOptimisationResults._Cast_GearSetOptimisationResults":
        return self._Cast_GearSetOptimisationResults(self)
