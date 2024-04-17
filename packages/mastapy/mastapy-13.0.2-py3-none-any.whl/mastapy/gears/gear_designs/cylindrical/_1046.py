"""CylindricalPlanetGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1016
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalPlanetGearDesign"
)

if TYPE_CHECKING:
    from mastapy.geometry.two_d import _315
    from mastapy.gears import _343
    from mastapy.gears.gear_designs.cylindrical import _1069, _1070
    from mastapy.gears.gear_designs import _951, _952


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearDesign",)


Self = TypeVar("Self", bound="CylindricalPlanetGearDesign")


class CylindricalPlanetGearDesign(_1016.CylindricalGearDesign):
    """CylindricalPlanetGearDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearDesign")

    class _Cast_CylindricalPlanetGearDesign:
        """Special nested class for casting CylindricalPlanetGearDesign to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign",
            parent: "CylindricalPlanetGearDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_design(
            self: "CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign",
        ) -> "_1016.CylindricalGearDesign":
            return self._parent._cast(_1016.CylindricalGearDesign)

        @property
        def gear_design(
            self: "CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign",
        ) -> "_951.GearDesign":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.GearDesign)

        @property
        def gear_design_component(
            self: "CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def cylindrical_planet_gear_design(
            self: "CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign",
        ) -> "CylindricalPlanetGearDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalPlanetGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_factorising_annulus(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasFactorisingAnnulus

        if temp is None:
            return False

        return temp

    @property
    def has_factorising_sun(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasFactorisingSun

        if temp is None:
            return False

        return temp

    @property
    def internal_external(self: Self) -> "_315.InternalExternalType":
        """mastapy.geometry.two_d.InternalExternalType"""
        temp = self.wrapped.InternalExternal

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Geometry.TwoD.InternalExternalType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.geometry.two_d._315", "InternalExternalType"
        )(value)

    @internal_external.setter
    @enforce_parameter_types
    def internal_external(self: Self, value: "_315.InternalExternalType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Geometry.TwoD.InternalExternalType"
        )
        self.wrapped.InternalExternal = value

    @property
    def suggested_maximum_number_of_planets(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuggestedMaximumNumberOfPlanets

        if temp is None:
            return 0

        return temp

    @property
    def planetary_details(self: Self) -> "_343.PlanetaryDetail":
        """mastapy.gears.PlanetaryDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planet_assembly_indices(self: Self) -> "List[_1069.NamedPlanetAssemblyIndex]":
        """List[mastapy.gears.gear_designs.cylindrical.NamedPlanetAssemblyIndex]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetAssemblyIndices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetary_sidebands_amplitude_factors(
        self: Self,
    ) -> "List[_1070.NamedPlanetSideBandAmplitudeFactor]":
        """List[mastapy.gears.gear_designs.cylindrical.NamedPlanetSideBandAmplitudeFactor]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetarySidebandsAmplitudeFactors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearDesign._Cast_CylindricalPlanetGearDesign":
        return self._Cast_CylindricalPlanetGearDesign(self)
