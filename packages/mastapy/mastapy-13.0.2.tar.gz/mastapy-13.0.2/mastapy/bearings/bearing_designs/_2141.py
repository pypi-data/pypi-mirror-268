"""NonLinearBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs import _2137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "NonLinearBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs import _2138
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
    from mastapy.bearings.bearing_designs.concept import _2204, _2205, _2206


__docformat__ = "restructuredtext en"
__all__ = ("NonLinearBearing",)


Self = TypeVar("Self", bound="NonLinearBearing")


class NonLinearBearing(_2137.BearingDesign):
    """NonLinearBearing

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NonLinearBearing")

    class _Cast_NonLinearBearing:
        """Special nested class for casting NonLinearBearing to subclasses."""

        def __init__(
            self: "NonLinearBearing._Cast_NonLinearBearing", parent: "NonLinearBearing"
        ):
            self._parent = parent

        @property
        def bearing_design(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2137.BearingDesign":
            return self._parent._cast(_2137.BearingDesign)

        @property
        def detailed_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def angular_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2142.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2142

            return self._parent._cast(_2142.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2143.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2143

            return self._parent._cast(_2143.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2144.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2144

            return self._parent._cast(_2144.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2145.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2145

            return self._parent._cast(_2145.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2146.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2146

            return self._parent._cast(_2146.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2147.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2147

            return self._parent._cast(_2147.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2149.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2149

            return self._parent._cast(_2149.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2155.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2155

            return self._parent._cast(_2155.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2156.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2157.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2161.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2161

            return self._parent._cast(_2161.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2166.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2166

            return self._parent._cast(_2166.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2167.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2168.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def self_aligning_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2173.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2173

            return self._parent._cast(_2173.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2176.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2176

            return self._parent._cast(_2176.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2177.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2177

            return self._parent._cast(_2177.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2178.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2178

            return self._parent._cast(_2178.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2179.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2179

            return self._parent._cast(_2179.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2180.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2180

            return self._parent._cast(_2180.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2181.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2181

            return self._parent._cast(_2181.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2194.PadFluidFilmBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2194

            return self._parent._cast(_2194.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2196.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2196

            return self._parent._cast(_2196.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2198.PlainJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2198

            return self._parent._cast(_2198.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2200.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2200

            return self._parent._cast(_2200.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2201.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2201

            return self._parent._cast(_2201.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2202.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2202

            return self._parent._cast(_2202.TiltingPadThrustBearing)

        @property
        def concept_axial_clearance_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2204.ConceptAxialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2204

            return self._parent._cast(_2204.ConceptAxialClearanceBearing)

        @property
        def concept_clearance_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2205.ConceptClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2205

            return self._parent._cast(_2205.ConceptClearanceBearing)

        @property
        def concept_radial_clearance_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "_2206.ConceptRadialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2206

            return self._parent._cast(_2206.ConceptRadialClearanceBearing)

        @property
        def non_linear_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "NonLinearBearing":
            return self._parent

        def __getattr__(self: "NonLinearBearing._Cast_NonLinearBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NonLinearBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NonLinearBearing._Cast_NonLinearBearing":
        return self._Cast_NonLinearBearing(self)
