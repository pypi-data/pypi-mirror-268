"""CylindricalGearSetMicroGeometry"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1237
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry",
    "CylindricalGearSetMicroGeometry",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1032, _1045, _1016
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107, _1104
    from mastapy.gears.analysis import _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetMicroGeometry",)


Self = TypeVar("Self", bound="CylindricalGearSetMicroGeometry")


class CylindricalGearSetMicroGeometry(_1237.GearSetImplementationDetail):
    """CylindricalGearSetMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetMicroGeometry")

    class _Cast_CylindricalGearSetMicroGeometry:
        """Special nested class for casting CylindricalGearSetMicroGeometry to subclasses."""

        def __init__(
            self: "CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry",
            parent: "CylindricalGearSetMicroGeometry",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_detail(
            self: "CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry",
        ) -> "_1237.GearSetImplementationDetail":
            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry",
        ) -> "CylindricalGearSetMicroGeometry":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetMicroGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set_design(self: Self) -> "_1032.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_micro_geometries(
        self: Self,
    ) -> "List[_1107.CylindricalGearMicroGeometryBase]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryBase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_mesh_micro_geometries(
        self: Self,
    ) -> "List[_1104.CylindricalGearMeshMicroGeometry]":
        """List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMeshMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def duplicate(self: Self) -> "CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry"""
        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate_and_add_to(
        self: Self, gear_set_design: "_1032.CylindricalGearSetDesign"
    ) -> "CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Args:
            gear_set_design (mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign)
        """
        method_result = self.wrapped.DuplicateAndAddTo(
            gear_set_design.wrapped if gear_set_design else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def duplicate_specifying_separate_micro_geometry_for_each_planet(
        self: Self,
    ) -> "_1237.GearSetImplementationDetail":
        """mastapy.gears.analysis.GearSetImplementationDetail"""
        method_result = (
            self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachPlanet()
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate_specifying_separate_micro_geometry_for_each_planet_and_add_to(
        self: Self, gear_set_design: "_1045.CylindricalPlanetaryGearSetDesign"
    ) -> "_1237.GearSetImplementationDetail":
        """mastapy.gears.analysis.GearSetImplementationDetail

        Args:
            gear_set_design (mastapy.gears.gear_designs.cylindrical.CylindricalPlanetaryGearSetDesign)
        """
        method_result = (
            self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachPlanetAndAddTo(
                gear_set_design.wrapped if gear_set_design else None
            )
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def duplicate_specifying_separate_micro_geometry_for_each_tooth(
        self: Self,
    ) -> "CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry"""
        method_result = (
            self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachTooth()
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate_specifying_separate_micro_geometry_for_each_tooth_for(
        self: Self, gears: "List[_1016.CylindricalGearDesign]"
    ) -> "CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Args:
            gears (List[mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign])
        """
        gears = conversion.mp_to_pn_objects_in_dotnet_list(gears)
        method_result = (
            self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachToothFor(gears)
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetMicroGeometry._Cast_CylindricalGearSetMicroGeometry":
        return self._Cast_CylindricalGearSetMicroGeometry(self)
