"""ToothFlankFractureAnalysisRowN1457"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical.iso6336 import _530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_ROW_N1457 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ToothFlankFractureAnalysisRowN1457",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _532


__docformat__ = "restructuredtext en"
__all__ = ("ToothFlankFractureAnalysisRowN1457",)


Self = TypeVar("Self", bound="ToothFlankFractureAnalysisRowN1457")


class ToothFlankFractureAnalysisRowN1457(
    _530.ToothFlankFractureAnalysisContactPointN1457
):
    """ToothFlankFractureAnalysisRowN1457

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_ROW_N1457
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ToothFlankFractureAnalysisRowN1457")

    class _Cast_ToothFlankFractureAnalysisRowN1457:
        """Special nested class for casting ToothFlankFractureAnalysisRowN1457 to subclasses."""

        def __init__(
            self: "ToothFlankFractureAnalysisRowN1457._Cast_ToothFlankFractureAnalysisRowN1457",
            parent: "ToothFlankFractureAnalysisRowN1457",
        ):
            self._parent = parent

        @property
        def tooth_flank_fracture_analysis_contact_point_n1457(
            self: "ToothFlankFractureAnalysisRowN1457._Cast_ToothFlankFractureAnalysisRowN1457",
        ) -> "_530.ToothFlankFractureAnalysisContactPointN1457":
            return self._parent._cast(_530.ToothFlankFractureAnalysisContactPointN1457)

        @property
        def tooth_flank_fracture_analysis_row_n1457(
            self: "ToothFlankFractureAnalysisRowN1457._Cast_ToothFlankFractureAnalysisRowN1457",
        ) -> "ToothFlankFractureAnalysisRowN1457":
            return self._parent

        def __getattr__(
            self: "ToothFlankFractureAnalysisRowN1457._Cast_ToothFlankFractureAnalysisRowN1457",
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
        self: Self, instance_to_wrap: "ToothFlankFractureAnalysisRowN1457.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_fatigue_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFatigueDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_point_with_maximum_fatigue_damage(
        self: Self,
    ) -> "_532.ToothFlankFractureAnalysisPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisPointN1457

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisPointWithMaximumFatigueDamage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def watch_points(self: Self) -> "List[_532.ToothFlankFractureAnalysisPointN1457]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisPointN1457]

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
    ) -> "ToothFlankFractureAnalysisRowN1457._Cast_ToothFlankFractureAnalysisRowN1457":
        return self._Cast_ToothFlankFractureAnalysisRowN1457(self)
