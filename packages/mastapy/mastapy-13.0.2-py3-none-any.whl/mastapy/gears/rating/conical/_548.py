"""ConicalMeshedGearRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalMeshedGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1158
    from mastapy.gears.rating.straight_bevel_diff import _404


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshedGearRating",)


Self = TypeVar("Self", bound="ConicalMeshedGearRating")


class ConicalMeshedGearRating(_0.APIBase):
    """ConicalMeshedGearRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshedGearRating")

    class _Cast_ConicalMeshedGearRating:
        """Special nested class for casting ConicalMeshedGearRating to subclasses."""

        def __init__(
            self: "ConicalMeshedGearRating._Cast_ConicalMeshedGearRating",
            parent: "ConicalMeshedGearRating",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_meshed_gear_rating(
            self: "ConicalMeshedGearRating._Cast_ConicalMeshedGearRating",
        ) -> "_404.StraightBevelDiffMeshedGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _404

            return self._parent._cast(_404.StraightBevelDiffMeshedGearRating)

        @property
        def conical_meshed_gear_rating(
            self: "ConicalMeshedGearRating._Cast_ConicalMeshedGearRating",
        ) -> "ConicalMeshedGearRating":
            return self._parent

        def __getattr__(
            self: "ConicalMeshedGearRating._Cast_ConicalMeshedGearRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshedGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self: Self) -> "_1158.ConicalFlanks":
        """mastapy.gears.gear_designs.conical.ConicalFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.ConicalFlanks"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1158", "ConicalFlanks"
        )(value)

    @property
    def axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_force_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialForceType

        if temp is None:
            return ""

        return temp

    @property
    def gleason_axial_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonAxialFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonSeparatingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def normal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForceType

        if temp is None:
            return ""

        return temp

    @property
    def tangential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ConicalMeshedGearRating._Cast_ConicalMeshedGearRating":
        return self._Cast_ConicalMeshedGearRating(self)
