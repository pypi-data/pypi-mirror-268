"""KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4517,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6924
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4381
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4483,
        _4509,
        _4528,
        _4476,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"
)


class KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool(
    _4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
):
    """KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4483.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(_4483.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4509.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(_4509.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4528.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(
                _4528.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4476.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def properties_changing_all_load_cases(
        self: Self,
    ) -> "_6924.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PropertiesChangingAllLoadCases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4381.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool(
            self
        )
