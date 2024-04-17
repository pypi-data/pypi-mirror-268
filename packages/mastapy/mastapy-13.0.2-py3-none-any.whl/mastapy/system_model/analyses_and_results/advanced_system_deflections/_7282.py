"""AdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7283,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AdvancedSystemDeflection")


class AdvancedSystemDeflection(_7558.StaticLoadAnalysisCase):
    """AdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdvancedSystemDeflection")

    class _Cast_AdvancedSystemDeflection:
        """Special nested class for casting AdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AdvancedSystemDeflection._Cast_AdvancedSystemDeflection",
            parent: "AdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "AdvancedSystemDeflection._Cast_AdvancedSystemDeflection",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "AdvancedSystemDeflection._Cast_AdvancedSystemDeflection",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "AdvancedSystemDeflection._Cast_AdvancedSystemDeflection",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def advanced_system_deflection(
            self: "AdvancedSystemDeflection._Cast_AdvancedSystemDeflection",
        ) -> "AdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AdvancedSystemDeflection._Cast_AdvancedSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection_options(
        self: Self,
    ) -> "_7283.AdvancedSystemDeflectionOptions":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.AdvancedSystemDeflectionOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedSystemDeflectionOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AdvancedSystemDeflection._Cast_AdvancedSystemDeflection":
        return self._Cast_AdvancedSystemDeflection(self)
