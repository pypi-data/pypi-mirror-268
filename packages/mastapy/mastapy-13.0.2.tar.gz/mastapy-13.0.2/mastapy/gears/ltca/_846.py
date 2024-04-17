"""GearMeshLoadedContactLine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_LOADED_CONTACT_LINE = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearMeshLoadedContactLine"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _847
    from mastapy.gears.ltca.cylindrical import _861
    from mastapy.gears.ltca.conical import _875


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshLoadedContactLine",)


Self = TypeVar("Self", bound="GearMeshLoadedContactLine")


class GearMeshLoadedContactLine(_0.APIBase):
    """GearMeshLoadedContactLine

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOADED_CONTACT_LINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshLoadedContactLine")

    class _Cast_GearMeshLoadedContactLine:
        """Special nested class for casting GearMeshLoadedContactLine to subclasses."""

        def __init__(
            self: "GearMeshLoadedContactLine._Cast_GearMeshLoadedContactLine",
            parent: "GearMeshLoadedContactLine",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_loaded_contact_line(
            self: "GearMeshLoadedContactLine._Cast_GearMeshLoadedContactLine",
        ) -> "_861.CylindricalGearMeshLoadedContactLine":
            from mastapy.gears.ltca.cylindrical import _861

            return self._parent._cast(_861.CylindricalGearMeshLoadedContactLine)

        @property
        def conical_mesh_loaded_contact_line(
            self: "GearMeshLoadedContactLine._Cast_GearMeshLoadedContactLine",
        ) -> "_875.ConicalMeshLoadedContactLine":
            from mastapy.gears.ltca.conical import _875

            return self._parent._cast(_875.ConicalMeshLoadedContactLine)

        @property
        def gear_mesh_loaded_contact_line(
            self: "GearMeshLoadedContactLine._Cast_GearMeshLoadedContactLine",
        ) -> "GearMeshLoadedContactLine":
            return self._parent

        def __getattr__(
            self: "GearMeshLoadedContactLine._Cast_GearMeshLoadedContactLine", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshLoadedContactLine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_line_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLineIndex

        if temp is None:
            return 0

        return temp

    @property
    def mesh_position_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPositionIndex

        if temp is None:
            return 0

        return temp

    @property
    def tooth_number_of_gear_a(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothNumberOfGearA

        if temp is None:
            return 0

        return temp

    @property
    def tooth_number_of_gear_b(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothNumberOfGearB

        if temp is None:
            return 0

        return temp

    @property
    def loaded_contact_strip_end_points(
        self: Self,
    ) -> "List[_847.GearMeshLoadedContactPoint]":
        """List[mastapy.gears.ltca.GearMeshLoadedContactPoint]

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
    ) -> "GearMeshLoadedContactLine._Cast_GearMeshLoadedContactLine":
        return self._Cast_GearMeshLoadedContactLine(self)
