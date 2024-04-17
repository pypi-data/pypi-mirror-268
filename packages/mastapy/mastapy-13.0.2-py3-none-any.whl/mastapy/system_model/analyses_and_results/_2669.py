"""CompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundCriticalSpeedAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CompoundCriticalSpeedAnalysis")


class CompoundCriticalSpeedAnalysis(_2627.CompoundAnalysis):
    """CompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundCriticalSpeedAnalysis")

    class _Cast_CompoundCriticalSpeedAnalysis:
        """Special nested class for casting CompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CompoundCriticalSpeedAnalysis._Cast_CompoundCriticalSpeedAnalysis",
            parent: "CompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundCriticalSpeedAnalysis._Cast_CompoundCriticalSpeedAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundCriticalSpeedAnalysis._Cast_CompoundCriticalSpeedAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_critical_speed_analysis(
            self: "CompoundCriticalSpeedAnalysis._Cast_CompoundCriticalSpeedAnalysis",
        ) -> "CompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundCriticalSpeedAnalysis._Cast_CompoundCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundCriticalSpeedAnalysis._Cast_CompoundCriticalSpeedAnalysis":
        return self._Cast_CompoundCriticalSpeedAnalysis(self)
