"""BoltedJointStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BoltedJointStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6839
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3771,
        _3852,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointStabilityAnalysis",)


Self = TypeVar("Self", bound="BoltedJointStabilityAnalysis")


class BoltedJointStabilityAnalysis(_3871.SpecialisedAssemblyStabilityAnalysis):
    """BoltedJointStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointStabilityAnalysis")

    class _Cast_BoltedJointStabilityAnalysis:
        """Special nested class for casting BoltedJointStabilityAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
            parent: "BoltedJointStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_3871.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3871.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_3771.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_3852.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
        ) -> "BoltedJointStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2450.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6839.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

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
    ) -> "BoltedJointStabilityAnalysis._Cast_BoltedJointStabilityAnalysis":
        return self._Cast_BoltedJointStabilityAnalysis(self)
