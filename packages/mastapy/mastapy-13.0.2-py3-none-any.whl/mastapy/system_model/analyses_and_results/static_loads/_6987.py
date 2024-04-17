"""TransmissionEfficiencySettings"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSMISSION_EFFICIENCY_SETTINGS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TransmissionEfficiencySettings",
)


__docformat__ = "restructuredtext en"
__all__ = ("TransmissionEfficiencySettings",)


Self = TypeVar("Self", bound="TransmissionEfficiencySettings")


class TransmissionEfficiencySettings(_0.APIBase):
    """TransmissionEfficiencySettings

    This is a mastapy class.
    """

    TYPE = _TRANSMISSION_EFFICIENCY_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TransmissionEfficiencySettings")

    class _Cast_TransmissionEfficiencySettings:
        """Special nested class for casting TransmissionEfficiencySettings to subclasses."""

        def __init__(
            self: "TransmissionEfficiencySettings._Cast_TransmissionEfficiencySettings",
            parent: "TransmissionEfficiencySettings",
        ):
            self._parent = parent

        @property
        def transmission_efficiency_settings(
            self: "TransmissionEfficiencySettings._Cast_TransmissionEfficiencySettings",
        ) -> "TransmissionEfficiencySettings":
            return self._parent

        def __getattr__(
            self: "TransmissionEfficiencySettings._Cast_TransmissionEfficiencySettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TransmissionEfficiencySettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_bearing_and_seal_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingAndSealLoss

        if temp is None:
            return False

        return temp

    @include_bearing_and_seal_loss.setter
    @enforce_parameter_types
    def include_bearing_and_seal_loss(self: Self, value: "bool"):
        self.wrapped.IncludeBearingAndSealLoss = (
            bool(value) if value is not None else False
        )

    @property
    def include_belt_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBeltLoss

        if temp is None:
            return False

        return temp

    @include_belt_loss.setter
    @enforce_parameter_types
    def include_belt_loss(self: Self, value: "bool"):
        self.wrapped.IncludeBeltLoss = bool(value) if value is not None else False

    @property
    def include_clearance_bearing_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeClearanceBearingLoss

        if temp is None:
            return False

        return temp

    @include_clearance_bearing_loss.setter
    @enforce_parameter_types
    def include_clearance_bearing_loss(self: Self, value: "bool"):
        self.wrapped.IncludeClearanceBearingLoss = (
            bool(value) if value is not None else False
        )

    @property
    def include_clutch_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeClutchLoss

        if temp is None:
            return False

        return temp

    @include_clutch_loss.setter
    @enforce_parameter_types
    def include_clutch_loss(self: Self, value: "bool"):
        self.wrapped.IncludeClutchLoss = bool(value) if value is not None else False

    @property
    def include_efficiency(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeEfficiency

        if temp is None:
            return False

        return temp

    @include_efficiency.setter
    @enforce_parameter_types
    def include_efficiency(self: Self, value: "bool"):
        self.wrapped.IncludeEfficiency = bool(value) if value is not None else False

    @property
    def include_gear_mesh_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGearMeshLoss

        if temp is None:
            return False

        return temp

    @include_gear_mesh_loss.setter
    @enforce_parameter_types
    def include_gear_mesh_loss(self: Self, value: "bool"):
        self.wrapped.IncludeGearMeshLoss = bool(value) if value is not None else False

    @property
    def include_gear_windage_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGearWindageLoss

        if temp is None:
            return False

        return temp

    @include_gear_windage_loss.setter
    @enforce_parameter_types
    def include_gear_windage_loss(self: Self, value: "bool"):
        self.wrapped.IncludeGearWindageLoss = (
            bool(value) if value is not None else False
        )

    @property
    def include_oil_pump_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeOilPumpLoss

        if temp is None:
            return False

        return temp

    @include_oil_pump_loss.setter
    @enforce_parameter_types
    def include_oil_pump_loss(self: Self, value: "bool"):
        self.wrapped.IncludeOilPumpLoss = bool(value) if value is not None else False

    @property
    def include_shaft_windage_loss(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeShaftWindageLoss

        if temp is None:
            return False

        return temp

    @include_shaft_windage_loss.setter
    @enforce_parameter_types
    def include_shaft_windage_loss(self: Self, value: "bool"):
        self.wrapped.IncludeShaftWindageLoss = (
            bool(value) if value is not None else False
        )

    @property
    def use_advanced_needle_roller_bearing_power_loss_calculation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedNeedleRollerBearingPowerLossCalculation

        if temp is None:
            return False

        return temp

    @use_advanced_needle_roller_bearing_power_loss_calculation.setter
    @enforce_parameter_types
    def use_advanced_needle_roller_bearing_power_loss_calculation(
        self: Self, value: "bool"
    ):
        self.wrapped.UseAdvancedNeedleRollerBearingPowerLossCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def volumetric_oil_air_mixture_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.VolumetricOilAirMixtureRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @volumetric_oil_air_mixture_ratio.setter
    @enforce_parameter_types
    def volumetric_oil_air_mixture_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.VolumetricOilAirMixtureRatio = value

    @property
    def cast_to(
        self: Self,
    ) -> "TransmissionEfficiencySettings._Cast_TransmissionEfficiencySettings":
        return self._Cast_TransmissionEfficiencySettings(self)
