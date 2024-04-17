"""ConicalGearCutter"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CUTTER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalGearCutter"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1167, _1168, _1177, _1176, _1169
    from mastapy.gears.manufacturing.bevel.cutters import _816, _817, _818, _819


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCutter",)


Self = TypeVar("Self", bound="ConicalGearCutter")


class ConicalGearCutter(_0.APIBase):
    """ConicalGearCutter

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CUTTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCutter")

    class _Cast_ConicalGearCutter:
        """Special nested class for casting ConicalGearCutter to subclasses."""

        def __init__(
            self: "ConicalGearCutter._Cast_ConicalGearCutter",
            parent: "ConicalGearCutter",
        ):
            self._parent = parent

        @property
        def pinion_finish_cutter(
            self: "ConicalGearCutter._Cast_ConicalGearCutter",
        ) -> "_816.PinionFinishCutter":
            from mastapy.gears.manufacturing.bevel.cutters import _816

            return self._parent._cast(_816.PinionFinishCutter)

        @property
        def pinion_rough_cutter(
            self: "ConicalGearCutter._Cast_ConicalGearCutter",
        ) -> "_817.PinionRoughCutter":
            from mastapy.gears.manufacturing.bevel.cutters import _817

            return self._parent._cast(_817.PinionRoughCutter)

        @property
        def wheel_finish_cutter(
            self: "ConicalGearCutter._Cast_ConicalGearCutter",
        ) -> "_818.WheelFinishCutter":
            from mastapy.gears.manufacturing.bevel.cutters import _818

            return self._parent._cast(_818.WheelFinishCutter)

        @property
        def wheel_rough_cutter(
            self: "ConicalGearCutter._Cast_ConicalGearCutter",
        ) -> "_819.WheelRoughCutter":
            from mastapy.gears.manufacturing.bevel.cutters import _819

            return self._parent._cast(_819.WheelRoughCutter)

        @property
        def dummy_conical_gear_cutter(
            self: "ConicalGearCutter._Cast_ConicalGearCutter",
        ) -> "_1169.DummyConicalGearCutter":
            from mastapy.gears.gear_designs.conical import _1169

            return self._parent._cast(_1169.DummyConicalGearCutter)

        @property
        def conical_gear_cutter(
            self: "ConicalGearCutter._Cast_ConicalGearCutter",
        ) -> "ConicalGearCutter":
            return self._parent

        def __getattr__(self: "ConicalGearCutter._Cast_ConicalGearCutter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearCutter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_point_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedPointWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_blade_type(self: Self) -> "_1167.CutterBladeType":
        """mastapy.gears.gear_designs.conical.CutterBladeType"""
        temp = self.wrapped.CutterBladeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.CutterBladeType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1167", "CutterBladeType"
        )(value)

    @cutter_blade_type.setter
    @enforce_parameter_types
    def cutter_blade_type(self: Self, value: "_1167.CutterBladeType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.CutterBladeType"
        )
        self.wrapped.CutterBladeType = value

    @property
    def cutter_gauge_length(self: Self) -> "_1168.CutterGaugeLengths":
        """mastapy.gears.gear_designs.conical.CutterGaugeLengths"""
        temp = self.wrapped.CutterGaugeLength

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.CutterGaugeLengths"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1168", "CutterGaugeLengths"
        )(value)

    @cutter_gauge_length.setter
    @enforce_parameter_types
    def cutter_gauge_length(self: Self, value: "_1168.CutterGaugeLengths"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.CutterGaugeLengths"
        )
        self.wrapped.CutterGaugeLength = value

    @property
    def inner_blade_angle_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerBladeAngleConvex

        if temp is None:
            return 0.0

        return temp

    @inner_blade_angle_convex.setter
    @enforce_parameter_types
    def inner_blade_angle_convex(self: Self, value: "float"):
        self.wrapped.InnerBladeAngleConvex = float(value) if value is not None else 0.0

    @property
    def inner_blade_point_radius_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerBladePointRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_blade_point_radius_convex.setter
    @enforce_parameter_types
    def inner_blade_point_radius_convex(self: Self, value: "float"):
        self.wrapped.InnerBladePointRadiusConvex = (
            float(value) if value is not None else 0.0
        )

    @property
    def inner_edge_radius_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerEdgeRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_edge_radius_convex.setter
    @enforce_parameter_types
    def inner_edge_radius_convex(self: Self, value: "float"):
        self.wrapped.InnerEdgeRadiusConvex = float(value) if value is not None else 0.0

    @property
    def inner_parabolic_apex_location_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerParabolicApexLocationConvex

        if temp is None:
            return 0.0

        return temp

    @inner_parabolic_apex_location_convex.setter
    @enforce_parameter_types
    def inner_parabolic_apex_location_convex(self: Self, value: "float"):
        self.wrapped.InnerParabolicApexLocationConvex = (
            float(value) if value is not None else 0.0
        )

    @property
    def inner_parabolic_coefficient_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerParabolicCoefficientConvex

        if temp is None:
            return 0.0

        return temp

    @inner_parabolic_coefficient_convex.setter
    @enforce_parameter_types
    def inner_parabolic_coefficient_convex(self: Self, value: "float"):
        self.wrapped.InnerParabolicCoefficientConvex = (
            float(value) if value is not None else 0.0
        )

    @property
    def inner_spherical_radius_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerSphericalRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_spherical_radius_convex.setter
    @enforce_parameter_types
    def inner_spherical_radius_convex(self: Self, value: "float"):
        self.wrapped.InnerSphericalRadiusConvex = (
            float(value) if value is not None else 0.0
        )

    @property
    def inner_toprem_angle_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerTopremAngleConvex

        if temp is None:
            return 0.0

        return temp

    @inner_toprem_angle_convex.setter
    @enforce_parameter_types
    def inner_toprem_angle_convex(self: Self, value: "float"):
        self.wrapped.InnerTopremAngleConvex = float(value) if value is not None else 0.0

    @property
    def inner_toprem_length_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerTopremLengthConvex

        if temp is None:
            return 0.0

        return temp

    @inner_toprem_length_convex.setter
    @enforce_parameter_types
    def inner_toprem_length_convex(self: Self, value: "float"):
        self.wrapped.InnerTopremLengthConvex = (
            float(value) if value is not None else 0.0
        )

    @property
    def inner_toprem_letter_convex(self: Self) -> "_1177.TopremLetter":
        """mastapy.gears.gear_designs.conical.TopremLetter"""
        temp = self.wrapped.InnerTopremLetterConvex

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.TopremLetter"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1177", "TopremLetter"
        )(value)

    @inner_toprem_letter_convex.setter
    @enforce_parameter_types
    def inner_toprem_letter_convex(self: Self, value: "_1177.TopremLetter"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.TopremLetter"
        )
        self.wrapped.InnerTopremLetterConvex = value

    @property
    def input_toprem_as(self: Self) -> "_1176.TopremEntryType":
        """mastapy.gears.gear_designs.conical.TopremEntryType"""
        temp = self.wrapped.InputTopremAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.TopremEntryType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1176", "TopremEntryType"
        )(value)

    @input_toprem_as.setter
    @enforce_parameter_types
    def input_toprem_as(self: Self, value: "_1176.TopremEntryType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.TopremEntryType"
        )
        self.wrapped.InputTopremAs = value

    @property
    def outer_blade_angle_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterBladeAngleConcave

        if temp is None:
            return 0.0

        return temp

    @outer_blade_angle_concave.setter
    @enforce_parameter_types
    def outer_blade_angle_concave(self: Self, value: "float"):
        self.wrapped.OuterBladeAngleConcave = float(value) if value is not None else 0.0

    @property
    def outer_blade_point_radius_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterBladePointRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_blade_point_radius_concave.setter
    @enforce_parameter_types
    def outer_blade_point_radius_concave(self: Self, value: "float"):
        self.wrapped.OuterBladePointRadiusConcave = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_edge_radius_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterEdgeRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_edge_radius_concave.setter
    @enforce_parameter_types
    def outer_edge_radius_concave(self: Self, value: "float"):
        self.wrapped.OuterEdgeRadiusConcave = float(value) if value is not None else 0.0

    @property
    def outer_parabolic_apex_location_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterParabolicApexLocationConcave

        if temp is None:
            return 0.0

        return temp

    @outer_parabolic_apex_location_concave.setter
    @enforce_parameter_types
    def outer_parabolic_apex_location_concave(self: Self, value: "float"):
        self.wrapped.OuterParabolicApexLocationConcave = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_parabolic_coefficient_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterParabolicCoefficientConcave

        if temp is None:
            return 0.0

        return temp

    @outer_parabolic_coefficient_concave.setter
    @enforce_parameter_types
    def outer_parabolic_coefficient_concave(self: Self, value: "float"):
        self.wrapped.OuterParabolicCoefficientConcave = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_spherical_radius_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterSphericalRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_spherical_radius_concave.setter
    @enforce_parameter_types
    def outer_spherical_radius_concave(self: Self, value: "float"):
        self.wrapped.OuterSphericalRadiusConcave = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_toprem_angle_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterTopremAngleConcave

        if temp is None:
            return 0.0

        return temp

    @outer_toprem_angle_concave.setter
    @enforce_parameter_types
    def outer_toprem_angle_concave(self: Self, value: "float"):
        self.wrapped.OuterTopremAngleConcave = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_toprem_length_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterTopremLengthConcave

        if temp is None:
            return 0.0

        return temp

    @outer_toprem_length_concave.setter
    @enforce_parameter_types
    def outer_toprem_length_concave(self: Self, value: "float"):
        self.wrapped.OuterTopremLengthConcave = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_toprem_letter_concave(self: Self) -> "_1177.TopremLetter":
        """mastapy.gears.gear_designs.conical.TopremLetter"""
        temp = self.wrapped.OuterTopremLetterConcave

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.TopremLetter"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1177", "TopremLetter"
        )(value)

    @outer_toprem_letter_concave.setter
    @enforce_parameter_types
    def outer_toprem_letter_concave(self: Self, value: "_1177.TopremLetter"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.TopremLetter"
        )
        self.wrapped.OuterTopremLetterConcave = value

    @property
    def protuberance_at_concave_blade(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceAtConcaveBlade

        if temp is None:
            return 0.0

        return temp

    @protuberance_at_concave_blade.setter
    @enforce_parameter_types
    def protuberance_at_concave_blade(self: Self, value: "float"):
        self.wrapped.ProtuberanceAtConcaveBlade = (
            float(value) if value is not None else 0.0
        )

    @property
    def protuberance_at_convex_blade(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProtuberanceAtConvexBlade

        if temp is None:
            return 0.0

        return temp

    @protuberance_at_convex_blade.setter
    @enforce_parameter_types
    def protuberance_at_convex_blade(self: Self, value: "float"):
        self.wrapped.ProtuberanceAtConvexBlade = (
            float(value) if value is not None else 0.0
        )

    @property
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConicalGearCutter._Cast_ConicalGearCutter":
        return self._Cast_ConicalGearCutter(self)
