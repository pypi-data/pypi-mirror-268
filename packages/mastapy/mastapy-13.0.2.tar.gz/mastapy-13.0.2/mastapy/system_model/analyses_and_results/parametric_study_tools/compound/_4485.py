"""ConicalGearSetCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4511,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConicalGearSetCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4338
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4457,
        _4464,
        _4469,
        _4515,
        _4519,
        _4522,
        _4525,
        _4552,
        _4558,
        _4561,
        _4579,
        _4549,
        _4451,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundParametricStudyTool")


class ConicalGearSetCompoundParametricStudyTool(
    _4511.GearSetCompoundParametricStudyTool
):
    """ConicalGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundParametricStudyTool"
    )

    class _Cast_ConicalGearSetCompoundParametricStudyTool:
        """Special nested class for casting ConicalGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
            parent: "ConicalGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4511.GearSetCompoundParametricStudyTool":
            return self._parent._cast(_4511.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4549.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4451.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4457.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4464.BevelDifferentialGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(
                _4464.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4469.BevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(_4469.BevelGearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4515.HypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(_4515.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4519.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4522.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4525.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(
                _4525.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4552.SpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4558.StraightBevelDiffGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(
                _4558.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4561.StraightBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "_4579.ZerolBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4579,
            )

            return self._parent._cast(
                _4579.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
        ) -> "ConicalGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4338.ConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4338.ConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConicalGearSetParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundParametricStudyTool._Cast_ConicalGearSetCompoundParametricStudyTool":
        return self._Cast_ConicalGearSetCompoundParametricStudyTool(self)
