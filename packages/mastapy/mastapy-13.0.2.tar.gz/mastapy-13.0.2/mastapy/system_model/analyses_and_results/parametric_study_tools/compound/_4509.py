"""GearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4528,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "GearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _361
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4370
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4455,
        _4462,
        _4465,
        _4466,
        _4467,
        _4480,
        _4483,
        _4498,
        _4501,
        _4504,
        _4513,
        _4517,
        _4520,
        _4523,
        _4550,
        _4556,
        _4559,
        _4562,
        _4563,
        _4574,
        _4577,
        _4476,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="GearCompoundParametricStudyTool")


class GearCompoundParametricStudyTool(
    _4528.MountableComponentCompoundParametricStudyTool
):
    """GearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundParametricStudyTool")

    class _Cast_GearCompoundParametricStudyTool:
        """Special nested class for casting GearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
            parent: "GearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4528.MountableComponentCompoundParametricStudyTool":
            return self._parent._cast(
                _4528.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4476.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4455.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4462.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(
                _4462.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4465.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(
                _4465.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4466.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4466,
            )

            return self._parent._cast(
                _4466.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4467.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.BevelGearCompoundParametricStudyTool)

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4480.ConceptGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4483.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(_4483.ConicalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4498.CylindricalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4501.CylindricalPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(
                _4501.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def face_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4504.FaceGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(_4504.FaceGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4513.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(_4513.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4520.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4523.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4550.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(_4550.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4556.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(
                _4556.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4559.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4562.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4563.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(
                _4563.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4574.WormGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4574,
            )

            return self._parent._cast(_4574.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "_4577.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4577,
            )

            return self._parent._cast(_4577.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
        ) -> "GearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_results(self: Self) -> "_361.GearDutyCycleRating":
        """mastapy.gears.rating.GearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases(self: Self) -> "List[_4370.GearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4370.GearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearCompoundParametricStudyTool._Cast_GearCompoundParametricStudyTool":
        return self._Cast_GearCompoundParametricStudyTool(self)
