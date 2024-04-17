"""ParabolicCylindricalGearTriangularEndModification"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARABOLIC_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ParabolicCylindricalGearTriangularEndModification",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParabolicCylindricalGearTriangularEndModification",)


Self = TypeVar("Self", bound="ParabolicCylindricalGearTriangularEndModification")


class ParabolicCylindricalGearTriangularEndModification(
    _1135.SingleCylindricalGearTriangularEndModification
):
    """ParabolicCylindricalGearTriangularEndModification

    This is a mastapy class.
    """

    TYPE = _PARABOLIC_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParabolicCylindricalGearTriangularEndModification"
    )

    class _Cast_ParabolicCylindricalGearTriangularEndModification:
        """Special nested class for casting ParabolicCylindricalGearTriangularEndModification to subclasses."""

        def __init__(
            self: "ParabolicCylindricalGearTriangularEndModification._Cast_ParabolicCylindricalGearTriangularEndModification",
            parent: "ParabolicCylindricalGearTriangularEndModification",
        ):
            self._parent = parent

        @property
        def single_cylindrical_gear_triangular_end_modification(
            self: "ParabolicCylindricalGearTriangularEndModification._Cast_ParabolicCylindricalGearTriangularEndModification",
        ) -> "_1135.SingleCylindricalGearTriangularEndModification":
            return self._parent._cast(
                _1135.SingleCylindricalGearTriangularEndModification
            )

        @property
        def parabolic_cylindrical_gear_triangular_end_modification(
            self: "ParabolicCylindricalGearTriangularEndModification._Cast_ParabolicCylindricalGearTriangularEndModification",
        ) -> "ParabolicCylindricalGearTriangularEndModification":
            return self._parent

        def __getattr__(
            self: "ParabolicCylindricalGearTriangularEndModification._Cast_ParabolicCylindricalGearTriangularEndModification",
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
        instance_to_wrap: "ParabolicCylindricalGearTriangularEndModification.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParabolicCylindricalGearTriangularEndModification._Cast_ParabolicCylindricalGearTriangularEndModification":
        return self._Cast_ParabolicCylindricalGearTriangularEndModification(self)
