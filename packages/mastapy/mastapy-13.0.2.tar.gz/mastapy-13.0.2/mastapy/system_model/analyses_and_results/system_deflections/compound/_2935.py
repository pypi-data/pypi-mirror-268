"""MassDiscCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2983
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "MassDiscCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.system_deflections import _2787
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2937,
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundSystemDeflection",)


Self = TypeVar("Self", bound="MassDiscCompoundSystemDeflection")


class MassDiscCompoundSystemDeflection(_2983.VirtualComponentCompoundSystemDeflection):
    """MassDiscCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscCompoundSystemDeflection")

    class _Cast_MassDiscCompoundSystemDeflection:
        """Special nested class for casting MassDiscCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
            parent: "MassDiscCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_system_deflection(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "_2983.VirtualComponentCompoundSystemDeflection":
            return self._parent._cast(_2983.VirtualComponentCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_compound_system_deflection(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
        ) -> "MassDiscCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.MassDisc":
        """mastapy.system_model.part_model.MassDisc

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
    ) -> "List[_2787.MassDiscSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection]

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
    def planetaries(self: Self) -> "List[MassDiscCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.MassDiscCompoundSystemDeflection]

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
    def component_analysis_cases(self: Self) -> "List[_2787.MassDiscSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection]

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
    ) -> "MassDiscCompoundSystemDeflection._Cast_MassDiscCompoundSystemDeflection":
        return self._Cast_MassDiscCompoundSystemDeflection(self)
