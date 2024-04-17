"""GuideDxfModelSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2723
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GuideDxfModelSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.power_flows import _4104
    from mastapy.system_model.analyses_and_results.system_deflections import _2793
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7555,
        _7556,
        _7553,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelSystemDeflection",)


Self = TypeVar("Self", bound="GuideDxfModelSystemDeflection")


class GuideDxfModelSystemDeflection(_2723.ComponentSystemDeflection):
    """GuideDxfModelSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelSystemDeflection")

    class _Cast_GuideDxfModelSystemDeflection:
        """Special nested class for casting GuideDxfModelSystemDeflection to subclasses."""

        def __init__(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
            parent: "GuideDxfModelSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def guide_dxf_model_system_deflection(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "GuideDxfModelSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6905.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4104.GuideDxfModelPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.GuideDxfModelPowerFlow

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
    ) -> "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection":
        return self._Cast_GuideDxfModelSystemDeflection(self)
