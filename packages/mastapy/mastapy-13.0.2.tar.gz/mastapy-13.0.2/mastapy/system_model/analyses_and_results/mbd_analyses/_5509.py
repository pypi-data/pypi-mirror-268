"""StraightBevelGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5404
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5508,
        _5507,
        _5390,
        _5421,
        _5448,
        _5497,
        _5384,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearSetMultibodyDynamicsAnalysis")


class StraightBevelGearSetMultibodyDynamicsAnalysis(
    _5404.BevelGearSetMultibodyDynamicsAnalysis
):
    """StraightBevelGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
            parent: "StraightBevelGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5404.BevelGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5404.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5421.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5448.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(_5448.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5497.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5384.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
        ) -> "StraightBevelGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelGearSetMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6973.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_5508.StraightBevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5508.StraightBevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5507.StraightBevelGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelGearSetMultibodyDynamicsAnalysis(self)
