"""SynchroniserPartAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SynchroniserPartAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2613
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7398,
        _7400,
        _7361,
        _7306,
        _7363,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserPartAdvancedSystemDeflection")


class SynchroniserPartAdvancedSystemDeflection(
    _7321.CouplingHalfAdvancedSystemDeflection
):
    """SynchroniserPartAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartAdvancedSystemDeflection"
    )

    class _Cast_SynchroniserPartAdvancedSystemDeflection:
        """Special nested class for casting SynchroniserPartAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
            parent: "SynchroniserPartAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7321.CouplingHalfAdvancedSystemDeflection":
            return self._parent._cast(_7321.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7361.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7306.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7363.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7398.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "_7400.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
        ) -> "SynchroniserPartAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SynchroniserPartAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2613.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartAdvancedSystemDeflection._Cast_SynchroniserPartAdvancedSystemDeflection":
        return self._Cast_SynchroniserPartAdvancedSystemDeflection(self)
