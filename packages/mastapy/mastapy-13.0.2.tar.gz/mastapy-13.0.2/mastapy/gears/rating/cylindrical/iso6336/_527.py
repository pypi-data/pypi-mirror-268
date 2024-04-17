"""ToothFlankFractureAnalysisContactPoint"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _528
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ToothFlankFractureAnalysisContactPoint",
)


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisContactPoint",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisContactPoint")


class ToothFlankFractureAnalysisContactPoint(
    _528.ToothFlankFractureAnalysisContactPointCommon
):
    """ToothFlankFractureAnalysisContactPoint

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ToothFlankFractureAnalysisContactPoint"
    )

    class _Cast_ToothFlankFractureAnalysisContactPoint:
        """Special nested class for casting ToothFlankFractureAnalysisContactPoint to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisContactPoint._Cast_ToothFlankFractureAnalysisContactPoint",
            parent: "ToothFlankFractureAnalysisContactPoint",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_contact_point_common(
            self: "ToothFlankFractureAnalysisContactPoint._Cast_ToothFlankFractureAnalysisContactPoint",
        ) -> "_528.ToothFlankFractureAnalysisContactPointCommon":
            return self._parent._cast(_528.ToothFlankFractureAnalysisContactPointCommon)

        @property
        def tooth_flank_fracture_analysis_contact_point(
            self: "ToothFlankFractureAnalysisContactPoint._Cast_ToothFlankFractureAnalysisContactPoint",
        ) -> "ToothFlankFractureAnalysisContactPoint":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisContactPoint._Cast_ToothFlankFractureAnalysisContactPoint",
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
        self: Self, instance_to_wrap: "ToothFlankFractureAnalysisContactPoint.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureAnalysisContactPoint._Cast_ToothFlankFractureAnalysisContactPoint":
        return self._Cast_ToothFlankFractureAnalysisContactPoint(self)
