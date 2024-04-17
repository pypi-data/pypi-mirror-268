"""ThrustBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs.rolling import _2147
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_THRUST_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "ThrustBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1896
    from mastapy.bearings.bearing_designs.rolling import _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("ThrustBallBearing",)


Self = TypeVar("Self", bound="ThrustBallBearing")


class ThrustBallBearing(_2147.BallBearing):
    """ThrustBallBearing

    This is a mastapy class.
    """

    TYPE = _THRUST_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ThrustBallBearing")

    class _Cast_ThrustBallBearing:
        """Special nested class for casting ThrustBallBearing to subclasses."""

        def __init__(
            self: "ThrustBallBearing._Cast_ThrustBallBearing",
            parent: "ThrustBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "ThrustBallBearing._Cast_ThrustBallBearing",
        ) -> "_2147.BallBearing":
            return self._parent._cast(_2147.BallBearing)

        @property
        def rolling_bearing(
            self: "ThrustBallBearing._Cast_ThrustBallBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "ThrustBallBearing._Cast_ThrustBallBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "ThrustBallBearing._Cast_ThrustBallBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "ThrustBallBearing._Cast_ThrustBallBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def thrust_ball_bearing(
            self: "ThrustBallBearing._Cast_ThrustBallBearing",
        ) -> "ThrustBallBearing":
            return self._parent

        def __getattr__(self: "ThrustBallBearing._Cast_ThrustBallBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ThrustBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def center_ring_corner_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CenterRingCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @center_ring_corner_radius.setter
    @enforce_parameter_types
    def center_ring_corner_radius(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CenterRingCornerRadius = value

    @property
    def inner_ring_outer_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_outer_diameter.setter
    @enforce_parameter_types
    def inner_ring_outer_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingOuterDiameter = value

    @property
    def outer_ring_inner_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterRingInnerDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_ring_inner_diameter.setter
    @enforce_parameter_types
    def outer_ring_inner_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterRingInnerDiameter = value

    @property
    def outer_ring_mounting(self: Self) -> "_1896.OuterRingMounting":
        """mastapy.bearings.OuterRingMounting"""
        temp = self.wrapped.OuterRingMounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.OuterRingMounting"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1896", "OuterRingMounting"
        )(value)

    @outer_ring_mounting.setter
    @enforce_parameter_types
    def outer_ring_mounting(self: Self, value: "_1896.OuterRingMounting"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.OuterRingMounting"
        )
        self.wrapped.OuterRingMounting = value

    @property
    def sphered_seat_offset(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpheredSeatOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @sphered_seat_offset.setter
    @enforce_parameter_types
    def sphered_seat_offset(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpheredSeatOffset = value

    @property
    def sphered_seat_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpheredSeatRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @sphered_seat_radius.setter
    @enforce_parameter_types
    def sphered_seat_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpheredSeatRadius = value

    @property
    def sum_of_the_centre_and_inner_ring_left_corner_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfTheCentreAndInnerRingLeftCornerRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_the_centre_and_inner_ring_right_corner_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfTheCentreAndInnerRingRightCornerRadius

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self: Self) -> "ThrustBallBearing._Cast_ThrustBallBearing":
        return self._Cast_ThrustBallBearing(self)
