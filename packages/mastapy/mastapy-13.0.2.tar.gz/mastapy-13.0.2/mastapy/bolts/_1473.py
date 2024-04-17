"""BoltedJointMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.materials import _272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MATERIAL = python_net_import("SMT.MastaAPI.Bolts", "BoltedJointMaterial")

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.bolts import _1477
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointMaterial",)


Self = TypeVar("Self", bound="BoltedJointMaterial")


class BoltedJointMaterial(_272.Material):
    """BoltedJointMaterial

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointMaterial")

    class _Cast_BoltedJointMaterial:
        """Special nested class for casting BoltedJointMaterial to subclasses."""

        def __init__(
            self: "BoltedJointMaterial._Cast_BoltedJointMaterial",
            parent: "BoltedJointMaterial",
        ):
            self._parent = parent

        @property
        def material(
            self: "BoltedJointMaterial._Cast_BoltedJointMaterial",
        ) -> "_272.Material":
            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "BoltedJointMaterial._Cast_BoltedJointMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def bolt_material(
            self: "BoltedJointMaterial._Cast_BoltedJointMaterial",
        ) -> "_1477.BoltMaterial":
            from mastapy.bolts import _1477

            return self._parent._cast(_1477.BoltMaterial)

        @property
        def bolted_joint_material(
            self: "BoltedJointMaterial._Cast_BoltedJointMaterial",
        ) -> "BoltedJointMaterial":
            return self._parent

        def __getattr__(
            self: "BoltedJointMaterial._Cast_BoltedJointMaterial", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_thermal_expansion_at_20c(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfThermalExpansionAt20C

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_thermal_expansion_at_20c.setter
    @enforce_parameter_types
    def coefficient_of_thermal_expansion_at_20c(self: Self, value: "float"):
        self.wrapped.CoefficientOfThermalExpansionAt20C = (
            float(value) if value is not None else 0.0
        )

    @property
    def limiting_surface_pressure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LimitingSurfacePressure

        if temp is None:
            return 0.0

        return temp

    @limiting_surface_pressure.setter
    @enforce_parameter_types
    def limiting_surface_pressure(self: Self, value: "float"):
        self.wrapped.LimitingSurfacePressure = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_tensile_strength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumTensileStrength

        if temp is None:
            return 0.0

        return temp

    @minimum_tensile_strength.setter
    @enforce_parameter_types
    def minimum_tensile_strength(self: Self, value: "float"):
        self.wrapped.MinimumTensileStrength = float(value) if value is not None else 0.0

    @property
    def modulus_of_elasticity_at_20c(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModulusOfElasticityAt20C

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity_at_20c.setter
    @enforce_parameter_types
    def modulus_of_elasticity_at_20c(self: Self, value: "float"):
        self.wrapped.ModulusOfElasticityAt20C = (
            float(value) if value is not None else 0.0
        )

    @property
    def proof_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProofStress

        if temp is None:
            return 0.0

        return temp

    @proof_stress.setter
    @enforce_parameter_types
    def proof_stress(self: Self, value: "float"):
        self.wrapped.ProofStress = float(value) if value is not None else 0.0

    @property
    def shearing_strength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShearingStrength

        if temp is None:
            return 0.0

        return temp

    @shearing_strength.setter
    @enforce_parameter_types
    def shearing_strength(self: Self, value: "float"):
        self.wrapped.ShearingStrength = float(value) if value is not None else 0.0

    @property
    def stress_endurance_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StressEnduranceLimit

        if temp is None:
            return 0.0

        return temp

    @stress_endurance_limit.setter
    @enforce_parameter_types
    def stress_endurance_limit(self: Self, value: "float"):
        self.wrapped.StressEnduranceLimit = float(value) if value is not None else 0.0

    @property
    def temperature_dependent_coefficient_of_thermal_expansion(
        self: Self,
    ) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TemperatureDependentCoefficientOfThermalExpansion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @temperature_dependent_coefficient_of_thermal_expansion.setter
    @enforce_parameter_types
    def temperature_dependent_coefficient_of_thermal_expansion(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.TemperatureDependentCoefficientOfThermalExpansion = value.wrapped

    @property
    def temperature_dependent_youngs_moduli(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.TemperatureDependentYoungsModuli

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @temperature_dependent_youngs_moduli.setter
    @enforce_parameter_types
    def temperature_dependent_youngs_moduli(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.TemperatureDependentYoungsModuli = value.wrapped

    @property
    def cast_to(self: Self) -> "BoltedJointMaterial._Cast_BoltedJointMaterial":
        return self._Cast_BoltedJointMaterial(self)
