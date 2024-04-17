"""OilSealSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2736
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "OilSealSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.static_loads import _6935
    from mastapy.system_model.analyses_and_results.power_flows import _4121
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
__all__ = ("OilSealSystemDeflection",)


Self = TypeVar("Self", bound="OilSealSystemDeflection")


class OilSealSystemDeflection(_2736.ConnectorSystemDeflection):
    """OilSealSystemDeflection

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealSystemDeflection")

    class _Cast_OilSealSystemDeflection:
        """Special nested class for casting OilSealSystemDeflection to subclasses."""

        def __init__(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
            parent: "OilSealSystemDeflection",
        ):
            self._parent = parent

        @property
        def connector_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2736.ConnectorSystemDeflection":
            return self._parent._cast(_2736.ConnectorSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2790.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2723.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2793.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_7555.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7555

            return self._parent._cast(_7555.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def oil_seal_system_deflection(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection",
        ) -> "OilSealSystemDeflection":
            return self._parent

        def __getattr__(
            self: "OilSealSystemDeflection._Cast_OilSealSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def reliability_for_oil_seal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReliabilityForOilSeal

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2473.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6935.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4121.OilSealPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.OilSealPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "OilSealSystemDeflection._Cast_OilSealSystemDeflection":
        return self._Cast_OilSealSystemDeflection(self)
