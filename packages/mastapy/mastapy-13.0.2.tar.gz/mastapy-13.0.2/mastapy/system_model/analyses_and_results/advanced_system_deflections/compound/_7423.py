"""BeltConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7479,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BeltConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2275
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7290,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7454,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BeltConnectionCompoundAdvancedSystemDeflection")


class BeltConnectionCompoundAdvancedSystemDeflection(
    _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """BeltConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionCompoundAdvancedSystemDeflection"
    )

    class _Cast_BeltConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting BeltConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
            parent: "BeltConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7454.CVTBeltConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7454,
            )

            return self._parent._cast(
                _7454.CVTBeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "BeltConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BeltConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7290.BeltConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BeltConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7290.BeltConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BeltConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionCompoundAdvancedSystemDeflection._Cast_BeltConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_BeltConnectionCompoundAdvancedSystemDeflection(self)
