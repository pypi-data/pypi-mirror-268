"""KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4380,
        _4383,
        _4369,
        _4376,
        _4339,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"
)


class KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool(
    _4336.ConicalGearMeshParametricStudyTool
):
    """KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
            parent: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_4336.ConicalGearMeshParametricStudyTool":
            return self._parent._cast(_4336.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_4369.GearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(_4369.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_4376.InterMountableComponentConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.InterMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_4339.ConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_4380.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(
                _4380.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "_4383.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(
                _4383.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool(
            self
        )
