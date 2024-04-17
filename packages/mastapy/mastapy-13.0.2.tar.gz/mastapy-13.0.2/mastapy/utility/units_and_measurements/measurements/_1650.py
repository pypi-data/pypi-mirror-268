"""ForcePerUnitLength"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_PER_UNIT_LENGTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "ForcePerUnitLength"
)


__docformat__ = "restructuredtext en"
__all__ = ("ForcePerUnitLength",)


Self = TypeVar("Self", bound="ForcePerUnitLength")


class ForcePerUnitLength(_1612.MeasurementBase):
    """ForcePerUnitLength

    This is a mastapy class.
    """

    TYPE = _FORCE_PER_UNIT_LENGTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForcePerUnitLength")

    class _Cast_ForcePerUnitLength:
        """Special nested class for casting ForcePerUnitLength to subclasses."""

        def __init__(
            self: "ForcePerUnitLength._Cast_ForcePerUnitLength",
            parent: "ForcePerUnitLength",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "ForcePerUnitLength._Cast_ForcePerUnitLength",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def force_per_unit_length(
            self: "ForcePerUnitLength._Cast_ForcePerUnitLength",
        ) -> "ForcePerUnitLength":
            return self._parent

        def __getattr__(self: "ForcePerUnitLength._Cast_ForcePerUnitLength", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForcePerUnitLength.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ForcePerUnitLength._Cast_ForcePerUnitLength":
        return self._Cast_ForcePerUnitLength(self)
