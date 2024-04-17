"""ConvergenceLogger"""

from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility.convergence import _1582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVERGENCE_LOGGER = python_net_import(
    "SMT.MastaAPI.MathUtility.Convergence", "ConvergenceLogger"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConvergenceLogger",)


Self = TypeVar("Self", bound="ConvergenceLogger")


class ConvergenceLogger(_1582.DataLogger):
    """ConvergenceLogger

    This is a mastapy class.
    """

    TYPE = _CONVERGENCE_LOGGER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConvergenceLogger")

    class _Cast_ConvergenceLogger:
        """Special nested class for casting ConvergenceLogger to subclasses."""

        def __init__(
            self: "ConvergenceLogger._Cast_ConvergenceLogger",
            parent: "ConvergenceLogger",
        ):
            self._parent = parent

        @property
        def data_logger(
            self: "ConvergenceLogger._Cast_ConvergenceLogger",
        ) -> "_1582.DataLogger":
            return self._parent._cast(_1582.DataLogger)

        @property
        def convergence_logger(
            self: "ConvergenceLogger._Cast_ConvergenceLogger",
        ) -> "ConvergenceLogger":
            return self._parent

        def __getattr__(self: "ConvergenceLogger._Cast_ConvergenceLogger", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConvergenceLogger.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConvergenceLogger._Cast_ConvergenceLogger":
        return self._Cast_ConvergenceLogger(self)
