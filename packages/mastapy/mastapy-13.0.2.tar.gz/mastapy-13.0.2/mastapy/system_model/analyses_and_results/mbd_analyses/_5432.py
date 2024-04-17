"""CycloidalDiscMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5385
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CycloidalDiscMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5386,
        _5412,
        _5475,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7557, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscMultibodyDynamicsAnalysis")


class CycloidalDiscMultibodyDynamicsAnalysis(
    _5385.AbstractShaftMultibodyDynamicsAnalysis
):
    """CycloidalDiscMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscMultibodyDynamicsAnalysis"
    )

    class _Cast_CycloidalDiscMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5385.AbstractShaftMultibodyDynamicsAnalysis":
            return self._parent._cast(_5385.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5386.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(
                _5386.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def component_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5412.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5475.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_7557.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7557

            return self._parent._cast(_7557.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6868.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

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
    ) -> "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis":
        return self._Cast_CycloidalDiscMultibodyDynamicsAnalysis(self)
