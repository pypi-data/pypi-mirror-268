"""CouplingConnectionCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6748,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6588
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6705,
        _6710,
        _6764,
        _6786,
        _6801,
        _6718,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundCriticalSpeedAnalysis")


class CouplingConnectionCompoundCriticalSpeedAnalysis(
    _6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """CouplingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CouplingConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
            parent: "CouplingConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6748.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6718.ConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(_6718.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6705.ClutchConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6710.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(
                _6710.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6764.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(
                _6764.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6786.SpringDamperConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "_6801.TorqueConverterConnectionCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(
                _6801.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "CouplingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "CouplingConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6588.CouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6588.CouplingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingConnectionCriticalSpeedAnalysis]

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
    ) -> "CouplingConnectionCompoundCriticalSpeedAnalysis._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_CouplingConnectionCompoundCriticalSpeedAnalysis(self)
