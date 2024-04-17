"""ConicalGearLeadModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.micro_geometry import _575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LEAD_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry",
    "ConicalGearLeadModification",
)

if TYPE_CHECKING:
    from mastapy.gears.micro_geometry import _582


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearLeadModification",)


Self = TypeVar("Self", bound="ConicalGearLeadModification")


class ConicalGearLeadModification(_575.LeadModification):
    """ConicalGearLeadModification

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LEAD_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearLeadModification")

    class _Cast_ConicalGearLeadModification:
        """Special nested class for casting ConicalGearLeadModification to subclasses."""

        def __init__(
            self: "ConicalGearLeadModification._Cast_ConicalGearLeadModification",
            parent: "ConicalGearLeadModification",
        ):
            self._parent = parent

        @property
        def lead_modification(
            self: "ConicalGearLeadModification._Cast_ConicalGearLeadModification",
        ) -> "_575.LeadModification":
            return self._parent._cast(_575.LeadModification)

        @property
        def modification(
            self: "ConicalGearLeadModification._Cast_ConicalGearLeadModification",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def conical_gear_lead_modification(
            self: "ConicalGearLeadModification._Cast_ConicalGearLeadModification",
        ) -> "ConicalGearLeadModification":
            return self._parent

        def __getattr__(
            self: "ConicalGearLeadModification._Cast_ConicalGearLeadModification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearLeadModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearLeadModification._Cast_ConicalGearLeadModification":
        return self._Cast_ConicalGearLeadModification(self)
