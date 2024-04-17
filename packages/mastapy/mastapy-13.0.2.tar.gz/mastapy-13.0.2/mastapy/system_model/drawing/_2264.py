"""StabilityAnalysisViewable"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.drawing import _2262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "StabilityAnalysisViewable"
)


__docformat__ = "restructuredtext en"
__all__ = ("StabilityAnalysisViewable",)


Self = TypeVar("Self", bound="StabilityAnalysisViewable")


class StabilityAnalysisViewable(_2262.RotorDynamicsViewable):
    """StabilityAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StabilityAnalysisViewable")

    class _Cast_StabilityAnalysisViewable:
        """Special nested class for casting StabilityAnalysisViewable to subclasses."""

        def __init__(
            self: "StabilityAnalysisViewable._Cast_StabilityAnalysisViewable",
            parent: "StabilityAnalysisViewable",
        ):
            self._parent = parent

        @property
        def rotor_dynamics_viewable(
            self: "StabilityAnalysisViewable._Cast_StabilityAnalysisViewable",
        ) -> "_2262.RotorDynamicsViewable":
            return self._parent._cast(_2262.RotorDynamicsViewable)

        @property
        def stability_analysis_viewable(
            self: "StabilityAnalysisViewable._Cast_StabilityAnalysisViewable",
        ) -> "StabilityAnalysisViewable":
            return self._parent

        def __getattr__(
            self: "StabilityAnalysisViewable._Cast_StabilityAnalysisViewable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StabilityAnalysisViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StabilityAnalysisViewable._Cast_StabilityAnalysisViewable":
        return self._Cast_StabilityAnalysisViewable(self)
