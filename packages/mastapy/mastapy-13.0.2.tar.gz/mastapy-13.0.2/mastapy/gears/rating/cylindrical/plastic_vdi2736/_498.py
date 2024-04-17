"""PlasticSNCurveForTheSpecifiedOperatingConditions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.materials import _607
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_SN_CURVE_FOR_THE_SPECIFIED_OPERATING_CONDITIONS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "PlasticSNCurveForTheSpecifiedOperatingConditions",
)

if TYPE_CHECKING:
    from mastapy.materials import _291


__docformat__ = "restructuredtext en"
__all__ = ("PlasticSNCurveForTheSpecifiedOperatingConditions",)


Self = TypeVar("Self", bound="PlasticSNCurveForTheSpecifiedOperatingConditions")


class PlasticSNCurveForTheSpecifiedOperatingConditions(_607.PlasticSNCurve):
    """PlasticSNCurveForTheSpecifiedOperatingConditions

    This is a mastapy class.
    """

    TYPE = _PLASTIC_SN_CURVE_FOR_THE_SPECIFIED_OPERATING_CONDITIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlasticSNCurveForTheSpecifiedOperatingConditions"
    )

    class _Cast_PlasticSNCurveForTheSpecifiedOperatingConditions:
        """Special nested class for casting PlasticSNCurveForTheSpecifiedOperatingConditions to subclasses."""

        def __init__(
            self: "PlasticSNCurveForTheSpecifiedOperatingConditions._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions",
            parent: "PlasticSNCurveForTheSpecifiedOperatingConditions",
        ):
            self._parent = parent

        @property
        def plastic_sn_curve(
            self: "PlasticSNCurveForTheSpecifiedOperatingConditions._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions",
        ) -> "_607.PlasticSNCurve":
            return self._parent._cast(_607.PlasticSNCurve)

        @property
        def plastic_sn_curve_for_the_specified_operating_conditions(
            self: "PlasticSNCurveForTheSpecifiedOperatingConditions._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions",
        ) -> "PlasticSNCurveForTheSpecifiedOperatingConditions":
            return self._parent

        def __getattr__(
            self: "PlasticSNCurveForTheSpecifiedOperatingConditions._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "PlasticSNCurveForTheSpecifiedOperatingConditions.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlankTemperature

        if temp is None:
            return 0.0

        return temp

    @flank_temperature.setter
    @enforce_parameter_types
    def flank_temperature(self: Self, value: "float"):
        self.wrapped.FlankTemperature = float(value) if value is not None else 0.0

    @property
    def life_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LifeCycles

        if temp is None:
            return 0.0

        return temp

    @life_cycles.setter
    @enforce_parameter_types
    def life_cycles(self: Self, value: "float"):
        self.wrapped.LifeCycles = float(value) if value is not None else 0.0

    @property
    def lubricant(self: Self) -> "_291.VDI2736LubricantType":
        """mastapy.materials.VDI2736LubricantType"""
        temp = self.wrapped.Lubricant

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.VDI2736LubricantType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._291", "VDI2736LubricantType"
        )(value)

    @lubricant.setter
    @enforce_parameter_types
    def lubricant(self: Self, value: "_291.VDI2736LubricantType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.VDI2736LubricantType"
        )
        self.wrapped.Lubricant = value

    @property
    def root_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RootTemperature

        if temp is None:
            return 0.0

        return temp

    @root_temperature.setter
    @enforce_parameter_types
    def root_temperature(self: Self, value: "float"):
        self.wrapped.RootTemperature = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "PlasticSNCurveForTheSpecifiedOperatingConditions._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions":
        return self._Cast_PlasticSNCurveForTheSpecifiedOperatingConditions(self)
