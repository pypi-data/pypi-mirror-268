"""CompoundDynamicModelAtAStiffnessAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results import _2627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundDynamicModelAtAStiffnessAnalysis",
)

if TYPE_CHECKING:
    from mastapy import _7561


__docformat__ = "restructuredtext en"
__all__ = ("CompoundDynamicModelAtAStiffnessAnalysis",)


Self = TypeVar("Self", bound="CompoundDynamicModelAtAStiffnessAnalysis")


class CompoundDynamicModelAtAStiffnessAnalysis(_2627.CompoundAnalysis):
    """CompoundDynamicModelAtAStiffnessAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CompoundDynamicModelAtAStiffnessAnalysis"
    )

    class _Cast_CompoundDynamicModelAtAStiffnessAnalysis:
        """Special nested class for casting CompoundDynamicModelAtAStiffnessAnalysis to subclasses."""

        def __init__(
            self: "CompoundDynamicModelAtAStiffnessAnalysis._Cast_CompoundDynamicModelAtAStiffnessAnalysis",
            parent: "CompoundDynamicModelAtAStiffnessAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundDynamicModelAtAStiffnessAnalysis._Cast_CompoundDynamicModelAtAStiffnessAnalysis",
        ) -> "_2627.CompoundAnalysis":
            return self._parent._cast(_2627.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundDynamicModelAtAStiffnessAnalysis._Cast_CompoundDynamicModelAtAStiffnessAnalysis",
        ) -> "_7561.MarshalByRefObjectPermanent":
            from mastapy import _7561

            return self._parent._cast(_7561.MarshalByRefObjectPermanent)

        @property
        def compound_dynamic_model_at_a_stiffness_analysis(
            self: "CompoundDynamicModelAtAStiffnessAnalysis._Cast_CompoundDynamicModelAtAStiffnessAnalysis",
        ) -> "CompoundDynamicModelAtAStiffnessAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundDynamicModelAtAStiffnessAnalysis._Cast_CompoundDynamicModelAtAStiffnessAnalysis",
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
        self: Self, instance_to_wrap: "CompoundDynamicModelAtAStiffnessAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundDynamicModelAtAStiffnessAnalysis._Cast_CompoundDynamicModelAtAStiffnessAnalysis":
        return self._Cast_CompoundDynamicModelAtAStiffnessAnalysis(self)
