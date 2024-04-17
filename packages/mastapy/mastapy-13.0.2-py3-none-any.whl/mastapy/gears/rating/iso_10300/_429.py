"""ISO10300MeshSingleFlankRatingMethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.iso_10300 import _425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_MESH_SINGLE_FLANK_RATING_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300MeshSingleFlankRatingMethodB2"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _397
    from mastapy.gears.rating.iso_10300 import _426, _427
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300MeshSingleFlankRatingMethodB2",)


Self = TypeVar("Self", bound="ISO10300MeshSingleFlankRatingMethodB2")


class ISO10300MeshSingleFlankRatingMethodB2(
    _425.ISO10300MeshSingleFlankRating["_394.VirtualCylindricalGearISO10300MethodB2"]
):
    """ISO10300MeshSingleFlankRatingMethodB2

    This is a mastapy class.
    """

    TYPE = _ISO10300_MESH_SINGLE_FLANK_RATING_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO10300MeshSingleFlankRatingMethodB2"
    )

    class _Cast_ISO10300MeshSingleFlankRatingMethodB2:
        """Special nested class for casting ISO10300MeshSingleFlankRatingMethodB2 to subclasses."""

        def __init__(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
            parent: "ISO10300MeshSingleFlankRatingMethodB2",
        ):
            self._parent = parent

        @property
        def iso10300_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
        ) -> "_425.ISO10300MeshSingleFlankRating":
            return self._parent._cast(_425.ISO10300MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
        ) -> "_549.ConicalMeshSingleFlankRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
        ) -> "_426.ISO10300MeshSingleFlankRatingBevelMethodB2":
            from mastapy.gears.rating.iso_10300 import _426

            return self._parent._cast(_426.ISO10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
        ) -> "_427.ISO10300MeshSingleFlankRatingHypoidMethodB2":
            from mastapy.gears.rating.iso_10300 import _427

            return self._parent._cast(_427.ISO10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
        ) -> "ISO10300MeshSingleFlankRatingMethodB2":
            return self._parent

        def __getattr__(
            self: "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2",
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
        self: Self, instance_to_wrap: "ISO10300MeshSingleFlankRatingMethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stress_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_adjustment_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressAdjustmentFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inertia_factor_value_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaFactorValueX

        if temp is None:
            return 0.0

        return temp

    @property
    def intermediate_value_x(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IntermediateValueX

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_action_at_critical_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionAtCriticalPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_action_considering_adjacent_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionConsideringAdjacentTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_contact_line(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfContactLine

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_ratio_for_bending_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingRatioForBendingMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_ratio_for_pitting_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingRatioForPittingMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_value_of_contact_stress_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalValueOfContactStressMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_profile_radius_of_curvature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionProfileRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_resistance_geometry_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PittingResistanceGeometryFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def position_change_alone_path_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PositionChangeAlonePathOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_of_curvature_change(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusOfCurvatureChange

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_length_of_action_ellipse_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeLengthOfActionEllipseContact

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_length_of_action_ellipse_contact_for_statically_loaded_straight_bevel_and_zerol_bevel_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeLengthOfActionEllipseContactForStaticallyLoadedStraightBevelAndZerolBevelGears
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_length_of_action_within_the_contact_ellipse(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeLengthOfActionWithinTheContactEllipse

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radius_of_profile_curvature_between_pinion_and_wheel(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeRadiusOfProfileCurvatureBetweenPinionAndWheel

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_factors_for_bending_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorsForBendingMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_factors_for_contact_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorsForContactMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_profile_radius_of_curvature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelProfileRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def yi(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YI

        if temp is None:
            return 0.0

        return temp

    @property
    def yi_for_bevel_and_zerol_bevel_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YIForBevelAndZerolBevelGear

        if temp is None:
            return 0.0

        return temp

    @property
    def yi_for_hypoid_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YIForHypoidGear

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_cylindrical_gear_set_method_b2(
        self: Self,
    ) -> "_397.VirtualCylindricalGearSetISO10300MethodB2":
        """mastapy.gears.rating.virtual_cylindrical_gears.VirtualCylindricalGearSetISO10300MethodB2

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualCylindricalGearSetMethodB2

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300MeshSingleFlankRatingMethodB2._Cast_ISO10300MeshSingleFlankRatingMethodB2":
        return self._Cast_ISO10300MeshSingleFlankRatingMethodB2(self)
