"""StraightBevelDiffGearCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4467,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "StraightBevelDiffGearCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.static_loads import _6968
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4428
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4562,
        _4563,
        _4455,
        _4483,
        _4509,
        _4528,
        _4476,
        _4530,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundParametricStudyTool")


class StraightBevelDiffGearCompoundParametricStudyTool(
    _4467.BevelGearCompoundParametricStudyTool
):
    """StraightBevelDiffGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundParametricStudyTool"
    )

    class _Cast_StraightBevelDiffGearCompoundParametricStudyTool:
        """Special nested class for casting StraightBevelDiffGearCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
            parent: "StraightBevelDiffGearCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4467.BevelGearCompoundParametricStudyTool":
            return self._parent._cast(_4467.BevelGearCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4455.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4483.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(_4483.ConicalGearCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4509.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(_4509.GearCompoundParametricStudyTool)

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4528.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(
                _4528.MountableComponentCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4476.ComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ComponentCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4530.PartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4562.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "_4563.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(
                _4563.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
        ) -> "StraightBevelDiffGearCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2552.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

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
    ) -> "_6968.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

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
    ) -> "List[_4428.StraightBevelDiffGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearParametricStudyTool]

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
    ) -> "List[_4428.StraightBevelDiffGearParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.StraightBevelDiffGearParametricStudyTool]

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
    ) -> "StraightBevelDiffGearCompoundParametricStudyTool._Cast_StraightBevelDiffGearCompoundParametricStudyTool":
        return self._Cast_StraightBevelDiffGearCompoundParametricStudyTool(self)
