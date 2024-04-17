"""FEPartDRIVASurfaceSelection"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.fe import _2390
from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.component_mode_synthesis import _227
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_DRIVA_SURFACE_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FEPartDRIVASurfaceSelection"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEPartDRIVASurfaceSelection",)


Self = TypeVar("Self", bound="FEPartDRIVASurfaceSelection")


class FEPartDRIVASurfaceSelection(_0.APIBase):
    """FEPartDRIVASurfaceSelection

    This is a mastapy class.
    """

    TYPE = _FE_PART_DRIVA_SURFACE_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartDRIVASurfaceSelection")

    class _Cast_FEPartDRIVASurfaceSelection:
        """Special nested class for casting FEPartDRIVASurfaceSelection to subclasses."""

        def __init__(
            self: "FEPartDRIVASurfaceSelection._Cast_FEPartDRIVASurfaceSelection",
            parent: "FEPartDRIVASurfaceSelection",
        ):
            self._parent = parent

        @property
        def fe_part_driva_surface_selection(
            self: "FEPartDRIVASurfaceSelection._Cast_FEPartDRIVASurfaceSelection",
        ) -> "FEPartDRIVASurfaceSelection":
            return self._parent

        def __getattr__(
            self: "FEPartDRIVASurfaceSelection._Cast_FEPartDRIVASurfaceSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartDRIVASurfaceSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_substructures(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_FESubstructure":
        """ListWithSelectedItem[mastapy.system_model.fe.FESubstructure]"""
        temp = self.wrapped.FESubstructures

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_FESubstructure",
        )(temp)

    @fe_substructures.setter
    @enforce_parameter_types
    def fe_substructures(self: Self, value: "_2390.FESubstructure"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructure.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_FESubstructure.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.FESubstructures = value

    @property
    def is_included(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsIncluded

        if temp is None:
            return False

        return temp

    @is_included.setter
    @enforce_parameter_types
    def is_included(self: Self, value: "bool"):
        self.wrapped.IsIncluded = bool(value) if value is not None else False

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
    def surfaces(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup":
        """ListWithSelectedItem[mastapy.nodal_analysis.component_mode_synthesis.CMSElementFaceGroup]"""
        temp = self.wrapped.Surfaces

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CMSElementFaceGroup",
        )(temp)

    @surfaces.setter
    @enforce_parameter_types
    def surfaces(self: Self, value: "_227.CMSElementFaceGroup"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CMSElementFaceGroup.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Surfaces = value

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
    ) -> "FEPartDRIVASurfaceSelection._Cast_FEPartDRIVASurfaceSelection":
        return self._Cast_FEPartDRIVASurfaceSelection(self)
