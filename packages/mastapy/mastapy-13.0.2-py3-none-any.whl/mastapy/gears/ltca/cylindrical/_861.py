"""CylindricalGearMeshLoadedContactLine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.ltca import _846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_LINE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalGearMeshLoadedContactLine"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _862


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshLoadedContactLine",)


Self = TypeVar("Self", bound="CylindricalGearMeshLoadedContactLine")


class CylindricalGearMeshLoadedContactLine(_846.GearMeshLoadedContactLine):
    """CylindricalGearMeshLoadedContactLine

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_LINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshLoadedContactLine")

    class _Cast_CylindricalGearMeshLoadedContactLine:
        """Special nested class for casting CylindricalGearMeshLoadedContactLine to subclasses."""

        def __init__(
            self: "CylindricalGearMeshLoadedContactLine._Cast_CylindricalGearMeshLoadedContactLine",
            parent: "CylindricalGearMeshLoadedContactLine",
        ):
            self._parent = parent

        @property
        def gear_mesh_loaded_contact_line(
            self: "CylindricalGearMeshLoadedContactLine._Cast_CylindricalGearMeshLoadedContactLine",
        ) -> "_846.GearMeshLoadedContactLine":
            return self._parent._cast(_846.GearMeshLoadedContactLine)

        @property
        def cylindrical_gear_mesh_loaded_contact_line(
            self: "CylindricalGearMeshLoadedContactLine._Cast_CylindricalGearMeshLoadedContactLine",
        ) -> "CylindricalGearMeshLoadedContactLine":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshLoadedContactLine._Cast_CylindricalGearMeshLoadedContactLine",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshLoadedContactLine.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_contact_strip_end_points(
        self: Self,
    ) -> "List[_862.CylindricalGearMeshLoadedContactPoint]":
        """List[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedContactStripEndPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshLoadedContactLine._Cast_CylindricalGearMeshLoadedContactLine":
        return self._Cast_CylindricalGearMeshLoadedContactLine(self)
