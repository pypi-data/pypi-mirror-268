"""AsymmetricSphericalRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2169
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ASYMMETRIC_SPHERICAL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "AsymmetricSphericalRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("AsymmetricSphericalRollerBearing",)


Self = TypeVar("Self", bound="AsymmetricSphericalRollerBearing")


class AsymmetricSphericalRollerBearing(_2169.RollerBearing):
    """AsymmetricSphericalRollerBearing

    This is a mastapy class.
    """

    TYPE = _ASYMMETRIC_SPHERICAL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AsymmetricSphericalRollerBearing")

    class _Cast_AsymmetricSphericalRollerBearing:
        """Special nested class for casting AsymmetricSphericalRollerBearing to subclasses."""

        def __init__(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
            parent: "AsymmetricSphericalRollerBearing",
        ):
            self._parent = parent

        @property
        def roller_bearing(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
        ) -> "_2169.RollerBearing":
            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
        ) -> "AsymmetricSphericalRollerBearing":
            return self._parent

        def __getattr__(
            self: "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AsymmetricSphericalRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_profile_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementProfileRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_profile_radius.setter
    @enforce_parameter_types
    def element_profile_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementProfileRadius = value

    @property
    def inner_race_groove_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRaceGrooveRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_race_groove_radius.setter
    @enforce_parameter_types
    def inner_race_groove_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRaceGrooveRadius = value

    @property
    def inner_rib_chamfer(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRibChamfer

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_rib_chamfer.setter
    @enforce_parameter_types
    def inner_rib_chamfer(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRibChamfer = value

    @property
    def inner_rib_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRibDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_rib_diameter.setter
    @enforce_parameter_types
    def inner_rib_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRibDiameter = value

    @property
    def major_diameter_offset_from_roller_centre(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MajorDiameterOffsetFromRollerCentre

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @major_diameter_offset_from_roller_centre.setter
    @enforce_parameter_types
    def major_diameter_offset_from_roller_centre(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MajorDiameterOffsetFromRollerCentre = value

    @property
    def outer_race_groove_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRaceGrooveRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_race_groove_radius.setter
    @enforce_parameter_types
    def outer_race_groove_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRaceGrooveRadius = value

    @property
    def cast_to(
        self: Self,
    ) -> "AsymmetricSphericalRollerBearing._Cast_AsymmetricSphericalRollerBearing":
        return self._Cast_AsymmetricSphericalRollerBearing(self)
