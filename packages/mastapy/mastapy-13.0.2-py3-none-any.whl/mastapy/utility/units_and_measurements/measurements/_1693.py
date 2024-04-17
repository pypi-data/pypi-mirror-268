"""MomentOfInertiaPerUnitLength"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_OF_INERTIA_PER_UNIT_LENGTH = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "MomentOfInertiaPerUnitLength",
)


__docformat__ = "restructuredtext en"
__all__ = ("MomentOfInertiaPerUnitLength",)


Self = TypeVar("Self", bound="MomentOfInertiaPerUnitLength")


class MomentOfInertiaPerUnitLength(_1612.MeasurementBase):
    """MomentOfInertiaPerUnitLength

    This is a mastapy class.
    """

    TYPE = _MOMENT_OF_INERTIA_PER_UNIT_LENGTH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MomentOfInertiaPerUnitLength")

    class _Cast_MomentOfInertiaPerUnitLength:
        """Special nested class for casting MomentOfInertiaPerUnitLength to subclasses."""

        def __init__(
            self: "MomentOfInertiaPerUnitLength._Cast_MomentOfInertiaPerUnitLength",
            parent: "MomentOfInertiaPerUnitLength",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "MomentOfInertiaPerUnitLength._Cast_MomentOfInertiaPerUnitLength",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def moment_of_inertia_per_unit_length(
            self: "MomentOfInertiaPerUnitLength._Cast_MomentOfInertiaPerUnitLength",
        ) -> "MomentOfInertiaPerUnitLength":
            return self._parent

        def __getattr__(
            self: "MomentOfInertiaPerUnitLength._Cast_MomentOfInertiaPerUnitLength",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MomentOfInertiaPerUnitLength.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MomentOfInertiaPerUnitLength._Cast_MomentOfInertiaPerUnitLength":
        return self._Cast_MomentOfInertiaPerUnitLength(self)
