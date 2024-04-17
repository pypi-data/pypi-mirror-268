"""ConicalGearSetParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ConicalGearSetParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4310,
        _4317,
        _4322,
        _4375,
        _4379,
        _4382,
        _4385,
        _4423,
        _4429,
        _4432,
        _4450,
        _4420,
        _4304,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetParametricStudyTool",)


Self = TypeVar("Self", bound="ConicalGearSetParametricStudyTool")


class ConicalGearSetParametricStudyTool(_4371.GearSetParametricStudyTool):
    """ConicalGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetParametricStudyTool")

    class _Cast_ConicalGearSetParametricStudyTool:
        """Special nested class for casting ConicalGearSetParametricStudyTool to subclasses."""

        def __init__(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
            parent: "ConicalGearSetParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4371.GearSetParametricStudyTool":
            return self._parent._cast(_4371.GearSetParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4420.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4304.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4310.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(
                _4310.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4317.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4322.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4322,
            )

            return self._parent._cast(_4322.BevelGearSetParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4375.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(_4375.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4379.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(
                _4379.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4382.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4382,
            )

            return self._parent._cast(
                _4382.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4385.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(
                _4385.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4423.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.SpiralBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4429.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4432.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.StraightBevelGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "_4450.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4450,
            )

            return self._parent._cast(_4450.ZerolBevelGearSetParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
        ) -> "ConicalGearSetParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConicalGearSetParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2531.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetParametricStudyTool._Cast_ConicalGearSetParametricStudyTool":
        return self._Cast_ConicalGearSetParametricStudyTool(self)
