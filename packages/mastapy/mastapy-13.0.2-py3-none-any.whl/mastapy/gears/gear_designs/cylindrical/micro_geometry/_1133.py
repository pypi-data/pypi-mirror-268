"""ProfileSlopeReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_SLOPE_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ProfileSlopeReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134


__docformat__ = "restructuredtext en"
__all__ = ("ProfileSlopeReliefWithDeviation",)


Self = TypeVar("Self", bound="ProfileSlopeReliefWithDeviation")


class ProfileSlopeReliefWithDeviation(_1132.ProfileReliefWithDeviation):
    """ProfileSlopeReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_SLOPE_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileSlopeReliefWithDeviation")

    class _Cast_ProfileSlopeReliefWithDeviation:
        """Special nested class for casting ProfileSlopeReliefWithDeviation to subclasses."""

        def __init__(
            self: "ProfileSlopeReliefWithDeviation._Cast_ProfileSlopeReliefWithDeviation",
            parent: "ProfileSlopeReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def profile_relief_with_deviation(
            self: "ProfileSlopeReliefWithDeviation._Cast_ProfileSlopeReliefWithDeviation",
        ) -> "_1132.ProfileReliefWithDeviation":
            return self._parent._cast(_1132.ProfileReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "ProfileSlopeReliefWithDeviation._Cast_ProfileSlopeReliefWithDeviation",
        ) -> "_1134.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134

            return self._parent._cast(_1134.ReliefWithDeviation)

        @property
        def profile_slope_relief_with_deviation(
            self: "ProfileSlopeReliefWithDeviation._Cast_ProfileSlopeReliefWithDeviation",
        ) -> "ProfileSlopeReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "ProfileSlopeReliefWithDeviation._Cast_ProfileSlopeReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProfileSlopeReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ProfileSlopeReliefWithDeviation._Cast_ProfileSlopeReliefWithDeviation":
        return self._Cast_ProfileSlopeReliefWithDeviation(self)
