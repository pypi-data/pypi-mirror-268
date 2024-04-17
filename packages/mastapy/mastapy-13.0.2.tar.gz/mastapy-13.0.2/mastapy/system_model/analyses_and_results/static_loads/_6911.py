"""HarmonicLoadDataImportFromMotorPackages"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines.harmonic_load_data import _1389
from mastapy.system_model.analyses_and_results.static_loads import _6910
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_IMPORT_FROM_MOTOR_PACKAGES = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataImportFromMotorPackages",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6889,
        _6907,
        _6909,
        _6912,
        _6913,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataImportFromMotorPackages",)


Self = TypeVar("Self", bound="HarmonicLoadDataImportFromMotorPackages")
T = TypeVar("T", bound="_6889.ElectricMachineHarmonicLoadImportOptionsBase")


class HarmonicLoadDataImportFromMotorPackages(_6910.HarmonicLoadDataImportBase[T]):
    """HarmonicLoadDataImportFromMotorPackages

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _HARMONIC_LOAD_DATA_IMPORT_FROM_MOTOR_PACKAGES
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HarmonicLoadDataImportFromMotorPackages"
    )

    class _Cast_HarmonicLoadDataImportFromMotorPackages:
        """Special nested class for casting HarmonicLoadDataImportFromMotorPackages to subclasses."""

        def __init__(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
            parent: "HarmonicLoadDataImportFromMotorPackages",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
        ) -> "_6910.HarmonicLoadDataImportBase":
            return self._parent._cast(_6910.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_csv_import(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
        ) -> "_6907.HarmonicLoadDataCSVImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6907

            return self._parent._cast(_6907.HarmonicLoadDataCSVImport)

        @property
        def harmonic_load_data_flux_import(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
        ) -> "_6909.HarmonicLoadDataFluxImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.HarmonicLoadDataFluxImport)

        @property
        def harmonic_load_data_jmag_import(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
        ) -> "_6912.HarmonicLoadDataJMAGImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.HarmonicLoadDataJMAGImport)

        @property
        def harmonic_load_data_motor_cad_import(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
        ) -> "_6913.HarmonicLoadDataMotorCADImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.HarmonicLoadDataMotorCADImport)

        @property
        def harmonic_load_data_import_from_motor_packages(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
        ) -> "HarmonicLoadDataImportFromMotorPackages":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages",
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
        self: Self, instance_to_wrap: "HarmonicLoadDataImportFromMotorPackages.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_slice_number(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.AxialSliceNumber

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @axial_slice_number.setter
    @enforce_parameter_types
    def axial_slice_number(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.AxialSliceNumber = value

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
    def speed(self: Self) -> "list_with_selected_item.ListWithSelectedItem_float":
        """ListWithSelectedItem[float]"""
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_float",
        )(temp)

    @speed.setter
    @enforce_parameter_types
    def speed(self: Self, value: "float"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0
        )
        self.wrapped.Speed = value

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataImportFromMotorPackages._Cast_HarmonicLoadDataImportFromMotorPackages":
        return self._Cast_HarmonicLoadDataImportFromMotorPackages(self)
