"""AreaSmall"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AREA_SMALL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AreaSmall"
)


__docformat__ = "restructuredtext en"
__all__ = ("AreaSmall",)


Self = TypeVar("Self", bound="AreaSmall")


class AreaSmall(_1612.MeasurementBase):
    """AreaSmall

    This is a mastapy class.
    """

    TYPE = _AREA_SMALL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AreaSmall")

    class _Cast_AreaSmall:
        """Special nested class for casting AreaSmall to subclasses."""

        def __init__(self: "AreaSmall._Cast_AreaSmall", parent: "AreaSmall"):
            self._parent = parent

        @property
        def measurement_base(
            self: "AreaSmall._Cast_AreaSmall",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def area_small(self: "AreaSmall._Cast_AreaSmall") -> "AreaSmall":
            return self._parent

        def __getattr__(self: "AreaSmall._Cast_AreaSmall", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AreaSmall.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AreaSmall._Cast_AreaSmall":
        return self._Cast_AreaSmall(self)
