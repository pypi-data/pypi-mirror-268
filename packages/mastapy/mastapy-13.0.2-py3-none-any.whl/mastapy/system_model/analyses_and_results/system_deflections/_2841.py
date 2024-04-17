"""TransmissionErrorResult"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSMISSION_ERROR_RESULT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "TransmissionErrorResult",
)


__docformat__ = "restructuredtext en"
__all__ = ("TransmissionErrorResult",)


Self = TypeVar("Self", bound="TransmissionErrorResult")


class TransmissionErrorResult(_0.APIBase):
    """TransmissionErrorResult

    This is a mastapy class.
    """

    TYPE = _TRANSMISSION_ERROR_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TransmissionErrorResult")

    class _Cast_TransmissionErrorResult:
        """Special nested class for casting TransmissionErrorResult to subclasses."""

        def __init__(
            self: "TransmissionErrorResult._Cast_TransmissionErrorResult",
            parent: "TransmissionErrorResult",
        ):
            self._parent = parent

        @property
        def transmission_error_result(
            self: "TransmissionErrorResult._Cast_TransmissionErrorResult",
        ) -> "TransmissionErrorResult":
            return self._parent

        def __getattr__(
            self: "TransmissionErrorResult._Cast_TransmissionErrorResult", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TransmissionErrorResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def transmission_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TransmissionError

        if temp is None:
            return 0.0

        return temp

    @transmission_error.setter
    @enforce_parameter_types
    def transmission_error(self: Self, value: "float"):
        self.wrapped.TransmissionError = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "TransmissionErrorResult._Cast_TransmissionErrorResult":
        return self._Cast_TransmissionErrorResult(self)
