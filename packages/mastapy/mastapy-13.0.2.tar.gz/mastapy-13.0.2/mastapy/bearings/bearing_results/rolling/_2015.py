"""LoadedCylindricalRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedCylindricalRollerBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2027, _2035, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCylindricalRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedCylindricalRollerBearingElement")


class LoadedCylindricalRollerBearingElement(_2034.LoadedNonBarrelRollerElement):
    """LoadedCylindricalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_CYLINDRICAL_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedCylindricalRollerBearingElement"
    )

    class _Cast_LoadedCylindricalRollerBearingElement:
        """Special nested class for casting LoadedCylindricalRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
            parent: "LoadedCylindricalRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_element(
            self: "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
        ) -> "_2034.LoadedNonBarrelRollerElement":
            return self._parent._cast(_2034.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
        ) -> "_2035.LoadedRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_needle_roller_bearing_element(
            self: "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
        ) -> "_2027.LoadedNeedleRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedNeedleRollerBearingElement)

        @property
        def loaded_cylindrical_roller_bearing_element(
            self: "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
        ) -> "LoadedCylindricalRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement",
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
        self: Self, instance_to_wrap: "LoadedCylindricalRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height_of_rib_roller_contact_above_race_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightOfRibRollerContactAboveRaceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRibStressOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedCylindricalRollerBearingElement._Cast_LoadedCylindricalRollerBearingElement":
        return self._Cast_LoadedCylindricalRollerBearingElement(self)
