"""DummyRollingBearing"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs import _2137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUMMY_ROLLING_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "DummyRollingBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("DummyRollingBearing",)


Self = TypeVar("Self", bound="DummyRollingBearing")


class DummyRollingBearing(_2137.BearingDesign):
    """DummyRollingBearing

    This is a mastapy class.
    """

    TYPE = _DUMMY_ROLLING_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DummyRollingBearing")

    class _Cast_DummyRollingBearing:
        """Special nested class for casting DummyRollingBearing to subclasses."""

        def __init__(
            self: "DummyRollingBearing._Cast_DummyRollingBearing",
            parent: "DummyRollingBearing",
        ):
            self._parent = parent

        @property
        def bearing_design(
            self: "DummyRollingBearing._Cast_DummyRollingBearing",
        ) -> "_2137.BearingDesign":
            return self._parent._cast(_2137.BearingDesign)

        @property
        def dummy_rolling_bearing(
            self: "DummyRollingBearing._Cast_DummyRollingBearing",
        ) -> "DummyRollingBearing":
            return self._parent

        def __getattr__(
            self: "DummyRollingBearing._Cast_DummyRollingBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DummyRollingBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "float"):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "DummyRollingBearing._Cast_DummyRollingBearing":
        return self._Cast_DummyRollingBearing(self)
