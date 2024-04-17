"""LinearCylindricalGearTriangularEndModification"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "LinearCylindricalGearTriangularEndModification",
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearCylindricalGearTriangularEndModification",)


Self = TypeVar("Self", bound="LinearCylindricalGearTriangularEndModification")


class LinearCylindricalGearTriangularEndModification(
    _1135.SingleCylindricalGearTriangularEndModification
):
    """LinearCylindricalGearTriangularEndModification

    This is a mastapy class.
    """

    TYPE = _LINEAR_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LinearCylindricalGearTriangularEndModification"
    )

    class _Cast_LinearCylindricalGearTriangularEndModification:
        """Special nested class for casting LinearCylindricalGearTriangularEndModification to subclasses."""

        def __init__(
            self: "LinearCylindricalGearTriangularEndModification._Cast_LinearCylindricalGearTriangularEndModification",
            parent: "LinearCylindricalGearTriangularEndModification",
        ):
            self._parent = parent

        @property
        def single_cylindrical_gear_triangular_end_modification(
            self: "LinearCylindricalGearTriangularEndModification._Cast_LinearCylindricalGearTriangularEndModification",
        ) -> "_1135.SingleCylindricalGearTriangularEndModification":
            return self._parent._cast(
                _1135.SingleCylindricalGearTriangularEndModification
            )

        @property
        def linear_cylindrical_gear_triangular_end_modification(
            self: "LinearCylindricalGearTriangularEndModification._Cast_LinearCylindricalGearTriangularEndModification",
        ) -> "LinearCylindricalGearTriangularEndModification":
            return self._parent

        def __getattr__(
            self: "LinearCylindricalGearTriangularEndModification._Cast_LinearCylindricalGearTriangularEndModification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "LinearCylindricalGearTriangularEndModification.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LinearCylindricalGearTriangularEndModification._Cast_LinearCylindricalGearTriangularEndModification":
        return self._Cast_LinearCylindricalGearTriangularEndModification(self)
