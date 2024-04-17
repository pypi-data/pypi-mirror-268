"""PartToPartShearCouplingHalfSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartToPartShearCouplingHalfSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6939
    from mastapy.system_model.analyses_and_results.power_flows import _4124
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
__all__ = ("PartToPartShearCouplingHalfSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfSystemDeflection")


class PartToPartShearCouplingHalfSystemDeflection(_2738.CouplingHalfSystemDeflection):
    """PartToPartShearCouplingHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfSystemDeflection"
    )

    class _Cast_PartToPartShearCouplingHalfSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingHalfSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
            parent: "PartToPartShearCouplingHalfSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_system_deflection(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_2738.CouplingHalfSystemDeflection":
            return self._parent._cast(_2738.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
        ) -> "PartToPartShearCouplingHalfSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingHalfSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4124.PartToPartShearCouplingHalfPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingHalfPowerFlow

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
    ) -> "PartToPartShearCouplingHalfSystemDeflection._Cast_PartToPartShearCouplingHalfSystemDeflection":
        return self._Cast_PartToPartShearCouplingHalfSystemDeflection(self)
