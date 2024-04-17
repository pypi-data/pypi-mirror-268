"""OilSealCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7450,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "OilSealCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7362,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7491,
        _7439,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="OilSealCompoundAdvancedSystemDeflection")


class OilSealCompoundAdvancedSystemDeflection(
    _7450.ConnectorCompoundAdvancedSystemDeflection
):
    """OilSealCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealCompoundAdvancedSystemDeflection"
    )

    class _Cast_OilSealCompoundAdvancedSystemDeflection:
        """Special nested class for casting OilSealCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
            parent: "OilSealCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connector_compound_advanced_system_deflection(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "_7450.ConnectorCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7450.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "_7491.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "_7439.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
        ) -> "OilSealCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "OilSealCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7362.OilSealAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.OilSealAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7362.OilSealAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.OilSealAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "OilSealCompoundAdvancedSystemDeflection._Cast_OilSealCompoundAdvancedSystemDeflection":
        return self._Cast_OilSealCompoundAdvancedSystemDeflection(self)
