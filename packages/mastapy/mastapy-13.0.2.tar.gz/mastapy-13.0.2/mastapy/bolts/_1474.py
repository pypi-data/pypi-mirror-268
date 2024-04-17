"""BoltedJointMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Bolts", "BoltedJointMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.bolts import _1473, _1478, _1483
    from mastapy.utility.databases import _1838, _1831


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointMaterialDatabase",)


Self = TypeVar("Self", bound="BoltedJointMaterialDatabase")
T = TypeVar("T", bound="_1473.BoltedJointMaterial")


class BoltedJointMaterialDatabase(_1835.NamedDatabase[T]):
    """BoltedJointMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _BOLTED_JOINT_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointMaterialDatabase")

    class _Cast_BoltedJointMaterialDatabase:
        """Special nested class for casting BoltedJointMaterialDatabase to subclasses."""

        def __init__(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
            parent: "BoltedJointMaterialDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
        ) -> "_1835.NamedDatabase":
            return self._parent._cast(_1835.NamedDatabase)

        @property
        def sql_database(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
        ) -> "_1838.SQLDatabase":
            pass

            from mastapy.utility.databases import _1838

            return self._parent._cast(_1838.SQLDatabase)

        @property
        def database(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
        ) -> "_1831.Database":
            pass

            from mastapy.utility.databases import _1831

            return self._parent._cast(_1831.Database)

        @property
        def bolt_material_database(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
        ) -> "_1478.BoltMaterialDatabase":
            from mastapy.bolts import _1478

            return self._parent._cast(_1478.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
        ) -> "_1483.ClampedSectionMaterialDatabase":
            from mastapy.bolts import _1483

            return self._parent._cast(_1483.ClampedSectionMaterialDatabase)

        @property
        def bolted_joint_material_database(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
        ) -> "BoltedJointMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointMaterialDatabase._Cast_BoltedJointMaterialDatabase":
        return self._Cast_BoltedJointMaterialDatabase(self)
