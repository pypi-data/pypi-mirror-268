"""FEPartCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2861
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "FEPartCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.system_deflections import _2765
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundSystemDeflection",)


Self = TypeVar("Self", bound="FEPartCompoundSystemDeflection")


class FEPartCompoundSystemDeflection(
    _2861.AbstractShaftOrHousingCompoundSystemDeflection
):
    """FEPartCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundSystemDeflection")

    class _Cast_FEPartCompoundSystemDeflection:
        """Special nested class for casting FEPartCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
            parent: "FEPartCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
        ) -> "_2861.AbstractShaftOrHousingCompoundSystemDeflection":
            return self._parent._cast(
                _2861.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def component_compound_system_deflection(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def fe_part_compound_system_deflection(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
        ) -> "FEPartCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.FEPart":
        """mastapy.system_model.part_model.FEPart

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
    ) -> "List[_2765.FEPartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection]

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
    def planetaries(self: Self) -> "List[FEPartCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.FEPartCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_2765.FEPartSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FEPartSystemDeflection]

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
    ) -> "FEPartCompoundSystemDeflection._Cast_FEPartCompoundSystemDeflection":
        return self._Cast_FEPartCompoundSystemDeflection(self)
