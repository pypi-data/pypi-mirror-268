"""CycloidalDiscDesignExporter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_DESIGN_EXPORTER = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CycloidalDiscDesignExporter"
)

if TYPE_CHECKING:
    from mastapy.cycloidal import _1467


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscDesignExporter",)


Self = TypeVar("Self", bound="CycloidalDiscDesignExporter")


class CycloidalDiscDesignExporter(_0.APIBase):
    """CycloidalDiscDesignExporter

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_DESIGN_EXPORTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscDesignExporter")

    class _Cast_CycloidalDiscDesignExporter:
        """Special nested class for casting CycloidalDiscDesignExporter to subclasses."""

        def __init__(
            self: "CycloidalDiscDesignExporter._Cast_CycloidalDiscDesignExporter",
            parent: "CycloidalDiscDesignExporter",
        ):
            self._parent = parent

        @property
        def cycloidal_disc_design_exporter(
            self: "CycloidalDiscDesignExporter._Cast_CycloidalDiscDesignExporter",
        ) -> "CycloidalDiscDesignExporter":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscDesignExporter._Cast_CycloidalDiscDesignExporter",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscDesignExporter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_to_export(self: Self) -> "_1467.GeometryToExport":
        """mastapy.cycloidal.GeometryToExport"""
        temp = self.wrapped.GeometryToExport

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Cycloidal.GeometryToExport"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.cycloidal._1467", "GeometryToExport"
        )(value)

    @geometry_to_export.setter
    @enforce_parameter_types
    def geometry_to_export(self: Self, value: "_1467.GeometryToExport"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Cycloidal.GeometryToExport"
        )
        self.wrapped.GeometryToExport = value

    @property
    def include_modifications(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeModifications

        if temp is None:
            return False

        return temp

    @include_modifications.setter
    @enforce_parameter_types
    def include_modifications(self: Self, value: "bool"):
        self.wrapped.IncludeModifications = bool(value) if value is not None else False

    @property
    def number_of_half_lobe_points_for_export(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfHalfLobePointsForExport

        if temp is None:
            return 0

        return temp

    @number_of_half_lobe_points_for_export.setter
    @enforce_parameter_types
    def number_of_half_lobe_points_for_export(self: Self, value: "int"):
        self.wrapped.NumberOfHalfLobePointsForExport = (
            int(value) if value is not None else 0
        )

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
    def profile_points(
        self: Self,
        geometry_to_export: "_1467.GeometryToExport",
        include_modifications_in_export: "bool",
        number_of_half_lobe_points_for_export: "int",
    ) -> "List[Vector2D]":
        """List[Vector2D]

        Args:
            geometry_to_export (mastapy.cycloidal.GeometryToExport)
            include_modifications_in_export (bool)
            number_of_half_lobe_points_for_export (int)
        """
        geometry_to_export = conversion.mp_to_pn_enum(
            geometry_to_export, "SMT.MastaAPI.Cycloidal.GeometryToExport"
        )
        include_modifications_in_export = bool(include_modifications_in_export)
        number_of_half_lobe_points_for_export = int(
            number_of_half_lobe_points_for_export
        )
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.ProfilePoints(
                geometry_to_export,
                (
                    include_modifications_in_export
                    if include_modifications_in_export
                    else False
                ),
                (
                    number_of_half_lobe_points_for_export
                    if number_of_half_lobe_points_for_export
                    else 0
                ),
            ),
            Vector2D,
        )

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
    ) -> "CycloidalDiscDesignExporter._Cast_CycloidalDiscDesignExporter":
        return self._Cast_CycloidalDiscDesignExporter(self)
