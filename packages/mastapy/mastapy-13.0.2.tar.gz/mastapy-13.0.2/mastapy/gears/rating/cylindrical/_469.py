"""CylindricalMeshDutyCycleRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _368
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalMeshDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _461
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshDutyCycleRating",)


Self = TypeVar("Self", bound="CylindricalMeshDutyCycleRating")


class CylindricalMeshDutyCycleRating(_368.MeshDutyCycleRating):
    """CylindricalMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalMeshDutyCycleRating")

    class _Cast_CylindricalMeshDutyCycleRating:
        """Special nested class for casting CylindricalMeshDutyCycleRating to subclasses."""

        def __init__(
            self: "CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating",
            parent: "CylindricalMeshDutyCycleRating",
        ):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(
            self: "CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating",
        ) -> "_368.MeshDutyCycleRating":
            return self._parent._cast(_368.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(
            self: "CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating",
        ) -> "CylindricalMeshDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalMeshDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_nominal_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNominalAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_nominal_tangential_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNominalTangentialLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_radial_separating_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumRadialSeparatingLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicropittingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_deformation_safety_factor_step_1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermanentDeformationSafetyFactorStep1

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_deformation_safety_factor_step_2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermanentDeformationSafetyFactorStep2

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_load_safety_factor_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingLoadSafetyFactorIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_flash_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_integral_temperature_method(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ScuffingSafetyFactorIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def highest_torque_load_case(self: Self) -> "_461.CylindricalGearMeshRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestTorqueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_mesh_ratings(self: Self) -> "List[_461.CylindricalGearMeshRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def loaded_cylindrical_mesh_ratings(
        self: Self,
    ) -> "List[_461.CylindricalGearMeshRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedCylindricalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating":
        return self._Cast_CylindricalMeshDutyCycleRating(self)
