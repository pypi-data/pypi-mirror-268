"""TorqueConverter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2591
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616, _2618
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverter",)


Self = TypeVar("Self", bound="TorqueConverter")


class TorqueConverter(_2591.Coupling):
    """TorqueConverter

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverter")

    class _Cast_TorqueConverter:
        """Special nested class for casting TorqueConverter to subclasses."""

        def __init__(
            self: "TorqueConverter._Cast_TorqueConverter", parent: "TorqueConverter"
        ):
            self._parent = parent

        @property
        def coupling(self: "TorqueConverter._Cast_TorqueConverter") -> "_2591.Coupling":
            return self._parent._cast(_2591.Coupling)

        @property
        def specialised_assembly(
            self: "TorqueConverter._Cast_TorqueConverter",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "TorqueConverter._Cast_TorqueConverter",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "TorqueConverter._Cast_TorqueConverter") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "TorqueConverter._Cast_TorqueConverter",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def torque_converter(
            self: "TorqueConverter._Cast_TorqueConverter",
        ) -> "TorqueConverter":
            return self._parent

        def __getattr__(self: "TorqueConverter._Cast_TorqueConverter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_to_oil_heat_transfer_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClutchToOilHeatTransferCoefficient

        if temp is None:
            return 0.0

        return temp

    @clutch_to_oil_heat_transfer_coefficient.setter
    @enforce_parameter_types
    def clutch_to_oil_heat_transfer_coefficient(self: Self, value: "float"):
        self.wrapped.ClutchToOilHeatTransferCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def has_lock_up_clutch(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasLockUpClutch

        if temp is None:
            return False

        return temp

    @has_lock_up_clutch.setter
    @enforce_parameter_types
    def has_lock_up_clutch(self: Self, value: "bool"):
        self.wrapped.HasLockUpClutch = bool(value) if value is not None else False

    @property
    def heat_transfer_area(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HeatTransferArea

        if temp is None:
            return 0.0

        return temp

    @heat_transfer_area.setter
    @enforce_parameter_types
    def heat_transfer_area(self: Self, value: "float"):
        self.wrapped.HeatTransferArea = float(value) if value is not None else 0.0

    @property
    def specific_heat_capacity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecificHeatCapacity

        if temp is None:
            return 0.0

        return temp

    @specific_heat_capacity.setter
    @enforce_parameter_types
    def specific_heat_capacity(self: Self, value: "float"):
        self.wrapped.SpecificHeatCapacity = float(value) if value is not None else 0.0

    @property
    def static_to_dynamic_friction_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StaticToDynamicFrictionRatio

        if temp is None:
            return 0.0

        return temp

    @static_to_dynamic_friction_ratio.setter
    @enforce_parameter_types
    def static_to_dynamic_friction_ratio(self: Self, value: "float"):
        self.wrapped.StaticToDynamicFrictionRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def thermal_mass(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThermalMass

        if temp is None:
            return 0.0

        return temp

    @thermal_mass.setter
    @enforce_parameter_types
    def thermal_mass(self: Self, value: "float"):
        self.wrapped.ThermalMass = float(value) if value is not None else 0.0

    @property
    def tolerance_for_speed_ratio_of_unity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceForSpeedRatioOfUnity

        if temp is None:
            return 0.0

        return temp

    @tolerance_for_speed_ratio_of_unity.setter
    @enforce_parameter_types
    def tolerance_for_speed_ratio_of_unity(self: Self, value: "float"):
        self.wrapped.ToleranceForSpeedRatioOfUnity = (
            float(value) if value is not None else 0.0
        )

    @property
    def torque_capacity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @torque_capacity.setter
    @enforce_parameter_types
    def torque_capacity(self: Self, value: "float"):
        self.wrapped.TorqueCapacity = float(value) if value is not None else 0.0

    @property
    def pump(self: Self) -> "_2616.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Pump

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def turbine(self: Self) -> "_2618.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Turbine

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "TorqueConverter._Cast_TorqueConverter":
        return self._Cast_TorqueConverter(self)
