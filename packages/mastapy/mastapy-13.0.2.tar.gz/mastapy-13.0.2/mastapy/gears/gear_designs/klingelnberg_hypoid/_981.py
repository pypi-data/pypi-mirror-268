"""KlingelnbergCycloPalloidHypoidGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.klingelnberg_conical import _985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1160
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearDesign",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearDesign")


class KlingelnbergCycloPalloidHypoidGearDesign(_985.KlingelnbergConicalGearDesign):
    """KlingelnbergCycloPalloidHypoidGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_DESIGN
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearDesign"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearDesign:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearDesign to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign",
            parent: "KlingelnbergCycloPalloidHypoidGearDesign",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_design(
            self: "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign",
        ) -> "_985.KlingelnbergConicalGearDesign":
            return self._parent._cast(_985.KlingelnbergConicalGearDesign)

        @property
        def conical_gear_design(
            self: "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign",
        ) -> "_1160.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1160

            return self._parent._cast(_1160.ConicalGearDesign)

        @property
        def gear_design(
            self: "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign",
        ) -> "KlingelnbergCycloPalloidHypoidGearDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearDesign.TYPE"
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
    ) -> "KlingelnbergCycloPalloidHypoidGearDesign._Cast_KlingelnbergCycloPalloidHypoidGearDesign":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearDesign(self)
