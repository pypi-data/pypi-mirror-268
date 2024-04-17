"""GearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4389
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "GearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.gears.rating import _361
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4309,
        _4316,
        _4318,
        _4319,
        _4321,
        _4334,
        _4337,
        _4352,
        _4354,
        _4365,
        _4374,
        _4378,
        _4381,
        _4384,
        _4422,
        _4428,
        _4431,
        _4433,
        _4434,
        _4446,
        _4449,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearParametricStudyTool",)


Self = TypeVar("Self", bound="GearParametricStudyTool")


class GearParametricStudyTool(_4389.MountableComponentParametricStudyTool):
    """GearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearParametricStudyTool")

    class _Cast_GearParametricStudyTool:
        """Special nested class for casting GearParametricStudyTool to subclasses."""

        def __init__(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
            parent: "GearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4309.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4316.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4318.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(
                _4318.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4319.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4321.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.BevelGearParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4334.ConceptGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4337.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.ConicalGearParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4352.CylindricalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4352,
            )

            return self._parent._cast(_4352.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4354.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4354,
            )

            return self._parent._cast(_4354.CylindricalPlanetGearParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4365.FaceGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.FaceGearParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4374.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(_4374.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(
                _4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(
                _4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4384.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(
                _4384.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4422.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.SpiralBevelGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4428.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4431.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4433.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4434.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.StraightBevelSunGearParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4446.WormGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4446,
            )

            return self._parent._cast(_4446.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "_4449.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4449,
            )

            return self._parent._cast(_4449.ZerolBevelGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool",
        ) -> "GearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearParametricStudyTool._Cast_GearParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_duty_cycle_results(self: Self) -> "List[_361.GearDutyCycleRating]":
        """List[mastapy.gears.rating.GearDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearParametricStudyTool._Cast_GearParametricStudyTool":
        return self._Cast_GearParametricStudyTool(self)
