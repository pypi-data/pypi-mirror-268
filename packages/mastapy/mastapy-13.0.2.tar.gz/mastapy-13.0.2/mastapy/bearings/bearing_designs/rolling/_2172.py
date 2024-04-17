"""RollingBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import (
    constructor,
    enum_with_selected_value_runtime,
    overridable_enum_runtime,
    conversion,
)
from mastapy.bearings import _1899, _1877, _1878, _1902
from mastapy.bearings.bearing_designs.rolling import _2158, _2159, _2165, _2182
from mastapy._internal.python_net import python_net_import
from mastapy.bearings.bearing_designs import _2138
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ROLLING_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "RollingBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import (
        _2154,
        _2175,
        _2153,
        _2162,
        _2150,
        _2174,
        _2142,
        _2143,
        _2144,
        _2145,
        _2146,
        _2147,
        _2149,
        _2155,
        _2156,
        _2157,
        _2161,
        _2166,
        _2167,
        _2168,
        _2169,
        _2173,
        _2176,
        _2177,
        _2178,
        _2179,
        _2180,
        _2181,
    )
    from mastapy.bearings import _1879, _1876
    from mastapy.materials import _248
    from mastapy.utility import _1589
    from mastapy.bearings.bearing_results.rolling import _1984
    from mastapy.bearings.bearing_designs import _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearing",)


Self = TypeVar("Self", bound="RollingBearing")


class RollingBearing(_2138.DetailedBearing):
    """RollingBearing

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingBearing")

    class _Cast_RollingBearing:
        """Special nested class for casting RollingBearing to subclasses."""

        def __init__(
            self: "RollingBearing._Cast_RollingBearing", parent: "RollingBearing"
        ):
            self._parent = parent

        @property
        def detailed_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2138.DetailedBearing":
            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def angular_contact_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2142.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2142

            return self._parent._cast(_2142.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2143.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2143

            return self._parent._cast(_2143.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2144.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2144

            return self._parent._cast(_2144.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2145.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2145

            return self._parent._cast(_2145.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2146.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2146

            return self._parent._cast(_2146.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2147.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2147

            return self._parent._cast(_2147.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2149.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2149

            return self._parent._cast(_2149.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2155.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2155

            return self._parent._cast(_2155.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2156.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2157.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2161.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2161

            return self._parent._cast(_2161.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2166.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2166

            return self._parent._cast(_2166.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2167.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2168.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def self_aligning_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2173.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2173

            return self._parent._cast(_2173.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2176.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2176

            return self._parent._cast(_2176.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2177.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2177

            return self._parent._cast(_2177.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2178.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2178

            return self._parent._cast(_2178.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2179.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2179

            return self._parent._cast(_2179.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2180.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2180

            return self._parent._cast(_2180.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "_2181.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2181

            return self._parent._cast(_2181.ToroidalRollerBearing)

        @property
        def rolling_bearing(
            self: "RollingBearing._Cast_RollingBearing",
        ) -> "RollingBearing":
            return self._parent

        def __getattr__(self: "RollingBearing._Cast_RollingBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def are_the_inner_rings_a_single_piece_of_metal(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.AreTheInnerRingsASinglePieceOfMetal

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @are_the_inner_rings_a_single_piece_of_metal.setter
    @enforce_parameter_types
    def are_the_inner_rings_a_single_piece_of_metal(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.AreTheInnerRingsASinglePieceOfMetal = value

    @property
    def are_the_outer_rings_a_single_piece_of_metal(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.AreTheOuterRingsASinglePieceOfMetal

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @are_the_outer_rings_a_single_piece_of_metal.setter
    @enforce_parameter_types
    def are_the_outer_rings_a_single_piece_of_metal(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.AreTheOuterRingsASinglePieceOfMetal = value

    @property
    def arrangement(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement":
        """EnumWithSelectedValue[mastapy.bearings.RollingBearingArrangement]"""
        temp = self.wrapped.Arrangement

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @arrangement.setter
    @enforce_parameter_types
    def arrangement(self: Self, value: "_1899.RollingBearingArrangement"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RollingBearingArrangement.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Arrangement = value

    @property
    def basic_dynamic_load_rating(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BasicDynamicLoadRating

        if temp is None:
            return 0.0

        return temp

    @basic_dynamic_load_rating.setter
    @enforce_parameter_types
    def basic_dynamic_load_rating(self: Self, value: "float"):
        self.wrapped.BasicDynamicLoadRating = float(value) if value is not None else 0.0

    @property
    def basic_dynamic_load_rating_calculation(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod":
        """EnumWithSelectedValue[mastapy.bearings.BasicDynamicLoadRatingCalculationMethod]"""
        temp = self.wrapped.BasicDynamicLoadRatingCalculation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @basic_dynamic_load_rating_calculation.setter
    @enforce_parameter_types
    def basic_dynamic_load_rating_calculation(
        self: Self, value: "_1877.BasicDynamicLoadRatingCalculationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BasicDynamicLoadRatingCalculation = value

    @property
    def basic_dynamic_load_rating_divided_by_correction_factors(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicDynamicLoadRatingDividedByCorrectionFactors

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_dynamic_load_rating_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicDynamicLoadRatingSource

        if temp is None:
            return ""

        return temp

    @property
    def basic_static_load_rating(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BasicStaticLoadRating

        if temp is None:
            return 0.0

        return temp

    @basic_static_load_rating.setter
    @enforce_parameter_types
    def basic_static_load_rating(self: Self, value: "float"):
        self.wrapped.BasicStaticLoadRating = float(value) if value is not None else 0.0

    @property
    def basic_static_load_rating_calculation(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod":
        """EnumWithSelectedValue[mastapy.bearings.BasicStaticLoadRatingCalculationMethod]"""
        temp = self.wrapped.BasicStaticLoadRatingCalculation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @basic_static_load_rating_calculation.setter
    @enforce_parameter_types
    def basic_static_load_rating_calculation(
        self: Self, value: "_1878.BasicStaticLoadRatingCalculationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BasicStaticLoadRatingCalculation = value

    @property
    def basic_static_load_rating_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicStaticLoadRatingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_static_load_rating_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicStaticLoadRatingSource

        if temp is None:
            return ""

        return temp

    @property
    def cage_bridge_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageBridgeAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_bridge_angle.setter
    @enforce_parameter_types
    def cage_bridge_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageBridgeAngle = value

    @property
    def cage_bridge_axial_surface_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageBridgeAxialSurfaceRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_bridge_axial_surface_radius.setter
    @enforce_parameter_types
    def cage_bridge_axial_surface_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageBridgeAxialSurfaceRadius = value

    @property
    def cage_bridge_radial_surface_radius(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageBridgeRadialSurfaceRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_bridge_radial_surface_radius.setter
    @enforce_parameter_types
    def cage_bridge_radial_surface_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageBridgeRadialSurfaceRadius = value

    @property
    def cage_bridge_shape(self: Self) -> "_2154.CageBridgeShape":
        """mastapy.bearings.bearing_designs.rolling.CageBridgeShape"""
        temp = self.wrapped.CageBridgeShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.CageBridgeShape"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.rolling._2154", "CageBridgeShape"
        )(value)

    @cage_bridge_shape.setter
    @enforce_parameter_types
    def cage_bridge_shape(self: Self, value: "_2154.CageBridgeShape"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.CageBridgeShape"
        )
        self.wrapped.CageBridgeShape = value

    @property
    def cage_bridge_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CageBridgeWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def cage_guiding_ring_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageGuidingRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_guiding_ring_width.setter
    @enforce_parameter_types
    def cage_guiding_ring_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageGuidingRingWidth = value

    @property
    def cage_mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageMass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_mass.setter
    @enforce_parameter_types
    def cage_mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageMass = value

    @property
    def cage_material(self: Self) -> "_1879.BearingCageMaterial":
        """mastapy.bearings.BearingCageMaterial"""
        temp = self.wrapped.CageMaterial

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingCageMaterial"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1879", "BearingCageMaterial"
        )(value)

    @cage_material.setter
    @enforce_parameter_types
    def cage_material(self: Self, value: "_1879.BearingCageMaterial"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingCageMaterial"
        )
        self.wrapped.CageMaterial = value

    @property
    def cage_pitch_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CagePitchRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_pitch_radius.setter
    @enforce_parameter_types
    def cage_pitch_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CagePitchRadius = value

    @property
    def cage_pocket_clearance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CagePocketClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_pocket_clearance.setter
    @enforce_parameter_types
    def cage_pocket_clearance(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CagePocketClearance = value

    @property
    def cage_thickness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_thickness.setter
    @enforce_parameter_types
    def cage_thickness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageThickness = value

    @property
    def cage_to_inner_ring_clearance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageToInnerRingClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_to_inner_ring_clearance.setter
    @enforce_parameter_types
    def cage_to_inner_ring_clearance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageToInnerRingClearance = value

    @property
    def cage_to_outer_ring_clearance(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageToOuterRingClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_to_outer_ring_clearance.setter
    @enforce_parameter_types
    def cage_to_outer_ring_clearance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageToOuterRingClearance = value

    @property
    def cage_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CageWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cage_width.setter
    @enforce_parameter_types
    def cage_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CageWidth = value

    @property
    def catalogue(self: Self) -> "_1876.BearingCatalog":
        """mastapy.bearings.BearingCatalog

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Catalogue

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bearings.BearingCatalog")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.bearings._1876", "BearingCatalog")(
            value
        )

    @property
    def combined_surface_roughness_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedSurfaceRoughnessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_surface_roughness_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedSurfaceRoughnessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ContactAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @contact_angle.setter
    @enforce_parameter_types
    def contact_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ContactAngle = value

    @property
    def contact_radius_in_rolling_direction_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRadiusInRollingDirectionInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_radius_in_rolling_direction_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRadiusInRollingDirectionOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def designation(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Designation

        if temp is None:
            return ""

        return temp

    @designation.setter
    @enforce_parameter_types
    def designation(self: Self, value: "str"):
        self.wrapped.Designation = str(value) if value is not None else ""

    @property
    def diameter_series(self: Self) -> "overridable.Overridable_DiameterSeries":
        """Overridable[mastapy.bearings.bearing_designs.rolling.DiameterSeries]"""
        temp = self.wrapped.DiameterSeries

        if temp is None:
            return None

        value = overridable.Overridable_DiameterSeries.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @diameter_series.setter
    @enforce_parameter_types
    def diameter_series(
        self: Self,
        value: "Union[_2158.DiameterSeries, Tuple[_2158.DiameterSeries, bool]]",
    ):
        wrapper_type = overridable.Overridable_DiameterSeries.wrapper_type()
        enclosed_type = overridable.Overridable_DiameterSeries.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.DiameterSeries = value

    @property
    def distance_between_element_centres(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DistanceBetweenElementCentres

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @distance_between_element_centres.setter
    @enforce_parameter_types
    def distance_between_element_centres(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DistanceBetweenElementCentres = value

    @property
    def dynamic_axial_load_factor_for_high_axial_radial_load_ratios(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicAxialLoadFactorForHighAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_axial_load_factor_for_high_axial_radial_load_ratios.setter
    @enforce_parameter_types
    def dynamic_axial_load_factor_for_high_axial_radial_load_ratios(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicAxialLoadFactorForHighAxialRadialLoadRatios = value

    @property
    def dynamic_axial_load_factor_for_low_axial_radial_load_ratios(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicAxialLoadFactorForLowAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_axial_load_factor_for_low_axial_radial_load_ratios.setter
    @enforce_parameter_types
    def dynamic_axial_load_factor_for_low_axial_radial_load_ratios(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicAxialLoadFactorForLowAxialRadialLoadRatios = value

    @property
    def dynamic_equivalent_load_factors_can_be_specified(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoadFactorsCanBeSpecified

        if temp is None:
            return False

        return temp

    @property
    def dynamic_radial_load_factor_for_high_axial_radial_load_ratios(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicRadialLoadFactorForHighAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_radial_load_factor_for_high_axial_radial_load_ratios.setter
    @enforce_parameter_types
    def dynamic_radial_load_factor_for_high_axial_radial_load_ratios(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicRadialLoadFactorForHighAxialRadialLoadRatios = value

    @property
    def dynamic_radial_load_factor_for_low_axial_radial_load_ratios(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DynamicRadialLoadFactorForLowAxialRadialLoadRatios

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @dynamic_radial_load_factor_for_low_axial_radial_load_ratios.setter
    @enforce_parameter_types
    def dynamic_radial_load_factor_for_low_axial_radial_load_ratios(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DynamicRadialLoadFactorForLowAxialRadialLoadRatios = value

    @property
    def element_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_diameter.setter
    @enforce_parameter_types
    def element_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementDiameter = value

    @property
    def element_material_reportable(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ElementMaterialReportable.SelectedItemName

        if temp is None:
            return ""

        return temp

    @element_material_reportable.setter
    @enforce_parameter_types
    def element_material_reportable(self: Self, value: "str"):
        self.wrapped.ElementMaterialReportable.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def element_offset(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_offset.setter
    @enforce_parameter_types
    def element_offset(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementOffset = value

    @property
    def element_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def element_surface_roughness_rms(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementSurfaceRoughnessRMS

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_surface_roughness_rms.setter
    @enforce_parameter_types
    def element_surface_roughness_rms(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementSurfaceRoughnessRMS = value

    @property
    def element_surface_roughness_ra(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementSurfaceRoughnessRa

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_surface_roughness_ra.setter
    @enforce_parameter_types
    def element_surface_roughness_ra(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementSurfaceRoughnessRa = value

    @property
    def extra_information(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExtraInformation

        if temp is None:
            return ""

        return temp

    @property
    def factor_for_basic_dynamic_load_rating_in_ansiabma(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FactorForBasicDynamicLoadRatingInANSIABMA

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_load_limit(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FatigueLoadLimit

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @fatigue_load_limit.setter
    @enforce_parameter_types
    def fatigue_load_limit(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FatigueLoadLimit = value

    @property
    def fatigue_load_limit_calculation_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum":
        """EnumWithSelectedValue[mastapy.bearings.bearing_designs.rolling.FatigueLoadLimitCalculationMethodEnum]"""
        temp = self.wrapped.FatigueLoadLimitCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @fatigue_load_limit_calculation_method.setter
    @enforce_parameter_types
    def fatigue_load_limit_calculation_method(
        self: Self, value: "_2159.FatigueLoadLimitCalculationMethodEnum"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FatigueLoadLimitCalculationMethod = value

    @property
    def free_space_between_elements(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FreeSpaceBetweenElements

        if temp is None:
            return 0.0

        return temp

    @property
    def height_series(self: Self) -> "overridable.Overridable_HeightSeries":
        """Overridable[mastapy.bearings.bearing_designs.rolling.HeightSeries]"""
        temp = self.wrapped.HeightSeries

        if temp is None:
            return None

        value = overridable.Overridable_HeightSeries.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @height_series.setter
    @enforce_parameter_types
    def height_series(
        self: Self, value: "Union[_2165.HeightSeries, Tuple[_2165.HeightSeries, bool]]"
    ):
        wrapper_type = overridable.Overridable_HeightSeries.wrapper_type()
        enclosed_type = overridable.Overridable_HeightSeries.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.HeightSeries = value

    @property
    def iso_material_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ISOMaterialFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @iso_material_factor.setter
    @enforce_parameter_types
    def iso_material_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ISOMaterialFactor = value

    @property
    def inner_race_hardness_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerRaceHardnessDepth

        if temp is None:
            return 0.0

        return temp

    @inner_race_hardness_depth.setter
    @enforce_parameter_types
    def inner_race_hardness_depth(self: Self, value: "float"):
        self.wrapped.InnerRaceHardnessDepth = float(value) if value is not None else 0.0

    @property
    def inner_race_material_reportable(self: Self) -> "str":
        """str"""
        temp = self.wrapped.InnerRaceMaterialReportable.SelectedItemName

        if temp is None:
            return ""

        return temp

    @inner_race_material_reportable.setter
    @enforce_parameter_types
    def inner_race_material_reportable(self: Self, value: "str"):
        self.wrapped.InnerRaceMaterialReportable.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def inner_race_outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRaceOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_race_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType":
        """EnumWithSelectedValue[mastapy.bearings.RollingBearingRaceType]"""
        temp = self.wrapped.InnerRaceType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @inner_race_type.setter
    @enforce_parameter_types
    def inner_race_type(self: Self, value: "_1902.RollingBearingRaceType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.InnerRaceType = value

    @property
    def inner_ring_left_corner_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingLeftCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_left_corner_radius.setter
    @enforce_parameter_types
    def inner_ring_left_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingLeftCornerRadius = value

    @property
    def inner_ring_right_corner_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingRightCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_right_corner_radius.setter
    @enforce_parameter_types
    def inner_ring_right_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingRightCornerRadius = value

    @property
    def inner_ring_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_width.setter
    @enforce_parameter_types
    def inner_ring_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingWidth = value

    @property
    def is_full_complement(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.IsFullComplement

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @is_full_complement.setter
    @enforce_parameter_types
    def is_full_complement(self: Self, value: "Union[bool, Tuple[bool, bool]]"):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.IsFullComplement = value

    @property
    def kz(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.KZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @kz.setter
    @enforce_parameter_types
    def kz(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.KZ = value

    @property
    def limiting_value_for_axial_load_ratio(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LimitingValueForAxialLoadRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @limiting_value_for_axial_load_ratio.setter
    @enforce_parameter_types
    def limiting_value_for_axial_load_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LimitingValueForAxialLoadRatio = value

    @property
    def manufacturer(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Manufacturer

        if temp is None:
            return ""

        return temp

    @manufacturer.setter
    @enforce_parameter_types
    def manufacturer(self: Self, value: "str"):
        self.wrapped.Manufacturer = str(value) if value is not None else ""

    @property
    def maximum_grease_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumGreaseSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_grease_speed.setter
    @enforce_parameter_types
    def maximum_grease_speed(self: Self, value: "float"):
        self.wrapped.MaximumGreaseSpeed = float(value) if value is not None else 0.0

    @property
    def maximum_oil_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumOilSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_oil_speed.setter
    @enforce_parameter_types
    def maximum_oil_speed(self: Self, value: "float"):
        self.wrapped.MaximumOilSpeed = float(value) if value is not None else 0.0

    @property
    def maximum_permissible_contact_stress_for_static_failure_inner(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumPermissibleContactStressForStaticFailureInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_permissible_contact_stress_for_static_failure_inner.setter
    @enforce_parameter_types
    def maximum_permissible_contact_stress_for_static_failure_inner(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumPermissibleContactStressForStaticFailureInner = value

    @property
    def maximum_permissible_contact_stress_for_static_failure_outer(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumPermissibleContactStressForStaticFailureOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_permissible_contact_stress_for_static_failure_outer.setter
    @enforce_parameter_types
    def maximum_permissible_contact_stress_for_static_failure_outer(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumPermissibleContactStressForStaticFailureOuter = value

    @property
    def minimum_surface_roughness_rms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSurfaceRoughnessRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_surface_roughness_ra(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSurfaceRoughnessRa

        if temp is None:
            return 0.0

        return temp

    @property
    def no_history(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NoHistory

        if temp is None:
            return ""

        return temp

    @property
    def number_of_elements(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_elements.setter
    @enforce_parameter_types
    def number_of_elements(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfElements = value

    @property
    def number_of_rows(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRows

        if temp is None:
            return 0

        return temp

    @number_of_rows.setter
    @enforce_parameter_types
    def number_of_rows(self: Self, value: "int"):
        self.wrapped.NumberOfRows = int(value) if value is not None else 0

    @property
    def outer_race_hardness_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterRaceHardnessDepth

        if temp is None:
            return 0.0

        return temp

    @outer_race_hardness_depth.setter
    @enforce_parameter_types
    def outer_race_hardness_depth(self: Self, value: "float"):
        self.wrapped.OuterRaceHardnessDepth = float(value) if value is not None else 0.0

    @property
    def outer_race_inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRaceInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_race_material_reportable(self: Self) -> "str":
        """str"""
        temp = self.wrapped.OuterRaceMaterialReportable.SelectedItemName

        if temp is None:
            return ""

        return temp

    @outer_race_material_reportable.setter
    @enforce_parameter_types
    def outer_race_material_reportable(self: Self, value: "str"):
        self.wrapped.OuterRaceMaterialReportable.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def outer_race_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType":
        """EnumWithSelectedValue[mastapy.bearings.RollingBearingRaceType]"""
        temp = self.wrapped.OuterRaceType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @outer_race_type.setter
    @enforce_parameter_types
    def outer_race_type(self: Self, value: "_1902.RollingBearingRaceType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RollingBearingRaceType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.OuterRaceType = value

    @property
    def outer_ring_left_corner_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingLeftCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_left_corner_radius.setter
    @enforce_parameter_types
    def outer_ring_left_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingLeftCornerRadius = value

    @property
    def outer_ring_offset(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_offset.setter
    @enforce_parameter_types
    def outer_ring_offset(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingOffset = value

    @property
    def outer_ring_right_corner_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingRightCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_right_corner_radius.setter
    @enforce_parameter_types
    def outer_ring_right_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingRightCornerRadius = value

    @property
    def outer_ring_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_width.setter
    @enforce_parameter_types
    def outer_ring_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingWidth = value

    @property
    def pitch_circle_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PitchCircleDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @pitch_circle_diameter.setter
    @enforce_parameter_types
    def pitch_circle_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PitchCircleDiameter = value

    @property
    def power_for_maximum_contact_stress_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerForMaximumContactStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def raceway_surface_roughness_rms_inner(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RacewaySurfaceRoughnessRMSInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @raceway_surface_roughness_rms_inner.setter
    @enforce_parameter_types
    def raceway_surface_roughness_rms_inner(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RacewaySurfaceRoughnessRMSInner = value

    @property
    def raceway_surface_roughness_rms_outer(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RacewaySurfaceRoughnessRMSOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @raceway_surface_roughness_rms_outer.setter
    @enforce_parameter_types
    def raceway_surface_roughness_rms_outer(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RacewaySurfaceRoughnessRMSOuter = value

    @property
    def raceway_surface_roughness_ra_inner(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RacewaySurfaceRoughnessRaInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @raceway_surface_roughness_ra_inner.setter
    @enforce_parameter_types
    def raceway_surface_roughness_ra_inner(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RacewaySurfaceRoughnessRaInner = value

    @property
    def raceway_surface_roughness_ra_outer(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RacewaySurfaceRoughnessRaOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @raceway_surface_roughness_ra_outer.setter
    @enforce_parameter_types
    def raceway_surface_roughness_ra_outer(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RacewaySurfaceRoughnessRaOuter = value

    @property
    def sleeve_type(self: Self) -> "_2175.SleeveType":
        """mastapy.bearings.bearing_designs.rolling.SleeveType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SleeveType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.SleeveType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.rolling._2175", "SleeveType"
        )(value)

    @property
    def theoretical_maximum_number_of_elements(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TheoreticalMaximumNumberOfElements

        if temp is None:
            return 0.0

        return temp

    @property
    def total_free_space_between_elements(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalFreeSpaceBetweenElements

        if temp is None:
            return 0.0

        return temp

    @property
    def type_(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Type

        if temp is None:
            return ""

        return temp

    @property
    def type_information(self: Self) -> "_2153.BearingTypeExtraInformation":
        """mastapy.bearings.bearing_designs.rolling.BearingTypeExtraInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TypeInformation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.BearingTypeExtraInformation",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.rolling._2153",
            "BearingTypeExtraInformation",
        )(value)

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
    def width_series(self: Self) -> "overridable.Overridable_WidthSeries":
        """Overridable[mastapy.bearings.bearing_designs.rolling.WidthSeries]"""
        temp = self.wrapped.WidthSeries

        if temp is None:
            return None

        value = overridable.Overridable_WidthSeries.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @width_series.setter
    @enforce_parameter_types
    def width_series(
        self: Self, value: "Union[_2182.WidthSeries, Tuple[_2182.WidthSeries, bool]]"
    ):
        wrapper_type = overridable.Overridable_WidthSeries.wrapper_type()
        enclosed_type = overridable.Overridable_WidthSeries.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.WidthSeries = value

    @property
    def element_material(self: Self) -> "_248.BearingMaterial":
        """mastapy.materials.BearingMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def geometric_constants(self: Self) -> "_2162.GeometricConstants":
        """mastapy.bearings.bearing_designs.rolling.GeometricConstants

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometricConstants

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def history(self: Self) -> "_1589.FileHistory":
        """mastapy.utility.FileHistory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso153122018(self: Self) -> "_1984.ISO153122018Results":
        """mastapy.bearings.bearing_results.rolling.ISO153122018Results

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO153122018

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_ring_material(self: Self) -> "_248.BearingMaterial":
        """mastapy.materials.BearingMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRingMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_ring_material(self: Self) -> "_248.BearingMaterial":
        """mastapy.materials.BearingMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRingMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def protection(self: Self) -> "_2150.BearingProtection":
        """mastapy.bearings.bearing_designs.rolling.BearingProtection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Protection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def skf_seal_frictional_moment_constants(
        self: Self,
    ) -> "_2174.SKFSealFrictionalMomentConstants":
        """mastapy.bearings.bearing_designs.rolling.SKFSealFrictionalMomentConstants

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SKFSealFrictionalMomentConstants

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def remove_inner_ring_while_keeping_other_geometry_constant(self: Self):
        """Method does not return."""
        self.wrapped.RemoveInnerRingWhileKeepingOtherGeometryConstant()

    def remove_outer_ring_while_keeping_other_geometry_constant(self: Self):
        """Method does not return."""
        self.wrapped.RemoveOuterRingWhileKeepingOtherGeometryConstant()

    def __copy__(self: Self) -> "RollingBearing":
        """mastapy.bearings.bearing_designs.rolling.RollingBearing"""
        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def __deepcopy__(self: Self, memo) -> "RollingBearing":
        """mastapy.bearings.bearing_designs.rolling.RollingBearing"""
        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def link_to_online_catalogue(self: Self):
        """Method does not return."""
        self.wrapped.LinkToOnlineCatalogue()

    @property
    def cast_to(self: Self) -> "RollingBearing._Cast_RollingBearing":
        return self._Cast_RollingBearing(self)
