"""ConnectorCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7491,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConnectorCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7317,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7422,
        _7492,
        _7510,
        _7439,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorCompoundAdvancedSystemDeflection")


class ConnectorCompoundAdvancedSystemDeflection(
    _7491.MountableComponentCompoundAdvancedSystemDeflection
):
    """ConnectorCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConnectorCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConnectorCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
            parent: "ConnectorCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7491.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7491.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7439.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7422.BearingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BearingCompoundAdvancedSystemDeflection)

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7492.OilSealCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.OilSealCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "_7510.ShaftHubConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connector_compound_advanced_system_deflection(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
        ) -> "ConnectorCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectorCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7317.ConnectorAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectorAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7317.ConnectorAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectorAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundAdvancedSystemDeflection._Cast_ConnectorCompoundAdvancedSystemDeflection":
        return self._Cast_ConnectorCompoundAdvancedSystemDeflection(self)
