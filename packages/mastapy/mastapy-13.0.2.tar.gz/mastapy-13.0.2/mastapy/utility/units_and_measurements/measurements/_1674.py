"""LengthShort"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_SHORT = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LengthShort"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1617


__docformat__ = "restructuredtext en"
__all__ = ("LengthShort",)


Self = TypeVar("Self", bound="LengthShort")


class LengthShort(_1612.MeasurementBase):
    """LengthShort

    This is a mastapy class.
    """

    TYPE = _LENGTH_SHORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LengthShort")

    class _Cast_LengthShort:
        """Special nested class for casting LengthShort to subclasses."""

        def __init__(self: "LengthShort._Cast_LengthShort", parent: "LengthShort"):
            self._parent = parent

        @property
        def measurement_base(
            self: "LengthShort._Cast_LengthShort",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def length_short(self: "LengthShort._Cast_LengthShort") -> "LengthShort":
            return self._parent

        def __getattr__(self: "LengthShort._Cast_LengthShort", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LengthShort.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def feet(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Feet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inches(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Inches

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def metres(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Metres

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micrometres(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Micrometres

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def millimetres(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Millimetres

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def thousandths_of_an_inch(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThousandthsOfAnInch

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "LengthShort._Cast_LengthShort":
        return self._Cast_LengthShort(self)
