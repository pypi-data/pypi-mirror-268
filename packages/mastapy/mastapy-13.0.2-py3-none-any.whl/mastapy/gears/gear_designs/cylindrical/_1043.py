"""CylindricalMeshedGearFlank"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESHED_GEAR_FLANK = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalMeshedGearFlank"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.gear_designs.cylindrical import _1029


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshedGearFlank",)


Self = TypeVar("Self", bound="CylindricalMeshedGearFlank")


class CylindricalMeshedGearFlank(_0.APIBase):
    """CylindricalMeshedGearFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESHED_GEAR_FLANK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalMeshedGearFlank")

    class _Cast_CylindricalMeshedGearFlank:
        """Special nested class for casting CylindricalMeshedGearFlank to subclasses."""

        def __init__(
            self: "CylindricalMeshedGearFlank._Cast_CylindricalMeshedGearFlank",
            parent: "CylindricalMeshedGearFlank",
        ):
            self._parent = parent

        @property
        def cylindrical_meshed_gear_flank(
            self: "CylindricalMeshedGearFlank._Cast_CylindricalMeshedGearFlank",
        ) -> "CylindricalMeshedGearFlank":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshedGearFlank._Cast_CylindricalMeshedGearFlank",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalMeshedGearFlank.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clearance_from_form_diameter_to_sap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ClearanceFromFormDiameterToSAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def dedendum_path_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DedendumPathOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankName

        if temp is None:
            return ""

        return temp

    @property
    def form_over_dimension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormOverDimension

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_addendum_path_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfAddendumPathOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def load_direction_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDirectionAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def partial_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartialContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_line_length_of_the_active_tooth_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileLineLengthOfTheActiveToothFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_factor_at_tooth_tip(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingFactorAtToothTip

        if temp is None:
            return 0.0

        return temp

    @property
    def specific_sliding_at_eap(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificSlidingAtEAP

        if temp is None:
            return 0.0

        return temp

    @property
    def specific_sliding_at_sap(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificSlidingAtSAP

        if temp is None:
            return 0.0

        return temp

    @property
    def specific_sliding_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificSlidingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def end_of_active_profile(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EndOfActiveProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def highest_point_of_fewest_tooth_contacts(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestPointOfFewestToothContacts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lowest_point_of_fewest_tooth_contacts(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestPointOfFewestToothContacts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def start_of_active_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StartOfActiveProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def working_pitch(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingPitch

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshedGearFlank._Cast_CylindricalMeshedGearFlank":
        return self._Cast_CylindricalMeshedGearFlank(self)
