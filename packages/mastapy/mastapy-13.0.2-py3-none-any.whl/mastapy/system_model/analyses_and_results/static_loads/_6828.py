"""BearingLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List


from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import (
    constructor,
    enum_with_selected_value_runtime,
    overridable_enum_runtime,
    conversion,
)
from mastapy.bearings.bearing_results.rolling import _1973, _1974, _1979, _2076
from mastapy.materials.efficiency import _295
from mastapy.system_model.part_model import _2447
from mastapy.math_utility.hertzian_contact import _1580
from mastapy.bearings.bearing_results import _1949
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results.static_loads import _6859
from mastapy._internal.cast_exception import CastException

_ARRAY = python_net_import("System", "Array")
_BEARING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BearingLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
    from mastapy.utility import _1596
    from mastapy.system_model.part_model import _2446
    from mastapy.math_utility.measured_vectors import _1571
    from mastapy.bearings.bearing_results.rolling.dysla import _2121
    from mastapy.bearings.bearing_results.rolling import _2077
    from mastapy.bearings.tolerances import _1921, _1927
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BearingLoadCase",)


Self = TypeVar("Self", bound="BearingLoadCase")


class BearingLoadCase(_6859.ConnectorLoadCase):
    """BearingLoadCase

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingLoadCase")

    class _Cast_BearingLoadCase:
        """Special nested class for casting BearingLoadCase to subclasses."""

        def __init__(
            self: "BearingLoadCase._Cast_BearingLoadCase", parent: "BearingLoadCase"
        ):
            self._parent = parent

        @property
        def connector_load_case(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "_6859.ConnectorLoadCase":
            return self._parent._cast(_6859.ConnectorLoadCase)

        @property
        def mountable_component_load_case(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_load_case(
            self: "BearingLoadCase._Cast_BearingLoadCase",
        ) -> "BearingLoadCase":
            return self._parent

        def __getattr__(self: "BearingLoadCase._Cast_BearingLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_displacement_preload(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialDisplacementPreload

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_displacement_preload.setter
    @enforce_parameter_types
    def axial_displacement_preload(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialDisplacementPreload = value

    @property
    def axial_force_preload(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialForcePreload

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_force_preload.setter
    @enforce_parameter_types
    def axial_force_preload(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialForcePreload = value

    @property
    def axial_internal_clearance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_internal_clearance.setter
    @enforce_parameter_types
    def axial_internal_clearance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialInternalClearance = value

    @property
    def axial_internal_clearance_tolerance_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AxialInternalClearanceToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @axial_internal_clearance_tolerance_factor.setter
    @enforce_parameter_types
    def axial_internal_clearance_tolerance_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AxialInternalClearanceToleranceFactor = value

    @property
    def ball_bearing_analysis_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BallBearingAnalysisMethod":
        """EnumWithSelectedValue[mastapy.bearings.bearing_results.rolling.BallBearingAnalysisMethod]"""
        temp = self.wrapped.BallBearingAnalysisMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BallBearingAnalysisMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @ball_bearing_analysis_method.setter
    @enforce_parameter_types
    def ball_bearing_analysis_method(
        self: Self, value: "_1973.BallBearingAnalysisMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BallBearingAnalysisMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BallBearingAnalysisMethod = value

    @property
    def ball_bearing_contact_calculation(
        self: Self,
    ) -> "overridable.Overridable_BallBearingContactCalculation":
        """Overridable[mastapy.bearings.bearing_results.rolling.BallBearingContactCalculation]"""
        temp = self.wrapped.BallBearingContactCalculation

        if temp is None:
            return None

        value = overridable.Overridable_BallBearingContactCalculation.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @ball_bearing_contact_calculation.setter
    @enforce_parameter_types
    def ball_bearing_contact_calculation(
        self: Self,
        value: "Union[_1974.BallBearingContactCalculation, Tuple[_1974.BallBearingContactCalculation, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_BallBearingContactCalculation.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_BallBearingContactCalculation.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.BallBearingContactCalculation = value

    @property
    def ball_bearing_friction_model_for_gyroscopic_moment(
        self: Self,
    ) -> "overridable.Overridable_FrictionModelForGyroscopicMoment":
        """Overridable[mastapy.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment]"""
        temp = self.wrapped.BallBearingFrictionModelForGyroscopicMoment

        if temp is None:
            return None

        value = overridable.Overridable_FrictionModelForGyroscopicMoment.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @ball_bearing_friction_model_for_gyroscopic_moment.setter
    @enforce_parameter_types
    def ball_bearing_friction_model_for_gyroscopic_moment(
        self: Self,
        value: "Union[_1979.FrictionModelForGyroscopicMoment, Tuple[_1979.FrictionModelForGyroscopicMoment, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_FrictionModelForGyroscopicMoment.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_FrictionModelForGyroscopicMoment.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.BallBearingFrictionModelForGyroscopicMoment = value

    @property
    def bearing_life_adjustment_factor_for_operating_conditions(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bearing_life_adjustment_factor_for_operating_conditions.setter
    @enforce_parameter_types
    def bearing_life_adjustment_factor_for_operating_conditions(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions = value

    @property
    def bearing_life_adjustment_factor_for_special_bearing_properties(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bearing_life_adjustment_factor_for_special_bearing_properties.setter
    @enforce_parameter_types
    def bearing_life_adjustment_factor_for_special_bearing_properties(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties = value

    @property
    def bearing_life_modification_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.BearingLifeModificationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bearing_life_modification_factor.setter
    @enforce_parameter_types
    def bearing_life_modification_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.BearingLifeModificationFactor = value

    @property
    def bearing_stiffness_model(self: Self) -> "_5394.BearingStiffnessModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.BearingStiffnessModel"""
        temp = self.wrapped.BearingStiffnessModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.BearingStiffnessModel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5394",
            "BearingStiffnessModel",
        )(value)

    @bearing_stiffness_model.setter
    @enforce_parameter_types
    def bearing_stiffness_model(self: Self, value: "_5394.BearingStiffnessModel"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.BearingStiffnessModel",
        )
        self.wrapped.BearingStiffnessModel = value

    @property
    def bearing_stiffness_model_used_in_analysis(
        self: Self,
    ) -> "_5394.BearingStiffnessModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.BearingStiffnessModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingStiffnessModelUsedInAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.BearingStiffnessModel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5394",
            "BearingStiffnessModel",
        )(value)

    @property
    def coefficient_of_friction(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @coefficient_of_friction.setter
    @enforce_parameter_types
    def coefficient_of_friction(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CoefficientOfFriction = value

    @property
    def contact_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ContactAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @contact_angle.setter
    @enforce_parameter_types
    def contact_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ContactAngle = value

    @property
    def contact_stiffness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @contact_stiffness.setter
    @enforce_parameter_types
    def contact_stiffness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ContactStiffness = value

    @property
    def diametrical_clearance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiametricalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diametrical_clearance.setter
    @enforce_parameter_types
    def diametrical_clearance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiametricalClearance = value

    @property
    def drag_scaling_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DragScalingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @drag_scaling_factor.setter
    @enforce_parameter_types
    def drag_scaling_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DragScalingFactor = value

    @property
    def efficiency_rating_method(
        self: Self,
    ) -> "overridable.Overridable_BearingEfficiencyRatingMethod":
        """Overridable[mastapy.materials.efficiency.BearingEfficiencyRatingMethod]"""
        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = overridable.Overridable_BearingEfficiencyRatingMethod.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @efficiency_rating_method.setter
    @enforce_parameter_types
    def efficiency_rating_method(
        self: Self,
        value: "Union[_295.BearingEfficiencyRatingMethod, Tuple[_295.BearingEfficiencyRatingMethod, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_BearingEfficiencyRatingMethod.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_BearingEfficiencyRatingMethod.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def element_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_temperature.setter
    @enforce_parameter_types
    def element_temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementTemperature = value

    @property
    def first_element_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FirstElementAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @first_element_angle.setter
    @enforce_parameter_types
    def first_element_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FirstElementAngle = value

    @property
    def force_at_zero_displacement_input_method(
        self: Self,
    ) -> "overridable.Overridable_BearingF0InputMethod":
        """Overridable[mastapy.system_model.part_model.BearingF0InputMethod]"""
        temp = self.wrapped.ForceAtZeroDisplacementInputMethod

        if temp is None:
            return None

        value = overridable.Overridable_BearingF0InputMethod.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @force_at_zero_displacement_input_method.setter
    @enforce_parameter_types
    def force_at_zero_displacement_input_method(
        self: Self,
        value: "Union[_2447.BearingF0InputMethod, Tuple[_2447.BearingF0InputMethod, bool]]",
    ):
        wrapper_type = overridable.Overridable_BearingF0InputMethod.wrapper_type()
        enclosed_type = overridable.Overridable_BearingF0InputMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.ForceAtZeroDisplacementInputMethod = value

    @property
    def grid_refinement_factor_contact_width(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.GridRefinementFactorContactWidth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @grid_refinement_factor_contact_width.setter
    @enforce_parameter_types
    def grid_refinement_factor_contact_width(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.GridRefinementFactorContactWidth = value

    @property
    def grid_refinement_factor_rib_height(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.GridRefinementFactorRibHeight

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @grid_refinement_factor_rib_height.setter
    @enforce_parameter_types
    def grid_refinement_factor_rib_height(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.GridRefinementFactorRibHeight = value

    @property
    def heat_due_to_external_cooling_or_heating(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.HeatDueToExternalCoolingOrHeating

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @heat_due_to_external_cooling_or_heating.setter
    @enforce_parameter_types
    def heat_due_to_external_cooling_or_heating(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.HeatDueToExternalCoolingOrHeating = value

    @property
    def hertzian_contact_deflection_calculation_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod":
        """EnumWithSelectedValue[mastapy.math_utility.hertzian_contact.HertzianContactDeflectionCalculationMethod]"""
        temp = self.wrapped.HertzianContactDeflectionCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @hertzian_contact_deflection_calculation_method.setter
    @enforce_parameter_types
    def hertzian_contact_deflection_calculation_method(
        self: Self, value: "_1580.HertzianContactDeflectionCalculationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.HertzianContactDeflectionCalculationMethod = value

    @property
    def include_fitting_effects(self: Self) -> "_1596.LoadCaseOverrideOption":
        """mastapy.utility.LoadCaseOverrideOption"""
        temp = self.wrapped.IncludeFittingEffects

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility._1596", "LoadCaseOverrideOption"
        )(value)

    @include_fitting_effects.setter
    @enforce_parameter_types
    def include_fitting_effects(self: Self, value: "_1596.LoadCaseOverrideOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )
        self.wrapped.IncludeFittingEffects = value

    @property
    def include_heat_emitted_by_lubricant_in_thermal_limiting_speed_calculation(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.IncludeHeatEmittedByLubricantInThermalLimitingSpeedCalculation
        )

        if temp is None:
            return False

        return temp

    @include_heat_emitted_by_lubricant_in_thermal_limiting_speed_calculation.setter
    @enforce_parameter_types
    def include_heat_emitted_by_lubricant_in_thermal_limiting_speed_calculation(
        self: Self, value: "bool"
    ):
        self.wrapped.IncludeHeatEmittedByLubricantInThermalLimitingSpeedCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def include_rib_contact_analysis(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.IncludeRibContactAnalysis

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @include_rib_contact_analysis.setter
    @enforce_parameter_types
    def include_rib_contact_analysis(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.IncludeRibContactAnalysis = value

    @property
    def include_ring_ovality(self: Self) -> "_1596.LoadCaseOverrideOption":
        """mastapy.utility.LoadCaseOverrideOption"""
        temp = self.wrapped.IncludeRingOvality

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility._1596", "LoadCaseOverrideOption"
        )(value)

    @include_ring_ovality.setter
    @enforce_parameter_types
    def include_ring_ovality(self: Self, value: "_1596.LoadCaseOverrideOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )
        self.wrapped.IncludeRingOvality = value

    @property
    def include_thermal_expansion_effects(self: Self) -> "_1596.LoadCaseOverrideOption":
        """mastapy.utility.LoadCaseOverrideOption"""
        temp = self.wrapped.IncludeThermalExpansionEffects

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility._1596", "LoadCaseOverrideOption"
        )(value)

    @include_thermal_expansion_effects.setter
    @enforce_parameter_types
    def include_thermal_expansion_effects(
        self: Self, value: "_1596.LoadCaseOverrideOption"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.LoadCaseOverrideOption"
        )
        self.wrapped.IncludeThermalExpansionEffects = value

    @property
    def inner_mounting_sleeve_bore_tolerance_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerMountingSleeveBoreToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_mounting_sleeve_bore_tolerance_factor.setter
    @enforce_parameter_types
    def inner_mounting_sleeve_bore_tolerance_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerMountingSleeveBoreToleranceFactor = value

    @property
    def inner_mounting_sleeve_outer_diameter_tolerance_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerMountingSleeveOuterDiameterToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_mounting_sleeve_outer_diameter_tolerance_factor.setter
    @enforce_parameter_types
    def inner_mounting_sleeve_outer_diameter_tolerance_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerMountingSleeveOuterDiameterToleranceFactor = value

    @property
    def inner_mounting_sleeve_temperature(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerMountingSleeveTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_mounting_sleeve_temperature.setter
    @enforce_parameter_types
    def inner_mounting_sleeve_temperature(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerMountingSleeveTemperature = value

    @property
    def inner_node_meaning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerNodeMeaning

        if temp is None:
            return ""

        return temp

    @property
    def lubricant_feed_pressure(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LubricantFeedPressure

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @lubricant_feed_pressure.setter
    @enforce_parameter_types
    def lubricant_feed_pressure(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LubricantFeedPressure = value

    @property
    def lubricant_film_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LubricantFilmTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @lubricant_film_temperature.setter
    @enforce_parameter_types
    def lubricant_film_temperature(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LubricantFilmTemperature = value

    @property
    def lubricant_flow_rate(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LubricantFlowRate

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @lubricant_flow_rate.setter
    @enforce_parameter_types
    def lubricant_flow_rate(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LubricantFlowRate = value

    @property
    def lubricant_windage_ampersand_churning_temperature(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LubricantWindageAmpersandChurningTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @lubricant_windage_ampersand_churning_temperature.setter
    @enforce_parameter_types
    def lubricant_windage_ampersand_churning_temperature(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LubricantWindageAmpersandChurningTemperature = value

    @property
    def maximum_friction_coefficient_for_ball_bearing_analysis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumFrictionCoefficientForBallBearingAnalysis

        if temp is None:
            return 0.0

        return temp

    @maximum_friction_coefficient_for_ball_bearing_analysis.setter
    @enforce_parameter_types
    def maximum_friction_coefficient_for_ball_bearing_analysis(
        self: Self, value: "float"
    ):
        self.wrapped.MaximumFrictionCoefficientForBallBearingAnalysis = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_clearance_for_ribs(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumClearanceForRibs

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_clearance_for_ribs.setter
    @enforce_parameter_types
    def minimum_clearance_for_ribs(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumClearanceForRibs = value

    @property
    def minimum_force_for_bearing_to_be_considered_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumForceForBearingToBeConsideredLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_force_for_bearing_to_be_considered_loaded.setter
    @enforce_parameter_types
    def minimum_force_for_bearing_to_be_considered_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumForceForBearingToBeConsideredLoaded = value

    @property
    def minimum_force_for_six_degree_of_freedom_models(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumForceForSixDegreeOfFreedomModels

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_force_for_six_degree_of_freedom_models.setter
    @enforce_parameter_types
    def minimum_force_for_six_degree_of_freedom_models(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumForceForSixDegreeOfFreedomModels = value

    @property
    def minimum_moment_for_bearing_to_be_considered_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumMomentForBearingToBeConsideredLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_moment_for_bearing_to_be_considered_loaded.setter
    @enforce_parameter_types
    def minimum_moment_for_bearing_to_be_considered_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumMomentForBearingToBeConsideredLoaded = value

    @property
    def model_bearing_mounting_clearances_automatically(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.ModelBearingMountingClearancesAutomatically

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @model_bearing_mounting_clearances_automatically.setter
    @enforce_parameter_types
    def model_bearing_mounting_clearances_automatically(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.ModelBearingMountingClearancesAutomatically = value

    @property
    def number_of_grid_points_across_rib_contact_width(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfGridPointsAcrossRibContactWidth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_grid_points_across_rib_contact_width.setter
    @enforce_parameter_types
    def number_of_grid_points_across_rib_contact_width(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfGridPointsAcrossRibContactWidth = value

    @property
    def number_of_grid_points_across_rib_height(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfGridPointsAcrossRibHeight

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_grid_points_across_rib_height.setter
    @enforce_parameter_types
    def number_of_grid_points_across_rib_height(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfGridPointsAcrossRibHeight = value

    @property
    def number_of_strips_for_roller_calculation(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfStripsForRollerCalculation

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_strips_for_roller_calculation.setter
    @enforce_parameter_types
    def number_of_strips_for_roller_calculation(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfStripsForRollerCalculation = value

    @property
    def oil_dip_coefficient(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OilDipCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @oil_dip_coefficient.setter
    @enforce_parameter_types
    def oil_dip_coefficient(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OilDipCoefficient = value

    @property
    def oil_inlet_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OilInletTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @oil_inlet_temperature.setter
    @enforce_parameter_types
    def oil_inlet_temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OilInletTemperature = value

    @property
    def oil_level(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OilLevel

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @oil_level.setter
    @enforce_parameter_types
    def oil_level(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OilLevel = value

    @property
    def outer_mounting_sleeve_bore_tolerance_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterMountingSleeveBoreToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_mounting_sleeve_bore_tolerance_factor.setter
    @enforce_parameter_types
    def outer_mounting_sleeve_bore_tolerance_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterMountingSleeveBoreToleranceFactor = value

    @property
    def outer_mounting_sleeve_outer_diameter_tolerance_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterMountingSleeveOuterDiameterToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_mounting_sleeve_outer_diameter_tolerance_factor.setter
    @enforce_parameter_types
    def outer_mounting_sleeve_outer_diameter_tolerance_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterMountingSleeveOuterDiameterToleranceFactor = value

    @property
    def outer_mounting_sleeve_temperature(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterMountingSleeveTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_mounting_sleeve_temperature.setter
    @enforce_parameter_types
    def outer_mounting_sleeve_temperature(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterMountingSleeveTemperature = value

    @property
    def outer_node_meaning(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterNodeMeaning

        if temp is None:
            return ""

        return temp

    @property
    def override_all_planets_inner_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideAllPlanetsInnerSupportDetail

        if temp is None:
            return False

        return temp

    @override_all_planets_inner_support_detail.setter
    @enforce_parameter_types
    def override_all_planets_inner_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideAllPlanetsInnerSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_all_planets_left_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideAllPlanetsLeftSupportDetail

        if temp is None:
            return False

        return temp

    @override_all_planets_left_support_detail.setter
    @enforce_parameter_types
    def override_all_planets_left_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideAllPlanetsLeftSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_all_planets_outer_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideAllPlanetsOuterSupportDetail

        if temp is None:
            return False

        return temp

    @override_all_planets_outer_support_detail.setter
    @enforce_parameter_types
    def override_all_planets_outer_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideAllPlanetsOuterSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_all_planets_right_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideAllPlanetsRightSupportDetail

        if temp is None:
            return False

        return temp

    @override_all_planets_right_support_detail.setter
    @enforce_parameter_types
    def override_all_planets_right_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideAllPlanetsRightSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_design_inner_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignInnerSupportDetail

        if temp is None:
            return False

        return temp

    @override_design_inner_support_detail.setter
    @enforce_parameter_types
    def override_design_inner_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideDesignInnerSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_design_left_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignLeftSupportDetail

        if temp is None:
            return False

        return temp

    @override_design_left_support_detail.setter
    @enforce_parameter_types
    def override_design_left_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideDesignLeftSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_design_outer_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignOuterSupportDetail

        if temp is None:
            return False

        return temp

    @override_design_outer_support_detail.setter
    @enforce_parameter_types
    def override_design_outer_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideDesignOuterSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_design_right_support_detail(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignRightSupportDetail

        if temp is None:
            return False

        return temp

    @override_design_right_support_detail.setter
    @enforce_parameter_types
    def override_design_right_support_detail(self: Self, value: "bool"):
        self.wrapped.OverrideDesignRightSupportDetail = (
            bool(value) if value is not None else False
        )

    @property
    def override_design_specified_stiffness_matrix(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignSpecifiedStiffnessMatrix

        if temp is None:
            return False

        return temp

    @override_design_specified_stiffness_matrix.setter
    @enforce_parameter_types
    def override_design_specified_stiffness_matrix(self: Self, value: "bool"):
        self.wrapped.OverrideDesignSpecifiedStiffnessMatrix = (
            bool(value) if value is not None else False
        )

    @property
    def permissible_axial_load_calculation_method(
        self: Self,
    ) -> "overridable.Overridable_CylindricalRollerMaxAxialLoadMethod":
        """Overridable[mastapy.bearings.bearing_results.CylindricalRollerMaxAxialLoadMethod]"""
        temp = self.wrapped.PermissibleAxialLoadCalculationMethod

        if temp is None:
            return None

        value = (
            overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapped_type()
        )
        return overridable_enum_runtime.create(temp, value)

    @permissible_axial_load_calculation_method.setter
    @enforce_parameter_types
    def permissible_axial_load_calculation_method(
        self: Self,
        value: "Union[_1949.CylindricalRollerMaxAxialLoadMethod, Tuple[_1949.CylindricalRollerMaxAxialLoadMethod, bool]]",
    ):
        wrapper_type = (
            overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapper_type()
        )
        enclosed_type = (
            overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.PermissibleAxialLoadCalculationMethod = value

    @property
    def preload_spring_initial_compression(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PreloadSpringInitialCompression

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @preload_spring_initial_compression.setter
    @enforce_parameter_types
    def preload_spring_initial_compression(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PreloadSpringInitialCompression = value

    @property
    def radial_internal_clearance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_internal_clearance.setter
    @enforce_parameter_types
    def radial_internal_clearance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialInternalClearance = value

    @property
    def radial_internal_clearance_tolerance_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialInternalClearanceToleranceFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_internal_clearance_tolerance_factor.setter
    @enforce_parameter_types
    def radial_internal_clearance_tolerance_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialInternalClearanceToleranceFactor = value

    @property
    def refine_grid_around_contact_point(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.RefineGridAroundContactPoint

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @refine_grid_around_contact_point.setter
    @enforce_parameter_types
    def refine_grid_around_contact_point(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.RefineGridAroundContactPoint = value

    @property
    def ring_ovality_scaling(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RingOvalityScaling

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ring_ovality_scaling.setter
    @enforce_parameter_types
    def ring_ovality_scaling(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RingOvalityScaling = value

    @property
    def roller_analysis_method(
        self: Self,
    ) -> "overridable.Overridable_RollerAnalysisMethod":
        """Overridable[mastapy.bearings.bearing_results.rolling.RollerAnalysisMethod]"""
        temp = self.wrapped.RollerAnalysisMethod

        if temp is None:
            return None

        value = overridable.Overridable_RollerAnalysisMethod.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @roller_analysis_method.setter
    @enforce_parameter_types
    def roller_analysis_method(
        self: Self,
        value: "Union[_2076.RollerAnalysisMethod, Tuple[_2076.RollerAnalysisMethod, bool]]",
    ):
        wrapper_type = overridable.Overridable_RollerAnalysisMethod.wrapper_type()
        enclosed_type = overridable.Overridable_RollerAnalysisMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.RollerAnalysisMethod = value

    @property
    def rolling_frictional_moment_factor_for_newly_greased_bearing(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RollingFrictionalMomentFactorForNewlyGreasedBearing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rolling_frictional_moment_factor_for_newly_greased_bearing.setter
    @enforce_parameter_types
    def rolling_frictional_moment_factor_for_newly_greased_bearing(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RollingFrictionalMomentFactorForNewlyGreasedBearing = value

    @property
    def set_first_element_angle_to_load_direction(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.SetFirstElementAngleToLoadDirection

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @set_first_element_angle_to_load_direction.setter
    @enforce_parameter_types
    def set_first_element_angle_to_load_direction(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.SetFirstElementAngleToLoadDirection = value

    @property
    def use_advanced_film_temperature_calculation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedFilmTemperatureCalculation

        if temp is None:
            return False

        return temp

    @use_advanced_film_temperature_calculation.setter
    @enforce_parameter_types
    def use_advanced_film_temperature_calculation(self: Self, value: "bool"):
        self.wrapped.UseAdvancedFilmTemperatureCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def use_design_friction_coefficients(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignFrictionCoefficients

        if temp is None:
            return False

        return temp

    @use_design_friction_coefficients.setter
    @enforce_parameter_types
    def use_design_friction_coefficients(self: Self, value: "bool"):
        self.wrapped.UseDesignFrictionCoefficients = (
            bool(value) if value is not None else False
        )

    @property
    def use_element_contact_angles_for_angular_velocities_in_ball_bearing(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearing

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_element_contact_angles_for_angular_velocities_in_ball_bearing.setter
    @enforce_parameter_types
    def use_element_contact_angles_for_angular_velocities_in_ball_bearing(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearing = value

    @property
    def use_mean_values_in_ball_bearing_friction_analysis(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMeanValuesInBallBearingFrictionAnalysis

        if temp is None:
            return False

        return temp

    @use_mean_values_in_ball_bearing_friction_analysis.setter
    @enforce_parameter_types
    def use_mean_values_in_ball_bearing_friction_analysis(self: Self, value: "bool"):
        self.wrapped.UseMeanValuesInBallBearingFrictionAnalysis = (
            bool(value) if value is not None else False
        )

    @property
    def use_node_per_row_inner(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseNodePerRowInner

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_node_per_row_inner.setter
    @enforce_parameter_types
    def use_node_per_row_inner(self: Self, value: "Union[bool, Tuple[bool, bool]]"):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseNodePerRowInner = value

    @property
    def use_node_per_row_outer(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseNodePerRowOuter

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_node_per_row_outer.setter
    @enforce_parameter_types
    def use_node_per_row_outer(self: Self, value: "Union[bool, Tuple[bool, bool]]"):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseNodePerRowOuter = value

    @property
    def use_specified_contact_stiffness(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.UseSpecifiedContactStiffness

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @use_specified_contact_stiffness.setter
    @enforce_parameter_types
    def use_specified_contact_stiffness(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.UseSpecifiedContactStiffness = value

    @property
    def viscosity_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ViscosityRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @viscosity_ratio.setter
    @enforce_parameter_types
    def viscosity_ratio(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ViscosityRatio = value

    @property
    def x_stiffness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.XStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @x_stiffness.setter
    @enforce_parameter_types
    def x_stiffness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.XStiffness = value

    @property
    def y_stiffness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.YStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @y_stiffness.setter
    @enforce_parameter_types
    def y_stiffness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.YStiffness = value

    @property
    def component_design(self: Self) -> "_2446.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def displacement_for_stiffness_operating_point(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementForStiffnessOperatingPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_analysis_options(self: Self) -> "_2121.DynamicBearingAnalysisOptions":
        """mastapy.bearings.bearing_results.rolling.dysla.DynamicBearingAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_at_zero_displacement(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceAtZeroDisplacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_for_stiffness_operating_point(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceForStiffnessOperatingPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def friction_coefficients(self: Self) -> "_2077.RollingBearingFrictionCoefficients":
        """mastapy.bearings.bearing_results.rolling.RollingBearingFrictionCoefficients

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionCoefficients

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_ring_detail(self: Self) -> "_1921.RaceDetail":
        """mastapy.bearings.tolerances.RaceDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRingDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_support_detail(self: Self) -> "_1927.SupportDetail":
        """mastapy.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_ring_detail(self: Self) -> "_1921.RaceDetail":
        """mastapy.bearings.tolerances.RaceDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftRingDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_support_detail(self: Self) -> "_1927.SupportDetail":
        """mastapy.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_ring_detail(self: Self) -> "_1921.RaceDetail":
        """mastapy.bearings.tolerances.RaceDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRingDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_support_detail(self: Self) -> "_1927.SupportDetail":
        """mastapy.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_ring_detail(self: Self) -> "_1921.RaceDetail":
        """mastapy.bearings.tolerances.RaceDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightRingDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_support_detail(self: Self) -> "_1927.SupportDetail":
        """mastapy.bearings.tolerances.SupportDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[BearingLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase]

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

    @property
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(
        self: Self,
    ) -> "List[List[float]]":
        """List[List[float]]"""
        temp = self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)

        if value is None:
            return None

        return value

    @specified_stiffness_for_linear_bearing_in_local_coordinate_system.setter
    @enforce_parameter_types
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(
        self: Self, value: "List[List[float]]"
    ):
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem = value

    @property
    def cast_to(self: Self) -> "BearingLoadCase._Cast_BearingLoadCase":
        return self._Cast_BearingLoadCase(self)
