"""ConicalGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _336
    from mastapy.gears.manufacturing.bevel import _799
    from mastapy.gears.gear_designs.cylindrical import _1084
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.gears.gear_designs.straight_bevel import _965
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _981
    from mastapy.gears.gear_designs.klingelnberg_conical import _985
    from mastapy.gears.gear_designs.hypoid import _989
    from mastapy.gears.gear_designs.bevel import _1186
    from mastapy.gears.gear_designs.agma_gleason_conical import _1199
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearDesign",)


Self = TypeVar("Self", bound="ConicalGearDesign")


class ConicalGearDesign(_951.GearDesign):
    """ConicalGearDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearDesign")

    class _Cast_ConicalGearDesign:
        """Special nested class for casting ConicalGearDesign to subclasses."""

        def __init__(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
            parent: "ConicalGearDesign",
        ):
            self._parent = parent

        @property
        def gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_951.GearDesign":
            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_956.ZerolBevelGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelGearDesign)

        @property
        def straight_bevel_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_965.StraightBevelGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_969.StraightBevelDiffGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_973.SpiralBevelGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_977.KlingelnbergCycloPalloidSpiralBevelGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977

            return self._parent._cast(
                _977.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_981.KlingelnbergCycloPalloidHypoidGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _981

            return self._parent._cast(_981.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_985.KlingelnbergConicalGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _985

            return self._parent._cast(_985.KlingelnbergConicalGearDesign)

        @property
        def hypoid_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_989.HypoidGearDesign":
            from mastapy.gears.gear_designs.hypoid import _989

            return self._parent._cast(_989.HypoidGearDesign)

        @property
        def bevel_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_1186.BevelGearDesign":
            from mastapy.gears.gear_designs.bevel import _1186

            return self._parent._cast(_1186.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "_1199.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1199

            return self._parent._cast(_1199.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "ConicalGearDesign._Cast_ConicalGearDesign",
        ) -> "ConicalGearDesign":
            return self._parent

        def __getattr__(self: "ConicalGearDesign._Cast_ConicalGearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutter_edge_radius_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterEdgeRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_edge_radius_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterEdgeRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def face_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def hand(self: Self) -> "_336.Hand":
        """mastapy.gears.Hand"""
        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.Hand")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._336", "Hand")(value)

    @hand.setter
    @enforce_parameter_types
    def hand(self: Self, value: "_336.Hand"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.Hand")
        self.wrapped.Hand = value

    @property
    def inner_root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def straddle_mounted(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.StraddleMounted

        if temp is None:
            return False

        return temp

    @straddle_mounted.setter
    @enforce_parameter_types
    def straddle_mounted(self: Self, value: "bool"):
        self.wrapped.StraddleMounted = bool(value) if value is not None else False

    @property
    def use_cutter_tilt(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCutterTilt

        if temp is None:
            return False

        return temp

    @use_cutter_tilt.setter
    @enforce_parameter_types
    def use_cutter_tilt(self: Self, value: "bool"):
        self.wrapped.UseCutterTilt = bool(value) if value is not None else False

    @property
    def flank_measurement_border(self: Self) -> "_799.FlankMeasurementBorder":
        """mastapy.gears.manufacturing.bevel.FlankMeasurementBorder

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankMeasurementBorder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def surface_roughness(self: Self) -> "_1084.SurfaceRoughness":
        """mastapy.gears.gear_designs.cylindrical.SurfaceRoughness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearDesign._Cast_ConicalGearDesign":
        return self._Cast_ConicalGearDesign(self)
