"""ClutchHalfCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2898
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ClutchHalfCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.system_deflections import _2720
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2937,
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ClutchHalfCompoundSystemDeflection")


class ClutchHalfCompoundSystemDeflection(_2898.CouplingHalfCompoundSystemDeflection):
    """ClutchHalfCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfCompoundSystemDeflection")

    class _Cast_ClutchHalfCompoundSystemDeflection:
        """Special nested class for casting ClutchHalfCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
            parent: "ClutchHalfCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_system_deflection(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "_2898.CouplingHalfCompoundSystemDeflection":
            return self._parent._cast(_2898.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_compound_system_deflection(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
        ) -> "ClutchHalfCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ClutchHalfCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

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
    ) -> "List[_2720.ClutchHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection]

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
    ) -> "List[_2720.ClutchHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection]

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
    ) -> "ClutchHalfCompoundSystemDeflection._Cast_ClutchHalfCompoundSystemDeflection":
        return self._Cast_ClutchHalfCompoundSystemDeflection(self)
