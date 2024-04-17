"""DataFromMotorPackagePerSpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_FROM_MOTOR_PACKAGE_PER_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "DataFromMotorPackagePerSpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6876


__docformat__ = "restructuredtext en"
__all__ = ("DataFromMotorPackagePerSpeed",)


Self = TypeVar("Self", bound="DataFromMotorPackagePerSpeed")


class DataFromMotorPackagePerSpeed(_0.APIBase):
    """DataFromMotorPackagePerSpeed

    This is a mastapy class.
    """

    TYPE = _DATA_FROM_MOTOR_PACKAGE_PER_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataFromMotorPackagePerSpeed")

    class _Cast_DataFromMotorPackagePerSpeed:
        """Special nested class for casting DataFromMotorPackagePerSpeed to subclasses."""

        def __init__(
            self: "DataFromMotorPackagePerSpeed._Cast_DataFromMotorPackagePerSpeed",
            parent: "DataFromMotorPackagePerSpeed",
        ):
            self._parent = parent

        @property
        def data_from_motor_package_per_speed(
            self: "DataFromMotorPackagePerSpeed._Cast_DataFromMotorPackagePerSpeed",
        ) -> "DataFromMotorPackagePerSpeed":
            return self._parent

        def __getattr__(
            self: "DataFromMotorPackagePerSpeed._Cast_DataFromMotorPackagePerSpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataFromMotorPackagePerSpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Include

        if temp is None:
            return False

        return temp

    @include.setter
    @enforce_parameter_types
    def include(self: Self, value: "bool"):
        self.wrapped.Include = bool(value) if value is not None else False

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_selector(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_float":
        """ListWithSelectedItem[float]"""
        temp = self.wrapped.TorqueSelector

        if temp is None:
            return 0.0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_float",
        )(temp)

    @torque_selector.setter
    @enforce_parameter_types
    def torque_selector(self: Self, value: "float"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0
        )
        self.wrapped.TorqueSelector = value

    @property
    def data_per_mean_torque(
        self: Self,
    ) -> "List[_6876.DataFromMotorPackagePerMeanTorque]":
        """List[mastapy.system_model.analyses_and_results.static_loads.DataFromMotorPackagePerMeanTorque]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataPerMeanTorque

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    ) -> "DataFromMotorPackagePerSpeed._Cast_DataFromMotorPackagePerSpeed":
        return self._Cast_DataFromMotorPackagePerSpeed(self)
