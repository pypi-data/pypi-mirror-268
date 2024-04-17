"""TorqueConverterAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "TorqueConverterAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2615
    from mastapy.system_model.analyses_and_results.static_loads import _6982
    from mastapy.system_model.analyses_and_results.system_deflections import _2838
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7382,
        _7278,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterAdvancedSystemDeflection")


class TorqueConverterAdvancedSystemDeflection(_7319.CouplingAdvancedSystemDeflection):
    """TorqueConverterAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterAdvancedSystemDeflection"
    )

    class _Cast_TorqueConverterAdvancedSystemDeflection:
        """Special nested class for casting TorqueConverterAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
            parent: "TorqueConverterAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_advanced_system_deflection(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_7319.CouplingAdvancedSystemDeflection":
            return self._parent._cast(_7319.CouplingAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_7382.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(_7382.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_7278.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_advanced_system_deflection(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
        ) -> "TorqueConverterAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "TorqueConverterAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2615.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6982.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2838.TorqueConverterSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterAdvancedSystemDeflection._Cast_TorqueConverterAdvancedSystemDeflection":
        return self._Cast_TorqueConverterAdvancedSystemDeflection(self)
