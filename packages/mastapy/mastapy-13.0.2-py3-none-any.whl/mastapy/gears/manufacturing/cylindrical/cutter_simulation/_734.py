"""CutterSimulationCalc"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUTTER_SIMULATION_CALC = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "CutterSimulationCalc",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
        _735,
        _740,
        _741,
        _743,
        _746,
        _748,
        _749,
        _750,
        _751,
    )
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _732


__docformat__ = "restructuredtext en"
__all__ = ("CutterSimulationCalc",)


Self = TypeVar("Self", bound="CutterSimulationCalc")


class CutterSimulationCalc(_0.APIBase):
    """CutterSimulationCalc

    This is a mastapy class.
    """

    TYPE = _CUTTER_SIMULATION_CALC
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CutterSimulationCalc")

    class _Cast_CutterSimulationCalc:
        """Special nested class for casting CutterSimulationCalc to subclasses."""

        def __init__(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
            parent: "CutterSimulationCalc",
        ):
            self._parent = parent

        @property
        def form_wheel_grinding_simulation_calculator(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "_741.FormWheelGrindingSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _741

            return self._parent._cast(_741.FormWheelGrindingSimulationCalculator)

        @property
        def hob_simulation_calculator(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "_743.HobSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _743

            return self._parent._cast(_743.HobSimulationCalculator)

        @property
        def rack_simulation_calculator(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "_746.RackSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _746

            return self._parent._cast(_746.RackSimulationCalculator)

        @property
        def shaper_simulation_calculator(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "_748.ShaperSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _748

            return self._parent._cast(_748.ShaperSimulationCalculator)

        @property
        def shaving_simulation_calculator(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "_749.ShavingSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _749

            return self._parent._cast(_749.ShavingSimulationCalculator)

        @property
        def virtual_simulation_calculator(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "_750.VirtualSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _750

            return self._parent._cast(_750.VirtualSimulationCalculator)

        @property
        def worm_grinder_simulation_calculator(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "_751.WormGrinderSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _751

            return self._parent._cast(_751.WormGrinderSimulationCalculator)

        @property
        def cutter_simulation_calc(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc",
        ) -> "CutterSimulationCalc":
            return self._parent

        def __getattr__(
            self: "CutterSimulationCalc._Cast_CutterSimulationCalc", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CutterSimulationCalc.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_to_form_radius_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseToFormRadiusClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def chamfer_transverse_pressure_angle_at_tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChamferTransversePressureAngleAtTipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def critical_section_diameter(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSectionDiameter

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def finish_cutter_tip_to_fillet_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishCutterTipToFilletClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def generating_circle_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeneratingCircleDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def lowest_sap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestSAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_finish_stock_arc_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFinishStockArcLength

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_finish_stock_arc_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFinishStockArcLength

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
    def normal_thickness_at_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThicknessAtFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_thickness_at_tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThicknessAtTipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_tip_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_tooth_thickness_on_the_reference_circle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalToothThicknessOnTheReferenceCircle

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_tooth_thickness_on_the_v_circle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalToothThicknessOnTheVCircle

        if temp is None:
            return 0.0

        return temp

    @property
    def notch_start_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NotchStartDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_shift_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_chamfer_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialChamferHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_clearance_between_rough_root_circle_and_theoretical_finish_root_circle(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RadialClearanceBetweenRoughRootCircleAndTheoreticalFinishRootCircle
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def residual_fillet_undercut(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResidualFilletUndercut

        if temp is None:
            return 0.0

        return temp

    @property
    def residual_fillet_undercut_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResidualFilletUndercutDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def rough_root_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughRootFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def sap_to_form_radius_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SAPToFormRadiusClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def theoretical_finish_root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TheoreticalFinishRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def theoretical_finish_root_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TheoreticalFinishRootFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_chamfer_angle_straight_line_approximation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseChamferAngleStraightLineApproximation

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_chamfer_angle_tangent_to_involute_at_tip_form_diameter(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseChamferAngleTangentToInvoluteAtTipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_root_fillet_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseRootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def gear(self: Self) -> "_735.CylindricalCutterSimulatableGear":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalCutterSimulatableGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stock_removed_at_designed_sap(self: Self) -> "_740.FinishStockPoint":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.FinishStockPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StockRemovedAtDesignedSAP

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stock_removed_at_reference_diameter(self: Self) -> "_740.FinishStockPoint":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.FinishStockPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StockRemovedAtReferenceDiameter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stock_removed_at_rough_tip_form(self: Self) -> "_740.FinishStockPoint":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.FinishStockPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StockRemovedAtRoughTipForm

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def finish_stock_indexed_arcs(self: Self) -> "List[_740.FinishStockPoint]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.FinishStockPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishStockIndexedArcs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_fillet_points(self: Self) -> "List[_732.NamedPoint]":
        """List[mastapy.gears.manufacturing.cylindrical.cutters.tangibles.NamedPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearFilletPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def main_profile_finish_stock(self: Self) -> "List[_740.FinishStockPoint]":
        """List[mastapy.gears.manufacturing.cylindrical.cutter_simulation.FinishStockPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MainProfileFinishStock

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
    def cast_to(self: Self) -> "CutterSimulationCalc._Cast_CutterSimulationCalc":
        return self._Cast_CutterSimulationCalc(self)
