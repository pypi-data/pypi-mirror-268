"""BoltedJointDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BoltedJointDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6839
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285, _6366
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointDynamicAnalysis",)


Self = TypeVar("Self", bound="BoltedJointDynamicAnalysis")


class BoltedJointDynamicAnalysis(_6385.SpecialisedAssemblyDynamicAnalysis):
    """BoltedJointDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointDynamicAnalysis")

    class _Cast_BoltedJointDynamicAnalysis:
        """Special nested class for casting BoltedJointDynamicAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
            parent: "BoltedJointDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_6385.SpecialisedAssemblyDynamicAnalysis":
            return self._parent._cast(_6385.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_6285.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_6366.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
        ) -> "BoltedJointDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointDynamicAnalysis.TYPE"):
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
    ) -> "BoltedJointDynamicAnalysis._Cast_BoltedJointDynamicAnalysis":
        return self._Cast_BoltedJointDynamicAnalysis(self)
