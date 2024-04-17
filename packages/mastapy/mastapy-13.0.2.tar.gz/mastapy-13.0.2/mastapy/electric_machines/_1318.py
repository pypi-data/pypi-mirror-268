"""VShapedMagnetLayerSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_V_SHAPED_MAGNET_LAYER_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "VShapedMagnetLayerSpecification"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1284, _1276


__docformat__ = "restructuredtext en"
__all__ = ("VShapedMagnetLayerSpecification",)


Self = TypeVar("Self", bound="VShapedMagnetLayerSpecification")


class VShapedMagnetLayerSpecification(_1301.RotorInternalLayerSpecification):
    """VShapedMagnetLayerSpecification

    This is a mastapy class.
    """

    TYPE = _V_SHAPED_MAGNET_LAYER_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VShapedMagnetLayerSpecification")

    class _Cast_VShapedMagnetLayerSpecification:
        """Special nested class for casting VShapedMagnetLayerSpecification to subclasses."""

        def __init__(
            self: "VShapedMagnetLayerSpecification._Cast_VShapedMagnetLayerSpecification",
            parent: "VShapedMagnetLayerSpecification",
        ):
            self._parent = parent

        @property
        def rotor_internal_layer_specification(
            self: "VShapedMagnetLayerSpecification._Cast_VShapedMagnetLayerSpecification",
        ) -> "_1301.RotorInternalLayerSpecification":
            return self._parent._cast(_1301.RotorInternalLayerSpecification)

        @property
        def v_shaped_magnet_layer_specification(
            self: "VShapedMagnetLayerSpecification._Cast_VShapedMagnetLayerSpecification",
        ) -> "VShapedMagnetLayerSpecification":
            return self._parent

        def __getattr__(
            self: "VShapedMagnetLayerSpecification._Cast_VShapedMagnetLayerSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VShapedMagnetLayerSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cut_out_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CutOutWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cut_out_width.setter
    @enforce_parameter_types
    def cut_out_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CutOutWidth = value

    @property
    def distance_between_magnets(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DistanceBetweenMagnets

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @distance_between_magnets.setter
    @enforce_parameter_types
    def distance_between_magnets(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DistanceBetweenMagnets = value

    @property
    def distance_to_v_shape(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceToVShape

        if temp is None:
            return 0.0

        return temp

    @distance_to_v_shape.setter
    @enforce_parameter_types
    def distance_to_v_shape(self: Self, value: "float"):
        self.wrapped.DistanceToVShape = float(value) if value is not None else 0.0

    @property
    def flux_barrier_length(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FluxBarrierLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @flux_barrier_length.setter
    @enforce_parameter_types
    def flux_barrier_length(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FluxBarrierLength = value

    @property
    def has_flux_barriers(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasFluxBarriers

        if temp is None:
            return False

        return temp

    @has_flux_barriers.setter
    @enforce_parameter_types
    def has_flux_barriers(self: Self, value: "bool"):
        self.wrapped.HasFluxBarriers = bool(value) if value is not None else False

    @property
    def lower_round_height(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LowerRoundHeight

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @lower_round_height.setter
    @enforce_parameter_types
    def lower_round_height(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LowerRoundHeight = value

    @property
    def magnet_clearance(self: Self) -> "_1284.MagnetClearance":
        """mastapy.electric_machines.MagnetClearance"""
        temp = self.wrapped.MagnetClearance

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

    @magnet_clearance.setter
    @enforce_parameter_types
    def magnet_clearance(self: Self, value: "_1284.MagnetClearance"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.MagnetClearance"
        )
        self.wrapped.MagnetClearance = value

    @property
    def thickness_of_flux_barriers(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ThicknessOfFluxBarriers

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @thickness_of_flux_barriers.setter
    @enforce_parameter_types
    def thickness_of_flux_barriers(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ThicknessOfFluxBarriers = value

    @property
    def upper_flux_barrier_web_specification(self: Self) -> "_1276.FluxBarrierOrWeb":
        """mastapy.electric_machines.FluxBarrierOrWeb"""
        temp = self.wrapped.UpperFluxBarrierWebSpecification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.FluxBarrierOrWeb"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1276", "FluxBarrierOrWeb"
        )(value)

    @upper_flux_barrier_web_specification.setter
    @enforce_parameter_types
    def upper_flux_barrier_web_specification(
        self: Self, value: "_1276.FluxBarrierOrWeb"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.ElectricMachines.FluxBarrierOrWeb"
        )
        self.wrapped.UpperFluxBarrierWebSpecification = value

    @property
    def upper_round_height(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UpperRoundHeight

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @upper_round_height.setter
    @enforce_parameter_types
    def upper_round_height(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UpperRoundHeight = value

    @property
    def v_shaped_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VShapedAngle

        if temp is None:
            return 0.0

        return temp

    @v_shaped_angle.setter
    @enforce_parameter_types
    def v_shaped_angle(self: Self, value: "float"):
        self.wrapped.VShapedAngle = float(value) if value is not None else 0.0

    @property
    def web_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WebLength

        if temp is None:
            return 0.0

        return temp

    @web_length.setter
    @enforce_parameter_types
    def web_length(self: Self, value: "float"):
        self.wrapped.WebLength = float(value) if value is not None else 0.0

    @property
    def web_thickness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.WebThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @web_thickness.setter
    @enforce_parameter_types
    def web_thickness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.WebThickness = value

    @property
    def cast_to(
        self: Self,
    ) -> "VShapedMagnetLayerSpecification._Cast_VShapedMagnetLayerSpecification":
        return self._Cast_VShapedMagnetLayerSpecification(self)
