"""CycloidalDiscDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_DESIGN = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CycloidalDiscDesign"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.cycloidal import _1462, _1465


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscDesign",)


Self = TypeVar("Self", bound="CycloidalDiscDesign")


class CycloidalDiscDesign(_0.APIBase):
    """CycloidalDiscDesign

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscDesign")

    class _Cast_CycloidalDiscDesign:
        """Special nested class for casting CycloidalDiscDesign to subclasses."""

        def __init__(
            self: "CycloidalDiscDesign._Cast_CycloidalDiscDesign",
            parent: "CycloidalDiscDesign",
        ):
            self._parent = parent

        @property
        def cycloidal_disc_design(
            self: "CycloidalDiscDesign._Cast_CycloidalDiscDesign",
        ) -> "CycloidalDiscDesign":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscDesign._Cast_CycloidalDiscDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrowningChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def disc_id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiscID

        if temp is None:
            return 0

        return temp

    @property
    def estimated_modifications_from_spline_fit(
        self: Self,
    ) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedModificationsFromSplineFit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def generating_wheel_centre_circle_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeneratingWheelCentreCircleDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def generating_wheel_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeneratingWheelDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def lobe_symmetry_angle_with_no_lobe_modifications(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LobeSymmetryAngleWithNoLobeModifications

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def exporter(self: Self) -> "_1462.CycloidalDiscDesignExporter":
        """mastapy.cycloidal.CycloidalDiscDesignExporter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Exporter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modifications_specification(
        self: Self,
    ) -> "_1465.CycloidalDiscModificationsSpecification":
        """mastapy.cycloidal.CycloidalDiscModificationsSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModificationsSpecification

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
    def cast_to(self: Self) -> "CycloidalDiscDesign._Cast_CycloidalDiscDesign":
        return self._Cast_CycloidalDiscDesign(self)
