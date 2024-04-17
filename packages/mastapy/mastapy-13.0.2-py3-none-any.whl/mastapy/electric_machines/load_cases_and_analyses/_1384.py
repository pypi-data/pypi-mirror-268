"""Temperatures"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEMPERATURES = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "Temperatures"
)


__docformat__ = "restructuredtext en"
__all__ = ("Temperatures",)


Self = TypeVar("Self", bound="Temperatures")


class Temperatures(_1593.IndependentReportablePropertiesBase["Temperatures"]):
    """Temperatures

    This is a mastapy class.
    """

    TYPE = _TEMPERATURES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Temperatures")

    class _Cast_Temperatures:
        """Special nested class for casting Temperatures to subclasses."""

        def __init__(self: "Temperatures._Cast_Temperatures", parent: "Temperatures"):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "Temperatures._Cast_Temperatures",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def temperatures(self: "Temperatures._Cast_Temperatures") -> "Temperatures":
            return self._parent

        def __getattr__(self: "Temperatures._Cast_Temperatures", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Temperatures.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnet_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MagnetTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @magnet_temperature.setter
    @enforce_parameter_types
    def magnet_temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MagnetTemperature = value

    @property
    def windings_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WindingsTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @windings_temperature.setter
    @enforce_parameter_types
    def windings_temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WindingsTemperature = value

    @property
    def cast_to(self: Self) -> "Temperatures._Cast_Temperatures":
        return self._Cast_Temperatures(self)
