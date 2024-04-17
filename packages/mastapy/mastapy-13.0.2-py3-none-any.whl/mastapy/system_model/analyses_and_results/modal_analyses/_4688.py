"""ShaftModalAnalysisMode"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_ANALYSIS_MODE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ShaftModalAnalysisMode",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftModalAnalysisMode",)


Self = TypeVar("Self", bound="ShaftModalAnalysisMode")


class ShaftModalAnalysisMode(_0.APIBase):
    """ShaftModalAnalysisMode

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_ANALYSIS_MODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftModalAnalysisMode")

    class _Cast_ShaftModalAnalysisMode:
        """Special nested class for casting ShaftModalAnalysisMode to subclasses."""

        def __init__(
            self: "ShaftModalAnalysisMode._Cast_ShaftModalAnalysisMode",
            parent: "ShaftModalAnalysisMode",
        ):
            self._parent = parent

        @property
        def shaft_modal_analysis_mode(
            self: "ShaftModalAnalysisMode._Cast_ShaftModalAnalysisMode",
        ) -> "ShaftModalAnalysisMode":
            return self._parent

        def __getattr__(
            self: "ShaftModalAnalysisMode._Cast_ShaftModalAnalysisMode", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftModalAnalysisMode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_displacement(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def linear_displacement(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ShaftModalAnalysisMode._Cast_ShaftModalAnalysisMode":
        return self._Cast_ShaftModalAnalysisMode(self)
