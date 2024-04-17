"""DetailedBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs import _2141
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "DetailedBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import (
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
        _2172,
        _2173,
        _2176,
        _2177,
        _2178,
        _2179,
        _2180,
        _2181,
    )
    from mastapy.bearings.bearing_designs.fluid_film import (
        _2194,
        _2196,
        _2198,
        _2200,
        _2201,
        _2202,
    )
    from mastapy.bearings.bearing_designs import _2137


__docformat__ = "restructuredtext en"
__all__ = ("DetailedBearing",)


Self = TypeVar("Self", bound="DetailedBearing")


class DetailedBearing(_2141.NonLinearBearing):
    """DetailedBearing

    This is a mastapy class.
    """

    TYPE = _DETAILED_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedBearing")

    class _Cast_DetailedBearing:
        """Special nested class for casting DetailedBearing to subclasses."""

        def __init__(
            self: "DetailedBearing._Cast_DetailedBearing", parent: "DetailedBearing"
        ):
            self._parent = parent

        @property
        def non_linear_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2141.NonLinearBearing":
            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def angular_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2142.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2142

            return self._parent._cast(_2142.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2143.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2143

            return self._parent._cast(_2143.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2144.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2144

            return self._parent._cast(_2144.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2145.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2145

            return self._parent._cast(_2145.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2146.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2146

            return self._parent._cast(_2146.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2147.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2147

            return self._parent._cast(_2147.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2149.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2149

            return self._parent._cast(_2149.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2155.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2155

            return self._parent._cast(_2155.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2156.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2157.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2161.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2161

            return self._parent._cast(_2161.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2166.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2166

            return self._parent._cast(_2166.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2167.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2168.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def self_aligning_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2173.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2173

            return self._parent._cast(_2173.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2176.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2176

            return self._parent._cast(_2176.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2177.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2177

            return self._parent._cast(_2177.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2178.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2178

            return self._parent._cast(_2178.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2179.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2179

            return self._parent._cast(_2179.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2180.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2180

            return self._parent._cast(_2180.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2181.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2181

            return self._parent._cast(_2181.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2194.PadFluidFilmBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2194

            return self._parent._cast(_2194.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2196.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2196

            return self._parent._cast(_2196.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2198.PlainJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2198

            return self._parent._cast(_2198.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2200.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2200

            return self._parent._cast(_2200.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2201.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2201

            return self._parent._cast(_2201.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2202.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2202

            return self._parent._cast(_2202.TiltingPadThrustBearing)

        @property
        def detailed_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "DetailedBearing":
            return self._parent

        def __getattr__(self: "DetailedBearing._Cast_DetailedBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DetailedBearing._Cast_DetailedBearing":
        return self._Cast_DetailedBearing(self)
