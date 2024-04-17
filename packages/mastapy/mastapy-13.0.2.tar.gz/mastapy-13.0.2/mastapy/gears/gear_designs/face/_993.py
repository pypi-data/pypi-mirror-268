"""FaceGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs import _951
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_FACE_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Face", "FaceGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears import _336
    from mastapy.gears.gear_designs.face import _998, _1001
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearDesign",)


Self = TypeVar("Self", bound="FaceGearDesign")


class FaceGearDesign(_951.GearDesign):
    """FaceGearDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearDesign")

    class _Cast_FaceGearDesign:
        """Special nested class for casting FaceGearDesign to subclasses."""

        def __init__(
            self: "FaceGearDesign._Cast_FaceGearDesign", parent: "FaceGearDesign"
        ):
            self._parent = parent

        @property
        def gear_design(
            self: "FaceGearDesign._Cast_FaceGearDesign",
        ) -> "_951.GearDesign":
            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "FaceGearDesign._Cast_FaceGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def face_gear_pinion_design(
            self: "FaceGearDesign._Cast_FaceGearDesign",
        ) -> "_998.FaceGearPinionDesign":
            from mastapy.gears.gear_designs.face import _998

            return self._parent._cast(_998.FaceGearPinionDesign)

        @property
        def face_gear_wheel_design(
            self: "FaceGearDesign._Cast_FaceGearDesign",
        ) -> "_1001.FaceGearWheelDesign":
            from mastapy.gears.gear_designs.face import _1001

            return self._parent._cast(_1001.FaceGearWheelDesign)

        @property
        def face_gear_design(
            self: "FaceGearDesign._Cast_FaceGearDesign",
        ) -> "FaceGearDesign":
            return self._parent

        def __getattr__(self: "FaceGearDesign._Cast_FaceGearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def iso_material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ISOMaterial.SelectedItemName

        if temp is None:
            return ""

        return temp

    @iso_material.setter
    @enforce_parameter_types
    def iso_material(self: Self, value: "str"):
        self.wrapped.ISOMaterial.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def mean_point_to_crossing_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanPointToCrossingPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchAngle

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
    def working_pitch_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingPitchRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "FaceGearDesign._Cast_FaceGearDesign":
        return self._Cast_FaceGearDesign(self)
