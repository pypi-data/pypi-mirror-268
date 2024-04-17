"""Clutch"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.couplings import _2591
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch")

if TYPE_CHECKING:
    from mastapy.math_utility.measured_data import _1572
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.math_utility import _1542
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5410
    from mastapy.system_model.connections_and_sockets.couplings import _2349
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("Clutch",)


Self = TypeVar("Self", bound="Clutch")


class Clutch(_2591.Coupling):
    """Clutch

    This is a mastapy class.
    """

    TYPE = _CLUTCH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Clutch")

    class _Cast_Clutch:
        """Special nested class for casting Clutch to subclasses."""

        def __init__(self: "Clutch._Cast_Clutch", parent: "Clutch"):
            self._parent = parent

        @property
        def coupling(self: "Clutch._Cast_Clutch") -> "_2591.Coupling":
            return self._parent._cast(_2591.Coupling)

        @property
        def specialised_assembly(
            self: "Clutch._Cast_Clutch",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "Clutch._Cast_Clutch") -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "Clutch._Cast_Clutch") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "Clutch._Cast_Clutch") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def clutch(self: "Clutch._Cast_Clutch") -> "Clutch":
            return self._parent

        def __getattr__(self: "Clutch._Cast_Clutch", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Clutch.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_speed_temperature_grid(self: Self) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.AngularSpeedTemperatureGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @angular_speed_temperature_grid.setter
    @enforce_parameter_types
    def angular_speed_temperature_grid(
        self: Self, value: "_1572.GriddedSurfaceAccessor"
    ):
        self.wrapped.AngularSpeedTemperatureGrid = value.wrapped

    @property
    def area_of_friction_surface(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaOfFrictionSurface

        if temp is None:
            return 0.0

        return temp

    @property
    def bore(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @property
    def clearance_between_friction_surfaces(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ClearanceBetweenFrictionSurfaces

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @clearance_between_friction_surfaces.setter
    @enforce_parameter_types
    def clearance_between_friction_surfaces(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ClearanceBetweenFrictionSurfaces = value

    @property
    def clutch_plate_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClutchPlateTemperature

        if temp is None:
            return 0.0

        return temp

    @clutch_plate_temperature.setter
    @enforce_parameter_types
    def clutch_plate_temperature(self: Self, value: "float"):
        self.wrapped.ClutchPlateTemperature = float(value) if value is not None else 0.0

    @property
    def clutch_specific_heat_capacity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClutchSpecificHeatCapacity

        if temp is None:
            return 0.0

        return temp

    @clutch_specific_heat_capacity.setter
    @enforce_parameter_types
    def clutch_specific_heat_capacity(self: Self, value: "float"):
        self.wrapped.ClutchSpecificHeatCapacity = (
            float(value) if value is not None else 0.0
        )

    @property
    def clutch_thermal_mass(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClutchThermalMass

        if temp is None:
            return 0.0

        return temp

    @clutch_thermal_mass.setter
    @enforce_parameter_types
    def clutch_thermal_mass(self: Self, value: "float"):
        self.wrapped.ClutchThermalMass = float(value) if value is not None else 0.0

    @property
    def clutch_type(self: Self) -> "_2587.ClutchType":
        """mastapy.system_model.part_model.couplings.ClutchType"""
        temp = self.wrapped.ClutchType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.Couplings.ClutchType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.couplings._2587", "ClutchType"
        )(value)

    @clutch_type.setter
    @enforce_parameter_types
    def clutch_type(self: Self, value: "_2587.ClutchType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.Couplings.ClutchType"
        )
        self.wrapped.ClutchType = value

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
    def diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_coefficient_of_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DynamicCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @dynamic_coefficient_of_friction.setter
    @enforce_parameter_types
    def dynamic_coefficient_of_friction(self: Self, value: "float"):
        self.wrapped.DynamicCoefficientOfFriction = (
            float(value) if value is not None else 0.0
        )

    @property
    def flow_rate_vs_speed(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.FlowRateVsSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @flow_rate_vs_speed.setter
    @enforce_parameter_types
    def flow_rate_vs_speed(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.FlowRateVsSpeed = value.wrapped

    @property
    def inner_diameter_of_friction_surface(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerDiameterOfFrictionSurface

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_friction_surface.setter
    @enforce_parameter_types
    def inner_diameter_of_friction_surface(self: Self, value: "float"):
        self.wrapped.InnerDiameterOfFrictionSurface = (
            float(value) if value is not None else 0.0
        )

    @property
    def kiss_point_clutch_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KissPointClutchPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def kiss_point_piston_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KissPointPistonPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def kiss_point_pressure_percent(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KissPointPressurePercent

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_speed_temperature_grid(self: Self) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.LinearSpeedTemperatureGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @linear_speed_temperature_grid.setter
    @enforce_parameter_types
    def linear_speed_temperature_grid(
        self: Self, value: "_1572.GriddedSurfaceAccessor"
    ):
        self.wrapped.LinearSpeedTemperatureGrid = value.wrapped

    @property
    def maximum_pressure_at_clutch(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumPressureAtClutch

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_pressure_at_clutch.setter
    @enforce_parameter_types
    def maximum_pressure_at_clutch(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumPressureAtClutch = value

    @property
    def maximum_pressure_at_piston(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumPressureAtPiston

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_pressure_at_piston.setter
    @enforce_parameter_types
    def maximum_pressure_at_piston(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumPressureAtPiston = value

    @property
    def number_of_friction_surfaces(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfFrictionSurfaces

        if temp is None:
            return 0

        return temp

    @number_of_friction_surfaces.setter
    @enforce_parameter_types
    def number_of_friction_surfaces(self: Self, value: "int"):
        self.wrapped.NumberOfFrictionSurfaces = int(value) if value is not None else 0

    @property
    def outer_diameter_of_friction_surface(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameterOfFrictionSurface

        if temp is None:
            return 0.0

        return temp

    @outer_diameter_of_friction_surface.setter
    @enforce_parameter_types
    def outer_diameter_of_friction_surface(self: Self, value: "float"):
        self.wrapped.OuterDiameterOfFrictionSurface = (
            float(value) if value is not None else 0.0
        )

    @property
    def piston_area(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PistonArea

        if temp is None:
            return 0.0

        return temp

    @piston_area.setter
    @enforce_parameter_types
    def piston_area(self: Self, value: "float"):
        self.wrapped.PistonArea = float(value) if value is not None else 0.0

    @property
    def specified_torque_capacity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedTorqueCapacity

        if temp is None:
            return 0.0

        return temp

    @specified_torque_capacity.setter
    @enforce_parameter_types
    def specified_torque_capacity(self: Self, value: "float"):
        self.wrapped.SpecifiedTorqueCapacity = (
            float(value) if value is not None else 0.0
        )

    @property
    def spring_preload(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpringPreload

        if temp is None:
            return 0.0

        return temp

    @spring_preload.setter
    @enforce_parameter_types
    def spring_preload(self: Self, value: "float"):
        self.wrapped.SpringPreload = float(value) if value is not None else 0.0

    @property
    def spring_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpringStiffness

        if temp is None:
            return 0.0

        return temp

    @spring_stiffness.setter
    @enforce_parameter_types
    def spring_stiffness(self: Self, value: "float"):
        self.wrapped.SpringStiffness = float(value) if value is not None else 0.0

    @property
    def spring_type(self: Self) -> "_5410.ClutchSpringType":
        """mastapy.system_model.analyses_and_results.mbd_analyses.ClutchSpringType"""
        temp = self.wrapped.SpringType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.ClutchSpringType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5410",
            "ClutchSpringType",
        )(value)

    @spring_type.setter
    @enforce_parameter_types
    def spring_type(self: Self, value: "_5410.ClutchSpringType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.ClutchSpringType",
        )
        self.wrapped.SpringType = value

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
    def use_friction_coefficient_lookup(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseFrictionCoefficientLookup

        if temp is None:
            return False

        return temp

    @use_friction_coefficient_lookup.setter
    @enforce_parameter_types
    def use_friction_coefficient_lookup(self: Self, value: "bool"):
        self.wrapped.UseFrictionCoefficientLookup = (
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
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def clutch_connection(self: Self) -> "_2349.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClutchConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Clutch._Cast_Clutch":
        return self._Cast_Clutch(self)
