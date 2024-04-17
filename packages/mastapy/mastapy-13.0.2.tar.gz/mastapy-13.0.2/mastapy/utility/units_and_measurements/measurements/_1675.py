"""LengthToTheFourth"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_TO_THE_FOURTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LengthToTheFourth"
)


__docformat__ = "restructuredtext en"
__all__ = ("LengthToTheFourth",)


Self = TypeVar("Self", bound="LengthToTheFourth")


class LengthToTheFourth(_1612.MeasurementBase):
    """LengthToTheFourth

    This is a mastapy class.
    """

    TYPE = _LENGTH_TO_THE_FOURTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthToTheFourth")

    class _Cast_LengthToTheFourth:
        """Special nested class for casting LengthToTheFourth to subclasses."""

        def __init__(
            self: "LengthToTheFourth._Cast_LengthToTheFourth",
            parent: "LengthToTheFourth",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthToTheFourth._Cast_LengthToTheFourth",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_to_the_fourth(
            self: "LengthToTheFourth._Cast_LengthToTheFourth",
        ) -> "LengthToTheFourth":
            return self._parent

        def __getattr__(self: "LengthToTheFourth._Cast_LengthToTheFourth", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthToTheFourth.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LengthToTheFourth._Cast_LengthToTheFourth":
        return self._Cast_LengthToTheFourth(self)
