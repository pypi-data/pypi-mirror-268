"""CylindricalGearDesignConstraints"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_CONSTRAINTS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearDesignConstraints"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1017


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearDesignConstraints",)


Self = TypeVar("Self", bound="CylindricalGearDesignConstraints")


class CylindricalGearDesignConstraints(_1836.NamedDatabaseItem):
    """CylindricalGearDesignConstraints

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_CONSTRAINTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearDesignConstraints")

    class _Cast_CylindricalGearDesignConstraints:
        """Special nested class for casting CylindricalGearDesignConstraints to subclasses."""

        def __init__(
            self: "CylindricalGearDesignConstraints._Cast_CylindricalGearDesignConstraints",
            parent: "CylindricalGearDesignConstraints",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "CylindricalGearDesignConstraints._Cast_CylindricalGearDesignConstraints",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_gear_design_constraints(
            self: "CylindricalGearDesignConstraints._Cast_CylindricalGearDesignConstraints",
        ) -> "CylindricalGearDesignConstraints":
            return self._parent

        def __getattr__(
            self: "CylindricalGearDesignConstraints._Cast_CylindricalGearDesignConstraints",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearDesignConstraints.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_constraints(self: Self) -> "List[_1017.CylindricalGearDesignConstraint]":
        """List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesignConstraint]

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
    ) -> "CylindricalGearDesignConstraints._Cast_CylindricalGearDesignConstraints":
        return self._Cast_CylindricalGearDesignConstraints(self)
