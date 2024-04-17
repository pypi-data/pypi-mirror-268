"""KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4485,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4379
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4522,
        _4525,
        _4511,
        _4549,
        _4451,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool(
    _4485.ConicalGearSetCompoundParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_4485.ConicalGearSetCompoundParametricStudyTool":
            return self._parent._cast(_4485.ConicalGearSetCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_4511.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(_4511.GearSetCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_4549.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_4451.AbstractAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_4522.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "_4525.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(
                _4525.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4379.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool]

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
    ) -> "List[_4379.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool(
            self
        )
