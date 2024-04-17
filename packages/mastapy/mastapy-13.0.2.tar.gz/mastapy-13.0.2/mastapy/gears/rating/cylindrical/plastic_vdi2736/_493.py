"""MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _495
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_METAL_PLASTIC_OR_PLASTIC_METAL_VDI2736_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _521
    from mastapy.gears.rating.cylindrical import _470
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",)


Self = TypeVar("Self", bound="MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating")


class MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating(
    _495.PlasticGearVDI2736AbstractMeshSingleFlankRating
):
    """MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _METAL_PLASTIC_OR_PLASTIC_METAL_VDI2736_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
    )

    class _Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating:
        """Special nested class for casting MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
            parent: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(
            self: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
        ) -> "_495.PlasticGearVDI2736AbstractMeshSingleFlankRating":
            return self._parent._cast(
                _495.PlasticGearVDI2736AbstractMeshSingleFlankRating
            )

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
        ) -> "_521.ISO6336AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _521

            return self._parent._cast(_521.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
        ) -> "_470.CylindricalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _470

            return self._parent._cast(_470.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(
            self: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
        ) -> "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
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
        instance_to_wrap: "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating":
        return self._Cast_MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating(self)
