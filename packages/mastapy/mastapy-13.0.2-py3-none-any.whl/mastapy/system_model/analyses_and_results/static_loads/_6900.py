"""GearManufactureError"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearManufactureError"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6854, _6871


__docformat__ = "restructuredtext en"
__all__ = ("GearManufactureError",)


Self = TypeVar("Self", bound="GearManufactureError")


class GearManufactureError(_0.APIBase):
    """GearManufactureError

    This is a mastapy class.
    """

    TYPE = _GEAR_MANUFACTURE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearManufactureError")

    class _Cast_GearManufactureError:
        """Special nested class for casting GearManufactureError to subclasses."""

        def __init__(
            self: "GearManufactureError._Cast_GearManufactureError",
            parent: "GearManufactureError",
        ):
            self._parent = parent

        @property
        def conical_gear_manufacture_error(
            self: "GearManufactureError._Cast_GearManufactureError",
        ) -> "_6854.ConicalGearManufactureError":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.ConicalGearManufactureError)

        @property
        def cylindrical_gear_manufacture_error(
            self: "GearManufactureError._Cast_GearManufactureError",
        ) -> "_6871.CylindricalGearManufactureError":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.CylindricalGearManufactureError)

        @property
        def gear_manufacture_error(
            self: "GearManufactureError._Cast_GearManufactureError",
        ) -> "GearManufactureError":
            return self._parent

        def __getattr__(
            self: "GearManufactureError._Cast_GearManufactureError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearManufactureError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_custom_pitch_errors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCustomPitchErrors

        if temp is None:
            return False

        return temp

    @use_custom_pitch_errors.setter
    @enforce_parameter_types
    def use_custom_pitch_errors(self: Self, value: "bool"):
        self.wrapped.UseCustomPitchErrors = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "GearManufactureError._Cast_GearManufactureError":
        return self._Cast_GearManufactureError(self)
