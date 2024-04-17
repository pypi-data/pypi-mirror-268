"""GeometryModellerDimensions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_DIMENSIONS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "GeometryModellerDimensions"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.geometry_modeller_link import (
        _158,
        _156,
        _157,
        _162,
        _164,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GeometryModellerDimensions",)


Self = TypeVar("Self", bound="GeometryModellerDimensions")


class GeometryModellerDimensions(_0.APIBase):
    """GeometryModellerDimensions

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_DIMENSIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GeometryModellerDimensions")

    class _Cast_GeometryModellerDimensions:
        """Special nested class for casting GeometryModellerDimensions to subclasses."""

        def __init__(
            self: "GeometryModellerDimensions._Cast_GeometryModellerDimensions",
            parent: "GeometryModellerDimensions",
        ):
            self._parent = parent

        @property
        def geometry_modeller_dimensions(
            self: "GeometryModellerDimensions._Cast_GeometryModellerDimensions",
        ) -> "GeometryModellerDimensions":
            return self._parent

        def __getattr__(
            self: "GeometryModellerDimensions._Cast_GeometryModellerDimensions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GeometryModellerDimensions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_modeller_design_information(
        self: Self,
    ) -> "_158.GeometryModellerDesignInformation":
        """mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryModellerDesignInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def angle_dimensions(self: Self) -> "List[_156.GeometryModellerAngleDimension]":
        """List[mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerAngleDimension]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleDimensions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def count_dimensions(self: Self) -> "List[_157.GeometryModellerCountDimension]":
        """List[mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerCountDimension]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CountDimensions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def length_dimensions(self: Self) -> "List[_162.GeometryModellerLengthDimension]":
        """List[mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerLengthDimension]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthDimensions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def unitless_dimensions(
        self: Self,
    ) -> "List[_164.GeometryModellerUnitlessDimension]":
        """List[mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerUnitlessDimension]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UnitlessDimensions

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
    ) -> "GeometryModellerDimensions._Cast_GeometryModellerDimensions":
        return self._Cast_GeometryModellerDimensions(self)
