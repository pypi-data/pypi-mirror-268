"""LoadedRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.bearings.bearing_results.rolling import _2021
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerBearingElement"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _2074,
        _1995,
        _2000,
        _2003,
        _2011,
        _2015,
        _2027,
        _2034,
        _2045,
        _2046,
        _2052,
        _2054,
        _2063,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedRollerBearingElement")


class LoadedRollerBearingElement(_2021.LoadedElement):
    """LoadedRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerBearingElement")

    class _Cast_LoadedRollerBearingElement:
        """Special nested class for casting LoadedRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
            parent: "LoadedRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2021.LoadedElement":
            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_asymmetric_spherical_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_1995.LoadedAsymmetricSphericalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _1995

            return self._parent._cast(
                _1995.LoadedAsymmetricSphericalRollerBearingElement
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2000.LoadedAxialThrustCylindricalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2000

            return self._parent._cast(
                _2000.LoadedAxialThrustCylindricalRollerBearingElement
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2003.LoadedAxialThrustNeedleRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2003

            return self._parent._cast(_2003.LoadedAxialThrustNeedleRollerBearingElement)

        @property
        def loaded_crossed_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2011.LoadedCrossedRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2011

            return self._parent._cast(_2011.LoadedCrossedRollerBearingElement)

        @property
        def loaded_cylindrical_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2015.LoadedCylindricalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_needle_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2027.LoadedNeedleRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedNeedleRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2034.LoadedNonBarrelRollerElement":
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedNonBarrelRollerElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2045.LoadedSphericalRadialRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2045

            return self._parent._cast(_2045.LoadedSphericalRadialRollerBearingElement)

        @property
        def loaded_spherical_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2046.LoadedSphericalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2046

            return self._parent._cast(_2046.LoadedSphericalRollerBearingElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2052.LoadedSphericalThrustRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2052

            return self._parent._cast(_2052.LoadedSphericalThrustRollerBearingElement)

        @property
        def loaded_taper_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2054.LoadedTaperRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedTaperRollerBearingElement)

        @property
        def loaded_toroidal_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "_2063.LoadedToroidalRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2063

            return self._parent._cast(_2063.LoadedToroidalRollerBearingElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
        ) -> "LoadedRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerBearingElement.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_length_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLengthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_length_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactLengthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_tilt(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ElementTilt

        if temp is None:
            return 0.0

        return temp

    @element_tilt.setter
    @enforce_parameter_types
    def element_tilt(self: Self, value: "float"):
        self.wrapped.ElementTilt = float(value) if value is not None else 0.0

    @property
    def maximum_contact_width_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_width_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_depth_of_maximum_shear_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDepthOfMaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_depth_of_maximum_shear_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumDepthOfMaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalEdgeStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalEdgeStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def rib_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def results_at_roller_offsets(self: Self) -> "List[_2074.ResultsAtRollerOffset]":
        """List[mastapy.bearings.bearing_results.rolling.ResultsAtRollerOffset]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsAtRollerOffsets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollerBearingElement._Cast_LoadedRollerBearingElement":
        return self._Cast_LoadedRollerBearingElement(self)
