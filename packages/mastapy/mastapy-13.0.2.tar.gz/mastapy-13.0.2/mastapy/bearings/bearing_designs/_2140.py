"""LinearBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs import _2137
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "LinearBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1889


__docformat__ = "restructuredtext en"
__all__ = ("LinearBearing",)


Self = TypeVar("Self", bound="LinearBearing")


class LinearBearing(_2137.BearingDesign):
    """LinearBearing

    This is a mastapy class.
    """

    TYPE = _LINEAR_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearBearing")

    class _Cast_LinearBearing:
        """Special nested class for casting LinearBearing to subclasses."""

        def __init__(
            self: "LinearBearing._Cast_LinearBearing", parent: "LinearBearing"
        ):
            self._parent = parent

        @property
        def bearing_design(
            self: "LinearBearing._Cast_LinearBearing",
        ) -> "_2137.BearingDesign":
            return self._parent._cast(_2137.BearingDesign)

        @property
        def linear_bearing(
            self: "LinearBearing._Cast_LinearBearing",
        ) -> "LinearBearing":
            return self._parent

        def __getattr__(self: "LinearBearing._Cast_LinearBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness.setter
    @enforce_parameter_types
    def axial_stiffness(self: Self, value: "float"):
        self.wrapped.AxialStiffness = float(value) if value is not None else 0.0

    @property
    def bore(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "float"):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def radial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness.setter
    @enforce_parameter_types
    def radial_stiffness(self: Self, value: "float"):
        self.wrapped.RadialStiffness = float(value) if value is not None else 0.0

    @property
    def stiffness_options(self: Self) -> "_1889.BearingStiffnessMatrixOption":
        """mastapy.bearings.BearingStiffnessMatrixOption"""
        temp = self.wrapped.StiffnessOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingStiffnessMatrixOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1889", "BearingStiffnessMatrixOption"
        )(value)

    @stiffness_options.setter
    @enforce_parameter_types
    def stiffness_options(self: Self, value: "_1889.BearingStiffnessMatrixOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingStiffnessMatrixOption"
        )
        self.wrapped.StiffnessOptions = value

    @property
    def tilt_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness.setter
    @enforce_parameter_types
    def tilt_stiffness(self: Self, value: "float"):
        self.wrapped.TiltStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "LinearBearing._Cast_LinearBearing":
        return self._Cast_LinearBearing(self)
