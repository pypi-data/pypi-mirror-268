"""FaceGearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "FaceGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.static_loads import _6894
    from mastapy.system_model.analyses_and_results.system_deflections import _2762
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4376,
        _4339,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="FaceGearMeshParametricStudyTool")


class FaceGearMeshParametricStudyTool(_4369.GearMeshParametricStudyTool):
    """FaceGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshParametricStudyTool")

    class _Cast_FaceGearMeshParametricStudyTool:
        """Special nested class for casting FaceGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
            parent: "FaceGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_mesh_parametric_study_tool(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "_4369.GearMeshParametricStudyTool":
            return self._parent._cast(_4369.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "_4376.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "_4339.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_mesh_parametric_study_tool(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
        ) -> "FaceGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2318.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6894.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

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
    ) -> "List[_2762.FaceGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection]

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
    ) -> "FaceGearMeshParametricStudyTool._Cast_FaceGearMeshParametricStudyTool":
        return self._Cast_FaceGearMeshParametricStudyTool(self)
