"""ConicalGearFlankMicroGeometry"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.micro_geometry import _573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FLANK_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry",
    "ConicalGearFlankMicroGeometry",
)

if TYPE_CHECKING:
    from mastapy.gears import _339
    from mastapy.gears.gear_designs.conical.micro_geometry import _1178, _1180, _1181
    from mastapy.gears.gear_designs.conical import _1160


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearFlankMicroGeometry",)


Self = TypeVar("Self", bound="ConicalGearFlankMicroGeometry")


class ConicalGearFlankMicroGeometry(_573.FlankMicroGeometry):
    """ConicalGearFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_FLANK_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearFlankMicroGeometry")

    class _Cast_ConicalGearFlankMicroGeometry:
        """Special nested class for casting ConicalGearFlankMicroGeometry to subclasses."""

        def __init__(
            self: "ConicalGearFlankMicroGeometry._Cast_ConicalGearFlankMicroGeometry",
            parent: "ConicalGearFlankMicroGeometry",
        ):
            self._parent = parent

        @property
        def flank_micro_geometry(
            self: "ConicalGearFlankMicroGeometry._Cast_ConicalGearFlankMicroGeometry",
        ) -> "_573.FlankMicroGeometry":
            return self._parent._cast(_573.FlankMicroGeometry)

        @property
        def conical_gear_flank_micro_geometry(
            self: "ConicalGearFlankMicroGeometry._Cast_ConicalGearFlankMicroGeometry",
        ) -> "ConicalGearFlankMicroGeometry":
            return self._parent

        def __getattr__(
            self: "ConicalGearFlankMicroGeometry._Cast_ConicalGearFlankMicroGeometry",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearFlankMicroGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_input_type(self: Self) -> "_339.MicroGeometryInputTypes":
        """mastapy.gears.MicroGeometryInputTypes"""
        temp = self.wrapped.MicroGeometryInputType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.MicroGeometryInputTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._339", "MicroGeometryInputTypes"
        )(value)

    @micro_geometry_input_type.setter
    @enforce_parameter_types
    def micro_geometry_input_type(self: Self, value: "_339.MicroGeometryInputTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.MicroGeometryInputTypes"
        )
        self.wrapped.MicroGeometryInputType = value

    @property
    def bias(self: Self) -> "_1178.ConicalGearBiasModification":
        """mastapy.gears.gear_designs.conical.micro_geometry.ConicalGearBiasModification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bias

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_relief(self: Self) -> "_1180.ConicalGearLeadModification":
        """mastapy.gears.gear_designs.conical.micro_geometry.ConicalGearLeadModification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_relief(self: Self) -> "_1181.ConicalGearProfileModification":
        """mastapy.gears.gear_designs.conical.micro_geometry.ConicalGearProfileModification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_design(self: Self) -> "_1160.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearFlankMicroGeometry._Cast_ConicalGearFlankMicroGeometry":
        return self._Cast_ConicalGearFlankMicroGeometry(self)
