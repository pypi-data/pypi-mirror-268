"""ISO63362006GearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _522
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63362006_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63362006GearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _511, _512, _518, _520
    from mastapy.gears.rating.cylindrical import _468
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO63362006GearSingleFlankRating",)


Self = TypeVar("Self", bound="ISO63362006GearSingleFlankRating")


class ISO63362006GearSingleFlankRating(_522.ISO6336AbstractMetalGearSingleFlankRating):
    """ISO63362006GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63362006_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO63362006GearSingleFlankRating")

    class _Cast_ISO63362006GearSingleFlankRating:
        """Special nested class for casting ISO63362006GearSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
            parent: "ISO63362006GearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
        ) -> "_522.ISO6336AbstractMetalGearSingleFlankRating":
            return self._parent._cast(_522.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
        ) -> "_520.ISO6336AbstractGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _520

            return self._parent._cast(_520.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
        ) -> "_468.CylindricalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _468

            return self._parent._cast(_468.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
        ) -> "_518.ISO63362019GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _518

            return self._parent._cast(_518.ISO63362019GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
        ) -> "ISO63362006GearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO63362006GearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def rim_thickness_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RimThicknessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rim_thickness_over_whole_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RimThicknessOverWholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def work_hardening_factor_for_reference_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkHardeningFactorForReferenceContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def work_hardening_factor_for_static_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkHardeningFactorForStaticContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_fatigue_fracture_results(
        self: Self,
    ) -> "_511.CylindricalGearToothFatigueFractureResults":
        """mastapy.gears.rating.cylindrical.iso6336.CylindricalGearToothFatigueFractureResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFatigueFractureResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_fatigue_fracture_results_according_to_french_proposal(
        self: Self,
    ) -> "_512.CylindricalGearToothFatigueFractureResultsN1457":
        """mastapy.gears.rating.cylindrical.iso6336.CylindricalGearToothFatigueFractureResultsN1457

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFatigueFractureResultsAccordingToFrenchProposal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ISO63362006GearSingleFlankRating._Cast_ISO63362006GearSingleFlankRating":
        return self._Cast_ISO63362006GearSingleFlankRating(self)
