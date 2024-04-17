"""PowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2840
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("PowerFlow",)


Self = TypeVar("Self", bound="PowerFlow")


class PowerFlow(_7558.StaticLoadAnalysisCase):
    """PowerFlow

    This is a mastapy class.
    """

    TYPE = _POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerFlow")

    class _Cast_PowerFlow:
        """Special nested class for casting PowerFlow to subclasses."""

        def __init__(self: "PowerFlow._Cast_PowerFlow", parent: "PowerFlow"):
            self._parent = parent

        @property
        def static_load_analysis_case(
            self: "PowerFlow._Cast_PowerFlow",
        ) -> "_7558.StaticLoadAnalysisCase":
            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(self: "PowerFlow._Cast_PowerFlow") -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(self: "PowerFlow._Cast_PowerFlow") -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def power_flow(self: "PowerFlow._Cast_PowerFlow") -> "PowerFlow":
            return self._parent

        def __getattr__(self: "PowerFlow._Cast_PowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Ratio

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_system_deflection(self: Self) -> "_2840.TorsionalSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.TorsionalSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PowerFlow._Cast_PowerFlow":
        return self._Cast_PowerFlow(self)
