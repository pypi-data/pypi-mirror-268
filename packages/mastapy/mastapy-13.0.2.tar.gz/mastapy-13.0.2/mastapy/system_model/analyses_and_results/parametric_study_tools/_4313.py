"""BeltConnectionParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4376
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "BeltConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2275
    from mastapy.system_model.analyses_and_results.static_loads import _6829
    from mastapy.system_model.analyses_and_results.system_deflections import _2707
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4344,
        _4339,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="BeltConnectionParametricStudyTool")


class BeltConnectionParametricStudyTool(
    _4376.InterMountableComponentConnectionParametricStudyTool
):
    """BeltConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnectionParametricStudyTool")

    class _Cast_BeltConnectionParametricStudyTool:
        """Special nested class for casting BeltConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
            parent: "BeltConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "_4376.InterMountableComponentConnectionParametricStudyTool":
            return self._parent._cast(
                _4376.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "_4339.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_parametric_study_tool(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "_4344.CVTBeltConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.CVTBeltConnectionParametricStudyTool)

        @property
        def belt_connection_parametric_study_tool(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
        ) -> "BeltConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool",
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
        self: Self, instance_to_wrap: "BeltConnectionParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6829.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2707.BeltConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionParametricStudyTool._Cast_BeltConnectionParametricStudyTool":
        return self._Cast_BeltConnectionParametricStudyTool(self)
