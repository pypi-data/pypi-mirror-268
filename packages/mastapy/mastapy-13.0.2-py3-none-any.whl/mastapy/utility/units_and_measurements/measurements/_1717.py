"""SpecificAcousticImpedance"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFIC_ACOUSTIC_IMPEDANCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "SpecificAcousticImpedance",
)


__docformat__ = "restructuredtext en"
__all__ = ("SpecificAcousticImpedance",)


Self = TypeVar("Self", bound="SpecificAcousticImpedance")


class SpecificAcousticImpedance(_1612.MeasurementBase):
    """SpecificAcousticImpedance

    This is a mastapy class.
    """

    TYPE = _SPECIFIC_ACOUSTIC_IMPEDANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecificAcousticImpedance")

    class _Cast_SpecificAcousticImpedance:
        """Special nested class for casting SpecificAcousticImpedance to subclasses."""

        def __init__(
            self: "SpecificAcousticImpedance._Cast_SpecificAcousticImpedance",
            parent: "SpecificAcousticImpedance",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "SpecificAcousticImpedance._Cast_SpecificAcousticImpedance",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def specific_acoustic_impedance(
            self: "SpecificAcousticImpedance._Cast_SpecificAcousticImpedance",
        ) -> "SpecificAcousticImpedance":
            return self._parent

        def __getattr__(
            self: "SpecificAcousticImpedance._Cast_SpecificAcousticImpedance", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpecificAcousticImpedance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SpecificAcousticImpedance._Cast_SpecificAcousticImpedance":
        return self._Cast_SpecificAcousticImpedance(self)
