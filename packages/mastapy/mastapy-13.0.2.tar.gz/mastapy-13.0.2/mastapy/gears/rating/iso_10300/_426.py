"""ISO10300MeshSingleFlankRatingBevelMethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.iso_10300 import _429
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_MESH_SINGLE_FLANK_RATING_BEVEL_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300MeshSingleFlankRatingBevelMethodB2"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _425
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300MeshSingleFlankRatingBevelMethodB2",)


Self = TypeVar("Self", bound="ISO10300MeshSingleFlankRatingBevelMethodB2")


class ISO10300MeshSingleFlankRatingBevelMethodB2(
    _429.ISO10300MeshSingleFlankRatingMethodB2
):
    """ISO10300MeshSingleFlankRatingBevelMethodB2

    This is a mastapy class.
    """

    TYPE = _ISO10300_MESH_SINGLE_FLANK_RATING_BEVEL_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO10300MeshSingleFlankRatingBevelMethodB2"
    )

    class _Cast_ISO10300MeshSingleFlankRatingBevelMethodB2:
        """Special nested class for casting ISO10300MeshSingleFlankRatingBevelMethodB2 to subclasses."""

        def __init__(
            self: "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2",
            parent: "ISO10300MeshSingleFlankRatingBevelMethodB2",
        ):
            self._parent = parent

        @property
        def iso10300_mesh_single_flank_rating_method_b2(
            self: "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2",
        ) -> "_429.ISO10300MeshSingleFlankRatingMethodB2":
            return self._parent._cast(_429.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def iso10300_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2",
        ) -> "_425.ISO10300MeshSingleFlankRating":
            pass

            from mastapy.gears.rating.iso_10300 import _425

            return self._parent._cast(_425.ISO10300MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2",
        ) -> "_549.ConicalMeshSingleFlankRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(
            self: "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2",
        ) -> "ISO10300MeshSingleFlankRatingBevelMethodB2":
            return self._parent

        def __getattr__(
            self: "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2",
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
        self: Self, instance_to_wrap: "ISO10300MeshSingleFlankRatingBevelMethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_sharing_ratio_for_bending_method_b2_for_none_statically_loaded_bevel_gear(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LoadSharingRatioForBendingMethodB2ForNoneStaticallyLoadedBevelGear
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_ratio_for_bending_method_b2_statically_loaded_straight_and_zerol_bevel_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LoadSharingRatioForBendingMethodB2StaticallyLoadedStraightAndZerolBevelGears
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfAction
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action_for_non_statically_loaded_with_modified_contact_ratio_larger_than_2(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForNonStaticallyLoadedWithModifiedContactRatioLargerThan2
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action_for_non_statically_loaded_with_modified_contact_ratio_less_or_equal_than_2(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForNonStaticallyLoadedWithModifiedContactRatioLessOrEqualThan2
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def location_of_point_of_load_application_for_maximum_bending_stress_on_path_of_action_for_statically_loaded_straight_bevel_and_zerol_bevel_gear(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LocationOfPointOfLoadApplicationForMaximumBendingStressOnPathOfActionForStaticallyLoadedStraightBevelAndZerolBevelGear
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_length_of_action_to_point_of_load_application_method_b2(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeLengthOfActionToPointOfLoadApplicationMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def gj(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GJ

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300MeshSingleFlankRatingBevelMethodB2._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2":
        return self._Cast_ISO10300MeshSingleFlankRatingBevelMethodB2(self)
