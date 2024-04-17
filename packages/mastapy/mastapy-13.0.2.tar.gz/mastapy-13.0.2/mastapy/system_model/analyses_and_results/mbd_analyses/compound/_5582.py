"""CycloidalDiscCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CycloidalDiscCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2576
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5432
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5539,
        _5562,
        _5616,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundMultibodyDynamicsAnalysis")


class CycloidalDiscCompoundMultibodyDynamicsAnalysis(
    _5538.AbstractShaftCompoundMultibodyDynamicsAnalysis
):
    """CycloidalDiscCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "_5538.AbstractShaftCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5538.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "_5539.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(
                _5539.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(_5562.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CycloidalDiscCompoundMultibodyDynamicsAnalysis.TYPE",
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5432.CycloidalDiscMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CycloidalDiscMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5432.CycloidalDiscMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CycloidalDiscMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CycloidalDiscCompoundMultibodyDynamicsAnalysis(self)
