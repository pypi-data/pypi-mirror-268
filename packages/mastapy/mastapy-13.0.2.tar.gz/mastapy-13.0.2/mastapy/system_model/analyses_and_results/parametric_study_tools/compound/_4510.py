"""GearMeshCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4516,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "GearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4369
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4456,
        _4463,
        _4468,
        _4481,
        _4484,
        _4499,
        _4505,
        _4514,
        _4518,
        _4521,
        _4524,
        _4551,
        _4557,
        _4560,
        _4575,
        _4578,
        _4486,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="GearMeshCompoundParametricStudyTool")


class GearMeshCompoundParametricStudyTool(
    _4516.InterMountableComponentConnectionCompoundParametricStudyTool
):
    """GearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundParametricStudyTool")

    class _Cast_GearMeshCompoundParametricStudyTool:
        """Special nested class for casting GearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
            parent: "GearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4516.InterMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent._cast(
                _4516.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4486.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4456.AGMAGleasonConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(
                _4456.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4463.BevelDifferentialGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(
                _4463.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4468.BevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.BevelGearMeshCompoundParametricStudyTool)

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4481.ConceptGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(_4481.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4484.ConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4499.CylindricalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(
                _4499.CylindricalGearMeshCompoundParametricStudyTool
            )

        @property
        def face_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4505.FaceGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.FaceGearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4514.HypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(_4514.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4518.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(
                _4518.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4521.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(
                _4521.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4524.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(
                _4524.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4551.SpiralBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4557.StraightBevelDiffGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(
                _4557.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4560.StraightBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(
                _4560.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4575.WormGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4575,
            )

            return self._parent._cast(_4575.WormGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "_4578.ZerolBevelGearMeshCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4578,
            )

            return self._parent._cast(
                _4578.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
        ) -> "GearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "GearMeshCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4369.GearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearMeshParametricStudyTool]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4369.GearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.GearMeshParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> (
        "GearMeshCompoundParametricStudyTool._Cast_GearMeshCompoundParametricStudyTool"
    ):
        return self._Cast_GearMeshCompoundParametricStudyTool(self)
