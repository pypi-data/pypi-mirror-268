"""CylindricalMeshLoadDistributionAtRotation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _845
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION = python_net_import(
    "SMT.MastaAPI.Gears.LTCA.Cylindrical", "CylindricalMeshLoadDistributionAtRotation"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1125
    from mastapy.gears.ltca.cylindrical import _861


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshLoadDistributionAtRotation",)


Self = TypeVar("Self", bound="CylindricalMeshLoadDistributionAtRotation")


class CylindricalMeshLoadDistributionAtRotation(
    _845.GearMeshLoadDistributionAtRotation
):
    """CylindricalMeshLoadDistributionAtRotation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalMeshLoadDistributionAtRotation"
    )

    class _Cast_CylindricalMeshLoadDistributionAtRotation:
        """Special nested class for casting CylindricalMeshLoadDistributionAtRotation to subclasses."""

        def __init__(
            self: "CylindricalMeshLoadDistributionAtRotation._Cast_CylindricalMeshLoadDistributionAtRotation",
            parent: "CylindricalMeshLoadDistributionAtRotation",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_distribution_at_rotation(
            self: "CylindricalMeshLoadDistributionAtRotation._Cast_CylindricalMeshLoadDistributionAtRotation",
        ) -> "_845.GearMeshLoadDistributionAtRotation":
            return self._parent._cast(_845.GearMeshLoadDistributionAtRotation)

        @property
        def cylindrical_mesh_load_distribution_at_rotation(
            self: "CylindricalMeshLoadDistributionAtRotation._Cast_CylindricalMeshLoadDistributionAtRotation",
        ) -> "CylindricalMeshLoadDistributionAtRotation":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshLoadDistributionAtRotation._Cast_CylindricalMeshLoadDistributionAtRotation",
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
        self: Self, instance_to_wrap: "CylindricalMeshLoadDistributionAtRotation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_alignment(self: Self) -> "_1125.MeshAlignment":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.MeshAlignment

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def loaded_contact_lines(
        self: Self,
    ) -> "List[_861.CylindricalGearMeshLoadedContactLine]":
        """List[mastapy.gears.ltca.cylindrical.CylindricalGearMeshLoadedContactLine]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedContactLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshLoadDistributionAtRotation._Cast_CylindricalMeshLoadDistributionAtRotation":
        return self._Cast_CylindricalMeshLoadDistributionAtRotation(self)
