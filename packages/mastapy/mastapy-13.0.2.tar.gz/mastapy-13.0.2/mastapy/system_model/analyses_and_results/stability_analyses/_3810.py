"""CouplingStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3794,
        _3799,
        _3855,
        _3877,
        _3895,
        _3771,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingStabilityAnalysis")


class CouplingStabilityAnalysis(_3871.SpecialisedAssemblyStabilityAnalysis):
    """CouplingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingStabilityAnalysis")

    class _Cast_CouplingStabilityAnalysis:
        """Special nested class for casting CouplingStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
            parent: "CouplingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3771.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3794.ClutchStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3799.ConceptCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.ConceptCouplingStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3855.PartToPartShearCouplingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.PartToPartShearCouplingStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3877.SpringDamperStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.SpringDamperStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "_3895.TorqueConverterStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3895,
            )

            return self._parent._cast(_3895.TorqueConverterStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "CouplingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2591.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis":
        return self._Cast_CouplingStabilityAnalysis(self)
