"""DatumAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "DatumAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6878
    from mastapy.system_model.analyses_and_results.system_deflections import _2759
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("DatumAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="DatumAdvancedSystemDeflection")


class DatumAdvancedSystemDeflection(_7306.ComponentAdvancedSystemDeflection):
    """DatumAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _DATUM_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumAdvancedSystemDeflection")

    class _Cast_DatumAdvancedSystemDeflection:
        """Special nested class for casting DatumAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
            parent: "DatumAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_advanced_system_deflection(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "_7306.ComponentAdvancedSystemDeflection":
            return self._parent._cast(_7306.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def datum_advanced_system_deflection(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
        ) -> "DatumAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumAdvancedSystemDeflection.TYPE"):
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
    def component_load_case(self: Self) -> "_6878.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

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
    ) -> "List[_2759.DatumSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection]

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
    ) -> "DatumAdvancedSystemDeflection._Cast_DatumAdvancedSystemDeflection":
        return self._Cast_DatumAdvancedSystemDeflection(self)
