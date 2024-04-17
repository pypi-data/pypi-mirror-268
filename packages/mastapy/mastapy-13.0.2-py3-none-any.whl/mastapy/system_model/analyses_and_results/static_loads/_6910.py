"""HarmonicLoadDataImportBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_IMPORT_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataImportBase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6889,
        _6907,
        _6908,
        _6909,
        _6911,
        _6912,
        _6913,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataImportBase",)


Self = TypeVar("Self", bound="HarmonicLoadDataImportBase")
T = TypeVar("T", bound="_6889.ElectricMachineHarmonicLoadImportOptionsBase")


class HarmonicLoadDataImportBase(_0.APIBase, Generic[T]):
    """HarmonicLoadDataImportBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _HARMONIC_LOAD_DATA_IMPORT_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataImportBase")

    class _Cast_HarmonicLoadDataImportBase:
        """Special nested class for casting HarmonicLoadDataImportBase to subclasses."""

        def __init__(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
            parent: "HarmonicLoadDataImportBase",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_csv_import(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
        ) -> "_6907.HarmonicLoadDataCSVImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.HarmonicLoadDataCSVImport)

        @property
        def harmonic_load_data_excel_import(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
        ) -> "_6908.HarmonicLoadDataExcelImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.HarmonicLoadDataExcelImport)

        @property
        def harmonic_load_data_flux_import(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
        ) -> "_6909.HarmonicLoadDataFluxImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.HarmonicLoadDataFluxImport)

        @property
        def harmonic_load_data_import_from_motor_packages(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
        ) -> "_6911.HarmonicLoadDataImportFromMotorPackages":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_jmag_import(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
        ) -> "_6912.HarmonicLoadDataJMAGImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.HarmonicLoadDataJMAGImport)

        @property
        def harmonic_load_data_motor_cad_import(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
        ) -> "_6913.HarmonicLoadDataMotorCADImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.HarmonicLoadDataMotorCADImport)

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
        ) -> "HarmonicLoadDataImportBase":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataImportBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def file_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.FileName

        if temp is None:
            return ""

        return temp

    @file_name.setter
    @enforce_parameter_types
    def file_name(self: Self, value: "str"):
        self.wrapped.FileName = str(value) if value is not None else ""

    @property
    def imported_data_has_different_direction_for_tooth_ids_to_masta_model(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.ImportedDataHasDifferentDirectionForToothIdsToMASTAModel

        if temp is None:
            return False

        return temp

    @imported_data_has_different_direction_for_tooth_ids_to_masta_model.setter
    @enforce_parameter_types
    def imported_data_has_different_direction_for_tooth_ids_to_masta_model(
        self: Self, value: "bool"
    ):
        self.wrapped.ImportedDataHasDifferentDirectionForToothIdsToMASTAModel = (
            bool(value) if value is not None else False
        )

    @property
    def negate_speed_data_on_import(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.NegateSpeedDataOnImport

        if temp is None:
            return False

        return temp

    @negate_speed_data_on_import.setter
    @enforce_parameter_types
    def negate_speed_data_on_import(self: Self, value: "bool"):
        self.wrapped.NegateSpeedDataOnImport = (
            bool(value) if value is not None else False
        )

    @property
    def negate_stator_axial_load_data_on_import(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.NegateStatorAxialLoadDataOnImport

        if temp is None:
            return False

        return temp

    @negate_stator_axial_load_data_on_import.setter
    @enforce_parameter_types
    def negate_stator_axial_load_data_on_import(self: Self, value: "bool"):
        self.wrapped.NegateStatorAxialLoadDataOnImport = (
            bool(value) if value is not None else False
        )

    @property
    def negate_stator_radial_load_data_on_import(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.NegateStatorRadialLoadDataOnImport

        if temp is None:
            return False

        return temp

    @negate_stator_radial_load_data_on_import.setter
    @enforce_parameter_types
    def negate_stator_radial_load_data_on_import(self: Self, value: "bool"):
        self.wrapped.NegateStatorRadialLoadDataOnImport = (
            bool(value) if value is not None else False
        )

    @property
    def negate_stator_tangential_load_data_on_import(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.NegateStatorTangentialLoadDataOnImport

        if temp is None:
            return False

        return temp

    @negate_stator_tangential_load_data_on_import.setter
    @enforce_parameter_types
    def negate_stator_tangential_load_data_on_import(self: Self, value: "bool"):
        self.wrapped.NegateStatorTangentialLoadDataOnImport = (
            bool(value) if value is not None else False
        )

    @property
    def negate_tooth_axial_moment_data_on_import(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.NegateToothAxialMomentDataOnImport

        if temp is None:
            return False

        return temp

    @negate_tooth_axial_moment_data_on_import.setter
    @enforce_parameter_types
    def negate_tooth_axial_moment_data_on_import(self: Self, value: "bool"):
        self.wrapped.NegateToothAxialMomentDataOnImport = (
            bool(value) if value is not None else False
        )

    @property
    def negate_torque_data_on_import(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.NegateTorqueDataOnImport

        if temp is None:
            return False

        return temp

    @negate_torque_data_on_import.setter
    @enforce_parameter_types
    def negate_torque_data_on_import(self: Self, value: "bool"):
        self.wrapped.NegateTorqueDataOnImport = (
            bool(value) if value is not None else False
        )

    @property
    def node_id_of_first_tooth(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.NodeIdOfFirstTooth

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @node_id_of_first_tooth.setter
    @enforce_parameter_types
    def node_id_of_first_tooth(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.NodeIdOfFirstTooth = value

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

    def read_data_from_file(self: Self):
        """Method does not return."""
        self.wrapped.ReadDataFromFile()

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
    ) -> "HarmonicLoadDataImportBase._Cast_HarmonicLoadDataImportBase":
        return self._Cast_HarmonicLoadDataImportBase(self)
