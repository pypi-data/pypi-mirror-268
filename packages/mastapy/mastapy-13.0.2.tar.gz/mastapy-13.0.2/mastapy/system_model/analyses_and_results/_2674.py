"""CompoundDynamicModelForStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundDynamicModelForStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundDynamicModelForStabilityAnalysis",)


Self = TypeVar("Self", bound="CompoundDynamicModelForStabilityAnalysis")


class CompoundDynamicModelForStabilityAnalysis(_2627.CompoundAnalysis):
    """CompoundDynamicModelForStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_MODEL_FOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundDynamicModelForStabilityAnalysis"
    )

    class _Cast_CompoundDynamicModelForStabilityAnalysis:
        """Special nested class for casting CompoundDynamicModelForStabilityAnalysis to subclasses."""

        def __init__(
            self: "CompoundDynamicModelForStabilityAnalysis._Cast_CompoundDynamicModelForStabilityAnalysis",
            parent: "CompoundDynamicModelForStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundDynamicModelForStabilityAnalysis._Cast_CompoundDynamicModelForStabilityAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundDynamicModelForStabilityAnalysis._Cast_CompoundDynamicModelForStabilityAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_dynamic_model_for_stability_analysis(
            self: "CompoundDynamicModelForStabilityAnalysis._Cast_CompoundDynamicModelForStabilityAnalysis",
        ) -> "CompoundDynamicModelForStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundDynamicModelForStabilityAnalysis._Cast_CompoundDynamicModelForStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CompoundDynamicModelForStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundDynamicModelForStabilityAnalysis._Cast_CompoundDynamicModelForStabilityAnalysis":
        return self._Cast_CompoundDynamicModelForStabilityAnalysis(self)
