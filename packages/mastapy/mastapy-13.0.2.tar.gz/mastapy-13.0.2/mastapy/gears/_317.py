"""AccuracyGrades"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACCURACY_GRADES = python_net_import("SMT.MastaAPI.Gears", "AccuracyGrades")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1140,
        _1144,
        _1150,
    )
    from mastapy.gears.gear_designs.agma_gleason_conical import _1198


__docformat__ = "restructuredtext en"
__all__ = ("AccuracyGrades",)


Self = TypeVar("Self", bound="AccuracyGrades")


class AccuracyGrades(_0.APIBase):
    """AccuracyGrades

    This is a mastapy class.
    """

    TYPE = _ACCURACY_GRADES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AccuracyGrades")

    class _Cast_AccuracyGrades:
        """Special nested class for casting AccuracyGrades to subclasses."""

        def __init__(
            self: "AccuracyGrades._Cast_AccuracyGrades", parent: "AccuracyGrades"
        ):
            self._parent = parent

        @property
        def agma20151_accuracy_grades(
            self: "AccuracyGrades._Cast_AccuracyGrades",
        ) -> "_1140.AGMA20151AccuracyGrades":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1140,
            )

            return self._parent._cast(_1140.AGMA20151AccuracyGrades)

        @property
        def cylindrical_accuracy_grades(
            self: "AccuracyGrades._Cast_AccuracyGrades",
        ) -> "_1144.CylindricalAccuracyGrades":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1144,
            )

            return self._parent._cast(_1144.CylindricalAccuracyGrades)

        @property
        def iso1328_accuracy_grades(
            self: "AccuracyGrades._Cast_AccuracyGrades",
        ) -> "_1150.ISO1328AccuracyGrades":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1150,
            )

            return self._parent._cast(_1150.ISO1328AccuracyGrades)

        @property
        def agma_gleason_conical_accuracy_grades(
            self: "AccuracyGrades._Cast_AccuracyGrades",
        ) -> "_1198.AGMAGleasonConicalAccuracyGrades":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1198

            return self._parent._cast(_1198.AGMAGleasonConicalAccuracyGrades)

        @property
        def accuracy_grades(
            self: "AccuracyGrades._Cast_AccuracyGrades",
        ) -> "AccuracyGrades":
            return self._parent

        def __getattr__(self: "AccuracyGrades._Cast_AccuracyGrades", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AccuracyGrades.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AccuracyGrades._Cast_AccuracyGrades":
        return self._Cast_AccuracyGrades(self)
