"""AbstractShaftOrHousingCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AbstractShaftOrHousingCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2694
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2860,
        _2904,
        _2916,
        _2955,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundSystemDeflection")


class AbstractShaftOrHousingCompoundSystemDeflection(
    _2884.ComponentCompoundSystemDeflection
):
    """AbstractShaftOrHousingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingCompoundSystemDeflection"
    )

    class _Cast_AbstractShaftOrHousingCompoundSystemDeflection:
        """Special nested class for casting AbstractShaftOrHousingCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
            parent: "AbstractShaftOrHousingCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_system_deflection(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_2860.AbstractShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(_2860.AbstractShaftCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_2904.CycloidalDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.CycloidalDiscCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_2916.FEPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(_2916.FEPartCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "_2955.ShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(_2955.ShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
        ) -> "AbstractShaftOrHousingCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2694.AbstractShaftOrHousingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection]

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
    ) -> "List[_2694.AbstractShaftOrHousingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection]

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
    ) -> "AbstractShaftOrHousingCompoundSystemDeflection._Cast_AbstractShaftOrHousingCompoundSystemDeflection":
        return self._Cast_AbstractShaftOrHousingCompoundSystemDeflection(self)
