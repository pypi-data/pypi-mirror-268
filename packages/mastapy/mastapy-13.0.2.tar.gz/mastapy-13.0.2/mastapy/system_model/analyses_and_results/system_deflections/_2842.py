"""UnbalancedMassSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2843
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "UnbalancedMassSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.static_loads import _6989
    from mastapy.system_model.analyses_and_results.power_flows import _4167
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2790,
        _2723,
        _2793,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassSystemDeflection",)


Self = TypeVar("Self", bound="UnbalancedMassSystemDeflection")


class UnbalancedMassSystemDeflection(_2843.VirtualComponentSystemDeflection):
    """UnbalancedMassSystemDeflection

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassSystemDeflection")

    class _Cast_UnbalancedMassSystemDeflection:
        """Special nested class for casting UnbalancedMassSystemDeflection to subclasses."""

        def __init__(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
            parent: "UnbalancedMassSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2843.VirtualComponentSystemDeflection":
            return self._parent._cast(_2843.VirtualComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def unbalanced_mass_system_deflection(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
        ) -> "UnbalancedMassSystemDeflection":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6989.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4167.UnbalancedMassPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.UnbalancedMassPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassSystemDeflection._Cast_UnbalancedMassSystemDeflection":
        return self._Cast_UnbalancedMassSystemDeflection(self)
