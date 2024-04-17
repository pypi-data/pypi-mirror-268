"""Force"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "Force"
)

if TYPE_CHECKING:
    from mastapy.utility.units_and_measurements import _1617


__docformat__ = "restructuredtext en"
__all__ = ("Force",)


Self = TypeVar("Self", bound="Force")


class Force(_1612.MeasurementBase):
    """Force

    This is a mastapy class.
    """

    TYPE = _FORCE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Force")

    class _Cast_Force:
        """Special nested class for casting Force to subclasses."""

        def __init__(self: "Force._Cast_Force", parent: "Force"):
            self._parent = parent

        @property
        def measurement_base(self: "Force._Cast_Force") -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def force(self: "Force._Cast_Force") -> "Force":
            return self._parent

        def __getattr__(self: "Force._Cast_Force", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Force.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def kilograms_force(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KilogramsForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def kilonewtons(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Kilonewtons

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def millinewtons(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Millinewtons

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def newtons(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Newtons

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ounces_force(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuncesForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pounds_force(self: Self) -> "_1617.Unit":
        """mastapy.utility.units_and_measurements.Unit

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PoundsForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Force._Cast_Force":
        return self._Cast_Force(self)
