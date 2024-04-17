"""BoltCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BoltCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5406
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5616
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BoltCompoundMultibodyDynamicsAnalysis")


class BoltCompoundMultibodyDynamicsAnalysis(
    _5562.ComponentCompoundMultibodyDynamicsAnalysis
):
    """BoltCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_BoltCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BoltCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
            parent: "BoltCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.ComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5562.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
        ) -> "BoltCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BoltCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2449.Bolt":
        """mastapy.system_model.part_model.Bolt

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
    ) -> "List[_5406.BoltMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BoltMultibodyDynamicsAnalysis]

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
    ) -> "List[_5406.BoltMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BoltMultibodyDynamicsAnalysis]

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
    ) -> "BoltCompoundMultibodyDynamicsAnalysis._Cast_BoltCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BoltCompoundMultibodyDynamicsAnalysis(self)
