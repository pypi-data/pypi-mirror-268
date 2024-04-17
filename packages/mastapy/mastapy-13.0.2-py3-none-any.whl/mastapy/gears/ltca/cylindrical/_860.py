"""CylindricalGearMeshLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy.gears.ltca import _844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearMeshLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case.cylindrical import _887
    from mastapy.gears.ltca import _835
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1104
    from mastapy.gears.cylindrical import _1220
    from mastapy.gears.rating.cylindrical import _461
    from mastapy.gears.ltca.cylindrical import _864
    from mastapy.gears.analysis import _1229, _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearMeshLoadDistributionAnalysis")


class CylindricalGearMeshLoadDistributionAnalysis(
    _844.GearMeshLoadDistributionAnalysis
):
    """CylindricalGearMeshLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshLoadDistributionAnalysis"
    )

    class _Cast_CylindricalGearMeshLoadDistributionAnalysis:
        """Special nested class for casting CylindricalGearMeshLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis",
            parent: "CylindricalGearMeshLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_distribution_analysis(
            self: "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis",
        ) -> "_844.GearMeshLoadDistributionAnalysis":
            return self._parent._cast(_844.GearMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis",
        ) -> "_1229.GearMeshImplementationAnalysis":
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis",
        ) -> "CylindricalGearMeshLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshLoadDistributionAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def calculated_face_load_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedFaceLoadFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def din_scuffing_bulk_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DINScuffingBulkToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def iso63362006_mesh_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO63362006MeshStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def iso63362006_mesh_stiffness_across_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO63362006MeshStiffnessAcrossFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def iso63362006_single_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO63362006SingleStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def iso63362006_single_stiffness_across_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO63362006SingleStiffnessAcrossFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def iso_scuffing_bulk_tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISOScuffingBulkToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEdgePressure

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_te(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTE

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Misalignment

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
    def strip_loads_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StripLoadsDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def strip_loads_maximum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StripLoadsMaximum

        if temp is None:
            return 0.0

        return temp

    @property
    def strip_loads_minimum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StripLoadsMinimum

        if temp is None:
            return 0.0

        return temp

    @property
    def theoretical_total_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TheoreticalTotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def utilization_force_per_unit_length_cutoff_value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UtilizationForcePerUnitLengthCutoffValue

        if temp is None:
            return 0.0

        return temp

    @property
    def cylindrical_mesh_load_case(self: Self) -> "_887.CylindricalMeshLoadCase":
        """mastapy.gears.load_case.cylindrical.CylindricalMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a_in_mesh(
        self: Self,
    ) -> "_835.CylindricalMeshedGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.CylindricalMeshedGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAInMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b_in_mesh(
        self: Self,
    ) -> "_835.CylindricalMeshedGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.CylindricalMeshedGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBInMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_micro_geometry(self: Self) -> "_1104.CylindricalGearMeshMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMeshMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshMicroGeometry

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
    def rating(self: Self) -> "_461.CylindricalGearMeshRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_distribution_analyses_at_single_rotation(
        self: Self,
    ) -> "List[_864.CylindricalMeshLoadDistributionAtRotation]":
        """List[mastapy.gears.ltca.cylindrical.CylindricalMeshLoadDistributionAtRotation]

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

    @property
    def meshed_gears(
        self: Self,
    ) -> "List[_835.CylindricalMeshedGearLoadDistributionAnalysis]":
        """List[mastapy.gears.ltca.CylindricalMeshedGearLoadDistributionAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def transmission_error_against_rotation(self: Self) -> "List[Vector2D]":
        """List[Vector2D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorAgainstRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)

        if value is None:
            return None

        return value

    def calculate_mesh_stiffness(self: Self):
        """Method does not return."""
        self.wrapped.CalculateMeshStiffness()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshLoadDistributionAnalysis._Cast_CylindricalGearMeshLoadDistributionAnalysis":
        return self._Cast_CylindricalGearMeshLoadDistributionAnalysis(self)
