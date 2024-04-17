"""CouplingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5457
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CouplingConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2353
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5407,
        _5413,
        _5476,
        _5501,
        _5516,
        _5422,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionMultibodyDynamicsAnalysis")


class CouplingConnectionMultibodyDynamicsAnalysis(
    _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """CouplingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_CouplingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting CouplingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
            parent: "CouplingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5407.ClutchConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5413.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(
                _5413.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5476.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(
                _5476.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5501.SpringDamperConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5516.TorqueConverterConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(
                _5516.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
        ) -> "CouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionMultibodyDynamicsAnalysis.TYPE"
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
    ) -> "CouplingConnectionMultibodyDynamicsAnalysis._Cast_CouplingConnectionMultibodyDynamicsAnalysis":
        return self._Cast_CouplingConnectionMultibodyDynamicsAnalysis(self)
