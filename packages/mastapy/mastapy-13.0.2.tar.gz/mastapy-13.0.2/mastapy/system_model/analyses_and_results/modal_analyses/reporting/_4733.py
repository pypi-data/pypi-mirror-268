"""ShaftPerModeResult"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4726
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_PER_MODE_RESULT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "ShaftPerModeResult",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftPerModeResult",)


Self = TypeVar("Self", bound="ShaftPerModeResult")


class ShaftPerModeResult(_4726.ComponentPerModeResult):
    """ShaftPerModeResult

    This is a mastapy class.
    """

    TYPE = _SHAFT_PER_MODE_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftPerModeResult")

    class _Cast_ShaftPerModeResult:
        """Special nested class for casting ShaftPerModeResult to subclasses."""

        def __init__(
            self: "ShaftPerModeResult._Cast_ShaftPerModeResult",
            parent: "ShaftPerModeResult",
        ):
            self._parent = parent

        @property
        def component_per_mode_result(
            self: "ShaftPerModeResult._Cast_ShaftPerModeResult",
        ) -> "_4726.ComponentPerModeResult":
            return self._parent._cast(_4726.ComponentPerModeResult)

        @property
        def shaft_per_mode_result(
            self: "ShaftPerModeResult._Cast_ShaftPerModeResult",
        ) -> "ShaftPerModeResult":
            return self._parent

        def __getattr__(self: "ShaftPerModeResult._Cast_ShaftPerModeResult", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftPerModeResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def torsional_mode_shape(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalModeShape

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ShaftPerModeResult._Cast_ShaftPerModeResult":
        return self._Cast_ShaftPerModeResult(self)
