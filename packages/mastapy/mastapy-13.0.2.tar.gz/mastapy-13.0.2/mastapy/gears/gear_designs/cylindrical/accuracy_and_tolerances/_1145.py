"""CylindricalGearAccuracyTolerances"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ACCURACY_TOLERANCES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "CylindricalGearAccuracyTolerances",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1138,
        _1139,
        _1141,
        _1147,
        _1148,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAccuracyTolerances",)


Self = TypeVar("Self", bound="CylindricalGearAccuracyTolerances")


class CylindricalGearAccuracyTolerances(_0.APIBase):
    """CylindricalGearAccuracyTolerances

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ACCURACY_TOLERANCES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearAccuracyTolerances")

    class _Cast_CylindricalGearAccuracyTolerances:
        """Special nested class for casting CylindricalGearAccuracyTolerances to subclasses."""

        def __init__(
            self: "CylindricalGearAccuracyTolerances._Cast_CylindricalGearAccuracyTolerances",
            parent: "CylindricalGearAccuracyTolerances",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_accuracy_tolerances(
            self: "CylindricalGearAccuracyTolerances._Cast_CylindricalGearAccuracyTolerances",
        ) -> "CylindricalGearAccuracyTolerances":
            return self._parent

        def __getattr__(
            self: "CylindricalGearAccuracyTolerances._Cast_CylindricalGearAccuracyTolerances",
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
        self: Self, instance_to_wrap: "CylindricalGearAccuracyTolerances.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def agma2000_gear_accuracy_tolerances(
        self: Self,
    ) -> "_1138.AGMA2000A88AccuracyGrader":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.AGMA2000A88AccuracyGrader

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMA2000GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma2015_gear_accuracy_tolerances(
        self: Self,
    ) -> "_1139.AGMA20151A01AccuracyGrader":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.AGMA20151A01AccuracyGrader

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMA2015GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agmaiso13281_gear_accuracy_tolerances(
        self: Self,
    ) -> "_1141.AGMAISO13281B14AccuracyGrader":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.AGMAISO13281B14AccuracyGrader

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAISO13281GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso132811995_gear_accuracy_tolerances(
        self: Self,
    ) -> "_1147.ISO132811995AccuracyGrader":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.ISO132811995AccuracyGrader

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO132811995GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso132812013_gear_accuracy_tolerances(
        self: Self,
    ) -> "_1148.ISO132812013AccuracyGrader":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.ISO132812013AccuracyGrader

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO132812013GearAccuracyTolerances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearAccuracyTolerances._Cast_CylindricalGearAccuracyTolerances":
        return self._Cast_CylindricalGearAccuracyTolerances(self)
