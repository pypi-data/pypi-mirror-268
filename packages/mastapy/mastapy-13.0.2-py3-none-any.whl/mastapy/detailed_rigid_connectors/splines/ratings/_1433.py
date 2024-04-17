"""DIN5466SplineRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines.ratings import _1439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIN5466_SPLINE_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "DIN5466SplineRating"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.rating import _1443


__docformat__ = "restructuredtext en"
__all__ = ("DIN5466SplineRating",)


Self = TypeVar("Self", bound="DIN5466SplineRating")


class DIN5466SplineRating(_1439.SplineJointRating):
    """DIN5466SplineRating

    This is a mastapy class.
    """

    TYPE = _DIN5466_SPLINE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DIN5466SplineRating")

    class _Cast_DIN5466SplineRating:
        """Special nested class for casting DIN5466SplineRating to subclasses."""

        def __init__(
            self: "DIN5466SplineRating._Cast_DIN5466SplineRating",
            parent: "DIN5466SplineRating",
        ):
            self._parent = parent

        @property
        def spline_joint_rating(
            self: "DIN5466SplineRating._Cast_DIN5466SplineRating",
        ) -> "_1439.SplineJointRating":
            return self._parent._cast(_1439.SplineJointRating)

        @property
        def shaft_hub_connection_rating(
            self: "DIN5466SplineRating._Cast_DIN5466SplineRating",
        ) -> "_1443.ShaftHubConnectionRating":
            from mastapy.detailed_rigid_connectors.rating import _1443

            return self._parent._cast(_1443.ShaftHubConnectionRating)

        @property
        def din5466_spline_rating(
            self: "DIN5466SplineRating._Cast_DIN5466SplineRating",
        ) -> "DIN5466SplineRating":
            return self._parent

        def __getattr__(
            self: "DIN5466SplineRating._Cast_DIN5466SplineRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DIN5466SplineRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def resultant_shear_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultantShearForce

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "DIN5466SplineRating._Cast_DIN5466SplineRating":
        return self._Cast_DIN5466SplineRating(self)
