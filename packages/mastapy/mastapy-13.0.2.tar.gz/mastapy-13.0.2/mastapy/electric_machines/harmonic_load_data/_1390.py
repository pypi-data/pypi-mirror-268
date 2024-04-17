"""SpeedDependentHarmonicLoadData"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.electric_machines.harmonic_load_data import _1387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_DEPENDENT_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.ElectricMachines.HarmonicLoadData", "SpeedDependentHarmonicLoadData"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.results import _1328
    from mastapy.electric_machines.harmonic_load_data import _1385
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6880,
        _6881,
        _6882,
        _6883,
        _6884,
        _6885,
        _6886,
        _6946,
        _6988,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpeedDependentHarmonicLoadData",)


Self = TypeVar("Self", bound="SpeedDependentHarmonicLoadData")


class SpeedDependentHarmonicLoadData(_1387.HarmonicLoadDataBase):
    """SpeedDependentHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _SPEED_DEPENDENT_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpeedDependentHarmonicLoadData")

    class _Cast_SpeedDependentHarmonicLoadData:
        """Special nested class for casting SpeedDependentHarmonicLoadData to subclasses."""

        def __init__(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
            parent: "SpeedDependentHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_base(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_1387.HarmonicLoadDataBase":
            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def dynamic_force_results(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_1328.DynamicForceResults":
            from mastapy.electric_machines.results import _1328

            return self._parent._cast(_1328.DynamicForceResults)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_1385.ElectricMachineHarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1385

            return self._parent._cast(_1385.ElectricMachineHarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6880.ElectricMachineHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6880

            return self._parent._cast(_6880.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_from_excel(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6881.ElectricMachineHarmonicLoadDataFromExcel":
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.ElectricMachineHarmonicLoadDataFromExcel)

        @property
        def electric_machine_harmonic_load_data_from_flux(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6882.ElectricMachineHarmonicLoadDataFromFlux":
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6883.ElectricMachineHarmonicLoadDataFromJMAG":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_masta(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6884.ElectricMachineHarmonicLoadDataFromMASTA":
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.ElectricMachineHarmonicLoadDataFromMASTA)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6885.ElectricMachineHarmonicLoadDataFromMotorCAD":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6886.ElectricMachineHarmonicLoadDataFromMotorPackages":
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(
                _6886.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def point_load_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6946.PointLoadHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.PointLoadHarmonicLoadData)

        @property
        def unbalanced_mass_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "_6988.UnbalancedMassHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.UnbalancedMassHarmonicLoadData)

        @property
        def speed_dependent_harmonic_load_data(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
        ) -> "SpeedDependentHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpeedDependentHarmonicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_speed(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_float":
        """ListWithSelectedItem[float]"""
        temp = self.wrapped.SelectedSpeed

        if temp is None:
            return 0.0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_float",
        )(temp)

    @selected_speed.setter
    @enforce_parameter_types
    def selected_speed(self: Self, value: "float"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_float.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_float.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0
        )
        self.wrapped.SelectedSpeed = value

    @property
    def show_all_speeds(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowAllSpeeds

        if temp is None:
            return False

        return temp

    @show_all_speeds.setter
    @enforce_parameter_types
    def show_all_speeds(self: Self, value: "bool"):
        self.wrapped.ShowAllSpeeds = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "SpeedDependentHarmonicLoadData._Cast_SpeedDependentHarmonicLoadData":
        return self._Cast_SpeedDependentHarmonicLoadData(self)
