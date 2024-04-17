"""SpringDamperHalfCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4490,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SpringDamperHalfCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2609
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4425
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4528,
        _4476,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundParametricStudyTool")


class SpringDamperHalfCompoundParametricStudyTool(
    _4490.CouplingHalfCompoundParametricStudyTool
):
    """SpringDamperHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundParametricStudyTool"
    )

    class _Cast_SpringDamperHalfCompoundParametricStudyTool:
        """Special nested class for casting SpringDamperHalfCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
            parent: "SpringDamperHalfCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "_4490.CouplingHalfCompoundParametricStudyTool":
            return self._parent._cast(_4490.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "_4528.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(
                _4528.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "_4476.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
        ) -> "SpringDamperHalfCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "SpringDamperHalfCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2609.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "_6966.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

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
    ) -> "List[_4425.SpringDamperHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperHalfParametricStudyTool]

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
    ) -> "List[_4425.SpringDamperHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperHalfParametricStudyTool]

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
    ) -> "SpringDamperHalfCompoundParametricStudyTool._Cast_SpringDamperHalfCompoundParametricStudyTool":
        return self._Cast_SpringDamperHalfCompoundParametricStudyTool(self)
