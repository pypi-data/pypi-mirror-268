"""ConicalMeshLoadedContactLine"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.ltca import _846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_LOADED_CONTACT_LINE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Conical", "ConicalMeshLoadedContactLine"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshLoadedContactLine",)


Self = TypeVar("Self", bound="ConicalMeshLoadedContactLine")


class ConicalMeshLoadedContactLine(_846.GearMeshLoadedContactLine):
    """ConicalMeshLoadedContactLine

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_LOADED_CONTACT_LINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshLoadedContactLine")

    class _Cast_ConicalMeshLoadedContactLine:
        """Special nested class for casting ConicalMeshLoadedContactLine to subclasses."""

        def __init__(
            self: "ConicalMeshLoadedContactLine._Cast_ConicalMeshLoadedContactLine",
            parent: "ConicalMeshLoadedContactLine",
        ):
            self._parent = parent

        @property
        def gear_mesh_loaded_contact_line(
            self: "ConicalMeshLoadedContactLine._Cast_ConicalMeshLoadedContactLine",
        ) -> "_846.GearMeshLoadedContactLine":
            return self._parent._cast(_846.GearMeshLoadedContactLine)

        @property
        def conical_mesh_loaded_contact_line(
            self: "ConicalMeshLoadedContactLine._Cast_ConicalMeshLoadedContactLine",
        ) -> "ConicalMeshLoadedContactLine":
            return self._parent

        def __getattr__(
            self: "ConicalMeshLoadedContactLine._Cast_ConicalMeshLoadedContactLine",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshLoadedContactLine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshLoadedContactLine._Cast_ConicalMeshLoadedContactLine":
        return self._Cast_ConicalMeshLoadedContactLine(self)
