"""SpringDamperConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpringDamperConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2357
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5457, _5422
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionMultibodyDynamicsAnalysis")


class SpringDamperConnectionMultibodyDynamicsAnalysis(
    _5424.CouplingConnectionMultibodyDynamicsAnalysis
):
    """SpringDamperConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_SpringDamperConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting SpringDamperConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
            parent: "SpringDamperConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_5424.CouplingConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5424.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_5422.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_7550.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
        ) -> "SpringDamperConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpringDamperConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Force

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def moment(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Moment

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_displacement(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_rotation(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def connection_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6965.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

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
    ) -> "SpringDamperConnectionMultibodyDynamicsAnalysis._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis":
        return self._Cast_SpringDamperConnectionMultibodyDynamicsAnalysis(self)
