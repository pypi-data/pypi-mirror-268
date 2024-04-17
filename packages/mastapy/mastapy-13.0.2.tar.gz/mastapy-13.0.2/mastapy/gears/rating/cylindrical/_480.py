"""MicroPittingResultsRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_PITTING_RESULTS_ROW = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "MicroPittingResultsRow"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029


__docformat__ = "restructuredtext en"
__all__ = ("MicroPittingResultsRow",)


Self = TypeVar("Self", bound="MicroPittingResultsRow")


class MicroPittingResultsRow(_0.APIBase):
    """MicroPittingResultsRow

    This is a mastapy class.
    """

    TYPE = _MICRO_PITTING_RESULTS_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MicroPittingResultsRow")

    class _Cast_MicroPittingResultsRow:
        """Special nested class for casting MicroPittingResultsRow to subclasses."""

        def __init__(
            self: "MicroPittingResultsRow._Cast_MicroPittingResultsRow",
            parent: "MicroPittingResultsRow",
        ):
            self._parent = parent

        @property
        def micro_pitting_results_row(
            self: "MicroPittingResultsRow._Cast_MicroPittingResultsRow",
        ) -> "MicroPittingResultsRow":
            return self._parent

        def __getattr__(
            self: "MicroPittingResultsRow._Cast_MicroPittingResultsRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MicroPittingResultsRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_point(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactPoint

        if temp is None:
            return 0.0

        return temp

    @contact_point.setter
    @enforce_parameter_types
    def contact_point(self: Self, value: "float"):
        self.wrapped.ContactPoint = float(value) if value is not None else 0.0

    @property
    def dynamic_viscosity_of_the_lubricant_at_contact_temperature(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.DynamicViscosityOfTheLubricantAtContactTemperature

        if temp is None:
            return 0.0

        return temp

    @dynamic_viscosity_of_the_lubricant_at_contact_temperature.setter
    @enforce_parameter_types
    def dynamic_viscosity_of_the_lubricant_at_contact_temperature(
        self: Self, value: "float"
    ):
        self.wrapped.DynamicViscosityOfTheLubricantAtContactTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def kinematic_viscosity_of_lubricant_at_contact_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.KinematicViscosityOfLubricantAtContactTemperature

        if temp is None:
            return 0.0

        return temp

    @kinematic_viscosity_of_lubricant_at_contact_temperature.setter
    @enforce_parameter_types
    def kinematic_viscosity_of_lubricant_at_contact_temperature(
        self: Self, value: "float"
    ):
        self.wrapped.KinematicViscosityOfLubricantAtContactTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def load_sharing_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @load_sharing_factor.setter
    @enforce_parameter_types
    def load_sharing_factor(self: Self, value: "float"):
        self.wrapped.LoadSharingFactor = float(value) if value is not None else 0.0

    @property
    def local_contact_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalContactTemperature

        if temp is None:
            return 0.0

        return temp

    @local_contact_temperature.setter
    @enforce_parameter_types
    def local_contact_temperature(self: Self, value: "float"):
        self.wrapped.LocalContactTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def local_flash_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @local_flash_temperature.setter
    @enforce_parameter_types
    def local_flash_temperature(self: Self, value: "float"):
        self.wrapped.LocalFlashTemperature = float(value) if value is not None else 0.0

    @property
    def local_hertzian_contact_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalHertzianContactStress

        if temp is None:
            return 0.0

        return temp

    @local_hertzian_contact_stress.setter
    @enforce_parameter_types
    def local_hertzian_contact_stress(self: Self, value: "float"):
        self.wrapped.LocalHertzianContactStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def local_load_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalLoadParameter

        if temp is None:
            return 0.0

        return temp

    @local_load_parameter.setter
    @enforce_parameter_types
    def local_load_parameter(self: Self, value: "float"):
        self.wrapped.LocalLoadParameter = float(value) if value is not None else 0.0

    @property
    def local_lubricant_film_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalLubricantFilmThickness

        if temp is None:
            return 0.0

        return temp

    @local_lubricant_film_thickness.setter
    @enforce_parameter_types
    def local_lubricant_film_thickness(self: Self, value: "float"):
        self.wrapped.LocalLubricantFilmThickness = (
            float(value) if value is not None else 0.0
        )

    @property
    def local_sliding_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalSlidingParameter

        if temp is None:
            return 0.0

        return temp

    @local_sliding_parameter.setter
    @enforce_parameter_types
    def local_sliding_parameter(self: Self, value: "float"):
        self.wrapped.LocalSlidingParameter = float(value) if value is not None else 0.0

    @property
    def local_sliding_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalSlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @local_sliding_velocity.setter
    @enforce_parameter_types
    def local_sliding_velocity(self: Self, value: "float"):
        self.wrapped.LocalSlidingVelocity = float(value) if value is not None else 0.0

    @property
    def local_velocity_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LocalVelocityParameter

        if temp is None:
            return 0.0

        return temp

    @local_velocity_parameter.setter
    @enforce_parameter_types
    def local_velocity_parameter(self: Self, value: "float"):
        self.wrapped.LocalVelocityParameter = float(value) if value is not None else 0.0

    @property
    def lubricant_density_at_contact_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LubricantDensityAtContactTemperature

        if temp is None:
            return 0.0

        return temp

    @lubricant_density_at_contact_temperature.setter
    @enforce_parameter_types
    def lubricant_density_at_contact_temperature(self: Self, value: "float"):
        self.wrapped.LubricantDensityAtContactTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def mesh(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Mesh

        if temp is None:
            return ""

        return temp

    @mesh.setter
    @enforce_parameter_types
    def mesh(self: Self, value: "str"):
        self.wrapped.Mesh = str(value) if value is not None else ""

    @property
    def normal_relative_radius_of_curvature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalRelativeRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @normal_relative_radius_of_curvature.setter
    @enforce_parameter_types
    def normal_relative_radius_of_curvature(self: Self, value: "float"):
        self.wrapped.NormalRelativeRadiusOfCurvature = (
            float(value) if value is not None else 0.0
        )

    @property
    def pinion_flank_radius_of_curvature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionFlankRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @pinion_flank_radius_of_curvature.setter
    @enforce_parameter_types
    def pinion_flank_radius_of_curvature(self: Self, value: "float"):
        self.wrapped.PinionFlankRadiusOfCurvature = (
            float(value) if value is not None else 0.0
        )

    @property
    def point_of_mesh(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PointOfMesh

        if temp is None:
            return ""

        return temp

    @property
    def pressure_viscosity_coefficient_at_contact_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureViscosityCoefficientAtContactTemperature

        if temp is None:
            return 0.0

        return temp

    @pressure_viscosity_coefficient_at_contact_temperature.setter
    @enforce_parameter_types
    def pressure_viscosity_coefficient_at_contact_temperature(
        self: Self, value: "float"
    ):
        self.wrapped.PressureViscosityCoefficientAtContactTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def sum_of_tangential_velocities(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SumOfTangentialVelocities

        if temp is None:
            return 0.0

        return temp

    @sum_of_tangential_velocities.setter
    @enforce_parameter_types
    def sum_of_tangential_velocities(self: Self, value: "float"):
        self.wrapped.SumOfTangentialVelocities = (
            float(value) if value is not None else 0.0
        )

    @property
    def transverse_relative_radius_of_curvature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TransverseRelativeRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @transverse_relative_radius_of_curvature.setter
    @enforce_parameter_types
    def transverse_relative_radius_of_curvature(self: Self, value: "float"):
        self.wrapped.TransverseRelativeRadiusOfCurvature = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_flank_radius_of_curvature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelFlankRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @wheel_flank_radius_of_curvature.setter
    @enforce_parameter_types
    def wheel_flank_radius_of_curvature(self: Self, value: "float"):
        self.wrapped.WheelFlankRadiusOfCurvature = (
            float(value) if value is not None else 0.0
        )

    @property
    def position_on_pinion(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOnPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def position_on_wheel(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOnWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "MicroPittingResultsRow._Cast_MicroPittingResultsRow":
        return self._Cast_MicroPittingResultsRow(self)
