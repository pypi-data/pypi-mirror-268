"""AxialThrustNeedleRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_THRUST_NEEDLE_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "AxialThrustNeedleRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2168, _2169, _2172
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("AxialThrustNeedleRollerBearing",)


Self = TypeVar("Self", bound="AxialThrustNeedleRollerBearing")


class AxialThrustNeedleRollerBearing(_2145.AxialThrustCylindricalRollerBearing):
    """AxialThrustNeedleRollerBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_THRUST_NEEDLE_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AxialThrustNeedleRollerBearing")

    class _Cast_AxialThrustNeedleRollerBearing:
        """Special nested class for casting AxialThrustNeedleRollerBearing to subclasses."""

        def __init__(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
            parent: "AxialThrustNeedleRollerBearing",
        ):
            self._parent = parent

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "_2145.AxialThrustCylindricalRollerBearing":
            return self._parent._cast(_2145.AxialThrustCylindricalRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "_2168.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def detailed_bearing(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
        ) -> "AxialThrustNeedleRollerBearing":
            return self._parent

        def __getattr__(
            self: "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AxialThrustNeedleRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AxialThrustNeedleRollerBearing._Cast_AxialThrustNeedleRollerBearing":
        return self._Cast_AxialThrustNeedleRollerBearing(self)
