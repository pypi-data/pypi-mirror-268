"""SynchroniserHalfCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4566,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SynchroniserHalfCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4435
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4490,
        _4528,
        _4476,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundParametricStudyTool")


class SynchroniserHalfCompoundParametricStudyTool(
    _4566.SynchroniserPartCompoundParametricStudyTool
):
    """SynchroniserHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundParametricStudyTool"
    )

    class _Cast_SynchroniserHalfCompoundParametricStudyTool:
        """Special nested class for casting SynchroniserHalfCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
            parent: "SynchroniserHalfCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_4566.SynchroniserPartCompoundParametricStudyTool":
            return self._parent._cast(_4566.SynchroniserPartCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_4490.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.CouplingHalfCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_4528.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(
                _4528.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_4476.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
        ) -> "SynchroniserHalfCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "_6976.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

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
    ) -> "List[_4435.SynchroniserHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserHalfParametricStudyTool]

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
    ) -> "List[_4435.SynchroniserHalfParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SynchroniserHalfParametricStudyTool]

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
    ) -> "SynchroniserHalfCompoundParametricStudyTool._Cast_SynchroniserHalfCompoundParametricStudyTool":
        return self._Cast_SynchroniserHalfCompoundParametricStudyTool(self)
