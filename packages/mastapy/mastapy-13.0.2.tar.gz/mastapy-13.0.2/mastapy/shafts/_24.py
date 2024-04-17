"""ShaftMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.materials import _272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MATERIAL = python_net_import("SMT.MastaAPI.Shafts", "ShaftMaterial")

if TYPE_CHECKING:
    from mastapy.shafts import _6
    from mastapy.materials import _251
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("ShaftMaterial",)


Self = TypeVar("Self", bound="ShaftMaterial")


class ShaftMaterial(_272.Material):
    """ShaftMaterial

    This is a mastapy class.
    """

    TYPE = _SHAFT_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftMaterial")

    class _Cast_ShaftMaterial:
        """Special nested class for casting ShaftMaterial to subclasses."""

        def __init__(
            self: "ShaftMaterial._Cast_ShaftMaterial", parent: "ShaftMaterial"
        ):
            self._parent = parent

        @property
        def material(self: "ShaftMaterial._Cast_ShaftMaterial") -> "_272.Material":
            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "ShaftMaterial._Cast_ShaftMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def shaft_material(
            self: "ShaftMaterial._Cast_ShaftMaterial",
        ) -> "ShaftMaterial":
            return self._parent

        def __getattr__(self: "ShaftMaterial._Cast_ShaftMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hardening_type_for_agma60016101e08(self: Self) -> "_6.AGMAHardeningType":
        """mastapy.shafts.AGMAHardeningType"""
        temp = self.wrapped.HardeningTypeForAGMA60016101E08

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Shafts.AGMAHardeningType")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.shafts._6", "AGMAHardeningType")(
            value
        )

    @hardening_type_for_agma60016101e08.setter
    @enforce_parameter_types
    def hardening_type_for_agma60016101e08(self: Self, value: "_6.AGMAHardeningType"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Shafts.AGMAHardeningType")
        self.wrapped.HardeningTypeForAGMA60016101E08 = value

    @property
    def specified_endurance_limit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecifiedEnduranceLimit

        if temp is None:
            return 0.0

        return temp

    @specified_endurance_limit.setter
    @enforce_parameter_types
    def specified_endurance_limit(self: Self, value: "float"):
        self.wrapped.SpecifiedEnduranceLimit = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_custom_sn_curve(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCustomSNCurve

        if temp is None:
            return False

        return temp

    @use_custom_sn_curve.setter
    @enforce_parameter_types
    def use_custom_sn_curve(self: Self, value: "bool"):
        self.wrapped.UseCustomSNCurve = bool(value) if value is not None else False

    @property
    def bh_curve_specification(self: Self) -> "_251.BHCurveSpecification":
        """mastapy.materials.BHCurveSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BHCurveSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ShaftMaterial._Cast_ShaftMaterial":
        return self._Cast_ShaftMaterial(self)
