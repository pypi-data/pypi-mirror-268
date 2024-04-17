"""AngularCompliance"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_COMPLIANCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AngularCompliance"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngularCompliance",)


Self = TypeVar("Self", bound="AngularCompliance")


class AngularCompliance(_1612.MeasurementBase):
    """AngularCompliance

    This is a mastapy class.
    """

    TYPE = _ANGULAR_COMPLIANCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularCompliance")

    class _Cast_AngularCompliance:
        """Special nested class for casting AngularCompliance to subclasses."""

        def __init__(
            self: "AngularCompliance._Cast_AngularCompliance",
            parent: "AngularCompliance",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "AngularCompliance._Cast_AngularCompliance",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angular_compliance(
            self: "AngularCompliance._Cast_AngularCompliance",
        ) -> "AngularCompliance":
            return self._parent

        def __getattr__(self: "AngularCompliance._Cast_AngularCompliance", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularCompliance.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AngularCompliance._Cast_AngularCompliance":
        return self._Cast_AngularCompliance(self)
