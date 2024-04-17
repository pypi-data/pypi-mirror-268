"""DIN3990MeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical.iso6336 import _515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN3990_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.DIN3990", "DIN3990MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _484, _485, _470
    from mastapy.gears.rating.cylindrical.iso6336 import _523, _521
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("DIN3990MeshSingleFlankRating",)


Self = TypeVar("Self", bound="DIN3990MeshSingleFlankRating")


class DIN3990MeshSingleFlankRating(_515.ISO63361996MeshSingleFlankRating):
    """DIN3990MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _DIN3990_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DIN3990MeshSingleFlankRating")

    class _Cast_DIN3990MeshSingleFlankRating:
        """Special nested class for casting DIN3990MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
            parent: "DIN3990MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso63361996_mesh_single_flank_rating(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
        ) -> "_515.ISO63361996MeshSingleFlankRating":
            return self._parent._cast(_515.ISO63361996MeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
        ) -> "_523.ISO6336AbstractMetalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _523

            return self._parent._cast(_523.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
        ) -> "_521.ISO6336AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _521

            return self._parent._cast(_521.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
        ) -> "_470.CylindricalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _470

            return self._parent._cast(_470.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
        ) -> "DIN3990MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DIN3990MeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_mean_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicMeanFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def estimated_bulk_temperature_flash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedBulkTemperatureFlash

        if temp is None:
            return 0.0

        return temp

    @property
    def estimated_bulk_temperature_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EstimatedBulkTemperatureIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def flash_factor_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlashFactorIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_at_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def integral_scuffing_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntegralScuffingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_at_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_coefficient_of_friction_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCoefficientOfFrictionIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_local_coefficient_of_friction_at_maximum_flash_temperature(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanLocalCoefficientOfFrictionAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def parameter_on_line_of_action_at_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterOnLineOfActionAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def resonance_ratio_in_the_main_resonance_range(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResonanceRatioInTheMainResonanceRange

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_rating_method_flash_temperature_method(
        self: Self,
    ) -> "_484.ScuffingFlashTemperatureRatingMethod":
        """mastapy.gears.rating.cylindrical.ScuffingFlashTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingRatingMethodFlashTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingFlashTemperatureRatingMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._484",
            "ScuffingFlashTemperatureRatingMethod",
        )(value)

    @property
    def scuffing_rating_method_integral_temperature_method(
        self: Self,
    ) -> "_485.ScuffingIntegralTemperatureRatingMethod":
        """mastapy.gears.rating.cylindrical.ScuffingIntegralTemperatureRatingMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.ScuffingIntegralTemperatureRatingMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._485",
            "ScuffingIntegralTemperatureRatingMethod",
        )(value)

    @property
    def thermo_elastic_factor_at_maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermoElasticFactorAtMaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_relief_factor_integral(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipReliefFactorIntegral

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_unit_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseUnitLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DIN3990MeshSingleFlankRating._Cast_DIN3990MeshSingleFlankRating":
        return self._Cast_DIN3990MeshSingleFlankRating(self)
