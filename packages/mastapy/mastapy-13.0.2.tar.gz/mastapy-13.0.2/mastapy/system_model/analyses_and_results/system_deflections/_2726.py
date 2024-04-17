"""ConceptCouplingHalfSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConceptCouplingHalfSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import _6848
    from mastapy.system_model.analyses_and_results.power_flows import _4067
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
__all__ = ("ConceptCouplingHalfSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingHalfSystemDeflection")


class ConceptCouplingHalfSystemDeflection(_2738.CouplingHalfSystemDeflection):
    """ConceptCouplingHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingHalfSystemDeflection")

    class _Cast_ConceptCouplingHalfSystemDeflection:
        """Special nested class for casting ConceptCouplingHalfSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
            parent: "ConceptCouplingHalfSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_system_deflection(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_2738.CouplingHalfSystemDeflection":
            return self._parent._cast(_2738.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_half_system_deflection(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
        ) -> "ConceptCouplingHalfSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection",
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
        self: Self, instance_to_wrap: "ConceptCouplingHalfSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6848.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4067.ConceptCouplingHalfPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingHalfPowerFlow

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
    ) -> (
        "ConceptCouplingHalfSystemDeflection._Cast_ConceptCouplingHalfSystemDeflection"
    ):
        return self._Cast_ConceptCouplingHalfSystemDeflection(self)
