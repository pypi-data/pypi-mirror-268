"""PlainJournalBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_designs import _2138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLAIN_JOURNAL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm", "PlainJournalBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.fluid_film import _2196, _2200
    from mastapy.bearings.bearing_designs import _2141, _2137


__docformat__ = "restructuredtext en"
__all__ = ("PlainJournalBearing",)


Self = TypeVar("Self", bound="PlainJournalBearing")


class PlainJournalBearing(_2138.DetailedBearing):
    """PlainJournalBearing

    This is a mastapy class.
    """

    TYPE = _PLAIN_JOURNAL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlainJournalBearing")

    class _Cast_PlainJournalBearing:
        """Special nested class for casting PlainJournalBearing to subclasses."""

        def __init__(
            self: "PlainJournalBearing._Cast_PlainJournalBearing",
            parent: "PlainJournalBearing",
        ):
            self._parent = parent

        @property
        def detailed_bearing(
            self: "PlainJournalBearing._Cast_PlainJournalBearing",
        ) -> "_2138.DetailedBearing":
            return self._parent._cast(_2138.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "PlainJournalBearing._Cast_PlainJournalBearing",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def bearing_design(
            self: "PlainJournalBearing._Cast_PlainJournalBearing",
        ) -> "_2137.BearingDesign":
            from mastapy.bearings.bearing_designs import _2137

            return self._parent._cast(_2137.BearingDesign)

        @property
        def plain_grease_filled_journal_bearing(
            self: "PlainJournalBearing._Cast_PlainJournalBearing",
        ) -> "_2196.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2196

            return self._parent._cast(_2196.PlainGreaseFilledJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "PlainJournalBearing._Cast_PlainJournalBearing",
        ) -> "_2200.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2200

            return self._parent._cast(_2200.PlainOilFedJournalBearing)

        @property
        def plain_journal_bearing(
            self: "PlainJournalBearing._Cast_PlainJournalBearing",
        ) -> "PlainJournalBearing":
            return self._parent

        def __getattr__(
            self: "PlainJournalBearing._Cast_PlainJournalBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlainJournalBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diametrical_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiametricalClearance

        if temp is None:
            return 0.0

        return temp

    @diametrical_clearance.setter
    @enforce_parameter_types
    def diametrical_clearance(self: Self, value: "float"):
        self.wrapped.DiametricalClearance = float(value) if value is not None else 0.0

    @property
    def land_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LandWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def land_width_to_diameter_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LandWidthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "PlainJournalBearing._Cast_PlainJournalBearing":
        return self._Cast_PlainJournalBearing(self)
