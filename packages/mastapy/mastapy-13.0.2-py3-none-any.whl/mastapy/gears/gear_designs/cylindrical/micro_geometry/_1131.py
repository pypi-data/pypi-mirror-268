"""ProfileFormReliefWithDeviation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_FORM_RELIEF_WITH_DEVIATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "ProfileFormReliefWithDeviation",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134


__docformat__ = "restructuredtext en"
__all__ = ("ProfileFormReliefWithDeviation",)


Self = TypeVar("Self", bound="ProfileFormReliefWithDeviation")


class ProfileFormReliefWithDeviation(_1132.ProfileReliefWithDeviation):
    """ProfileFormReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_FORM_RELIEF_WITH_DEVIATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileFormReliefWithDeviation")

    class _Cast_ProfileFormReliefWithDeviation:
        """Special nested class for casting ProfileFormReliefWithDeviation to subclasses."""

        def __init__(
            self: "ProfileFormReliefWithDeviation._Cast_ProfileFormReliefWithDeviation",
            parent: "ProfileFormReliefWithDeviation",
        ):
            self._parent = parent

        @property
        def profile_relief_with_deviation(
            self: "ProfileFormReliefWithDeviation._Cast_ProfileFormReliefWithDeviation",
        ) -> "_1132.ProfileReliefWithDeviation":
            return self._parent._cast(_1132.ProfileReliefWithDeviation)

        @property
        def relief_with_deviation(
            self: "ProfileFormReliefWithDeviation._Cast_ProfileFormReliefWithDeviation",
        ) -> "_1134.ReliefWithDeviation":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1134

            return self._parent._cast(_1134.ReliefWithDeviation)

        @property
        def profile_form_relief_with_deviation(
            self: "ProfileFormReliefWithDeviation._Cast_ProfileFormReliefWithDeviation",
        ) -> "ProfileFormReliefWithDeviation":
            return self._parent

        def __getattr__(
            self: "ProfileFormReliefWithDeviation._Cast_ProfileFormReliefWithDeviation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProfileFormReliefWithDeviation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ProfileFormReliefWithDeviation._Cast_ProfileFormReliefWithDeviation":
        return self._Cast_ProfileFormReliefWithDeviation(self)
