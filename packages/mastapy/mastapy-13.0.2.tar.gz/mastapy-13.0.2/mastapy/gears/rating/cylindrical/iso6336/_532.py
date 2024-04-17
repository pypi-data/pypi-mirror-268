"""ToothFlankFractureAnalysisPointN1457"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_POINT_N1457 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ToothFlankFractureAnalysisPointN1457",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _534


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisPointN1457",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisPointN1457")


class ToothFlankFractureAnalysisPointN1457(_0.APIBase):
    """ToothFlankFractureAnalysisPointN1457

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_POINT_N1457
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothFlankFractureAnalysisPointN1457")

    class _Cast_ToothFlankFractureAnalysisPointN1457:
        """Special nested class for casting ToothFlankFractureAnalysisPointN1457 to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisPointN1457._Cast_ToothFlankFractureAnalysisPointN1457",
            parent: "ToothFlankFractureAnalysisPointN1457",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_point_n1457(
            self: "ToothFlankFractureAnalysisPointN1457._Cast_ToothFlankFractureAnalysisPointN1457",
        ) -> "ToothFlankFractureAnalysisPointN1457":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisPointN1457._Cast_ToothFlankFractureAnalysisPointN1457",
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
        self: Self, instance_to_wrap: "ToothFlankFractureAnalysisPointN1457.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth_from_surface(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DepthFromSurface

        if temp is None:
            return 0.0

        return temp

    @property
    def fatigue_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_conversion_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HardnessConversionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def local_material_hardness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalMaterialHardness

        if temp is None:
            return 0.0

        return temp

    @property
    def local_permissible_shear_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalPermissibleShearStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_equivalent_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEquivalentStress

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_depth_from_surface(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalisedDepthFromSurface

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_component_of_compressive_residual_stresses(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialComponentOfCompressiveResidualStresses

        if temp is None:
            return 0.0

        return temp

    @property
    def coordinates(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Coordinates

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def stress_analysis_with_maximum_equivalent_stress(
        self: Self,
    ) -> "_534.ToothFlankFractureStressStepAtAnalysisPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureStressStepAtAnalysisPointN1457

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressAnalysisWithMaximumEquivalentStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stress_history(
        self: Self,
    ) -> "List[_534.ToothFlankFractureStressStepAtAnalysisPointN1457]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureStressStepAtAnalysisPointN1457]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressHistory

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureAnalysisPointN1457._Cast_ToothFlankFractureAnalysisPointN1457":
        return self._Cast_ToothFlankFractureAnalysisPointN1457(self)
