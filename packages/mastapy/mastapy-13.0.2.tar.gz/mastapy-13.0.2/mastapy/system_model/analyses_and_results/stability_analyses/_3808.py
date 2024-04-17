"""CouplingConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2353
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3792,
        _3797,
        _3853,
        _3875,
        _3893,
        _3806,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionStabilityAnalysis")


class CouplingConnectionStabilityAnalysis(
    _3838.InterMountableComponentConnectionStabilityAnalysis
):
    """CouplingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionStabilityAnalysis")

    class _Cast_CouplingConnectionStabilityAnalysis:
        """Special nested class for casting CouplingConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
            parent: "CouplingConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3838.InterMountableComponentConnectionStabilityAnalysis":
            return self._parent._cast(
                _3838.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3806.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3792.ClutchConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.ClutchConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3797.ConceptCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3853.PartToPartShearCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(
                _3853.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def spring_damper_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3875.SpringDamperConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.SpringDamperConnectionStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "_3893.TorqueConverterConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.TorqueConverterConnectionStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
        ) -> "CouplingConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2353.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> (
        "CouplingConnectionStabilityAnalysis._Cast_CouplingConnectionStabilityAnalysis"
    ):
        return self._Cast_CouplingConnectionStabilityAnalysis(self)
