"""WormWheelDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.worm import _961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_WHEEL_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Worm", "WormWheelDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("WormWheelDesign",)


Self = TypeVar("Self", bound="WormWheelDesign")


class WormWheelDesign(_961.WormGearDesign):
    """WormWheelDesign

    This is a mastapy class.
    """

    TYPE = _WORM_WHEEL_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormWheelDesign")

    class _Cast_WormWheelDesign:
        """Special nested class for casting WormWheelDesign to subclasses."""

        def __init__(
            self: "WormWheelDesign._Cast_WormWheelDesign", parent: "WormWheelDesign"
        ):
            self._parent = parent

        @property
        def worm_gear_design(
            self: "WormWheelDesign._Cast_WormWheelDesign",
        ) -> "_961.WormGearDesign":
            return self._parent._cast(_961.WormGearDesign)

        @property
        def gear_design(
            self: "WormWheelDesign._Cast_WormWheelDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "WormWheelDesign._Cast_WormWheelDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def worm_wheel_design(
            self: "WormWheelDesign._Cast_WormWheelDesign",
        ) -> "WormWheelDesign":
            return self._parent

        def __getattr__(self: "WormWheelDesign._Cast_WormWheelDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormWheelDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_helix_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanHelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_helix_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceHelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def throat_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThroatRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def throat_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThroatTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def working_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "WormWheelDesign._Cast_WormWheelDesign":
        return self._Cast_WormWheelDesign(self)
