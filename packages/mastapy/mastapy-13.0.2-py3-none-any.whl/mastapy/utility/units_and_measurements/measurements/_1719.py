"""SquareRootOfUnitForcePerUnitArea"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQUARE_ROOT_OF_UNIT_FORCE_PER_UNIT_AREA = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "SquareRootOfUnitForcePerUnitArea",
)


__docformat__ = "restructuredtext en"
__all__ = ("SquareRootOfUnitForcePerUnitArea",)


Self = TypeVar("Self", bound="SquareRootOfUnitForcePerUnitArea")


class SquareRootOfUnitForcePerUnitArea(_1612.MeasurementBase):
    """SquareRootOfUnitForcePerUnitArea

    This is a mastapy class.
    """

    TYPE = _SQUARE_ROOT_OF_UNIT_FORCE_PER_UNIT_AREA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SquareRootOfUnitForcePerUnitArea")

    class _Cast_SquareRootOfUnitForcePerUnitArea:
        """Special nested class for casting SquareRootOfUnitForcePerUnitArea to subclasses."""

        def __init__(
            self: "SquareRootOfUnitForcePerUnitArea._Cast_SquareRootOfUnitForcePerUnitArea",
            parent: "SquareRootOfUnitForcePerUnitArea",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "SquareRootOfUnitForcePerUnitArea._Cast_SquareRootOfUnitForcePerUnitArea",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def square_root_of_unit_force_per_unit_area(
            self: "SquareRootOfUnitForcePerUnitArea._Cast_SquareRootOfUnitForcePerUnitArea",
        ) -> "SquareRootOfUnitForcePerUnitArea":
            return self._parent

        def __getattr__(
            self: "SquareRootOfUnitForcePerUnitArea._Cast_SquareRootOfUnitForcePerUnitArea",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SquareRootOfUnitForcePerUnitArea.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SquareRootOfUnitForcePerUnitArea._Cast_SquareRootOfUnitForcePerUnitArea":
        return self._Cast_SquareRootOfUnitForcePerUnitArea(self)
