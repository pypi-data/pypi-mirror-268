"""PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_VDI2736_GEAR_SINGLE_FLANK_RATING_IN_A_PLASTIC_PLASTIC_MESH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _520
    from mastapy.gears.rating.cylindrical import _468
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",)


Self = TypeVar("Self", bound="PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh")


class PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh(
    _494.PlasticGearVDI2736AbstractGearSingleFlankRating
):
    """PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh

    This is a mastapy class.
    """

    TYPE = _PLASTIC_VDI2736_GEAR_SINGLE_FLANK_RATING_IN_A_PLASTIC_PLASTIC_MESH
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
    )

    class _Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh:
        """Special nested class for casting PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh to subclasses."""

        def __init__(
            self: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
            parent: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
        ):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(
            self: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
        ) -> "_494.PlasticGearVDI2736AbstractGearSingleFlankRating":
            return self._parent._cast(
                _494.PlasticGearVDI2736AbstractGearSingleFlankRating
            )

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
        ) -> "_520.ISO6336AbstractGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _520

            return self._parent._cast(_520.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
        ) -> "_468.CylindricalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _468

            return self._parent._cast(_468.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(
            self: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
        ) -> "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh":
            return self._parent

        def __getattr__(
            self: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
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
        instance_to_wrap: "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh":
        return self._Cast_PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh(self)
