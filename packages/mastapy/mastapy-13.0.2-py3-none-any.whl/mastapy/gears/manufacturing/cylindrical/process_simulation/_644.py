"""ShapingProcessSimulation"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.cylindrical.process_simulation import _642
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAPING_PROCESS_SIMULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.ProcessSimulation",
    "ShapingProcessSimulation",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShapingProcessSimulation",)


Self = TypeVar("Self", bound="ShapingProcessSimulation")


class ShapingProcessSimulation(_642.CutterProcessSimulation):
    """ShapingProcessSimulation

    This is a mastapy class.
    """

    TYPE = _SHAPING_PROCESS_SIMULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShapingProcessSimulation")

    class _Cast_ShapingProcessSimulation:
        """Special nested class for casting ShapingProcessSimulation to subclasses."""

        def __init__(
            self: "ShapingProcessSimulation._Cast_ShapingProcessSimulation",
            parent: "ShapingProcessSimulation",
        ):
            self._parent = parent

        @property
        def cutter_process_simulation(
            self: "ShapingProcessSimulation._Cast_ShapingProcessSimulation",
        ) -> "_642.CutterProcessSimulation":
            return self._parent._cast(_642.CutterProcessSimulation)

        @property
        def shaping_process_simulation(
            self: "ShapingProcessSimulation._Cast_ShapingProcessSimulation",
        ) -> "ShapingProcessSimulation":
            return self._parent

        def __getattr__(
            self: "ShapingProcessSimulation._Cast_ShapingProcessSimulation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShapingProcessSimulation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def circle_blade_flank_angle_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CircleBladeFlankAngleError

        if temp is None:
            return 0.0

        return temp

    @circle_blade_flank_angle_error.setter
    @enforce_parameter_types
    def circle_blade_flank_angle_error(self: Self, value: "float"):
        self.wrapped.CircleBladeFlankAngleError = (
            float(value) if value is not None else 0.0
        )

    @property
    def circle_blade_rake_angle_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CircleBladeRakeAngleError

        if temp is None:
            return 0.0

        return temp

    @circle_blade_rake_angle_error.setter
    @enforce_parameter_types
    def circle_blade_rake_angle_error(self: Self, value: "float"):
        self.wrapped.CircleBladeRakeAngleError = (
            float(value) if value is not None else 0.0
        )

    @property
    def circumstance_feed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CircumstanceFeed

        if temp is None:
            return 0.0

        return temp

    @circumstance_feed.setter
    @enforce_parameter_types
    def circumstance_feed(self: Self, value: "float"):
        self.wrapped.CircumstanceFeed = float(value) if value is not None else 0.0

    @property
    def deviation_in_x_direction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeviationInXDirection

        if temp is None:
            return 0.0

        return temp

    @deviation_in_x_direction.setter
    @enforce_parameter_types
    def deviation_in_x_direction(self: Self, value: "float"):
        self.wrapped.DeviationInXDirection = float(value) if value is not None else 0.0

    @property
    def deviation_in_y_direction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeviationInYDirection

        if temp is None:
            return 0.0

        return temp

    @deviation_in_y_direction.setter
    @enforce_parameter_types
    def deviation_in_y_direction(self: Self, value: "float"):
        self.wrapped.DeviationInYDirection = float(value) if value is not None else 0.0

    @property
    def distance_between_two_sections(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceBetweenTwoSections

        if temp is None:
            return 0.0

        return temp

    @distance_between_two_sections.setter
    @enforce_parameter_types
    def distance_between_two_sections(self: Self, value: "float"):
        self.wrapped.DistanceBetweenTwoSections = (
            float(value) if value is not None else 0.0
        )

    @property
    def eap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def face_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceRunout

        if temp is None:
            return 0.0

        return temp

    @face_runout.setter
    @enforce_parameter_types
    def face_runout(self: Self, value: "float"):
        self.wrapped.FaceRunout = float(value) if value is not None else 0.0

    @property
    def face_runout_check_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceRunoutCheckDiameter

        if temp is None:
            return 0.0

        return temp

    @face_runout_check_diameter.setter
    @enforce_parameter_types
    def face_runout_check_diameter(self: Self, value: "float"):
        self.wrapped.FaceRunoutCheckDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Factor

        if temp is None:
            return 0.0

        return temp

    @factor.setter
    @enforce_parameter_types
    def factor(self: Self, value: "float"):
        self.wrapped.Factor = float(value) if value is not None else 0.0

    @property
    def first_phase_maximum_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstPhaseMaximumAngle

        if temp is None:
            return 0.0

        return temp

    @first_phase_maximum_angle.setter
    @enforce_parameter_types
    def first_phase_maximum_angle(self: Self, value: "float"):
        self.wrapped.FirstPhaseMaximumAngle = float(value) if value is not None else 0.0

    @property
    def first_section_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FirstSectionRunout

        if temp is None:
            return 0.0

        return temp

    @first_section_runout.setter
    @enforce_parameter_types
    def first_section_runout(self: Self, value: "float"):
        self.wrapped.FirstSectionRunout = float(value) if value is not None else 0.0

    @property
    def pressure_angle_error_left_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngleErrorLeftFlank

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_error_left_flank.setter
    @enforce_parameter_types
    def pressure_angle_error_left_flank(self: Self, value: "float"):
        self.wrapped.PressureAngleErrorLeftFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def pressure_angle_error_right_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngleErrorRightFlank

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_error_right_flank.setter
    @enforce_parameter_types
    def pressure_angle_error_right_flank(self: Self, value: "float"):
        self.wrapped.PressureAngleErrorRightFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_lower_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationLowerLimit

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_lower_limit.setter
    @enforce_parameter_types
    def profile_evaluation_lower_limit(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationLowerLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_evaluation_upper_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProfileEvaluationUpperLimit

        if temp is None:
            return 0.0

        return temp

    @profile_evaluation_upper_limit.setter
    @enforce_parameter_types
    def profile_evaluation_upper_limit(self: Self, value: "float"):
        self.wrapped.ProfileEvaluationUpperLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def second_phase_max_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SecondPhaseMaxAngle

        if temp is None:
            return 0.0

        return temp

    @second_phase_max_angle.setter
    @enforce_parameter_types
    def second_phase_max_angle(self: Self, value: "float"):
        self.wrapped.SecondPhaseMaxAngle = float(value) if value is not None else 0.0

    @property
    def second_section_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SecondSectionRunout

        if temp is None:
            return 0.0

        return temp

    @second_section_runout.setter
    @enforce_parameter_types
    def second_section_runout(self: Self, value: "float"):
        self.wrapped.SecondSectionRunout = float(value) if value is not None else 0.0

    @property
    def shaper_cumulative_pitch_error_left_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaperCumulativePitchErrorLeftFlank

        if temp is None:
            return 0.0

        return temp

    @shaper_cumulative_pitch_error_left_flank.setter
    @enforce_parameter_types
    def shaper_cumulative_pitch_error_left_flank(self: Self, value: "float"):
        self.wrapped.ShaperCumulativePitchErrorLeftFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaper_cumulative_pitch_error_right_flank(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaperCumulativePitchErrorRightFlank

        if temp is None:
            return 0.0

        return temp

    @shaper_cumulative_pitch_error_right_flank.setter
    @enforce_parameter_types
    def shaper_cumulative_pitch_error_right_flank(self: Self, value: "float"):
        self.wrapped.ShaperCumulativePitchErrorRightFlank = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaper_radial_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaperRadialRunout

        if temp is None:
            return 0.0

        return temp

    @shaper_radial_runout.setter
    @enforce_parameter_types
    def shaper_radial_runout(self: Self, value: "float"):
        self.wrapped.ShaperRadialRunout = float(value) if value is not None else 0.0

    @property
    def shaper_stoke(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaperStoke

        if temp is None:
            return 0.0

        return temp

    @shaper_stoke.setter
    @enforce_parameter_types
    def shaper_stoke(self: Self, value: "float"):
        self.wrapped.ShaperStoke = float(value) if value is not None else 0.0

    @property
    def shaper_tilt_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaperTiltAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def spindle_angle_at_maximum_face_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpindleAngleAtMaximumFaceRunout

        if temp is None:
            return 0.0

        return temp

    @spindle_angle_at_maximum_face_runout.setter
    @enforce_parameter_types
    def spindle_angle_at_maximum_face_runout(self: Self, value: "float"):
        self.wrapped.SpindleAngleAtMaximumFaceRunout = (
            float(value) if value is not None else 0.0
        )

    @property
    def spindle_angle_at_maximum_radial_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpindleAngleAtMaximumRadialRunout

        if temp is None:
            return 0.0

        return temp

    @spindle_angle_at_maximum_radial_runout.setter
    @enforce_parameter_types
    def spindle_angle_at_maximum_radial_runout(self: Self, value: "float"):
        self.wrapped.SpindleAngleAtMaximumRadialRunout = (
            float(value) if value is not None else 0.0
        )

    @property
    def test_distance_in_x_direction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TestDistanceInXDirection

        if temp is None:
            return 0.0

        return temp

    @test_distance_in_x_direction.setter
    @enforce_parameter_types
    def test_distance_in_x_direction(self: Self, value: "float"):
        self.wrapped.TestDistanceInXDirection = (
            float(value) if value is not None else 0.0
        )

    @property
    def test_distance_in_y_direction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TestDistanceInYDirection

        if temp is None:
            return 0.0

        return temp

    @test_distance_in_y_direction.setter
    @enforce_parameter_types
    def test_distance_in_y_direction(self: Self, value: "float"):
        self.wrapped.TestDistanceInYDirection = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_sin_curve_for_shaper_pitch_error(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSinCurveForShaperPitchError

        if temp is None:
            return False

        return temp

    @use_sin_curve_for_shaper_pitch_error.setter
    @enforce_parameter_types
    def use_sin_curve_for_shaper_pitch_error(self: Self, value: "bool"):
        self.wrapped.UseSinCurveForShaperPitchError = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ShapingProcessSimulation._Cast_ShapingProcessSimulation":
        return self._Cast_ShapingProcessSimulation(self)
