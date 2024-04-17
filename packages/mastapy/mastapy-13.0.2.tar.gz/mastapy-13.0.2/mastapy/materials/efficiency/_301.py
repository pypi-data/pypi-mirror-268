"""OilPumpDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_PUMP_DETAIL = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "OilPumpDetail"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.materials.efficiency import _302


__docformat__ = "restructuredtext en"
__all__ = ("OilPumpDetail",)


Self = TypeVar("Self", bound="OilPumpDetail")


class OilPumpDetail(_1593.IndependentReportablePropertiesBase["OilPumpDetail"]):
    """OilPumpDetail

    This is a mastapy class.
    """

    TYPE = _OIL_PUMP_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilPumpDetail")

    class _Cast_OilPumpDetail:
        """Special nested class for casting OilPumpDetail to subclasses."""

        def __init__(
            self: "OilPumpDetail._Cast_OilPumpDetail", parent: "OilPumpDetail"
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "OilPumpDetail._Cast_OilPumpDetail",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def oil_pump_detail(
            self: "OilPumpDetail._Cast_OilPumpDetail",
        ) -> "OilPumpDetail":
            return self._parent

        def __getattr__(self: "OilPumpDetail._Cast_OilPumpDetail", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilPumpDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_motor_efficiency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ElectricMotorEfficiency

        if temp is None:
            return 0.0

        return temp

    @electric_motor_efficiency.setter
    @enforce_parameter_types
    def electric_motor_efficiency(self: Self, value: "float"):
        self.wrapped.ElectricMotorEfficiency = (
            float(value) if value is not None else 0.0
        )

    @property
    def electric_power_consumed_vs_speed(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.ElectricPowerConsumedVsSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @electric_power_consumed_vs_speed.setter
    @enforce_parameter_types
    def electric_power_consumed_vs_speed(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.ElectricPowerConsumedVsSpeed = value.wrapped

    @property
    def oil_flow_rate_vs_speed(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.OilFlowRateVsSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @oil_flow_rate_vs_speed.setter
    @enforce_parameter_types
    def oil_flow_rate_vs_speed(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.OilFlowRateVsSpeed = value.wrapped

    @property
    def oil_pump_drive_type(self: Self) -> "_302.OilPumpDriveType":
        """mastapy.materials.efficiency.OilPumpDriveType"""
        temp = self.wrapped.OilPumpDriveType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.Efficiency.OilPumpDriveType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials.efficiency._302", "OilPumpDriveType"
        )(value)

    @oil_pump_drive_type.setter
    @enforce_parameter_types
    def oil_pump_drive_type(self: Self, value: "_302.OilPumpDriveType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.Efficiency.OilPumpDriveType"
        )
        self.wrapped.OilPumpDriveType = value

    @property
    def oil_pump_efficiency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilPumpEfficiency

        if temp is None:
            return 0.0

        return temp

    @oil_pump_efficiency.setter
    @enforce_parameter_types
    def oil_pump_efficiency(self: Self, value: "float"):
        self.wrapped.OilPumpEfficiency = float(value) if value is not None else 0.0

    @property
    def operating_oil_pressure_vs_speed(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.OperatingOilPressureVsSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @operating_oil_pressure_vs_speed.setter
    @enforce_parameter_types
    def operating_oil_pressure_vs_speed(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.OperatingOilPressureVsSpeed = value.wrapped

    @property
    def cast_to(self: Self) -> "OilPumpDetail._Cast_OilPumpDetail":
        return self._Cast_OilPumpDetail(self)
