"""SplineMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.materials import _272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_MATERIAL = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "SplineMaterial"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1405
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("SplineMaterial",)


Self = TypeVar("Self", bound="SplineMaterial")


class SplineMaterial(_272.Material):
    """SplineMaterial

    This is a mastapy class.
    """

    TYPE = _SPLINE_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplineMaterial")

    class _Cast_SplineMaterial:
        """Special nested class for casting SplineMaterial to subclasses."""

        def __init__(
            self: "SplineMaterial._Cast_SplineMaterial", parent: "SplineMaterial"
        ):
            self._parent = parent

        @property
        def material(self: "SplineMaterial._Cast_SplineMaterial") -> "_272.Material":
            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "SplineMaterial._Cast_SplineMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def spline_material(
            self: "SplineMaterial._Cast_SplineMaterial",
        ) -> "SplineMaterial":
            return self._parent

        def __getattr__(self: "SplineMaterial._Cast_SplineMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplineMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def core_hardness_h_rc(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoreHardnessHRc

        if temp is None:
            return 0.0

        return temp

    @core_hardness_h_rc.setter
    @enforce_parameter_types
    def core_hardness_h_rc(self: Self, value: "float"):
        self.wrapped.CoreHardnessHRc = float(value) if value is not None else 0.0

    @property
    def heat_treatment_type(self: Self) -> "_1405.HeatTreatmentTypes":
        """mastapy.detailed_rigid_connectors.splines.HeatTreatmentTypes"""
        temp = self.wrapped.HeatTreatmentType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.HeatTreatmentTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.splines._1405", "HeatTreatmentTypes"
        )(value)

    @heat_treatment_type.setter
    @enforce_parameter_types
    def heat_treatment_type(self: Self, value: "_1405.HeatTreatmentTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.HeatTreatmentTypes"
        )
        self.wrapped.HeatTreatmentType = value

    @property
    def cast_to(self: Self) -> "SplineMaterial._Cast_SplineMaterial":
        return self._Cast_SplineMaterial(self)
