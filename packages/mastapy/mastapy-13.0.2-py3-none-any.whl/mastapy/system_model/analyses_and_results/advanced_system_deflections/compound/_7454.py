"""CVTBeltConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7423,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CVTBeltConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7323,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7479,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundAdvancedSystemDeflection")


class CVTBeltConnectionCompoundAdvancedSystemDeflection(
    _7423.BeltConnectionCompoundAdvancedSystemDeflection
):
    """CVTBeltConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection"
    )

    class _Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting CVTBeltConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
            parent: "CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7423.BeltConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7423.BeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
        ) -> "CVTBeltConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CVTBeltConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7323.CVTBeltConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTBeltConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7323.CVTBeltConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTBeltConnectionAdvancedSystemDeflection]

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
    ) -> "CVTBeltConnectionCompoundAdvancedSystemDeflection._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_CVTBeltConnectionCompoundAdvancedSystemDeflection(self)
