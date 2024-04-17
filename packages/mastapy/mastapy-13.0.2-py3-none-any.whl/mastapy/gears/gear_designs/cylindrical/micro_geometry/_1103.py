"""CylindricalGearLeadModificationAtProfilePosition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LEAD_MODIFICATION_AT_PROFILE_POSITION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearLeadModificationAtProfilePosition",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.gears.micro_geometry import _575, _582


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearLeadModificationAtProfilePosition",)


Self = TypeVar("Self", bound="CylindricalGearLeadModificationAtProfilePosition")


class CylindricalGearLeadModificationAtProfilePosition(
    _1102.CylindricalGearLeadModification
):
    """CylindricalGearLeadModificationAtProfilePosition

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LEAD_MODIFICATION_AT_PROFILE_POSITION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearLeadModificationAtProfilePosition"
    )

    class _Cast_CylindricalGearLeadModificationAtProfilePosition:
        """Special nested class for casting CylindricalGearLeadModificationAtProfilePosition to subclasses."""

        def __init__(
            self: "CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition",
            parent: "CylindricalGearLeadModificationAtProfilePosition",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_lead_modification(
            self: "CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition",
        ) -> "_1102.CylindricalGearLeadModification":
            return self._parent._cast(_1102.CylindricalGearLeadModification)

        @property
        def lead_modification(
            self: "CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition",
        ) -> "_575.LeadModification":
            from mastapy.gears.micro_geometry import _575

            return self._parent._cast(_575.LeadModification)

        @property
        def modification(
            self: "CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_lead_modification_at_profile_position(
            self: "CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition",
        ) -> "CylindricalGearLeadModificationAtProfilePosition":
            return self._parent

        def __getattr__(
            self: "CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition",
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
        instance_to_wrap: "CylindricalGearLeadModificationAtProfilePosition.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def position_on_profile_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PositionOnProfileFactor

        if temp is None:
            return 0.0

        return temp

    @position_on_profile_factor.setter
    @enforce_parameter_types
    def position_on_profile_factor(self: Self, value: "float"):
        self.wrapped.PositionOnProfileFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def profile_measurement(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileMeasurement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearLeadModificationAtProfilePosition._Cast_CylindricalGearLeadModificationAtProfilePosition":
        return self._Cast_CylindricalGearLeadModificationAtProfilePosition(self)
