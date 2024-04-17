"""ZerolBevelGearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ZerolBevelGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2338
    from mastapy.system_model.analyses_and_results.static_loads import _6995
    from mastapy.system_model.analyses_and_results.system_deflections import _2847
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4308,
        _4336,
        _4369,
        _4376,
        _4339,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshParametricStudyTool",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshParametricStudyTool")


class ZerolBevelGearMeshParametricStudyTool(_4320.BevelGearMeshParametricStudyTool):
    """ZerolBevelGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshParametricStudyTool"
    )

    class _Cast_ZerolBevelGearMeshParametricStudyTool:
        """Special nested class for casting ZerolBevelGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
            parent: "ZerolBevelGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_parametric_study_tool(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_4320.BevelGearMeshParametricStudyTool":
            return self._parent._cast(_4320.BevelGearMeshParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_parametric_study_tool(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_4308.AGMAGleasonConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(
                _4308.AGMAGleasonConicalGearMeshParametricStudyTool
            )

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_4336.ConicalGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_4369.GearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(_4369.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_4376.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_4339.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
        ) -> "ZerolBevelGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2338.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6995.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

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
    ) -> "List[_2847.ZerolBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection]

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
    ) -> "ZerolBevelGearMeshParametricStudyTool._Cast_ZerolBevelGearMeshParametricStudyTool":
        return self._Cast_ZerolBevelGearMeshParametricStudyTool(self)
