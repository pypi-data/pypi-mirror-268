"""CylindricalGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CylindricalGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears import _326
    from mastapy.gears.rating.cylindrical import _461
    from mastapy.system_model.connections_and_sockets.gears import _2316
    from mastapy.system_model.analyses_and_results.static_loads import _6872
    from mastapy.gears.gear_designs.cylindrical import _1022, _1016
    from mastapy.gears.cylindrical import _1220
    from mastapy.math_utility import _1520
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7329,
        _7318,
        _7348,
        _7316,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2748
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearMeshAdvancedSystemDeflection")


class CylindricalGearMeshAdvancedSystemDeflection(
    _7342.GearMeshAdvancedSystemDeflection
):
    """CylindricalGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshAdvancedSystemDeflection"
    )

    class _Cast_CylindricalGearMeshAdvancedSystemDeflection:
        """Special nested class for casting CylindricalGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
            parent: "CylindricalGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_advanced_system_deflection(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_7342.GearMeshAdvancedSystemDeflection":
            return self._parent._cast(_7342.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_7348.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_7316.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
        ) -> "CylindricalGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self: Self) -> "_326.CylindricalFlanks":
        """mastapy.gears.CylindricalFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.CylindricalFlanks")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._326", "CylindricalFlanks")(
            value
        )

    @property
    def average_operating_axial_contact_ratio_for_first_tooth_passing_period(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageOperatingAxialContactRatioForFirstToothPassingPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def average_operating_transverse_contact_ratio_for_first_tooth_passing_period(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AverageOperatingTransverseContactRatioForFirstToothPassingPeriod
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_load_sharing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_chart_gap_to_loaded_flank_gear_a(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToLoadedFlankGearA

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def contact_chart_gap_to_loaded_flank_gear_a_as_text_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToLoadedFlankGearAAsTextFile

        if temp is None:
            return ""

        return temp

    @property
    def contact_chart_gap_to_loaded_flank_gear_b(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToLoadedFlankGearB

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def contact_chart_gap_to_loaded_flank_gear_b_as_text_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToLoadedFlankGearBAsTextFile

        if temp is None:
            return ""

        return temp

    @property
    def contact_chart_gap_to_unloaded_flank_gear_a(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToUnloadedFlankGearA

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def contact_chart_gap_to_unloaded_flank_gear_a_as_text_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToUnloadedFlankGearAAsTextFile

        if temp is None:
            return ""

        return temp

    @property
    def contact_chart_gap_to_unloaded_flank_gear_b(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToUnloadedFlankGearB

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def contact_chart_gap_to_unloaded_flank_gear_b_as_text_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartGapToUnloadedFlankGearBAsTextFile

        if temp is None:
            return ""

        return temp

    @property
    def contact_chart_max_pressure_gear_a(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartMaxPressureGearA

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def contact_chart_max_pressure_gear_a_as_text_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartMaxPressureGearAAsTextFile

        if temp is None:
            return ""

        return temp

    @property
    def contact_chart_max_pressure_gear_b(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartMaxPressureGearB

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def contact_chart_max_pressure_gear_b_as_text_file(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactChartMaxPressureGearBAsTextFile

        if temp is None:
            return ""

        return temp

    @property
    def face_load_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def inactive_flank(self: Self) -> "_326.CylindricalFlanks":
        """mastapy.gears.CylindricalFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InactiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.CylindricalFlanks")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._326", "CylindricalFlanks")(
            value
        )

    @property
    def maximum_contact_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEdgeStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_stress_including_tip_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEdgeStressIncludingTipContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_stress_on_gear_a_including_tip_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEdgeStressOnGearAIncludingTipContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_stress_on_gear_b_including_tip_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEdgeStressOnGearBIncludingTipContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_principal_root_stress_on_tension_side_from_gear_fe_model(
        self: Self,
    ) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalRootStressOnTensionSideFromGearFEModel

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def mean_mesh_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanMeshStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_mesh_tilt_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanMeshTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_te_excluding_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTEExcludingBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_total_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_mesh_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakMeshStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_te(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakTE

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_share(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueShare

        if temp is None:
            return 0.0

        return temp

    @property
    def use_advanced_ltca(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedLTCA

        if temp is None:
            return False

        return temp

    @use_advanced_ltca.setter
    @enforce_parameter_types
    def use_advanced_ltca(self: Self, value: "bool"):
        self.wrapped.UseAdvancedLTCA = bool(value) if value is not None else False

    @property
    def component_detailed_analysis(self: Self) -> "_461.CylindricalGearMeshRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2316.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6872.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_design(self: Self) -> "_1022.CylindricalGearMeshDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def points_with_worst_results(self: Self) -> "_1220.PointsWithWorstResults":
        """mastapy.gears.cylindrical.PointsWithWorstResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointsWithWorstResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transmission_error_fourier_series_for_first_tooth_passing_period(
        self: Self,
    ) -> "_1520.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorFourierSeriesForFirstToothPassingPeriod

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_advanced_analyses(
        self: Self,
    ) -> "List[_7329.CylindricalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearAdvancedAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_mesh_system_deflection_results(
        self: Self,
    ) -> "List[_2748.CylindricalGearMeshSystemDeflectionTimestep]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionTimestep]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMeshSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_designs(self: Self) -> "List[_1016.CylindricalGearDesign]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def max_pressure_contact_chart_for_each_tooth_pass_for_gear_a(
        self: Self,
    ) -> "List[_7318.ContactChartPerToothPass]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ContactChartPerToothPass]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxPressureContactChartForEachToothPassForGearA

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def animation_of_max_pressure_contact_chart_for_each_tooth_pass_for_gear_a(
        self: Self,
    ):
        """Method does not return."""
        self.wrapped.AnimationOfMaxPressureContactChartForEachToothPassForGearA()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshAdvancedSystemDeflection._Cast_CylindricalGearMeshAdvancedSystemDeflection":
        return self._Cast_CylindricalGearMeshAdvancedSystemDeflection(self)
