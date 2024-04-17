"""ToothFlankFractureAnalysisContactPointN1457"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_N1457 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ToothFlankFractureAnalysisContactPointN1457",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.gears.rating.cylindrical.iso6336 import _533


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisContactPointN1457",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisContactPointN1457")


class ToothFlankFractureAnalysisContactPointN1457(_0.APIBase):
    """ToothFlankFractureAnalysisContactPointN1457

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_CONTACT_POINT_N1457
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ToothFlankFractureAnalysisContactPointN1457"
    )

    class _Cast_ToothFlankFractureAnalysisContactPointN1457:
        """Special nested class for casting ToothFlankFractureAnalysisContactPointN1457 to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisContactPointN1457._Cast_ToothFlankFractureAnalysisContactPointN1457",
            parent: "ToothFlankFractureAnalysisContactPointN1457",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_row_n1457(
            self: "ToothFlankFractureAnalysisContactPointN1457._Cast_ToothFlankFractureAnalysisContactPointN1457",
        ) -> "_533.ToothFlankFractureAnalysisRowN1457":
            from mastapy.gears.rating.cylindrical.iso6336 import _533

            return self._parent._cast(_533.ToothFlankFractureAnalysisRowN1457)

        @property
        def tooth_flank_fracture_analysis_contact_point_n1457(
            self: "ToothFlankFractureAnalysisContactPointN1457._Cast_ToothFlankFractureAnalysisContactPointN1457",
        ) -> "ToothFlankFractureAnalysisContactPointN1457":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisContactPointN1457._Cast_ToothFlankFractureAnalysisContactPointN1457",
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
        self: Self, instance_to_wrap: "ToothFlankFractureAnalysisContactPointN1457.TYPE"
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
    def mean_coefficient_of_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanCoefficientOfFriction

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
    def position_on_profile(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionOnProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ToothFlankFractureAnalysisContactPointN1457._Cast_ToothFlankFractureAnalysisContactPointN1457":
        return self._Cast_ToothFlankFractureAnalysisContactPointN1457(self)
