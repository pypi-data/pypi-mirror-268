"""GearCutterSimulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CUTTER_SIMULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "GearCutterSimulation",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
        _734,
        _750,
        _737,
        _738,
        _739,
        _747,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearCutterSimulation",)


Self = TypeVar("Self", bound="GearCutterSimulation")


class GearCutterSimulation(_0.APIBase):
    """GearCutterSimulation

    This is a mastapy class.
    """

    TYPE = _GEAR_CUTTER_SIMULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCutterSimulation")

    class _Cast_GearCutterSimulation:
        """Special nested class for casting GearCutterSimulation to subclasses."""

        def __init__(
            self: "GearCutterSimulation._Cast_GearCutterSimulation",
            parent: "GearCutterSimulation",
        ):
            self._parent = parent

        @property
        def finish_cutter_simulation(
            self: "GearCutterSimulation._Cast_GearCutterSimulation",
        ) -> "_739.FinishCutterSimulation":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _739

            return self._parent._cast(_739.FinishCutterSimulation)

        @property
        def rough_cutter_simulation(
            self: "GearCutterSimulation._Cast_GearCutterSimulation",
        ) -> "_747.RoughCutterSimulation":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _747

            return self._parent._cast(_747.RoughCutterSimulation)

        @property
        def gear_cutter_simulation(
            self: "GearCutterSimulation._Cast_GearCutterSimulation",
        ) -> "GearCutterSimulation":
            return self._parent

        def __getattr__(
            self: "GearCutterSimulation._Cast_GearCutterSimulation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCutterSimulation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def highest_finished_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestFinishedFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def least_sap_to_form_radius_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeastSAPToFormRadiusClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def lowest_finished_tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestFinishedTipFormDiameter

        if temp is None:
            return 0.0

        return temp

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
    def average_thickness(self: Self) -> "_734.CutterSimulationCalc":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CutterSimulationCalc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def average_thickness_virtual(self: Self) -> "_750.VirtualSimulationCalculator":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.VirtualSimulationCalculator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageThicknessVirtual

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_thickness(self: Self) -> "_734.CutterSimulationCalc":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CutterSimulationCalc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_thickness_virtual(self: Self) -> "_750.VirtualSimulationCalculator":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.VirtualSimulationCalculator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumThicknessVirtual

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_thickness(self: Self) -> "_734.CutterSimulationCalc":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CutterSimulationCalc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumThickness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_thickness_virtual(self: Self) -> "_750.VirtualSimulationCalculator":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.VirtualSimulationCalculator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumThicknessVirtual

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cutter_simulation(self: Self) -> "GearCutterSimulation":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.GearCutterSimulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def smallest_active_profile(self: Self) -> "_734.CutterSimulationCalc":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CutterSimulationCalc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallestActiveProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_cutter_simulations(
        self: Self,
    ) -> "List[_737.CylindricalManufacturedRealGearInMesh]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalManufacturedRealGearInMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshCutterSimulations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_cutter_simulations_virtual(
        self: Self,
    ) -> "List[_738.CylindricalManufacturedVirtualGearInMesh]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalManufacturedVirtualGearInMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshCutterSimulationsVirtual

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def thickness_calculators(self: Self) -> "List[_734.CutterSimulationCalc]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.CutterSimulationCalc]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThicknessCalculators

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def virtual_thickness_calculators(
        self: Self,
    ) -> "List[_750.VirtualSimulationCalculator]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.VirtualSimulationCalculator]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualThicknessCalculators

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
    def cast_to(self: Self) -> "GearCutterSimulation._Cast_GearCutterSimulation":
        return self._Cast_GearCutterSimulation(self)
