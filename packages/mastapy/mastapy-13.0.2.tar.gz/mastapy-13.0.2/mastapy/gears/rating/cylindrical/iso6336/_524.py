"""ISO6336MeanStressInfluenceFactor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_MEAN_STRESS_INFLUENCE_FACTOR = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO6336MeanStressInfluenceFactor"
)

if TYPE_CHECKING:
    from mastapy.gears import _326


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336MeanStressInfluenceFactor",)


Self = TypeVar("Self", bound="ISO6336MeanStressInfluenceFactor")


class ISO6336MeanStressInfluenceFactor(_0.APIBase):
    """ISO6336MeanStressInfluenceFactor

    This is a mastapy class.
    """

    TYPE = _ISO6336_MEAN_STRESS_INFLUENCE_FACTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336MeanStressInfluenceFactor")

    class _Cast_ISO6336MeanStressInfluenceFactor:
        """Special nested class for casting ISO6336MeanStressInfluenceFactor to subclasses."""

        def __init__(
            self: "ISO6336MeanStressInfluenceFactor._Cast_ISO6336MeanStressInfluenceFactor",
            parent: "ISO6336MeanStressInfluenceFactor",
        ):
            self._parent = parent

        @property
        def iso6336_mean_stress_influence_factor(
            self: "ISO6336MeanStressInfluenceFactor._Cast_ISO6336MeanStressInfluenceFactor",
        ) -> "ISO6336MeanStressInfluenceFactor":
            return self._parent

        def __getattr__(
            self: "ISO6336MeanStressInfluenceFactor._Cast_ISO6336MeanStressInfluenceFactor",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO6336MeanStressInfluenceFactor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def higher_loaded_flank(self: Self) -> "_326.CylindricalFlanks":
        """mastapy.gears.CylindricalFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HigherLoadedFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.CylindricalFlanks")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._326", "CylindricalFlanks")(
            value
        )

    @property
    def load_per_unit_face_width_of_the_higher_loaded_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadPerUnitFaceWidthOfTheHigherLoadedFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def load_per_unit_face_width_of_the_lower_loaded_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadPerUnitFaceWidthOfTheLowerLoadedFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_stress_ratio_for_reference_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanStressRatioForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_stress_ratio_for_static_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanStressRatioForStaticStress

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_influence_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressInfluenceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_influence_factor_for_reference_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressInfluenceFactorForReferenceStress

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO6336MeanStressInfluenceFactor._Cast_ISO6336MeanStressInfluenceFactor":
        return self._Cast_ISO6336MeanStressInfluenceFactor(self)
