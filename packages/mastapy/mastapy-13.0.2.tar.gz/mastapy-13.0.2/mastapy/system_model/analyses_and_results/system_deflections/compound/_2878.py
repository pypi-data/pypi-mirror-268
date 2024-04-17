"""BoltCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BoltCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2449
    from mastapy.system_model.analyses_and_results.system_deflections import _2718
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BoltCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BoltCompoundSystemDeflection")


class BoltCompoundSystemDeflection(_2884.ComponentCompoundSystemDeflection):
    """BoltCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltCompoundSystemDeflection")

    class _Cast_BoltCompoundSystemDeflection:
        """Special nested class for casting BoltCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
            parent: "BoltCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_system_deflection(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bolt_compound_system_deflection(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
        ) -> "BoltCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2449.Bolt":
        """mastapy.system_model.part_model.Bolt

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
    ) -> "List[_2718.BoltSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection]

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
    def component_analysis_cases(self: Self) -> "List[_2718.BoltSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection]

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
    ) -> "BoltCompoundSystemDeflection._Cast_BoltCompoundSystemDeflection":
        return self._Cast_BoltCompoundSystemDeflection(self)
