"""MicroGeometryInputsProfile"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical import _636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS_PROFILE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "MicroGeometryInputsProfile"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1496


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryInputsProfile",)


Self = TypeVar("Self", bound="MicroGeometryInputsProfile")


class MicroGeometryInputsProfile(
    _636.MicroGeometryInputs["_640.ProfileModificationSegment"]
):
    """MicroGeometryInputsProfile

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_INPUTS_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MicroGeometryInputsProfile")

    class _Cast_MicroGeometryInputsProfile:
        """Special nested class for casting MicroGeometryInputsProfile to subclasses."""

        def __init__(
            self: "MicroGeometryInputsProfile._Cast_MicroGeometryInputsProfile",
            parent: "MicroGeometryInputsProfile",
        ):
            self._parent = parent

        @property
        def micro_geometry_inputs(
            self: "MicroGeometryInputsProfile._Cast_MicroGeometryInputsProfile",
        ) -> "_636.MicroGeometryInputs":
            return self._parent._cast(_636.MicroGeometryInputs)

        @property
        def micro_geometry_inputs_profile(
            self: "MicroGeometryInputsProfile._Cast_MicroGeometryInputsProfile",
        ) -> "MicroGeometryInputsProfile":
            return self._parent

        def __getattr__(
            self: "MicroGeometryInputsProfile._Cast_MicroGeometryInputsProfile",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MicroGeometryInputsProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_profile_segments(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfProfileSegments

        if temp is None:
            return 0

        return temp

    @number_of_profile_segments.setter
    @enforce_parameter_types
    def number_of_profile_segments(self: Self, value: "int"):
        self.wrapped.NumberOfProfileSegments = int(value) if value is not None else 0

    @property
    def profile_micro_geometry_range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileMicroGeometryRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def z_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ZPlane

        if temp is None:
            return 0.0

        return temp

    @z_plane.setter
    @enforce_parameter_types
    def z_plane(self: Self, value: "float"):
        self.wrapped.ZPlane = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryInputsProfile._Cast_MicroGeometryInputsProfile":
        return self._Cast_MicroGeometryInputsProfile(self)
