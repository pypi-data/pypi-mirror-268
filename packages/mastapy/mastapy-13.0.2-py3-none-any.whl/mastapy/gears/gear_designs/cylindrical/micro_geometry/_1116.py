"""CylindricalGearTriangularEndModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.micro_geometry import _582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearTriangularEndModification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1117


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearTriangularEndModification",)


Self = TypeVar("Self", bound="CylindricalGearTriangularEndModification")


class CylindricalGearTriangularEndModification(_582.Modification):
    """CylindricalGearTriangularEndModification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearTriangularEndModification"
    )

    class _Cast_CylindricalGearTriangularEndModification:
        """Special nested class for casting CylindricalGearTriangularEndModification to subclasses."""

        def __init__(
            self: "CylindricalGearTriangularEndModification._Cast_CylindricalGearTriangularEndModification",
            parent: "CylindricalGearTriangularEndModification",
        ):
            self._parent = parent

        @property
        def modification(
            self: "CylindricalGearTriangularEndModification._Cast_CylindricalGearTriangularEndModification",
        ) -> "_582.Modification":
            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_triangular_end_modification(
            self: "CylindricalGearTriangularEndModification._Cast_CylindricalGearTriangularEndModification",
        ) -> "CylindricalGearTriangularEndModification":
            return self._parent

        def __getattr__(
            self: "CylindricalGearTriangularEndModification._Cast_CylindricalGearTriangularEndModification",
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
        self: Self, instance_to_wrap: "CylindricalGearTriangularEndModification.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def root_left(
        self: Self,
    ) -> "_1117.CylindricalGearTriangularEndModificationAtOrientation":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearTriangularEndModificationAtOrientation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootLeft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def root_right(
        self: Self,
    ) -> "_1117.CylindricalGearTriangularEndModificationAtOrientation":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearTriangularEndModificationAtOrientation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootRight

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tip_left(
        self: Self,
    ) -> "_1117.CylindricalGearTriangularEndModificationAtOrientation":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearTriangularEndModificationAtOrientation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipLeft

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tip_right(
        self: Self,
    ) -> "_1117.CylindricalGearTriangularEndModificationAtOrientation":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearTriangularEndModificationAtOrientation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipRight

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def relief_of(self: Self, face_width: "float", roll_distance: "float") -> "float":
        """float

        Args:
            face_width (float)
            roll_distance (float)
        """
        face_width = float(face_width)
        roll_distance = float(roll_distance)
        method_result = self.wrapped.ReliefOf(
            face_width if face_width else 0.0, roll_distance if roll_distance else 0.0
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearTriangularEndModification._Cast_CylindricalGearTriangularEndModification":
        return self._Cast_CylindricalGearTriangularEndModification(self)
