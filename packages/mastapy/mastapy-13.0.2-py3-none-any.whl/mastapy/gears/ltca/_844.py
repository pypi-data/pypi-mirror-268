"""GearMeshLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.analysis import _1229
from mastapy._internal.cast_exception import CastException

_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearLoadDistributionAnalysis"
)
_GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearMeshLoadDistributionAnalysis"
)
_GEAR_FLANKS = python_net_import("SMT.MastaAPI.Gears", "GearFlanks")
_STRESS_RESULTS_TYPE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "StressResultsType"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1520
    from mastapy.gears.ltca import _845, _843
    from mastapy.gears import _329
    from mastapy.nodal_analysis import _90
    from mastapy.gears.ltca.cylindrical import _860
    from mastapy.gears.ltca.conical import _873
    from mastapy.gears.analysis import _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="GearMeshLoadDistributionAnalysis")


class GearMeshLoadDistributionAnalysis(_1229.GearMeshImplementationAnalysis):
    """GearMeshLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshLoadDistributionAnalysis")

    class _Cast_GearMeshLoadDistributionAnalysis:
        """Special nested class for casting GearMeshLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
            parent: "GearMeshLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
        ) -> "_1229.GearMeshImplementationAnalysis":
            return self._parent._cast(_1229.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
        ) -> "_860.CylindricalGearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _860

            return self._parent._cast(_860.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
        ) -> "_873.ConicalMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _873

            return self._parent._cast(_873.ConicalMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
        ) -> "GearMeshLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshLoadDistributionAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_total_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualTotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisName

        if temp is None:
            return ""

        return temp

    @property
    def index_of_roll_angle_with_maximum_contact_stress(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IndexOfRollAngleWithMaximumContactStress

        if temp is None:
            return 0

        return temp

    @property
    def is_advanced_ltca(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsAdvancedLTCA

        if temp is None:
            return False

        return temp

    @is_advanced_ltca.setter
    @enforce_parameter_types
    def is_advanced_ltca(self: Self, value: "bool"):
        self.wrapped.IsAdvancedLTCA = bool(value) if value is not None else False

    @property
    def load_case_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ""

        return temp

    @property
    def maximum_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_force_per_unit_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumForcePerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pressure_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPressureVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_force_per_unit_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumForcePerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_roll_angles(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfRollAngles

        if temp is None:
            return 0

        return temp

    @property
    def peakto_peak_moment_about_centre(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeaktoPeakMomentAboutCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_about_centre_fourier_series(self: Self) -> "_1520.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentAboutCentreFourierSeries

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transmission_error_fourier_series(self: Self) -> "_1520.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorFourierSeries

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_distribution_analyses_at_single_rotation(
        self: Self,
    ) -> "List[_845.GearMeshLoadDistributionAtRotation]":
        """List[mastapy.gears.ltca.GearMeshLoadDistributionAtRotation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionAnalysesAtSingleRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def maximum_root_stress_with_flanks(
        self: Self,
        gear: "_843.GearLoadDistributionAnalysis",
        flank: "_329.GearFlanks",
        stress_type: "_90.StressResultsType",
    ) -> "float":
        """float

        Args:
            gear (mastapy.gears.ltca.GearLoadDistributionAnalysis)
            flank (mastapy.gears.GearFlanks)
            stress_type (mastapy.nodal_analysis.StressResultsType)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        stress_type = conversion.mp_to_pn_enum(
            stress_type, "SMT.MastaAPI.NodalAnalysis.StressResultsType"
        )
        method_result = self.wrapped.MaximumRootStress.Overloads[
            _GEAR_LOAD_DISTRIBUTION_ANALYSIS, _GEAR_FLANKS, _STRESS_RESULTS_TYPE
        ](gear.wrapped if gear else None, flank, stress_type)
        return method_result

    @enforce_parameter_types
    def maximum_root_stress(
        self: Self,
        gear: "_843.GearLoadDistributionAnalysis",
        stress_type: "_90.StressResultsType",
    ) -> "float":
        """float

        Args:
            gear (mastapy.gears.ltca.GearLoadDistributionAnalysis)
            stress_type (mastapy.nodal_analysis.StressResultsType)
        """
        stress_type = conversion.mp_to_pn_enum(
            stress_type, "SMT.MastaAPI.NodalAnalysis.StressResultsType"
        )
        method_result = self.wrapped.MaximumRootStress.Overloads[
            _GEAR_LOAD_DISTRIBUTION_ANALYSIS, _STRESS_RESULTS_TYPE
        ](gear.wrapped if gear else None, stress_type)
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis":
        return self._Cast_GearMeshLoadDistributionAnalysis(self)
