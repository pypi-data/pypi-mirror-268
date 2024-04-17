"""TorsionalSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.system_deflections import _2833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORSIONAL_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "TorsionalSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7552,
        _7558,
        _7543,
    )
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("TorsionalSystemDeflection",)


Self = TypeVar("Self", bound="TorsionalSystemDeflection")


class TorsionalSystemDeflection(_2833.SystemDeflection):
    """TorsionalSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORSIONAL_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorsionalSystemDeflection")

    class _Cast_TorsionalSystemDeflection:
        """Special nested class for casting TorsionalSystemDeflection to subclasses."""

        def __init__(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection",
            parent: "TorsionalSystemDeflection",
        ):
            self._parent = parent

        @property
        def system_deflection(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection",
        ) -> "_2833.SystemDeflection":
            return self._parent._cast(_2833.SystemDeflection)

        @property
        def fe_analysis(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection",
        ) -> "_7552.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7552

            return self._parent._cast(_7552.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection",
        ) -> "_7558.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7558

            return self._parent._cast(_7558.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection",
        ) -> "_7543.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.AnalysisCase)

        @property
        def context(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def torsional_system_deflection(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection",
        ) -> "TorsionalSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorsionalSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "TorsionalSystemDeflection._Cast_TorsionalSystemDeflection":
        return self._Cast_TorsionalSystemDeflection(self)
