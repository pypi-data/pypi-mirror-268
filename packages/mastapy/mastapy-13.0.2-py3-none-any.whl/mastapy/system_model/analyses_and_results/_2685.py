"""CompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundStabilityAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CompoundStabilityAnalysis")


class CompoundStabilityAnalysis(_2627.CompoundAnalysis):
    """CompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundStabilityAnalysis")

    class _Cast_CompoundStabilityAnalysis:
        """Special nested class for casting CompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CompoundStabilityAnalysis._Cast_CompoundStabilityAnalysis",
            parent: "CompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundStabilityAnalysis._Cast_CompoundStabilityAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundStabilityAnalysis._Cast_CompoundStabilityAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_stability_analysis(
            self: "CompoundStabilityAnalysis._Cast_CompoundStabilityAnalysis",
        ) -> "CompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundStabilityAnalysis._Cast_CompoundStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundStabilityAnalysis._Cast_CompoundStabilityAnalysis":
        return self._Cast_CompoundStabilityAnalysis(self)
