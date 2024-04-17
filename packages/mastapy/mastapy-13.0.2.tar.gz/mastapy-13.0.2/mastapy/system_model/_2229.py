"""SystemReporting"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_REPORTING = python_net_import("SMT.MastaAPI.SystemModel", "SystemReporting")

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612


__docformat__ = "restructuredtext en"
__all__ = ("SystemReporting",)


Self = TypeVar("Self", bound="SystemReporting")


class SystemReporting(_0.APIBase):
    """SystemReporting

    This is a mastapy class.
    """

    TYPE = _SYSTEM_REPORTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemReporting")

    class _Cast_SystemReporting:
        """Special nested class for casting SystemReporting to subclasses."""

        def __init__(
            self: "SystemReporting._Cast_SystemReporting", parent: "SystemReporting"
        ):
            self._parent = parent

        @property
        def system_reporting(
            self: "SystemReporting._Cast_SystemReporting",
        ) -> "SystemReporting":
            return self._parent

        def __getattr__(self: "SystemReporting._Cast_SystemReporting", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemReporting.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_date_and_time(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentDateAndTime

        if temp is None:
            return ""

        return temp

    @property
    def current_date_and_time_iso8601(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentDateAndTimeISO8601

        if temp is None:
            return ""

        return temp

    @property
    def masta_version(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MASTAVersion

        if temp is None:
            return ""

        return temp

    @property
    def all_measurements(self: Self) -> "List[_1612.MeasurementBase]":
        """List[mastapy.utility.units_and_measurements.MeasurementBase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllMeasurements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def measurements_not_using_si_unit(self: Self) -> "List[_1612.MeasurementBase]":
        """List[mastapy.utility.units_and_measurements.MeasurementBase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementsNotUsingSIUnit

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SystemReporting._Cast_SystemReporting":
        return self._Cast_SystemReporting(self)
