"""MagnetomotiveForce"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETOMOTIVE_FORCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "MagnetomotiveForce"
)


__docformat__ = "restructuredtext en"
__all__ = ("MagnetomotiveForce",)


Self = TypeVar("Self", bound="MagnetomotiveForce")


class MagnetomotiveForce(_1612.MeasurementBase):
    """MagnetomotiveForce

    This is a mastapy class.
    """

    TYPE = _MAGNETOMOTIVE_FORCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagnetomotiveForce")

    class _Cast_MagnetomotiveForce:
        """Special nested class for casting MagnetomotiveForce to subclasses."""

        def __init__(
            self: "MagnetomotiveForce._Cast_MagnetomotiveForce",
            parent: "MagnetomotiveForce",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "MagnetomotiveForce._Cast_MagnetomotiveForce",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def magnetomotive_force(
            self: "MagnetomotiveForce._Cast_MagnetomotiveForce",
        ) -> "MagnetomotiveForce":
            return self._parent

        def __getattr__(self: "MagnetomotiveForce._Cast_MagnetomotiveForce", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagnetomotiveForce.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MagnetomotiveForce._Cast_MagnetomotiveForce":
        return self._Cast_MagnetomotiveForce(self)
