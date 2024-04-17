"""TorqueConverterPumpAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "TorqueConverterPumpAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.system_deflections import _2837
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7361,
        _7306,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterPumpAdvancedSystemDeflection")


class TorqueConverterPumpAdvancedSystemDeflection(
    _7321.CouplingHalfAdvancedSystemDeflection
):
    """TorqueConverterPumpAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpAdvancedSystemDeflection"
    )

    class _Cast_TorqueConverterPumpAdvancedSystemDeflection:
        """Special nested class for casting TorqueConverterPumpAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
            parent: "TorqueConverterPumpAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_7321.CouplingHalfAdvancedSystemDeflection":
            return self._parent._cast(_7321.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_7361.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_7306.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
        ) -> "TorqueConverterPumpAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2616.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6983.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2837.TorqueConverterPumpSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpAdvancedSystemDeflection._Cast_TorqueConverterPumpAdvancedSystemDeflection":
        return self._Cast_TorqueConverterPumpAdvancedSystemDeflection(self)
