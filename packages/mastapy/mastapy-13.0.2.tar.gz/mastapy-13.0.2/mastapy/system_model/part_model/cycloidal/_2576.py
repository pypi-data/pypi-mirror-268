"""CycloidalDisc"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2442
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CYCLOIDAL_DISC = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
)

if TYPE_CHECKING:
    from mastapy.cycloidal import _1461
    from mastapy.materials import _272
    from mastapy.system_model.part_model import _2468, _2443, _2451, _2475
    from mastapy.system_model.connections_and_sockets.cycloidal import _2346
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDisc",)


Self = TypeVar("Self", bound="CycloidalDisc")


class CycloidalDisc(_2442.AbstractShaft):
    """CycloidalDisc

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDisc")

    class _Cast_CycloidalDisc:
        """Special nested class for casting CycloidalDisc to subclasses."""

        def __init__(
            self: "CycloidalDisc._Cast_CycloidalDisc", parent: "CycloidalDisc"
        ):
            self._parent = parent

        @property
        def abstract_shaft(
            self: "CycloidalDisc._Cast_CycloidalDisc",
        ) -> "_2442.AbstractShaft":
            return self._parent._cast(_2442.AbstractShaft)

        @property
        def abstract_shaft_or_housing(
            self: "CycloidalDisc._Cast_CycloidalDisc",
        ) -> "_2443.AbstractShaftOrHousing":
            from mastapy.system_model.part_model import _2443

            return self._parent._cast(_2443.AbstractShaftOrHousing)

        @property
        def component(self: "CycloidalDisc._Cast_CycloidalDisc") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "CycloidalDisc._Cast_CycloidalDisc") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "CycloidalDisc._Cast_CycloidalDisc",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cycloidal_disc(
            self: "CycloidalDisc._Cast_CycloidalDisc",
        ) -> "CycloidalDisc":
            return self._parent

        def __getattr__(self: "CycloidalDisc._Cast_CycloidalDisc", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDisc.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BoreDiameter

        if temp is None:
            return 0.0

        return temp

    @bore_diameter.setter
    @enforce_parameter_types
    def bore_diameter(self: Self, value: "float"):
        self.wrapped.BoreDiameter = float(value) if value is not None else 0.0

    @property
    def disc_material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DiscMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @disc_material_database.setter
    @enforce_parameter_types
    def disc_material_database(self: Self, value: "str"):
        self.wrapped.DiscMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def hole_diameter_for_eccentric_bearing(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HoleDiameterForEccentricBearing

        if temp is None:
            return 0.0

        return temp

    @hole_diameter_for_eccentric_bearing.setter
    @enforce_parameter_types
    def hole_diameter_for_eccentric_bearing(self: Self, value: "float"):
        self.wrapped.HoleDiameterForEccentricBearing = (
            float(value) if value is not None else 0.0
        )

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def number_of_planetary_sockets(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPlanetarySockets

        if temp is None:
            return 0

        return temp

    @number_of_planetary_sockets.setter
    @enforce_parameter_types
    def number_of_planetary_sockets(self: Self, value: "int"):
        self.wrapped.NumberOfPlanetarySockets = int(value) if value is not None else 0

    @property
    def cycloidal_disc_design(self: Self) -> "_1461.CycloidalDiscDesign":
        """mastapy.cycloidal.CycloidalDiscDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CycloidalDiscDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def disc_material(self: Self) -> "_272.Material":
        """mastapy.materials.Material

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiscMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_sharing_settings(self: Self) -> "_2468.LoadSharingSettings":
        """mastapy.system_model.part_model.LoadSharingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetary_bearing_sockets(
        self: Self,
    ) -> "List[_2346.CycloidalDiscPlanetaryBearingSocket]":
        """List[mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingSocket]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryBearingSockets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CycloidalDisc._Cast_CycloidalDisc":
        return self._Cast_CycloidalDisc(self)
