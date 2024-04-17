"""CMSElementFaceGroupWithSelectionOption"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_ELEMENT_FACE_GROUP_WITH_SELECTION_OPTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CMSElementFaceGroupWithSelectionOption",
)


__docformat__ = "restructuredtext en"
__all__ = ("CMSElementFaceGroupWithSelectionOption",)


Self = TypeVar("Self", bound="CMSElementFaceGroupWithSelectionOption")


class CMSElementFaceGroupWithSelectionOption(_0.APIBase):
    """CMSElementFaceGroupWithSelectionOption

    This is a mastapy class.
    """

    TYPE = _CMS_ELEMENT_FACE_GROUP_WITH_SELECTION_OPTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CMSElementFaceGroupWithSelectionOption"
    )

    class _Cast_CMSElementFaceGroupWithSelectionOption:
        """Special nested class for casting CMSElementFaceGroupWithSelectionOption to subclasses."""

        def __init__(
            self: "CMSElementFaceGroupWithSelectionOption._Cast_CMSElementFaceGroupWithSelectionOption",
            parent: "CMSElementFaceGroupWithSelectionOption",
        ):
            self._parent = parent

        @property
        def cms_element_face_group_with_selection_option(
            self: "CMSElementFaceGroupWithSelectionOption._Cast_CMSElementFaceGroupWithSelectionOption",
        ) -> "CMSElementFaceGroupWithSelectionOption":
            return self._parent

        def __getattr__(
            self: "CMSElementFaceGroupWithSelectionOption._Cast_CMSElementFaceGroupWithSelectionOption",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CMSElementFaceGroupWithSelectionOption.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def log_surface(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LogSurface

        if temp is None:
            return False

        return temp

    @log_surface.setter
    @enforce_parameter_types
    def log_surface(self: Self, value: "bool"):
        self.wrapped.LogSurface = bool(value) if value is not None else False

    @property
    def surface_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceName

        if temp is None:
            return ""

        return temp

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
    ) -> "CMSElementFaceGroupWithSelectionOption._Cast_CMSElementFaceGroupWithSelectionOption":
        return self._Cast_CMSElementFaceGroupWithSelectionOption(self)
