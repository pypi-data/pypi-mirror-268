"""CylindricalGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5184
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.static_loads import _6870
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5175,
        _5203,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CylindricalGearModalAnalysisAtASpeed")


class CylindricalGearModalAnalysisAtASpeed(_5184.GearModalAnalysisAtASpeed):
    """CylindricalGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearModalAnalysisAtASpeed")

    class _Cast_CylindricalGearModalAnalysisAtASpeed:
        """Special nested class for casting CylindricalGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
            parent: "CylindricalGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5184.GearModalAnalysisAtASpeed":
            return self._parent._cast(_5184.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "_5175.CylindricalPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
        ) -> "CylindricalGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CylindricalGearModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2532.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6870.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CylindricalGearModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearModalAnalysisAtASpeed._Cast_CylindricalGearModalAnalysisAtASpeed":
        return self._Cast_CylindricalGearModalAnalysisAtASpeed(self)
