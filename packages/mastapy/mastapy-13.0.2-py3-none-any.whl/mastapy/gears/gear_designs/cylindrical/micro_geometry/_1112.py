"""CylindricalGearProfileModificationAtFaceWidthPosition"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PROFILE_MODIFICATION_AT_FACE_WIDTH_POSITION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
)

if TYPE_CHECKING:
    from mastapy.gears.micro_geometry import _585, _582


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearProfileModificationAtFaceWidthPosition",)


Self = TypeVar("Self", bound="CylindricalGearProfileModificationAtFaceWidthPosition")


class CylindricalGearProfileModificationAtFaceWidthPosition(
    _1111.CylindricalGearProfileModification
):
    """CylindricalGearProfileModificationAtFaceWidthPosition

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PROFILE_MODIFICATION_AT_FACE_WIDTH_POSITION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearProfileModificationAtFaceWidthPosition"
    )

    class _Cast_CylindricalGearProfileModificationAtFaceWidthPosition:
        """Special nested class for casting CylindricalGearProfileModificationAtFaceWidthPosition to subclasses."""

        def __init__(
            self: "CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition",
            parent: "CylindricalGearProfileModificationAtFaceWidthPosition",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_profile_modification(
            self: "CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition",
        ) -> "_1111.CylindricalGearProfileModification":
            return self._parent._cast(_1111.CylindricalGearProfileModification)

        @property
        def profile_modification(
            self: "CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition",
        ) -> "_585.ProfileModification":
            from mastapy.gears.micro_geometry import _585

            return self._parent._cast(_585.ProfileModification)

        @property
        def modification(
            self: "CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition",
        ) -> "_582.Modification":
            from mastapy.gears.micro_geometry import _582

            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_profile_modification_at_face_width_position(
            self: "CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition",
        ) -> "CylindricalGearProfileModificationAtFaceWidthPosition":
            return self._parent

        def __getattr__(
            self: "CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition",
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
        instance_to_wrap: "CylindricalGearProfileModificationAtFaceWidthPosition.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width_position(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidthPosition

        if temp is None:
            return 0.0

        return temp

    @face_width_position.setter
    @enforce_parameter_types
    def face_width_position(self: Self, value: "float"):
        self.wrapped.FaceWidthPosition = float(value) if value is not None else 0.0

    @property
    def face_width_position_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidthPositionFactor

        if temp is None:
            return 0.0

        return temp

    @face_width_position_factor.setter
    @enforce_parameter_types
    def face_width_position_factor(self: Self, value: "float"):
        self.wrapped.FaceWidthPositionFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearProfileModificationAtFaceWidthPosition._Cast_CylindricalGearProfileModificationAtFaceWidthPosition":
        return self._Cast_CylindricalGearProfileModificationAtFaceWidthPosition(self)
