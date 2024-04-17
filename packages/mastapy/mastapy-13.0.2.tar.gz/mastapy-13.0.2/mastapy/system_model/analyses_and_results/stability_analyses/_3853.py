"""PartToPartShearCouplingConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3808
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3838,
        _3806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingConnectionStabilityAnalysis")


class PartToPartShearCouplingConnectionStabilityAnalysis(
    _3808.CouplingConnectionStabilityAnalysis
):
    """PartToPartShearCouplingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingConnectionStabilityAnalysis"
    )

    class _Cast_PartToPartShearCouplingConnectionStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
            parent: "PartToPartShearCouplingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_3808.CouplingConnectionStabilityAnalysis":
            return self._parent._cast(_3808.CouplingConnectionStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_3838.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(
                _3838.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
        ) -> "PartToPartShearCouplingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6938.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionStabilityAnalysis._Cast_PartToPartShearCouplingConnectionStabilityAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionStabilityAnalysis(self)
