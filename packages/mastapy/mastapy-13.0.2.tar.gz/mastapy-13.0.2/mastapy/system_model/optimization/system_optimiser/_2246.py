"""SystemOptimiser"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.load_case_groups import _5672
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_OPTIMISER = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization.SystemOptimiser", "SystemOptimiser"
)

if TYPE_CHECKING:
    from mastapy.system_model import _2207
    from mastapy.system_model.optimization.system_optimiser import _2247, _2248, _2244
    from mastapy.utility.logging import _1815
    from mastapy.system_model.part_model.gears import _2533, _2539
    from mastapy.gears.rating import _365
    from mastapy.system_model.analyses_and_results.load_case_groups import _5676


__docformat__ = "restructuredtext en"
__all__ = ("SystemOptimiser",)


Self = TypeVar("Self", bound="SystemOptimiser")


class SystemOptimiser(_0.APIBase):
    """SystemOptimiser

    This is a mastapy class.
    """

    TYPE = _SYSTEM_OPTIMISER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemOptimiser")

    class _Cast_SystemOptimiser:
        """Special nested class for casting SystemOptimiser to subclasses."""

        def __init__(
            self: "SystemOptimiser._Cast_SystemOptimiser", parent: "SystemOptimiser"
        ):
            self._parent = parent

        @property
        def system_optimiser(
            self: "SystemOptimiser._Cast_SystemOptimiser",
        ) -> "SystemOptimiser":
            return self._parent

        def __getattr__(self: "SystemOptimiser._Cast_SystemOptimiser", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemOptimiser.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_duty_cycle_for_system_optimiser(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_DutyCycle":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle]"""
        temp = self.wrapped.SelectedDutyCycleForSystemOptimiser

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_DutyCycle",
        )(temp)

    @selected_duty_cycle_for_system_optimiser.setter
    @enforce_parameter_types
    def selected_duty_cycle_for_system_optimiser(self: Self, value: "_5672.DutyCycle"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_DutyCycle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_DutyCycle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectedDutyCycleForSystemOptimiser = value

    @property
    def design(self: Self) -> "_2207.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def details(self: Self) -> "_2247.SystemOptimiserDetails":
        """mastapy.system_model.optimization.system_optimiser.SystemOptimiserDetails

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Details

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def log(self: Self) -> "_1815.Logger":
        """mastapy.utility.logging.Logger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Log

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_number_finder(self: Self) -> "_2248.ToothNumberFinder":
        """mastapy.system_model.optimization.system_optimiser.ToothNumberFinder

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothNumberFinder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_sets(self: Self) -> "List[_2533.CylindricalGearSet]":
        """List[mastapy.system_model.part_model.gears.CylindricalGearSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set_ratings_fast_power_flow(
        self: Self,
    ) -> "List[_365.GearSetDutyCycleRating]":
        """List[mastapy.gears.rating.GearSetDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetRatingsFastPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_sets(self: Self) -> "List[_2539.GearSet]":
        """List[mastapy.system_model.part_model.gears.GearSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_optimisation_gear_sets(
        self: Self,
    ) -> "List[_5676.SystemOptimisationGearSet]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.SystemOptimisationGearSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemOptimisationGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def target_ratios(self: Self) -> "List[_2244.DesignStateTargetRatio]":
        """List[mastapy.system_model.optimization.system_optimiser.DesignStateTargetRatio]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TargetRatios

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_optimiser_duty_cycle(self: Self) -> "_5672.DutyCycle":
        """mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle"""
        temp = self.wrapped.SystemOptimiserDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @system_optimiser_duty_cycle.setter
    @enforce_parameter_types
    def system_optimiser_duty_cycle(self: Self, value: "_5672.DutyCycle"):
        self.wrapped.SystemOptimiserDutyCycle = value.wrapped

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
    def cast_to(self: Self) -> "SystemOptimiser._Cast_SystemOptimiser":
        return self._Cast_SystemOptimiser(self)
