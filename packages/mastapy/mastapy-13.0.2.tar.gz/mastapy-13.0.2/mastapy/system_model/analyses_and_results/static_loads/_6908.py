"""HarmonicLoadDataExcelImport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.utility.units_and_measurements import _1617
from mastapy.system_model.analyses_and_results.static_loads import _6910
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_EXCEL_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataExcelImport",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6934


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataExcelImport",)


Self = TypeVar("Self", bound="HarmonicLoadDataExcelImport")


class HarmonicLoadDataExcelImport(
    _6910.HarmonicLoadDataImportBase[
        "_6887.ElectricMachineHarmonicLoadExcelImportOptions"
    ]
):
    """HarmonicLoadDataExcelImport

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_EXCEL_IMPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataExcelImport")

    class _Cast_HarmonicLoadDataExcelImport:
        """Special nested class for casting HarmonicLoadDataExcelImport to subclasses."""

        def __init__(
            self: "HarmonicLoadDataExcelImport._Cast_HarmonicLoadDataExcelImport",
            parent: "HarmonicLoadDataExcelImport",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataExcelImport._Cast_HarmonicLoadDataExcelImport",
        ) -> "_6910.HarmonicLoadDataImportBase":
            return self._parent._cast(_6910.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_excel_import(
            self: "HarmonicLoadDataExcelImport._Cast_HarmonicLoadDataExcelImport",
        ) -> "HarmonicLoadDataExcelImport":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataExcelImport._Cast_HarmonicLoadDataExcelImport",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataExcelImport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def column_index_of_first_data_point(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ColumnIndexOfFirstDataPoint

        if temp is None:
            return 0

        return temp

    @column_index_of_first_data_point.setter
    @enforce_parameter_types
    def column_index_of_first_data_point(self: Self, value: "int"):
        self.wrapped.ColumnIndexOfFirstDataPoint = (
            int(value) if value is not None else 0
        )

    @property
    def column_index_of_first_speed_point(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ColumnIndexOfFirstSpeedPoint

        if temp is None:
            return 0

        return temp

    @column_index_of_first_speed_point.setter
    @enforce_parameter_types
    def column_index_of_first_speed_point(self: Self, value: "int"):
        self.wrapped.ColumnIndexOfFirstSpeedPoint = (
            int(value) if value is not None else 0
        )

    @property
    def excitation_order_as_rotational_order_of_shaft(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ExcitationOrderAsRotationalOrderOfShaft

        if temp is None:
            return 0.0

        return temp

    @excitation_order_as_rotational_order_of_shaft.setter
    @enforce_parameter_types
    def excitation_order_as_rotational_order_of_shaft(self: Self, value: "float"):
        self.wrapped.ExcitationOrderAsRotationalOrderOfShaft = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_speeds(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSpeeds

        if temp is None:
            return 0

        return temp

    @number_of_speeds.setter
    @enforce_parameter_types
    def number_of_speeds(self: Self, value: "int"):
        self.wrapped.NumberOfSpeeds = int(value) if value is not None else 0

    @property
    def read_speeds_from_excel_sheet(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ReadSpeedsFromExcelSheet

        if temp is None:
            return False

        return temp

    @read_speeds_from_excel_sheet.setter
    @enforce_parameter_types
    def read_speeds_from_excel_sheet(self: Self, value: "bool"):
        self.wrapped.ReadSpeedsFromExcelSheet = (
            bool(value) if value is not None else False
        )

    @property
    def row_index_of_first_data_point(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RowIndexOfFirstDataPoint

        if temp is None:
            return 0

        return temp

    @row_index_of_first_data_point.setter
    @enforce_parameter_types
    def row_index_of_first_data_point(self: Self, value: "int"):
        self.wrapped.RowIndexOfFirstDataPoint = int(value) if value is not None else 0

    @property
    def row_index_of_first_speed_point(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RowIndexOfFirstSpeedPoint

        if temp is None:
            return 0

        return temp

    @row_index_of_first_speed_point.setter
    @enforce_parameter_types
    def row_index_of_first_speed_point(self: Self, value: "int"):
        self.wrapped.RowIndexOfFirstSpeedPoint = int(value) if value is not None else 0

    @property
    def row_index_of_last_data_point(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RowIndexOfLastDataPoint

        if temp is None:
            return 0

        return temp

    @row_index_of_last_data_point.setter
    @enforce_parameter_types
    def row_index_of_last_data_point(self: Self, value: "int"):
        self.wrapped.RowIndexOfLastDataPoint = int(value) if value is not None else 0

    @property
    def sheet_for_first_set_of_data(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.SheetForFirstSetOfData

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sheet_for_first_set_of_data.setter
    @enforce_parameter_types
    def sheet_for_first_set_of_data(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.SheetForFirstSetOfData = value

    @property
    def sheet_with_speed_data(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.SheetWithSpeedData

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @sheet_with_speed_data.setter
    @enforce_parameter_types
    def sheet_with_speed_data(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.SheetWithSpeedData = value

    @property
    def speed_units(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.SpeedUnits

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @speed_units.setter
    @enforce_parameter_types
    def speed_units(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SpeedUnits = value

    @property
    def units_for_data_being_imported(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.UnitsForDataBeingImported

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @units_for_data_being_imported.setter
    @enforce_parameter_types
    def units_for_data_being_imported(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.UnitsForDataBeingImported = value

    @property
    def speeds(self: Self) -> "List[_6934.NamedSpeed]":
        """List[mastapy.system_model.analyses_and_results.static_loads.NamedSpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speeds

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def select_excel_file(self: Self):
        """Method does not return."""
        self.wrapped.SelectExcelFile()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataExcelImport._Cast_HarmonicLoadDataExcelImport":
        return self._Cast_HarmonicLoadDataExcelImport(self)
