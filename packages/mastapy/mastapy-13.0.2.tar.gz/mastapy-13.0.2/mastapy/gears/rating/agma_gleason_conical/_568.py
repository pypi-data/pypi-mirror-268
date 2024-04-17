"""AGMAGleasonConicalGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.conical import _542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1175
    from mastapy.gears.rating.zerol_bevel import _372
    from mastapy.gears.rating.straight_bevel import _398
    from mastapy.gears.rating.spiral_bevel import _405
    from mastapy.gears.rating.hypoid import _441
    from mastapy.gears.rating.bevel import _557
    from mastapy.gears.rating import _363, _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshRating",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshRating")


class AGMAGleasonConicalGearMeshRating(_542.ConicalGearMeshRating):
    """AGMAGleasonConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshRating")

    class _Cast_AGMAGleasonConicalGearMeshRating:
        """Special nested class for casting AGMAGleasonConicalGearMeshRating to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
            parent: "AGMAGleasonConicalGearMeshRating",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_542.ConicalGearMeshRating":
            return self._parent._cast(_542.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_363.GearMeshRating":
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_372.ZerolBevelGearMeshRating":
            from mastapy.gears.rating.zerol_bevel import _372

            return self._parent._cast(_372.ZerolBevelGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_398.StraightBevelGearMeshRating":
            from mastapy.gears.rating.straight_bevel import _398

            return self._parent._cast(_398.StraightBevelGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_405.SpiralBevelGearMeshRating":
            from mastapy.gears.rating.spiral_bevel import _405

            return self._parent._cast(_405.SpiralBevelGearMeshRating)

        @property
        def hypoid_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_441.HypoidGearMeshRating":
            from mastapy.gears.rating.hypoid import _441

            return self._parent._cast(_441.HypoidGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "_557.BevelGearMeshRating":
            from mastapy.gears.rating.bevel import _557

            return self._parent._cast(_557.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
        ) -> "AGMAGleasonConicalGearMeshRating":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_distribution_factor_method(
        self: Self,
    ) -> "_1175.LoadDistributionFactorMethods":
        """mastapy.gears.gear_designs.conical.LoadDistributionFactorMethods

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.LoadDistributionFactorMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1175", "LoadDistributionFactorMethods"
        )(value)

    @property
    def maximum_relative_displacement(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRelativeDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverloadFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def overload_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OverloadFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating":
        return self._Cast_AGMAGleasonConicalGearMeshRating(self)
