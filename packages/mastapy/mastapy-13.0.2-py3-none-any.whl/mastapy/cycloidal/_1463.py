"""CycloidalDiscMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MATERIAL = python_net_import(
    "SMT.MastaAPI.Cycloidal", "CycloidalDiscMaterial"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscMaterial",)


Self = TypeVar("Self", bound="CycloidalDiscMaterial")


class CycloidalDiscMaterial(_272.Material):
    """CycloidalDiscMaterial

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscMaterial")

    class _Cast_CycloidalDiscMaterial:
        """Special nested class for casting CycloidalDiscMaterial to subclasses."""

        def __init__(
            self: "CycloidalDiscMaterial._Cast_CycloidalDiscMaterial",
            parent: "CycloidalDiscMaterial",
        ):
            self._parent = parent

        @property
        def material(
            self: "CycloidalDiscMaterial._Cast_CycloidalDiscMaterial",
        ) -> "_272.Material":
            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "CycloidalDiscMaterial._Cast_CycloidalDiscMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cycloidal_disc_material(
            self: "CycloidalDiscMaterial._Cast_CycloidalDiscMaterial",
        ) -> "CycloidalDiscMaterial":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscMaterial._Cast_CycloidalDiscMaterial", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CycloidalDiscMaterial._Cast_CycloidalDiscMaterial":
        return self._Cast_CycloidalDiscMaterial(self)
