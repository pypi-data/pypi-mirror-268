"""Eccentricity"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ECCENTRICITY = python_net_import("SMT.MastaAPI.ElectricMachines", "Eccentricity")


__docformat__ = "restructuredtext en"
__all__ = ("Eccentricity",)


Self = TypeVar("Self", bound="Eccentricity")


class Eccentricity(_1593.IndependentReportablePropertiesBase["Eccentricity"]):
    """Eccentricity

    This is a mastapy class.
    """

    TYPE = _ECCENTRICITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Eccentricity")

    class _Cast_Eccentricity:
        """Special nested class for casting Eccentricity to subclasses."""

        def __init__(self: "Eccentricity._Cast_Eccentricity", parent: "Eccentricity"):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "Eccentricity._Cast_Eccentricity",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def eccentricity(self: "Eccentricity._Cast_Eccentricity") -> "Eccentricity":
            return self._parent

        def __getattr__(self: "Eccentricity._Cast_Eccentricity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Eccentricity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DynamicX

        if temp is None:
            return 0.0

        return temp

    @dynamic_x.setter
    @enforce_parameter_types
    def dynamic_x(self: Self, value: "float"):
        self.wrapped.DynamicX = float(value) if value is not None else 0.0

    @property
    def dynamic_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DynamicY

        if temp is None:
            return 0.0

        return temp

    @dynamic_y.setter
    @enforce_parameter_types
    def dynamic_y(self: Self, value: "float"):
        self.wrapped.DynamicY = float(value) if value is not None else 0.0

    @property
    def static_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StaticX

        if temp is None:
            return 0.0

        return temp

    @static_x.setter
    @enforce_parameter_types
    def static_x(self: Self, value: "float"):
        self.wrapped.StaticX = float(value) if value is not None else 0.0

    @property
    def static_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StaticY

        if temp is None:
            return 0.0

        return temp

    @static_y.setter
    @enforce_parameter_types
    def static_y(self: Self, value: "float"):
        self.wrapped.StaticY = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "Eccentricity._Cast_Eccentricity":
        return self._Cast_Eccentricity(self)
