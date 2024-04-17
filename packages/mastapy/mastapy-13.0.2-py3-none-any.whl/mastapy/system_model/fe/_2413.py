"""RaceBearingFE"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2455
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACE_BEARING_FE = python_net_import("SMT.MastaAPI.SystemModel.FE", "RaceBearingFE")

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2364, _2371


__docformat__ = "restructuredtext en"
__all__ = ("RaceBearingFE",)


Self = TypeVar("Self", bound="RaceBearingFE")


class RaceBearingFE(_0.APIBase):
    """RaceBearingFE

    This is a mastapy class.
    """

    TYPE = _RACE_BEARING_FE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RaceBearingFE")

    class _Cast_RaceBearingFE:
        """Special nested class for casting RaceBearingFE to subclasses."""

        def __init__(
            self: "RaceBearingFE._Cast_RaceBearingFE", parent: "RaceBearingFE"
        ):
            self._parent = parent

        @property
        def race_bearing_fe(
            self: "RaceBearingFE._Cast_RaceBearingFE",
        ) -> "RaceBearingFE":
            return self._parent

        def __getattr__(self: "RaceBearingFE._Cast_RaceBearingFE", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RaceBearingFE.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alignment_method(self: Self) -> "_2364.AlignmentMethodForRaceBearing":
        """mastapy.system_model.fe.AlignmentMethodForRaceBearing"""
        temp = self.wrapped.AlignmentMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.FE.AlignmentMethodForRaceBearing"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.fe._2364", "AlignmentMethodForRaceBearing"
        )(value)

    @alignment_method.setter
    @enforce_parameter_types
    def alignment_method(self: Self, value: "_2364.AlignmentMethodForRaceBearing"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.FE.AlignmentMethodForRaceBearing"
        )
        self.wrapped.AlignmentMethod = value

    @property
    def datum(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Datum":
        """ListWithSelectedItem[mastapy.system_model.part_model.Datum]"""
        temp = self.wrapped.Datum

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Datum",
        )(temp)

    @datum.setter
    @enforce_parameter_types
    def datum(self: Self, value: "_2455.Datum"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Datum.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Datum.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Datum = value

    @property
    def fe_filename(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEFilename

        if temp is None:
            return ""

        return temp

    @property
    def links(self: Self) -> "List[_2371.BearingRaceNodeLink]":
        """List[mastapy.system_model.fe.BearingRaceNodeLink]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Links

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

    def copy_datum_to_manual(self: Self):
        """Method does not return."""
        self.wrapped.CopyDatumToManual()

    def find_nodes_for_links(self: Self):
        """Method does not return."""
        self.wrapped.FindNodesForLinks()

    def import_fe_mesh(self: Self):
        """Method does not return."""
        self.wrapped.ImportFEMesh()

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
    def cast_to(self: Self) -> "RaceBearingFE._Cast_RaceBearingFE":
        return self._Cast_RaceBearingFE(self)
