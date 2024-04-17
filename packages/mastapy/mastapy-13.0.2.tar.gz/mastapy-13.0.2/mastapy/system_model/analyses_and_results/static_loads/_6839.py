"""BoltedJointLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltedJointLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6815, _6937
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointLoadCase",)


Self = TypeVar("Self", bound="BoltedJointLoadCase")


class BoltedJointLoadCase(_6961.SpecialisedAssemblyLoadCase):
    """BoltedJointLoadCase

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointLoadCase")

    class _Cast_BoltedJointLoadCase:
        """Special nested class for casting BoltedJointLoadCase to subclasses."""

        def __init__(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
            parent: "BoltedJointLoadCase",
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "_6961.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6961.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "_6815.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6815

            return self._parent._cast(_6815.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolted_joint_load_case(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "BoltedJointLoadCase":
            return self._parent

        def __getattr__(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointLoadCase.TYPE"):
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
    def cast_to(self: Self) -> "BoltedJointLoadCase._Cast_BoltedJointLoadCase":
        return self._Cast_BoltedJointLoadCase(self)
