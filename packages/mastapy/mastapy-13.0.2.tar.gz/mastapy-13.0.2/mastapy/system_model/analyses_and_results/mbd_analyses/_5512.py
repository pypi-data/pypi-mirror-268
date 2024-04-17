"""SynchroniserHalfMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5514
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SynchroniserHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5425,
        _5472,
        _5412,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfMultibodyDynamicsAnalysis")


class SynchroniserHalfMultibodyDynamicsAnalysis(
    _5514.SynchroniserPartMultibodyDynamicsAnalysis
):
    """SynchroniserHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
            parent: "SynchroniserHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_5514.SynchroniserPartMultibodyDynamicsAnalysis":
            return self._parent._cast(_5514.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_5425.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(_5425.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_5472.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
        ) -> "SynchroniserHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserHalfMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6976.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfMultibodyDynamicsAnalysis._Cast_SynchroniserHalfMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserHalfMultibodyDynamicsAnalysis(self)
