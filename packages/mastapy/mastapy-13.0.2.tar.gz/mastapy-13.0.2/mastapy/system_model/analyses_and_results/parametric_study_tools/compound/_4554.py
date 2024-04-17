"""SpringDamperConnectionCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4489,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "SpringDamperConnectionCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2357
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4424
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4516,
        _4486,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundParametricStudyTool")


class SpringDamperConnectionCompoundParametricStudyTool(
    _4489.CouplingConnectionCompoundParametricStudyTool
):
    """SpringDamperConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundParametricStudyTool"
    )

    class _Cast_SpringDamperConnectionCompoundParametricStudyTool:
        """Special nested class for casting SpringDamperConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
            parent: "SpringDamperConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
        ) -> "_4489.CouplingConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4489.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
        ) -> "_4516.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
        ) -> "_4486.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_parametric_study_tool(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
        ) -> "SpringDamperConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "SpringDamperConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4424.SpringDamperConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4424.SpringDamperConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.SpringDamperConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperConnectionCompoundParametricStudyTool._Cast_SpringDamperConnectionCompoundParametricStudyTool":
        return self._Cast_SpringDamperConnectionCompoundParametricStudyTool(self)
