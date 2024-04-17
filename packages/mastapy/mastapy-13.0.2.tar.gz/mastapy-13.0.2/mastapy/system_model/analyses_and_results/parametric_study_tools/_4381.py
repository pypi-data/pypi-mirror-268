"""KlingelnbergCycloPalloidHypoidGearParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4378
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6924
    from mastapy.system_model.analyses_and_results.system_deflections import _2781
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4337,
        _4370,
        _4389,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearParametricStudyTool",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearParametricStudyTool")


class KlingelnbergCycloPalloidHypoidGearParametricStudyTool(
    _4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool
):
    """KlingelnbergCycloPalloidHypoidGearParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
            parent: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            return self._parent._cast(
                _4378.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def conical_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4337.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.ConicalGearParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4370.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(_4370.GearParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearParametricStudyTool.TYPE",
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
    def component_load_case(
        self: Self,
    ) -> "_6924.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2781.KlingelnbergCycloPalloidHypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearParametricStudyTool(self)
