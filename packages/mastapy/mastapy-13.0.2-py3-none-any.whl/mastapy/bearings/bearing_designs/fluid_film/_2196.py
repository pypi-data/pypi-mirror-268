"""PlainGreaseFilledJournalBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs.fluid_film import _2198
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_GREASE_FILLED_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PlainGreaseFilledJournalBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.fluid_film import _2197, _2199
    from mastapy.bearings.bearing_designs import _2138, _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("PlainGreaseFilledJournalBearing",)


Self = TypeVar("Self", bound="PlainGreaseFilledJournalBearing")


class PlainGreaseFilledJournalBearing(_2198.PlainJournalBearing):
    """PlainGreaseFilledJournalBearing

    This is a mastapy class.
    """

    TYPE = _PLAIN_GREASE_FILLED_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlainGreaseFilledJournalBearing")

    class _Cast_PlainGreaseFilledJournalBearing:
        """Special nested class for casting PlainGreaseFilledJournalBearing to subclasses."""

        def __init__(
            self: "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing",
            parent: "PlainGreaseFilledJournalBearing",
        ):
            self._parent = parent

        @property
        def plain_journal_bearing(
            self: "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing",
        ) -> "_2198.PlainJournalBearing":
            return self._parent._cast(_2198.PlainJournalBearing)

        @property
        def detailed_bearing(
            self: "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def plain_grease_filled_journal_bearing(
            self: "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing",
        ) -> "PlainGreaseFilledJournalBearing":
            return self._parent

        def __getattr__(
            self: "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlainGreaseFilledJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def housing_type(self: Self) -> "_2197.PlainGreaseFilledJournalBearingHousingType":
        """mastapy.bearings.bearing_designs.fluid_film.PlainGreaseFilledJournalBearingHousingType"""
        temp = self.wrapped.HousingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm.PlainGreaseFilledJournalBearingHousingType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_designs.fluid_film._2197",
            "PlainGreaseFilledJournalBearingHousingType",
        )(value)

    @housing_type.setter
    @enforce_parameter_types
    def housing_type(
        self: Self, value: "_2197.PlainGreaseFilledJournalBearingHousingType"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm.PlainGreaseFilledJournalBearingHousingType",
        )
        self.wrapped.HousingType = value

    @property
    def housing_detail(self: Self) -> "_2199.PlainJournalHousing":
        """mastapy.bearings.bearing_designs.fluid_film.PlainJournalHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HousingDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlainGreaseFilledJournalBearing._Cast_PlainGreaseFilledJournalBearing":
        return self._Cast_PlainGreaseFilledJournalBearing(self)
