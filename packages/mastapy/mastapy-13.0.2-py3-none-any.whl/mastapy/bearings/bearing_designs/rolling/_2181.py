"""ToroidalRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOROIDAL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "ToroidalRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2169, _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("ToroidalRollerBearing",)


Self = TypeVar("Self", bound="ToroidalRollerBearing")


class ToroidalRollerBearing(_2149.BarrelRollerBearing):
    """ToroidalRollerBearing

    This is a mastapy class.
    """

    TYPE = _TOROIDAL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToroidalRollerBearing")

    class _Cast_ToroidalRollerBearing:
        """Special nested class for casting ToroidalRollerBearing to subclasses."""

        def __init__(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
            parent: "ToroidalRollerBearing",
        ):
            self._parent = parent

        @property
        def barrel_roller_bearing(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
        ) -> "_2149.BarrelRollerBearing":
            return self._parent._cast(_2149.BarrelRollerBearing)

        @property
        def roller_bearing(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def toroidal_roller_bearing(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing",
        ) -> "ToroidalRollerBearing":
            return self._parent

        def __getattr__(
            self: "ToroidalRollerBearing._Cast_ToroidalRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ToroidalRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_displacement_capability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialDisplacementCapability

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_capability_towards_snap_ring(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialDisplacementCapabilityTowardsSnapRing

        if temp is None:
            return 0.0

        return temp

    @property
    def snap_ring_offset_from_element(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SnapRingOffsetFromElement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @snap_ring_offset_from_element.setter
    @enforce_parameter_types
    def snap_ring_offset_from_element(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SnapRingOffsetFromElement = value

    @property
    def snap_ring_width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SnapRingWidth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @snap_ring_width.setter
    @enforce_parameter_types
    def snap_ring_width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SnapRingWidth = value

    @property
    def cast_to(self: Self) -> "ToroidalRollerBearing._Cast_ToroidalRollerBearing":
        return self._Cast_ToroidalRollerBearing(self)
