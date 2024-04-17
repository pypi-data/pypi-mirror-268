"""ToothFlankFractureAnalysisContactPointCommon"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_COMMON = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ToothFlankFractureAnalysisContactPointCommon",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _531, _527, _529


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisContactPointCommon",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisContactPointCommon")


class ToothFlankFractureAnalysisContactPointCommon(_0.APIBase):
    """ToothFlankFractureAnalysisContactPointCommon

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_COMMON
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ToothFlankFractureAnalysisContactPointCommon"
    )

    class _Cast_ToothFlankFractureAnalysisContactPointCommon:
        """Special nested class for casting ToothFlankFractureAnalysisContactPointCommon to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisContactPointCommon._Cast_ToothFlankFractureAnalysisContactPointCommon",
            parent: "ToothFlankFractureAnalysisContactPointCommon",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_contact_point(
            self: "ToothFlankFractureAnalysisContactPointCommon._Cast_ToothFlankFractureAnalysisContactPointCommon",
        ) -> "_527.ToothFlankFractureAnalysisContactPoint":
            from mastapy.gears.rating.cylindrical.iso6336 import _527

            return self._parent._cast(_527.ToothFlankFractureAnalysisContactPoint)

        @property
        def tooth_flank_fracture_analysis_contact_point_method_a(
            self: "ToothFlankFractureAnalysisContactPointCommon._Cast_ToothFlankFractureAnalysisContactPointCommon",
        ) -> "_529.ToothFlankFractureAnalysisContactPointMethodA":
            from mastapy.gears.rating.cylindrical.iso6336 import _529

            return self._parent._cast(
                _529.ToothFlankFractureAnalysisContactPointMethodA
            )

        @property
        def tooth_flank_fracture_analysis_contact_point_common(
            self: "ToothFlankFractureAnalysisContactPointCommon._Cast_ToothFlankFractureAnalysisContactPointCommon",
        ) -> "ToothFlankFractureAnalysisContactPointCommon":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisContactPointCommon._Cast_ToothFlankFractureAnalysisContactPointCommon",
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
        instance_to_wrap: "ToothFlankFractureAnalysisContactPointCommon.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_case_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveCaseDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def half_of_hertzian_contact_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HalfOfHertzianContactWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def local_normal_radius_of_relative_curvature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LocalNormalRadiusOfRelativeCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def material_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def material_factor_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialFactorConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_material_exposure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMaterialExposure

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_residual_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumResidualStress

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_thickness_at_the_diameter_corresponding_to_the_middle_between_b_and_d(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.TransverseThicknessAtTheDiameterCorrespondingToTheMiddleBetweenBAndD
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_point_with_maximum_local_material_exposure(
        self: Self,
    ) -> "_531.ToothFlankFractureAnalysisPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisPointWithMaximumLocalMaterialExposure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def watch_points(self: Self) -> "List[_531.ToothFlankFractureAnalysisPoint]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WatchPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureAnalysisContactPointCommon._Cast_ToothFlankFractureAnalysisContactPointCommon":
        return self._Cast_ToothFlankFractureAnalysisContactPointCommon(self)
