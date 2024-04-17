"""KlingelnbergCycloPalloidSpiralBevelGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.klingelnberg_conical import _985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1160
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearDesign",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearDesign")


class KlingelnbergCycloPalloidSpiralBevelGearDesign(_985.KlingelnbergConicalGearDesign):
    """KlingelnbergCycloPalloidSpiralBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_DESIGN
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearDesign to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearDesign",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_design(
            self: "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign",
        ) -> "_985.KlingelnbergConicalGearDesign":
            return self._parent._cast(_985.KlingelnbergConicalGearDesign)

        @property
        def conical_gear_design(
            self: "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign",
        ) -> "_1160.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1160

            return self._parent._cast(_1160.ConicalGearDesign)

        @property
        def gear_design(
            self: "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def generating_cone_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeneratingConeAngle

        if temp is None:
            return 0.0

        return temp

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
    def inner_tip_diameter_with_tooth_chamfer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerTipDiameterWithToothChamfer

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_spiral_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanSpiralAngle

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
    def outer_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign(self)
