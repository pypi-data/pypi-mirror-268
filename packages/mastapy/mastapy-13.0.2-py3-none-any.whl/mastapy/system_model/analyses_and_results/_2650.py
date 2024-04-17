"""StabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "StabilityAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("StabilityAnalysis",)


Self = TypeVar("Self", bound="StabilityAnalysis")


class StabilityAnalysis(_2628.SingleAnalysis):
    """StabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StabilityAnalysis")

    class _Cast_StabilityAnalysis:
        """Special nested class for casting StabilityAnalysis to subclasses."""

        def __init__(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
            parent: "StabilityAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def stability_analysis(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "StabilityAnalysis":
            return self._parent

        def __getattr__(self: "StabilityAnalysis._Cast_StabilityAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StabilityAnalysis._Cast_StabilityAnalysis":
        return self._Cast_StabilityAnalysis(self)
