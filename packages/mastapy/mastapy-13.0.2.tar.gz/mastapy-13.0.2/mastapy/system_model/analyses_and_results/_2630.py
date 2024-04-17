"""AdvancedSystemDeflectionSubAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "AdvancedSystemDeflectionSubAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedSystemDeflectionSubAnalysis",)


Self = TypeVar("Self", bound="AdvancedSystemDeflectionSubAnalysis")


class AdvancedSystemDeflectionSubAnalysis(_2628.SingleAnalysis):
    """AdvancedSystemDeflectionSubAnalysis

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdvancedSystemDeflectionSubAnalysis")

    class _Cast_AdvancedSystemDeflectionSubAnalysis:
        """Special nested class for casting AdvancedSystemDeflectionSubAnalysis to subclasses."""

        def __init__(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
            parent: "AdvancedSystemDeflectionSubAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
        ) -> "AdvancedSystemDeflectionSubAnalysis":
            return self._parent

        def __getattr__(
            self: "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis",
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
        self: Self, instance_to_wrap: "AdvancedSystemDeflectionSubAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "AdvancedSystemDeflectionSubAnalysis._Cast_AdvancedSystemDeflectionSubAnalysis"
    ):
        return self._Cast_AdvancedSystemDeflectionSubAnalysis(self)
