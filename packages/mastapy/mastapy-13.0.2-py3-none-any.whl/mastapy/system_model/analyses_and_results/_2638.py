"""DynamicModelForStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2628
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "DynamicModelForStabilityAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForStabilityAnalysis",)


Self = TypeVar("Self", bound="DynamicModelForStabilityAnalysis")


class DynamicModelForStabilityAnalysis(_2628.SingleAnalysis):
    """DynamicModelForStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelForStabilityAnalysis")

    class _Cast_DynamicModelForStabilityAnalysis:
        """Special nested class for casting DynamicModelForStabilityAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
            parent: "DynamicModelForStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_2628.SingleAnalysis":
            return self._parent._cast(_2628.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def dynamic_model_for_stability_analysis(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
        ) -> "DynamicModelForStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelForStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForStabilityAnalysis._Cast_DynamicModelForStabilityAnalysis":
        return self._Cast_DynamicModelForStabilityAnalysis(self)
