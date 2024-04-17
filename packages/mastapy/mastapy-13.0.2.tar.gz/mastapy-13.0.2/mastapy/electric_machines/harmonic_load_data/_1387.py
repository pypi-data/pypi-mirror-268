"""HarmonicLoadDataBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.electric_machines.harmonic_load_data import _1389
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_DOUBLE = python_net_import("System", "Double")
_STRING = python_net_import("System", "String")
_FOURIER_SERIES = python_net_import("SMT.MastaAPI.MathUtility", "FourierSeries")
_LIST = python_net_import("System.Collections.Generic", "List")
_MEASUREMENT_TYPE = python_net_import(
    "SMT.MastaAPIUtility.UnitsAndMeasurements", "MeasurementType"
)
_HARMONIC_LOAD_DATA_BASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "HarmonicLoadDataBase"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1520
    from mastapy.units_and_measurements import _7568
    from mastapy.electric_machines.results import _1328
    from mastapy.electric_machines.harmonic_load_data import _1385, _1390
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6856,
        _6873,
        _6880,
        _6881,
        _6882,
        _6883,
        _6884,
        _6885,
        _6886,
        _6903,
        _6946,
        _6988,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataBase",)


Self = TypeVar("Self", bound="HarmonicLoadDataBase")


class HarmonicLoadDataBase(_0.APIBase):
    """HarmonicLoadDataBase

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataBase")

    class _Cast_HarmonicLoadDataBase:
        """Special nested class for casting HarmonicLoadDataBase to subclasses."""

        def __init__(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
            parent: "HarmonicLoadDataBase",
        ):
            self._parent = parent

        @property
        def dynamic_force_results(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_1328.DynamicForceResults":
            from mastapy.electric_machines.results import _1328

            return self._parent._cast(_1328.DynamicForceResults)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_1385.ElectricMachineHarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1385

            return self._parent._cast(_1385.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_1390.SpeedDependentHarmonicLoadData":
            from mastapy.electric_machines.harmonic_load_data import _1390

            return self._parent._cast(_1390.SpeedDependentHarmonicLoadData)

        @property
        def conical_gear_set_harmonic_load_data(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6856.ConicalGearSetHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.ConicalGearSetHarmonicLoadData)

        @property
        def cylindrical_gear_set_harmonic_load_data(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6873.CylindricalGearSetHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.CylindricalGearSetHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6880.ElectricMachineHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6880

            return self._parent._cast(_6880.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_from_excel(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6881.ElectricMachineHarmonicLoadDataFromExcel":
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6882.ElectricMachineHarmonicLoadDataFromFlux":
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6883.ElectricMachineHarmonicLoadDataFromJMAG":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6884.ElectricMachineHarmonicLoadDataFromMASTA":
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.ElectricMachineHarmonicLoadDataFromMASTA)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6885.ElectricMachineHarmonicLoadDataFromMotorCAD":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6886.ElectricMachineHarmonicLoadDataFromMotorPackages":
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(
                _6886.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def gear_set_harmonic_load_data(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6903.GearSetHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6903

            return self._parent._cast(_6903.GearSetHarmonicLoadData)

        @property
        def point_load_harmonic_load_data(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6946.PointLoadHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.PointLoadHarmonicLoadData)

        @property
        def unbalanced_mass_harmonic_load_data(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "_6988.UnbalancedMassHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.UnbalancedMassHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase",
        ) -> "HarmonicLoadDataBase":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType":
        """EnumWithSelectedValue[mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataType]"""
        temp = self.wrapped.DataType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @data_type.setter
    @enforce_parameter_types
    def data_type(self: Self, value: "_1389.HarmonicLoadDataType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicLoadDataType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DataType = value

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
    def number_of_cycles_in_signal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfCyclesInSignal

        if temp is None:
            return 0.0

        return temp

    @number_of_cycles_in_signal.setter
    @enforce_parameter_types
    def number_of_cycles_in_signal(self: Self, value: "float"):
        self.wrapped.NumberOfCyclesInSignal = float(value) if value is not None else 0.0

    @property
    def number_of_harmonics(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfHarmonics

        if temp is None:
            return 0

        return temp

    @number_of_harmonics.setter
    @enforce_parameter_types
    def number_of_harmonics(self: Self, value: "int"):
        self.wrapped.NumberOfHarmonics = int(value) if value is not None else 0

    @property
    def number_of_values(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfValues

        if temp is None:
            return 0

        return temp

    @number_of_values.setter
    @enforce_parameter_types
    def number_of_values(self: Self, value: "int"):
        self.wrapped.NumberOfValues = int(value) if value is not None else 0

    @property
    def excitations(self: Self) -> "List[_1520.FourierSeries]":
        """List[mastapy.math_utility.FourierSeries]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mean_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanValue

        if temp is None:
            return 0.0

        return temp

    @mean_value.setter
    @enforce_parameter_types
    def mean_value(self: Self, value: "float"):
        self.wrapped.MeanValue = float(value) if value is not None else 0.0

    @property
    def peak_to_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeak

        if temp is None:
            return 0.0

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

    def clear_all_data(self: Self):
        """Method does not return."""
        self.wrapped.ClearAllData()

    def clear_selected_data(self: Self):
        """Method does not return."""
        self.wrapped.ClearSelectedData()

    @enforce_parameter_types
    def set_selected_harmonic_load_data_with_fourier_series(
        self: Self, fourier_series: "_1520.FourierSeries"
    ):
        """Method does not return.

        Args:
            fourier_series (mastapy.math_utility.FourierSeries)
        """
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[_FOURIER_SERIES](
            fourier_series.wrapped if fourier_series else None
        )

    @enforce_parameter_types
    def set_selected_harmonic_load_data_extended(
        self: Self,
        amplitudes: "List[float]",
        phases: "List[float]",
        mean_value: "float",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7568.MeasurementType",
    ):
        """Method does not return.

        Args:
            amplitudes (List[float])
            phases (List[float])
            mean_value (float)
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        amplitudes = conversion.mp_to_pn_list_float(amplitudes)
        phases = conversion.mp_to_pn_list_float(phases)
        mean_value = float(mean_value)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[
            _LIST[_DOUBLE], _LIST[_DOUBLE], _DOUBLE, _STRING, _MEASUREMENT_TYPE
        ](
            amplitudes,
            phases,
            mean_value if mean_value else 0.0,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
        )

    @enforce_parameter_types
    def set_selected_harmonic_load_data(
        self: Self,
        fourier_series_values: "List[float]",
        fourier_series_name: "str",
        fourier_series_measurement_type: "_7568.MeasurementType",
    ):
        """Method does not return.

        Args:
            fourier_series_values (List[float])
            fourier_series_name (str)
            fourier_series_measurement_type (mastapy.units_and_measurements.MeasurementType)
        """
        fourier_series_values = conversion.mp_to_pn_array_float(fourier_series_values)
        fourier_series_name = str(fourier_series_name)
        fourier_series_measurement_type = conversion.mp_to_pn_enum(
            fourier_series_measurement_type,
            "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType",
        )
        self.wrapped.SetSelectedHarmonicLoadData.Overloads[
            _ARRAY[_DOUBLE], _STRING, _MEASUREMENT_TYPE
        ](
            fourier_series_values,
            fourier_series_name if fourier_series_name else "",
            fourier_series_measurement_type,
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
    def cast_to(self: Self) -> "HarmonicLoadDataBase._Cast_HarmonicLoadDataBase":
        return self._Cast_HarmonicLoadDataBase(self)
