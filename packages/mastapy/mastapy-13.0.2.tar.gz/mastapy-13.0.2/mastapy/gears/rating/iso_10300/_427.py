"""ISO10300MeshSingleFlankRatingHypoidMethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.iso_10300 import _429
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_MESH_SINGLE_FLANK_RATING_HYPOID_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300MeshSingleFlankRatingHypoidMethodB2"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _425
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300MeshSingleFlankRatingHypoidMethodB2",)


Self = TypeVar("Self", bound="ISO10300MeshSingleFlankRatingHypoidMethodB2")


class ISO10300MeshSingleFlankRatingHypoidMethodB2(
    _429.ISO10300MeshSingleFlankRatingMethodB2
):
    """ISO10300MeshSingleFlankRatingHypoidMethodB2

    This is a mastapy class.
    """

    TYPE = _ISO10300_MESH_SINGLE_FLANK_RATING_HYPOID_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2"
    )

    class _Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2:
        """Special nested class for casting ISO10300MeshSingleFlankRatingHypoidMethodB2 to subclasses."""

        def __init__(
            self: "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
            parent: "ISO10300MeshSingleFlankRatingHypoidMethodB2",
        ):
            self._parent = parent

        @property
        def iso10300_mesh_single_flank_rating_method_b2(
            self: "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
        ) -> "_429.ISO10300MeshSingleFlankRatingMethodB2":
            return self._parent._cast(_429.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def iso10300_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
        ) -> "_425.ISO10300MeshSingleFlankRating":
            pass

            from mastapy.gears.rating.iso_10300 import _425

            return self._parent._cast(_425.ISO10300MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
        ) -> "_549.ConicalMeshSingleFlankRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(
            self: "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
        ) -> "ISO10300MeshSingleFlankRatingHypoidMethodB2":
            return self._parent

        def __getattr__(
            self: "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2",
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
        self: Self, instance_to_wrap: "ISO10300MeshSingleFlankRatingHypoidMethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length_of_action_from_pinion_tip_to_point_of_load_application(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionFromPinionTipToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def length_of_action_from_wheel_tip_to_point_of_load_application(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfActionFromWheelTipToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def lengthwise_load_sharing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthwiseLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_length_of_action_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionLengthOfActionPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_load_sharing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_length_of_action_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelLengthOfActionPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300MeshSingleFlankRatingHypoidMethodB2._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2":
        return self._Cast_ISO10300MeshSingleFlankRatingHypoidMethodB2(self)
