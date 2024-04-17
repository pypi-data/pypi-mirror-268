"""ShaftPointStressCycleReporting"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_POINT_STRESS_CYCLE_REPORTING = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftPointStressCycleReporting"
)

if TYPE_CHECKING:
    from mastapy.shafts import _28


__docformat__ = "restructuredtext en"
__all__ = ("ShaftPointStressCycleReporting",)


Self = TypeVar("Self", bound="ShaftPointStressCycleReporting")


class ShaftPointStressCycleReporting(_0.APIBase):
    """ShaftPointStressCycleReporting

    This is a mastapy class.
    """

    TYPE = _SHAFT_POINT_STRESS_CYCLE_REPORTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftPointStressCycleReporting")

    class _Cast_ShaftPointStressCycleReporting:
        """Special nested class for casting ShaftPointStressCycleReporting to subclasses."""

        def __init__(
            self: "ShaftPointStressCycleReporting._Cast_ShaftPointStressCycleReporting",
            parent: "ShaftPointStressCycleReporting",
        ):
            self._parent = parent

        @property
        def shaft_point_stress_cycle_reporting(
            self: "ShaftPointStressCycleReporting._Cast_ShaftPointStressCycleReporting",
        ) -> "ShaftPointStressCycleReporting":
            return self._parent

        def __getattr__(
            self: "ShaftPointStressCycleReporting._Cast_ShaftPointStressCycleReporting",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftPointStressCycleReporting.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_alternating_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EquivalentAlternatingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_stress(self: Self) -> "_28.ShaftPointStressCycle":
        """mastapy.shafts.ShaftPointStressCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stress(self: Self) -> "_28.ShaftPointStressCycle":
        """mastapy.shafts.ShaftPointStressCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftPointStressCycleReporting._Cast_ShaftPointStressCycleReporting":
        return self._Cast_ShaftPointStressCycleReporting(self)
