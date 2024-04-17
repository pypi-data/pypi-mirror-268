"""TorqueConverterPumpParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "TorqueConverterPumpParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.system_deflections import _2837
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4389,
        _4329,
        _4401,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpParametricStudyTool",)


Self = TypeVar("Self", bound="TorqueConverterPumpParametricStudyTool")


class TorqueConverterPumpParametricStudyTool(_4342.CouplingHalfParametricStudyTool):
    """TorqueConverterPumpParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpParametricStudyTool"
    )

    class _Cast_TorqueConverterPumpParametricStudyTool:
        """Special nested class for casting TorqueConverterPumpParametricStudyTool to subclasses."""

        def __init__(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
            parent: "TorqueConverterPumpParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_half_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4342.CouplingHalfParametricStudyTool":
            return self._parent._cast(_4342.CouplingHalfParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4389.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4389,
            )

            return self._parent._cast(_4389.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4329.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_4401.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
        ) -> "TorqueConverterPumpParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2616.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6983.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "List[_2837.TorqueConverterPumpSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection]

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
    ) -> "TorqueConverterPumpParametricStudyTool._Cast_TorqueConverterPumpParametricStudyTool":
        return self._Cast_TorqueConverterPumpParametricStudyTool(self)
