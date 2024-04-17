"""WormDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.worm import _961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_DESIGN = python_net_import("SMT.MastaAPI.Gears.GearDesigns.Worm", "WormDesign")

if TYPE_CHECKING:
    from mastapy.gears import _353
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("WormDesign",)


Self = TypeVar("Self", bound="WormDesign")


class WormDesign(_961.WormGearDesign):
    """WormDesign

    This is a mastapy class.
    """

    TYPE = _WORM_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormDesign")

    class _Cast_WormDesign:
        """Special nested class for casting WormDesign to subclasses."""

        def __init__(self: "WormDesign._Cast_WormDesign", parent: "WormDesign"):
            self._parent = parent

        @property
        def worm_gear_design(
            self: "WormDesign._Cast_WormDesign",
        ) -> "_961.WormGearDesign":
            return self._parent._cast(_961.WormGearDesign)

        @property
        def gear_design(self: "WormDesign._Cast_WormDesign") -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "WormDesign._Cast_WormDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def worm_design(self: "WormDesign._Cast_WormDesign") -> "WormDesign":
            return self._parent

        def __getattr__(self: "WormDesign._Cast_WormDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Addendum

        if temp is None:
            return 0.0

        return temp

    @property
    def addendum_factor(self: Self) -> "_353.WormAddendumFactor":
        """mastapy.gears.WormAddendumFactor"""
        temp = self.wrapped.AddendumFactor

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.WormAddendumFactor")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._353", "WormAddendumFactor")(
            value
        )

    @addendum_factor.setter
    @enforce_parameter_types
    def addendum_factor(self: Self, value: "_353.WormAddendumFactor"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.WormAddendumFactor")
        self.wrapped.AddendumFactor = value

    @property
    def axial_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Clearance

        if temp is None:
            return 0.0

        return temp

    @property
    def clearance_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @clearance_factor.setter
    @enforce_parameter_types
    def clearance_factor(self: Self, value: "float"):
        self.wrapped.ClearanceFactor = float(value) if value is not None else 0.0

    @property
    def dedendum(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Dedendum

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DiameterFactor

        if temp is None:
            return 0.0

        return temp

    @diameter_factor.setter
    @enforce_parameter_types
    def diameter_factor(self: Self, value: "float"):
        self.wrapped.DiameterFactor = float(value) if value is not None else 0.0

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
    def fillet_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def fillet_radius_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FilletRadiusFactor

        if temp is None:
            return 0.0

        return temp

    @fillet_radius_factor.setter
    @enforce_parameter_types
    def fillet_radius_factor(self: Self, value: "float"):
        self.wrapped.FilletRadiusFactor = float(value) if value is not None else 0.0

    @property
    def lead(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Lead

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @reference_diameter.setter
    @enforce_parameter_types
    def reference_diameter(self: Self, value: "float"):
        self.wrapped.ReferenceDiameter = float(value) if value is not None else 0.0

    @property
    def reference_lead_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceLeadAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def working_depth_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingDepthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def working_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def working_pitch_lead_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingPitchLeadAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def worm_starts(self: Self) -> "int":
        """int"""
        temp = self.wrapped.WormStarts

        if temp is None:
            return 0

        return temp

    @worm_starts.setter
    @enforce_parameter_types
    def worm_starts(self: Self, value: "int"):
        self.wrapped.WormStarts = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "WormDesign._Cast_WormDesign":
        return self._Cast_WormDesign(self)
