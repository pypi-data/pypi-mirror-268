"""ISO6336AbstractGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical import _468
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ISO6336AbstractGearSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494, _499, _500
    from mastapy.gears.rating.cylindrical.iso6336 import _514, _516, _518, _522
    from mastapy.gears.rating.cylindrical.din3990 import _535
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336AbstractGearSingleFlankRating",)


Self = TypeVar("Self", bound="ISO6336AbstractGearSingleFlankRating")


class ISO6336AbstractGearSingleFlankRating(_468.CylindricalGearSingleFlankRating):
    """ISO6336AbstractGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336AbstractGearSingleFlankRating")

    class _Cast_ISO6336AbstractGearSingleFlankRating:
        """Special nested class for casting ISO6336AbstractGearSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
            parent: "ISO6336AbstractGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_468.CylindricalGearSingleFlankRating":
            return self._parent._cast(_468.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_494.PlasticGearVDI2736AbstractGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494

            return self._parent._cast(
                _494.PlasticGearVDI2736AbstractGearSingleFlankRating
            )

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> (
            "_499.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh"
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _499

            return self._parent._cast(
                _499.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh
            )

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_500.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _500

            return self._parent._cast(
                _500.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
            )

        @property
        def iso63361996_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_514.ISO63361996GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _514

            return self._parent._cast(_514.ISO63361996GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_516.ISO63362006GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _516

            return self._parent._cast(_516.ISO63362006GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_518.ISO63362019GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _518

            return self._parent._cast(_518.ISO63362019GearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_522.ISO6336AbstractMetalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _522

            return self._parent._cast(_522.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "_535.DIN3990GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _535

            return self._parent._cast(_535.DIN3990GearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
        ) -> "ISO6336AbstractGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating",
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
        self: Self, instance_to_wrap: "ISO6336AbstractGearSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def e(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.E

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_for_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthForRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def form_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def g(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.G

        if temp is None:
            return 0.0

        return temp

    @property
    def h(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.H

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tooth_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def notch_parameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NotchParameter

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor_bending_for_test_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactorBendingForTestGears

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO6336AbstractGearSingleFlankRating._Cast_ISO6336AbstractGearSingleFlankRating":
        return self._Cast_ISO6336AbstractGearSingleFlankRating(self)
