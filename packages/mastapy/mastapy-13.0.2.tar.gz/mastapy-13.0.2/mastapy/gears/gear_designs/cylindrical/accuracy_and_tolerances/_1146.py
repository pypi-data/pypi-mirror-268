"""DIN3967SystemOfGearFits"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN3967_SYSTEM_OF_GEAR_FITS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "DIN3967SystemOfGearFits",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1047, _1048


__docformat__ = "restructuredtext en"
__all__ = ("DIN3967SystemOfGearFits",)


Self = TypeVar("Self", bound="DIN3967SystemOfGearFits")


class DIN3967SystemOfGearFits(_0.APIBase):
    """DIN3967SystemOfGearFits

    This is a mastapy class.
    """

    TYPE = _DIN3967_SYSTEM_OF_GEAR_FITS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DIN3967SystemOfGearFits")

    class _Cast_DIN3967SystemOfGearFits:
        """Special nested class for casting DIN3967SystemOfGearFits to subclasses."""

        def __init__(
            self: "DIN3967SystemOfGearFits._Cast_DIN3967SystemOfGearFits",
            parent: "DIN3967SystemOfGearFits",
        ):
            self._parent = parent

        @property
        def din3967_system_of_gear_fits(
            self: "DIN3967SystemOfGearFits._Cast_DIN3967SystemOfGearFits",
        ) -> "DIN3967SystemOfGearFits":
            return self._parent

        def __getattr__(
            self: "DIN3967SystemOfGearFits._Cast_DIN3967SystemOfGearFits", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DIN3967SystemOfGearFits.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tooth_thickness_reduction_allowance(
        self: Self,
    ) -> "_1047.DIN3967AllowanceSeries":
        """mastapy.gears.gear_designs.cylindrical.DIN3967AllowanceSeries"""
        temp = self.wrapped.ToothThicknessReductionAllowance

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DIN3967AllowanceSeries"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1047", "DIN3967AllowanceSeries"
        )(value)

    @tooth_thickness_reduction_allowance.setter
    @enforce_parameter_types
    def tooth_thickness_reduction_allowance(
        self: Self, value: "_1047.DIN3967AllowanceSeries"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DIN3967AllowanceSeries"
        )
        self.wrapped.ToothThicknessReductionAllowance = value

    @property
    def tooth_thickness_tolerance(self: Self) -> "_1048.DIN3967ToleranceSeries":
        """mastapy.gears.gear_designs.cylindrical.DIN3967ToleranceSeries"""
        temp = self.wrapped.ToothThicknessTolerance

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DIN3967ToleranceSeries"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1048", "DIN3967ToleranceSeries"
        )(value)

    @tooth_thickness_tolerance.setter
    @enforce_parameter_types
    def tooth_thickness_tolerance(self: Self, value: "_1048.DIN3967ToleranceSeries"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DIN3967ToleranceSeries"
        )
        self.wrapped.ToothThicknessTolerance = value

    @property
    def cast_to(self: Self) -> "DIN3967SystemOfGearFits._Cast_DIN3967SystemOfGearFits":
        return self._Cast_DIN3967SystemOfGearFits(self)
