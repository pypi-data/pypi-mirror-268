"""UShapedLayerSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_U_SHAPED_LAYER_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "UShapedLayerSpecification"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1284, _1285, _1288


__docformat__ = "restructuredtext en"
__all__ = ("UShapedLayerSpecification",)


Self = TypeVar("Self", bound="UShapedLayerSpecification")


class UShapedLayerSpecification(_1301.RotorInternalLayerSpecification):
    """UShapedLayerSpecification

    This is a mastapy class.
    """

    TYPE = _U_SHAPED_LAYER_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UShapedLayerSpecification")

    class _Cast_UShapedLayerSpecification:
        """Special nested class for casting UShapedLayerSpecification to subclasses."""

        def __init__(
            self: "UShapedLayerSpecification._Cast_UShapedLayerSpecification",
            parent: "UShapedLayerSpecification",
        ):
            self._parent = parent

        @property
        def rotor_internal_layer_specification(
            self: "UShapedLayerSpecification._Cast_UShapedLayerSpecification",
        ) -> "_1301.RotorInternalLayerSpecification":
            return self._parent._cast(_1301.RotorInternalLayerSpecification)

        @property
        def u_shaped_layer_specification(
            self: "UShapedLayerSpecification._Cast_UShapedLayerSpecification",
        ) -> "UShapedLayerSpecification":
            return self._parent

        def __getattr__(
            self: "UShapedLayerSpecification._Cast_UShapedLayerSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UShapedLayerSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_inner_and_outer_sections(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AngleBetweenInnerAndOuterSections

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle_between_inner_and_outer_sections.setter
    @enforce_parameter_types
    def angle_between_inner_and_outer_sections(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AngleBetweenInnerAndOuterSections = value

    @property
    def bridge_offset_above_layer_bend(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BridgeOffsetAboveLayerBend

        if temp is None:
            return 0.0

        return temp

    @bridge_offset_above_layer_bend.setter
    @enforce_parameter_types
    def bridge_offset_above_layer_bend(self: Self, value: "float"):
        self.wrapped.BridgeOffsetAboveLayerBend = (
            float(value) if value is not None else 0.0
        )

    @property
    def bridge_offset_below_layer_bend(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BridgeOffsetBelowLayerBend

        if temp is None:
            return 0.0

        return temp

    @bridge_offset_below_layer_bend.setter
    @enforce_parameter_types
    def bridge_offset_below_layer_bend(self: Self, value: "float"):
        self.wrapped.BridgeOffsetBelowLayerBend = (
            float(value) if value is not None else 0.0
        )

    @property
    def bridge_thickness_above_layer_bend(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BridgeThicknessAboveLayerBend

        if temp is None:
            return 0.0

        return temp

    @bridge_thickness_above_layer_bend.setter
    @enforce_parameter_types
    def bridge_thickness_above_layer_bend(self: Self, value: "float"):
        self.wrapped.BridgeThicknessAboveLayerBend = (
            float(value) if value is not None else 0.0
        )

    @property
    def bridge_thickness_below_layer_bend(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BridgeThicknessBelowLayerBend

        if temp is None:
            return 0.0

        return temp

    @bridge_thickness_below_layer_bend.setter
    @enforce_parameter_types
    def bridge_thickness_below_layer_bend(self: Self, value: "float"):
        self.wrapped.BridgeThicknessBelowLayerBend = (
            float(value) if value is not None else 0.0
        )

    @property
    def distance_between_inner_magnets(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DistanceBetweenInnerMagnets

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @distance_between_inner_magnets.setter
    @enforce_parameter_types
    def distance_between_inner_magnets(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DistanceBetweenInnerMagnets = value

    @property
    def distance_between_outer_magnets_and_bridge(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DistanceBetweenOuterMagnetsAndBridge

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @distance_between_outer_magnets_and_bridge.setter
    @enforce_parameter_types
    def distance_between_outer_magnets_and_bridge(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DistanceBetweenOuterMagnetsAndBridge = value

    @property
    def distance_to_layer(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceToLayer

        if temp is None:
            return 0.0

        return temp

    @distance_to_layer.setter
    @enforce_parameter_types
    def distance_to_layer(self: Self, value: "float"):
        self.wrapped.DistanceToLayer = float(value) if value is not None else 0.0

    @property
    def inner_magnet_clearance(self: Self) -> "_1284.MagnetClearance":
        """mastapy.electric_machines.MagnetClearance"""
        temp = self.wrapped.InnerMagnetClearance

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.MagnetClearance"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1284", "MagnetClearance"
        )(value)

    @inner_magnet_clearance.setter
    @enforce_parameter_types
    def inner_magnet_clearance(self: Self, value: "_1284.MagnetClearance"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.MagnetClearance"
        )
        self.wrapped.InnerMagnetClearance = value

    @property
    def magnet_configuration(self: Self) -> "_1285.MagnetConfiguration":
        """mastapy.electric_machines.MagnetConfiguration"""
        temp = self.wrapped.MagnetConfiguration

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.MagnetConfiguration"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1285", "MagnetConfiguration"
        )(value)

    @magnet_configuration.setter
    @enforce_parameter_types
    def magnet_configuration(self: Self, value: "_1285.MagnetConfiguration"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.MagnetConfiguration"
        )
        self.wrapped.MagnetConfiguration = value

    @property
    def outer_magnet_lower_clearance(self: Self) -> "_1284.MagnetClearance":
        """mastapy.electric_machines.MagnetClearance"""
        temp = self.wrapped.OuterMagnetLowerClearance

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.MagnetClearance"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1284", "MagnetClearance"
        )(value)

    @outer_magnet_lower_clearance.setter
    @enforce_parameter_types
    def outer_magnet_lower_clearance(self: Self, value: "_1284.MagnetClearance"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.MagnetClearance"
        )
        self.wrapped.OuterMagnetLowerClearance = value

    @property
    def thickness_of_inner_flux_barriers(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ThicknessOfInnerFluxBarriers

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @thickness_of_inner_flux_barriers.setter
    @enforce_parameter_types
    def thickness_of_inner_flux_barriers(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ThicknessOfInnerFluxBarriers = value

    @property
    def thickness_of_outer_flux_barriers(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ThicknessOfOuterFluxBarriers

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @thickness_of_outer_flux_barriers.setter
    @enforce_parameter_types
    def thickness_of_outer_flux_barriers(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ThicknessOfOuterFluxBarriers = value

    @property
    def web_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WebThickness

        if temp is None:
            return 0.0

        return temp

    @web_thickness.setter
    @enforce_parameter_types
    def web_thickness(self: Self, value: "float"):
        self.wrapped.WebThickness = float(value) if value is not None else 0.0

    @property
    def outer_magnets(self: Self) -> "_1288.MagnetForLayer":
        """mastapy.electric_machines.MagnetForLayer

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterMagnets

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "UShapedLayerSpecification._Cast_UShapedLayerSpecification":
        return self._Cast_UShapedLayerSpecification(self)
