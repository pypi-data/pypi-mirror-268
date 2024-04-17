"""HobManufactureError"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _692
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOB_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobManufactureError",
)


__docformat__ = "restructuredtext en"
__all__ = ("HobManufactureError",)


Self = TypeVar("Self", bound="HobManufactureError")


class HobManufactureError(_692.RackManufactureError):
    """HobManufactureError

    This is a mastapy class.
    """

    TYPE = _HOB_MANUFACTURE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobManufactureError")

    class _Cast_HobManufactureError:
        """Special nested class for casting HobManufactureError to subclasses."""

        def __init__(
            self: "HobManufactureError._Cast_HobManufactureError",
            parent: "HobManufactureError",
        ):
            self._parent = parent

        @property
        def rack_manufacture_error(
            self: "HobManufactureError._Cast_HobManufactureError",
        ) -> "_692.RackManufactureError":
            return self._parent._cast(_692.RackManufactureError)

        @property
        def hob_manufacture_error(
            self: "HobManufactureError._Cast_HobManufactureError",
        ) -> "HobManufactureError":
            return self._parent

        def __getattr__(
            self: "HobManufactureError._Cast_HobManufactureError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobManufactureError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_relief_variation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TotalReliefVariation

        if temp is None:
            return 0.0

        return temp

    @total_relief_variation.setter
    @enforce_parameter_types
    def total_relief_variation(self: Self, value: "float"):
        self.wrapped.TotalReliefVariation = float(value) if value is not None else 0.0

    @property
    def use_sin_curve_for_top_relief(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSinCurveForTopRelief

        if temp is None:
            return False

        return temp

    @use_sin_curve_for_top_relief.setter
    @enforce_parameter_types
    def use_sin_curve_for_top_relief(self: Self, value: "bool"):
        self.wrapped.UseSinCurveForTopRelief = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "HobManufactureError._Cast_HobManufactureError":
        return self._Cast_HobManufactureError(self)
