"""ShaftSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Iterable, List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.analyses_and_results.system_deflections import _2695
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.shafts import _34, _19
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.system_model.analyses_and_results.power_flows import _4141
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2810,
        _2811,
        _2694,
        _2723,
        _2793,
    )
    from mastapy.math_utility.measured_vectors import _1568
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSystemDeflection",)


Self = TypeVar("Self", bound="ShaftSystemDeflection")


class ShaftSystemDeflection(_2695.AbstractShaftSystemDeflection):
    """ShaftSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSystemDeflection")

    class _Cast_ShaftSystemDeflection:
        """Special nested class for casting ShaftSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
            parent: "ShaftSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_system_deflection(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_2695.AbstractShaftSystemDeflection":
            return self._parent._cast(_2695.AbstractShaftSystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_2694.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2694,
            )

            return self._parent._cast(_2694.AbstractShaftOrHousingSystemDeflection)

        @property
        def component_system_deflection(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_system_deflection(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection",
        ) -> "ShaftSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftSystemDeflection._Cast_ShaftSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_axial_forces_with_mounted_components(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingAxialForcesWithMountedComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def first_node_deflection_angular(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstNodeDeflectionAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def first_node_deflection_linear(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstNodeDeflectionLinear

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def flexible_pin_additional_deflection_amplitude(
        self: Self,
    ) -> "Iterable[Vector3D]":
        """Iterable[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlexiblePinAdditionalDeflectionAmplitude

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_iterable(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def number_of_cycles_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCyclesForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def pin_tangential_oscillation_amplitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinTangentialOscillationAmplitude

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_rating_method(self: Self) -> "_34.ShaftRatingMethod":
        """mastapy.shafts.ShaftRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Shafts.ShaftRatingMethod")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.shafts._34", "ShaftRatingMethod")(
            value
        )

    @property
    def component_design(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_19.ShaftDamageResults":
        """mastapy.shafts.ShaftDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6959.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4141.ShaftPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ShaftPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor(
        self: Self,
    ) -> "_2810.ShaftSectionEndResultsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor_for_infinite_life(
        self: Self,
    ) -> "_2810.ShaftSectionEndResultsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_section_end_with_worst_static_safety_factor(
        self: Self,
    ) -> "_2810.ShaftSectionEndResultsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndWithWorstStaticSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mounted_components_applying_torque(self: Self) -> "List[_1568.ForceResults]":
        """List[mastapy.math_utility.measured_vectors.ForceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MountedComponentsApplyingTorque

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[ShaftSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection]

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
    def shaft_section_end_results_by_offset_with_worst_safety_factor(
        self: Self,
    ) -> "List[_2810.ShaftSectionEndResultsSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndResultsByOffsetWithWorstSafetyFactor

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_section_results(self: Self) -> "List[_2811.ShaftSectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def calculate_outer_diameter_to_achieve_fatigue_safety_factor_requirement(
        self: Self,
    ):
        """Method does not return."""
        self.wrapped.CalculateOuterDiameterToAchieveFatigueSafetyFactorRequirement()

    @property
    def cast_to(self: Self) -> "ShaftSystemDeflection._Cast_ShaftSystemDeflection":
        return self._Cast_ShaftSystemDeflection(self)
