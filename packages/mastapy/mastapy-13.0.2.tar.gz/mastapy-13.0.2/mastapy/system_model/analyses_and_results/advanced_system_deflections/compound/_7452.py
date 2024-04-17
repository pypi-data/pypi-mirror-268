"""CouplingConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7479,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7320,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7436,
        _7441,
        _7495,
        _7517,
        _7532,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundAdvancedSystemDeflection")


class CouplingConnectionCompoundAdvancedSystemDeflection(
    _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """CouplingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
            parent: "CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7436.ClutchConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7441.ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(
                _7441.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7495.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7495,
            )

            return self._parent._cast(
                _7495.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7517.SpringDamperConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7517,
            )

            return self._parent._cast(
                _7517.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7532.TorqueConverterConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7532,
            )

            return self._parent._cast(
                _7532.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "CouplingConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "CouplingConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7320.CouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7320.CouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingConnectionCompoundAdvancedSystemDeflection(self)
