"""AbstractShaftOrHousingCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7439,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7280,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7415,
        _7459,
        _7470,
        _7509,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundAdvancedSystemDeflection")


class AbstractShaftOrHousingCompoundAdvancedSystemDeflection(
    _7439.ComponentCompoundAdvancedSystemDeflection
):
    """AbstractShaftOrHousingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    )

    class _Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftOrHousingCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
            parent: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_system_deflection(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7439.ComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7439.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7415.AbstractShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7459.CycloidalDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(
                _7459.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7470.FEPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(_7470.FEPartCompoundAdvancedSystemDeflection)

        @property
        def shaft_compound_advanced_system_deflection(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "_7509.ShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(_7509.ShaftCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
        ) -> "AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7280.AbstractShaftOrHousingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftOrHousingAdvancedSystemDeflection]

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
    ) -> "List[_7280.AbstractShaftOrHousingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftOrHousingAdvancedSystemDeflection]

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
    ) -> "AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
        return self._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection(self)
