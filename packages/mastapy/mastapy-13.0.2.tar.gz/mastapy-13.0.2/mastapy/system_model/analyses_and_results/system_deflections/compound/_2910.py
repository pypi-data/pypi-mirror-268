"""DatumCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "DatumCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.system_deflections import _2759
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("DatumCompoundSystemDeflection",)


Self = TypeVar("Self", bound="DatumCompoundSystemDeflection")


class DatumCompoundSystemDeflection(_2884.ComponentCompoundSystemDeflection):
    """DatumCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumCompoundSystemDeflection")

    class _Cast_DatumCompoundSystemDeflection:
        """Special nested class for casting DatumCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
            parent: "DatumCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_system_deflection(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def datum_compound_system_deflection(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
        ) -> "DatumCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.Datum":
        """mastapy.system_model.part_model.Datum

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
    ) -> "List[_2759.DatumSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection]

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
    def component_analysis_cases(self: Self) -> "List[_2759.DatumSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection]

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
    ) -> "DatumCompoundSystemDeflection._Cast_DatumCompoundSystemDeflection":
        return self._Cast_DatumCompoundSystemDeflection(self)
