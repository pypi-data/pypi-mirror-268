"""BoltMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.bolts import _1473
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_MATERIAL = python_net_import("SMT.MastaAPI.Bolts", "BoltMaterial")

if TYPE_CHECKING:
    from mastapy.bolts import _1492
    from mastapy.materials import _272
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("BoltMaterial",)


Self = TypeVar("Self", bound="BoltMaterial")


class BoltMaterial(_1473.BoltedJointMaterial):
    """BoltMaterial

    This is a mastapy class.
    """

    TYPE = _BOLT_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltMaterial")

    class _Cast_BoltMaterial:
        """Special nested class for casting BoltMaterial to subclasses."""

        def __init__(self: "BoltMaterial._Cast_BoltMaterial", parent: "BoltMaterial"):
            self._parent = parent

        @property
        def bolted_joint_material(
            self: "BoltMaterial._Cast_BoltMaterial",
        ) -> "_1473.BoltedJointMaterial":
            return self._parent._cast(_1473.BoltedJointMaterial)

        @property
        def material(self: "BoltMaterial._Cast_BoltMaterial") -> "_272.Material":
            from mastapy.materials import _272

            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "BoltMaterial._Cast_BoltMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def bolt_material(self: "BoltMaterial._Cast_BoltMaterial") -> "BoltMaterial":
            return self._parent

        def __getattr__(self: "BoltMaterial._Cast_BoltMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def strength_grade(self: Self) -> "_1492.StrengthGrades":
        """mastapy.bolts.StrengthGrades"""
        temp = self.wrapped.StrengthGrade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Bolts.StrengthGrades")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.bolts._1492", "StrengthGrades")(
            value
        )

    @strength_grade.setter
    @enforce_parameter_types
    def strength_grade(self: Self, value: "_1492.StrengthGrades"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Bolts.StrengthGrades")
        self.wrapped.StrengthGrade = value

    @property
    def cast_to(self: Self) -> "BoltMaterial._Cast_BoltMaterial":
        return self._Cast_BoltMaterial(self)
