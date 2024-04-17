"""CurrentPerLength"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CURRENT_PER_LENGTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "CurrentPerLength"
)


__docformat__ = "restructuredtext en"
__all__ = ("CurrentPerLength",)


Self = TypeVar("Self", bound="CurrentPerLength")


class CurrentPerLength(_1612.MeasurementBase):
    """CurrentPerLength

    This is a mastapy class.
    """

    TYPE = _CURRENT_PER_LENGTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CurrentPerLength")

    class _Cast_CurrentPerLength:
        """Special nested class for casting CurrentPerLength to subclasses."""

        def __init__(
            self: "CurrentPerLength._Cast_CurrentPerLength", parent: "CurrentPerLength"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "CurrentPerLength._Cast_CurrentPerLength",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def current_per_length(
            self: "CurrentPerLength._Cast_CurrentPerLength",
        ) -> "CurrentPerLength":
            return self._parent

        def __getattr__(self: "CurrentPerLength._Cast_CurrentPerLength", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CurrentPerLength.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CurrentPerLength._Cast_CurrentPerLength":
        return self._Cast_CurrentPerLength(self)
