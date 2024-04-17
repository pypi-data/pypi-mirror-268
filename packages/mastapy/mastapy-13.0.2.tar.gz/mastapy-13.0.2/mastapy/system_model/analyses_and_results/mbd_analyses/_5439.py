"""ExternalCADModelMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5412
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ExternalCADModelMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.static_loads import _6892
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5475
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelMultibodyDynamicsAnalysis")


class ExternalCADModelMultibodyDynamicsAnalysis(
    _5412.ComponentMultibodyDynamicsAnalysis
):
    """ExternalCADModelMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelMultibodyDynamicsAnalysis"
    )

    class _Cast_ExternalCADModelMultibodyDynamicsAnalysis:
        """Special nested class for casting ExternalCADModelMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
            parent: "ExternalCADModelMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
        ) -> "ExternalCADModelMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ExternalCADModelMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6892.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

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
    ) -> "ExternalCADModelMultibodyDynamicsAnalysis._Cast_ExternalCADModelMultibodyDynamicsAnalysis":
        return self._Cast_ExternalCADModelMultibodyDynamicsAnalysis(self)
