"""ToothFlankFractureAnalysisContactPointMethodA"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _528
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_METHOD_A = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ToothFlankFractureAnalysisContactPointMethodA",
)


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisContactPointMethodA",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisContactPointMethodA")


class ToothFlankFractureAnalysisContactPointMethodA(
    _528.ToothFlankFractureAnalysisContactPointCommon
):
    """ToothFlankFractureAnalysisContactPointMethodA

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_METHOD_A
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ToothFlankFractureAnalysisContactPointMethodA"
    )

    class _Cast_ToothFlankFractureAnalysisContactPointMethodA:
        """Special nested class for casting ToothFlankFractureAnalysisContactPointMethodA to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisContactPointMethodA._Cast_ToothFlankFractureAnalysisContactPointMethodA",
            parent: "ToothFlankFractureAnalysisContactPointMethodA",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_contact_point_common(
            self: "ToothFlankFractureAnalysisContactPointMethodA._Cast_ToothFlankFractureAnalysisContactPointMethodA",
        ) -> "_528.ToothFlankFractureAnalysisContactPointCommon":
            return self._parent._cast(_528.ToothFlankFractureAnalysisContactPointCommon)

        @property
        def tooth_flank_fracture_analysis_contact_point_method_a(
            self: "ToothFlankFractureAnalysisContactPointMethodA._Cast_ToothFlankFractureAnalysisContactPointMethodA",
        ) -> "ToothFlankFractureAnalysisContactPointMethodA":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisContactPointMethodA._Cast_ToothFlankFractureAnalysisContactPointMethodA",
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
        instance_to_wrap: "ToothFlankFractureAnalysisContactPointMethodA.TYPE",
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
    ) -> "ToothFlankFractureAnalysisContactPointMethodA._Cast_ToothFlankFractureAnalysisContactPointMethodA":
        return self._Cast_ToothFlankFractureAnalysisContactPointMethodA(self)
