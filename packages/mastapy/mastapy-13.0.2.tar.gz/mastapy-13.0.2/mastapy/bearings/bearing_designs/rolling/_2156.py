"""CylindricalRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs.rolling import _2168
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "CylindricalRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1949
    from mastapy.bearings.bearing_designs.rolling import _2167, _2169, _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalRollerBearing",)


Self = TypeVar("Self", bound="CylindricalRollerBearing")


class CylindricalRollerBearing(_2168.NonBarrelRollerBearing):
    """CylindricalRollerBearing

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalRollerBearing")

    class _Cast_CylindricalRollerBearing:
        """Special nested class for casting CylindricalRollerBearing to subclasses."""

        def __init__(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
            parent: "CylindricalRollerBearing",
        ):
            self._parent = parent

        @property
        def non_barrel_roller_bearing(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "_2168.NonBarrelRollerBearing":
            return self._parent._cast(_2168.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def needle_roller_bearing(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "_2167.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.NeedleRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing",
        ) -> "CylindricalRollerBearing":
            return self._parent

        def __getattr__(
            self: "CylindricalRollerBearing._Cast_CylindricalRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_axial_load_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AllowableAxialLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @allowable_axial_load_factor.setter
    @enforce_parameter_types
    def allowable_axial_load_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AllowableAxialLoadFactor = value

    @property
    def capacity_lubrication_factor_for_permissible_axial_load_grease(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadGrease

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @capacity_lubrication_factor_for_permissible_axial_load_grease.setter
    @enforce_parameter_types
    def capacity_lubrication_factor_for_permissible_axial_load_grease(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadGrease = value

    @property
    def capacity_lubrication_factor_for_permissible_axial_load_oil(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadOil

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @capacity_lubrication_factor_for_permissible_axial_load_oil.setter
    @enforce_parameter_types
    def capacity_lubrication_factor_for_permissible_axial_load_oil(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadOil = value

    @property
    def diameter_exponent_factor_for_permissible_axial_load(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiameterExponentFactorForPermissibleAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter_exponent_factor_for_permissible_axial_load.setter
    @enforce_parameter_types
    def diameter_exponent_factor_for_permissible_axial_load(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiameterExponentFactorForPermissibleAxialLoad = value

    @property
    def diameter_scaling_factor_for_permissible_axial_load(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DiameterScalingFactorForPermissibleAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter_scaling_factor_for_permissible_axial_load.setter
    @enforce_parameter_types
    def diameter_scaling_factor_for_permissible_axial_load(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DiameterScalingFactorForPermissibleAxialLoad = value

    @property
    def permissible_axial_load_default_calculation_method(
        self: Self,
    ) -> "_1949.CylindricalRollerMaxAxialLoadMethod":
        """mastapy.bearings.bearing_results.CylindricalRollerMaxAxialLoadMethod"""
        temp = self.wrapped.PermissibleAxialLoadDefaultCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.CylindricalRollerMaxAxialLoadMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results._1949",
            "CylindricalRollerMaxAxialLoadMethod",
        )(value)

    @permissible_axial_load_default_calculation_method.setter
    @enforce_parameter_types
    def permissible_axial_load_default_calculation_method(
        self: Self, value: "_1949.CylindricalRollerMaxAxialLoadMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.BearingResults.CylindricalRollerMaxAxialLoadMethod",
        )
        self.wrapped.PermissibleAxialLoadDefaultCalculationMethod = value

    @property
    def permissible_axial_load_dimension_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PermissibleAxialLoadDimensionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @permissible_axial_load_dimension_factor.setter
    @enforce_parameter_types
    def permissible_axial_load_dimension_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PermissibleAxialLoadDimensionFactor = value

    @property
    def permissible_axial_load_internal_dimension_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PermissibleAxialLoadInternalDimensionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @permissible_axial_load_internal_dimension_factor.setter
    @enforce_parameter_types
    def permissible_axial_load_internal_dimension_factor(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PermissibleAxialLoadInternalDimensionFactor = value

    @property
    def radial_load_lubrication_factor_for_permissible_axial_load_grease(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadGrease

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_load_lubrication_factor_for_permissible_axial_load_grease.setter
    @enforce_parameter_types
    def radial_load_lubrication_factor_for_permissible_axial_load_grease(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadGrease = value

    @property
    def radial_load_lubrication_factor_for_permissible_axial_load_oil(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadOil

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radial_load_lubrication_factor_for_permissible_axial_load_oil.setter
    @enforce_parameter_types
    def radial_load_lubrication_factor_for_permissible_axial_load_oil(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadOil = value

    @property
    def reference_rotation_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReferenceRotationSpeed

        if temp is None:
            return 0.0

        return temp

    @reference_rotation_speed.setter
    @enforce_parameter_types
    def reference_rotation_speed(self: Self, value: "float"):
        self.wrapped.ReferenceRotationSpeed = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalRollerBearing._Cast_CylindricalRollerBearing":
        return self._Cast_CylindricalRollerBearing(self)
