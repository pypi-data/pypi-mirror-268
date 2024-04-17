"""PartToPartShearCouplingCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6589
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6940
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6652,
        _6551,
        _6633,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCriticalSpeedAnalysis")


class PartToPartShearCouplingCriticalSpeedAnalysis(_6589.CouplingCriticalSpeedAnalysis):
    """PartToPartShearCouplingCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingCriticalSpeedAnalysis"
    )

    class _Cast_PartToPartShearCouplingCriticalSpeedAnalysis:
        """Special nested class for casting PartToPartShearCouplingCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
            parent: "PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_6589.CouplingCriticalSpeedAnalysis":
            return self._parent._cast(_6589.CouplingCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_6652.SpecialisedAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_6551.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_6633.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "PartToPartShearCouplingCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2596.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6940.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis":
        return self._Cast_PartToPartShearCouplingCriticalSpeedAnalysis(self)
