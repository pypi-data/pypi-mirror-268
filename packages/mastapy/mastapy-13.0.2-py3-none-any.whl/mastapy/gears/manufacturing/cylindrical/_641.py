"""SuitableCutterSetup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUITABLE_CUTTER_SETUP = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "SuitableCutterSetup"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _725
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _744


__docformat__ = "restructuredtext en"
__all__ = ("SuitableCutterSetup",)


Self = TypeVar("Self", bound="SuitableCutterSetup")


class SuitableCutterSetup(_0.APIBase):
    """SuitableCutterSetup

    This is a mastapy class.
    """

    TYPE = _SUITABLE_CUTTER_SETUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SuitableCutterSetup")

    class _Cast_SuitableCutterSetup:
        """Special nested class for casting SuitableCutterSetup to subclasses."""

        def __init__(
            self: "SuitableCutterSetup._Cast_SuitableCutterSetup",
            parent: "SuitableCutterSetup",
        ):
            self._parent = parent

        @property
        def suitable_cutter_setup(
            self: "SuitableCutterSetup._Cast_SuitableCutterSetup",
        ) -> "SuitableCutterSetup":
            return self._parent

        def __getattr__(
            self: "SuitableCutterSetup._Cast_SuitableCutterSetup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SuitableCutterSetup.TYPE"):
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
    def rough_cutter_creation_settings(
        self: Self,
    ) -> "_725.RoughCutterCreationSettings":
        """mastapy.gears.manufacturing.cylindrical.cutters.RoughCutterCreationSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughCutterCreationSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tool_clearances(self: Self) -> "_744.ManufacturingOperationConstraints":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.ManufacturingOperationConstraints

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToolClearances

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
    def cast_to(self: Self) -> "SuitableCutterSetup._Cast_SuitableCutterSetup":
        return self._Cast_SuitableCutterSetup(self)
