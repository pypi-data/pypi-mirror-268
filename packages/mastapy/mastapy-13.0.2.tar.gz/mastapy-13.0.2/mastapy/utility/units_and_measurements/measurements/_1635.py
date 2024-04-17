"""Damage"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.units_and_measurements.measurements import _1653
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DAMAGE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Damage"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1612


__docformat__ = "restructuredtext en"
__all__ = ("Damage",)


Self = TypeVar("Self", bound="Damage")


class Damage(_1653.FractionMeasurementBase):
    """Damage

    This is a mastapy class.
    """

    TYPE = _DAMAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Damage")

    class _Cast_Damage:
        """Special nested class for casting Damage to subclasses."""

        def __init__(self: "Damage._Cast_Damage", parent: "Damage"):
            self._parent = parent

        @property
        def fraction_measurement_base(
            self: "Damage._Cast_Damage",
        ) -> "_1653.FractionMeasurementBase":
            return self._parent._cast(_1653.FractionMeasurementBase)

        @property
        def measurement_base(self: "Damage._Cast_Damage") -> "_1612.MeasurementBase":
            from mastapy.utility.units_and_measurements import _1612

            return self._parent._cast(_1612.MeasurementBase)

        @property
        def damage(self: "Damage._Cast_Damage") -> "Damage":
            return self._parent

        def __getattr__(self: "Damage._Cast_Damage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Damage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Damage._Cast_Damage":
        return self._Cast_Damage(self)
