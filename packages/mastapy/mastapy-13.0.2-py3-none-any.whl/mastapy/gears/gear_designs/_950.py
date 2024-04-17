"""DesignConstraintsCollection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy.gears.gear_designs import _948
from mastapy._internal import conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_CONSTRAINTS_COLLECTION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "DesignConstraintsCollection"
)

if TYPE_CHECKING:
    from mastapy.utility.property import _1843


__docformat__ = "restructuredtext en"
__all__ = ("DesignConstraintsCollection",)


Self = TypeVar("Self", bound="DesignConstraintsCollection")


class DesignConstraintsCollection(_1836.NamedDatabaseItem):
    """DesignConstraintsCollection

    This is a mastapy class.
    """

    TYPE = _DESIGN_CONSTRAINTS_COLLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignConstraintsCollection")

    class _Cast_DesignConstraintsCollection:
        """Special nested class for casting DesignConstraintsCollection to subclasses."""

        def __init__(
            self: "DesignConstraintsCollection._Cast_DesignConstraintsCollection",
            parent: "DesignConstraintsCollection",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "DesignConstraintsCollection._Cast_DesignConstraintsCollection",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def design_constraints_collection(
            self: "DesignConstraintsCollection._Cast_DesignConstraintsCollection",
        ) -> "DesignConstraintsCollection":
            return self._parent

        def __getattr__(
            self: "DesignConstraintsCollection._Cast_DesignConstraintsCollection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignConstraintsCollection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_constraints(
        self: Self,
    ) -> "List[_1843.DeletableCollectionMember[_948.DesignConstraint]]":
        """List[mastapy.utility.property.DeletableCollectionMember[mastapy.gears.gear_designs.DesignConstraint]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignConstraints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "DesignConstraintsCollection._Cast_DesignConstraintsCollection":
        return self._Cast_DesignConstraintsCollection(self)
