"""PartToPartShearCouplingConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.analyses_and_results.stability_analyses import _3853
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3970,
        _3940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionCompoundStabilityAnalysis"
)


class PartToPartShearCouplingConnectionCompoundStabilityAnalysis(
    _3943.CouplingConnectionCompoundStabilityAnalysis
):
    """PartToPartShearCouplingConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
            parent: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_stability_analysis(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_3943.CouplingConnectionCompoundStabilityAnalysis":
            return self._parent._cast(_3943.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_3970.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_3940.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
        ) -> "PartToPartShearCouplingConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3853.PartToPartShearCouplingConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartToPartShearCouplingConnectionStabilityAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3853.PartToPartShearCouplingConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartToPartShearCouplingConnectionStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingConnectionCompoundStabilityAnalysis._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionCompoundStabilityAnalysis(
            self
        )
