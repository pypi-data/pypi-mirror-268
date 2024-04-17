"""KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.rating.klingelnberg_conical.kn3030 import _417
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030",
    "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _419
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating")


class KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating(
    _417.KlingelnbergConicalMeshSingleFlankRating
):
    """KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
            parent: "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_mesh_single_flank_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
        ) -> "_417.KlingelnbergConicalMeshSingleFlankRating":
            return self._parent._cast(_417.KlingelnbergConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_mesh_single_flank_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
        ) -> "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_scuffing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioFactorScuffing

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def friction_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def integral_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntegralFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_transverse(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def relating_factor_for_the_thermal_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelatingFactorForTheThermalFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_speed_sum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialSpeedSum

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_flash_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalFlashFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_single_flank_ratings(
        self: Self,
    ) -> "List[_419.KlingelnbergCycloPalloidConicalGearSingleFlankRating]":
        """List[mastapy.gears.rating.klingelnberg_conical.kn3030.KlingelnbergCycloPalloidConicalGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def kn3030_klingelnberg_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_419.KlingelnbergCycloPalloidConicalGearSingleFlankRating]":
        """List[mastapy.gears.rating.klingelnberg_conical.kn3030.KlingelnbergCycloPalloidConicalGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KN3030KlingelnbergGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating(self)
