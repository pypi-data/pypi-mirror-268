"""RollingBearingDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.utility.databases import _1838
from mastapy.bearings import _1901
from mastapy.bearings.bearing_designs.rolling import _2172
from mastapy._internal.cast_exception import CastException

_ROLLING_BEARING_TYPE = python_net_import("SMT.MastaAPI.Bearings", "RollingBearingType")
_BEARING_CATALOG = python_net_import("SMT.MastaAPI.Bearings", "BearingCatalog")
_HYBRID_STEEL_ALL = python_net_import("SMT.MastaAPI.Bearings", "HybridSteelAll")
_ROLLING_BEARING_DATABASE = python_net_import(
    "SMT.MastaAPI.Bearings", "RollingBearingDatabase"
)
_STRING = python_net_import("System", "String")
_INT_32 = python_net_import("System", "Int32")
_RANGE = python_net_import("SMT.MastaAPI.MathUtility", "Range")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1831
    from mastapy.bearings import _1903, _1876, _1892
    from mastapy.math_utility import _1496


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingDatabase",)


Self = TypeVar("Self", bound="RollingBearingDatabase")


class RollingBearingDatabase(
    _1838.SQLDatabase["_1901.RollingBearingKey", "_2172.RollingBearing"]
):
    """RollingBearingDatabase

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingBearingDatabase")

    class _Cast_RollingBearingDatabase:
        """Special nested class for casting RollingBearingDatabase to subclasses."""

        def __init__(
            self: "RollingBearingDatabase._Cast_RollingBearingDatabase",
            parent: "RollingBearingDatabase",
        ):
            self._parent = parent

        @property
        def sql_database(
            self: "RollingBearingDatabase._Cast_RollingBearingDatabase",
        ) -> "_1838.SQLDatabase":
            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "RollingBearingDatabase._Cast_RollingBearingDatabase",
        ) -> "_1831.Database":
            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def rolling_bearing_database(
            self: "RollingBearingDatabase._Cast_RollingBearingDatabase",
        ) -> "RollingBearingDatabase":
            return self._parent

        def __getattr__(
            self: "RollingBearingDatabase._Cast_RollingBearingDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingBearingDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def add_to_database(self: Self, bearing: "_2172.RollingBearing"):
        """Method does not return.

        Args:
            bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        """
        self.wrapped.AddToDatabase(bearing.wrapped if bearing else None)

    @enforce_parameter_types
    def create_bearing(
        self: Self, type_: "_1903.RollingBearingType", designation: "str" = "None"
    ) -> "_2172.RollingBearing":
        """mastapy.bearings.bearing_designs.rolling.RollingBearing

        Args:
            type_ (mastapy.bearings.RollingBearingType)
            designation (str, optional)
        """
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        designation = str(designation)
        method_result = self.wrapped.CreateBearing.Overloads[
            _ROLLING_BEARING_TYPE, _STRING
        ](type_, designation if designation else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_bearing_with_type_name(
        self: Self, type_: "str", designation: "str" = "None"
    ) -> "_2172.RollingBearing":
        """mastapy.bearings.bearing_designs.rolling.RollingBearing

        Args:
            type_ (str)
            designation (str, optional)
        """
        type_ = str(type_)
        designation = str(designation)
        method_result = self.wrapped.CreateBearing.Overloads[_STRING, _STRING](
            type_ if type_ else "", designation if designation else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_key(
        self: Self, type_: "_1903.RollingBearingType", designation: "str" = "None"
    ) -> "_1901.RollingBearingKey":
        """mastapy.bearings.RollingBearingKey

        Args:
            type_ (mastapy.bearings.RollingBearingType)
            designation (str, optional)
        """
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        designation = str(designation)
        method_result = self.wrapped.CreateKey.Overloads[
            _ROLLING_BEARING_TYPE, _STRING
        ](type_, designation if designation else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def create_key_with_type_name(
        self: Self, type_: "str", designation: "str" = "None"
    ) -> "_1901.RollingBearingKey":
        """mastapy.bearings.RollingBearingKey

        Args:
            type_ (str)
            designation (str, optional)
        """
        type_ = str(type_)
        designation = str(designation)
        method_result = self.wrapped.CreateKey.Overloads[_STRING, _STRING](
            type_ if type_ else "", designation if designation else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def remove_from_database(self: Self, bearing: "_2172.RollingBearing"):
        """Method does not return.

        Args:
            bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        """
        self.wrapped.RemoveFromDatabase(bearing.wrapped if bearing else None)

    @enforce_parameter_types
    def search_for_rolling_bearing_with_catalog(
        self: Self, catalog: "_1876.BearingCatalog"
    ) -> "List[_2172.RollingBearing]":
        """List[mastapy.bearings.bearing_designs.rolling.RollingBearing]

        Args:
            catalog (mastapy.bearings.BearingCatalog)
        """
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.SearchForRollingBearing.Overloads[_BEARING_CATALOG](catalog)
        )

    @enforce_parameter_types
    def search_for_rolling_bearing_with_name_and_catalog(
        self: Self, designation: "str", catalog: "_1876.BearingCatalog"
    ) -> "_2172.RollingBearing":
        """mastapy.bearings.bearing_designs.rolling.RollingBearing

        Args:
            designation (str)
            catalog (mastapy.bearings.BearingCatalog)
        """
        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        method_result = self.wrapped.SearchForRollingBearing.Overloads[
            _STRING, _BEARING_CATALOG
        ](designation if designation else "", catalog)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def search_for_rolling_bearing_with_name_catalog_and_type(
        self: Self,
        designation: "str",
        catalog: "_1876.BearingCatalog",
        type_: "_1903.RollingBearingType",
    ) -> "List[_2172.RollingBearing]":
        """List[mastapy.bearings.bearing_designs.rolling.RollingBearing]

        Args:
            designation (str)
            catalog (mastapy.bearings.BearingCatalog)
            type_ (mastapy.bearings.RollingBearingType)
        """
        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.SearchForRollingBearing.Overloads[
                _STRING, _BEARING_CATALOG, _ROLLING_BEARING_TYPE
            ](designation if designation else "", catalog, type_)
        )

    @enforce_parameter_types
    def search_for_rolling_bearing(
        self: Self,
        designation: "str",
        catalog: "_1876.BearingCatalog",
        type_: "_1903.RollingBearingType",
        bore_range: "_1496.Range",
        outer_diameter_range: "_1496.Range",
        width_range: "_1496.Range",
        dynamic_capacity_range: "_1496.Range",
        number_of_rows: "int",
        material_type: "_1892.HybridSteelAll",
    ) -> "List[_2172.RollingBearing]":
        """List[mastapy.bearings.bearing_designs.rolling.RollingBearing]

        Args:
            designation (str)
            catalog (mastapy.bearings.BearingCatalog)
            type_ (mastapy.bearings.RollingBearingType)
            bore_range (mastapy.math_utility.Range)
            outer_diameter_range (mastapy.math_utility.Range)
            width_range (mastapy.math_utility.Range)
            dynamic_capacity_range (mastapy.math_utility.Range)
            number_of_rows (int)
            material_type (mastapy.bearings.HybridSteelAll)
        """
        designation = str(designation)
        catalog = conversion.mp_to_pn_enum(
            catalog, "SMT.MastaAPI.Bearings.BearingCatalog"
        )
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.Bearings.RollingBearingType"
        )
        number_of_rows = int(number_of_rows)
        material_type = conversion.mp_to_pn_enum(
            material_type, "SMT.MastaAPI.Bearings.HybridSteelAll"
        )
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.SearchForRollingBearing.Overloads[
                _STRING,
                _BEARING_CATALOG,
                _ROLLING_BEARING_TYPE,
                _RANGE,
                _RANGE,
                _RANGE,
                _RANGE,
                _INT_32,
                _HYBRID_STEEL_ALL,
            ](
                designation if designation else "",
                catalog,
                type_,
                bore_range.wrapped if bore_range else None,
                outer_diameter_range.wrapped if outer_diameter_range else None,
                width_range.wrapped if width_range else None,
                dynamic_capacity_range.wrapped if dynamic_capacity_range else None,
                number_of_rows if number_of_rows else 0,
                material_type,
            )
        )

    @property
    def cast_to(self: Self) -> "RollingBearingDatabase._Cast_RollingBearingDatabase":
        return self._Cast_RollingBearingDatabase(self)
