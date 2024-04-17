"""CriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CriticalSpeedAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CriticalSpeedAnalysis")


class CriticalSpeedAnalysis(_2628.SingleAnalysis):
    """CriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CriticalSpeedAnalysis")

    class _Cast_CriticalSpeedAnalysis:
        """Special nested class for casting CriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
            parent: "CriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def critical_speed_analysis(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis",
        ) -> "CriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CriticalSpeedAnalysis._Cast_CriticalSpeedAnalysis":
        return self._Cast_CriticalSpeedAnalysis(self)
