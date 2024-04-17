"""FinishStockSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1073
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_STOCK_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash",
    "FinishStockSpecification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
        _1096,
    )
    from mastapy.gears.gear_designs.cylindrical import _1089


__docformat__ = "restructuredtext en"
__all__ = ("FinishStockSpecification",)


Self = TypeVar("Self", bound="FinishStockSpecification")


class FinishStockSpecification(
    _1073.RelativeValuesSpecification["FinishStockSpecification"]
):
    """FinishStockSpecification

    This is a mastapy class.
    """

    TYPE = _FINISH_STOCK_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FinishStockSpecification")

    class _Cast_FinishStockSpecification:
        """Special nested class for casting FinishStockSpecification to subclasses."""

        def __init__(
            self: "FinishStockSpecification._Cast_FinishStockSpecification",
            parent: "FinishStockSpecification",
        ):
            self._parent = parent

        @property
        def relative_values_specification(
            self: "FinishStockSpecification._Cast_FinishStockSpecification",
        ) -> "_1073.RelativeValuesSpecification":
            pass

            return self._parent._cast(_1073.RelativeValuesSpecification)

        @property
        def finish_stock_specification(
            self: "FinishStockSpecification._Cast_FinishStockSpecification",
        ) -> "FinishStockSpecification":
            return self._parent

        def __getattr__(
            self: "FinishStockSpecification._Cast_FinishStockSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FinishStockSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_stock_rough_thickness_specification_method(
        self: Self,
    ) -> "_1096.FinishStockType":
        """mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash.FinishStockType"""
        temp = self.wrapped.FinishStockRoughThicknessSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash.FinishStockType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash._1096",
            "FinishStockType",
        )(value)

    @finish_stock_rough_thickness_specification_method.setter
    @enforce_parameter_types
    def finish_stock_rough_thickness_specification_method(
        self: Self, value: "_1096.FinishStockType"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.ThicknessStockAndBacklash.FinishStockType",
        )
        self.wrapped.FinishStockRoughThicknessSpecificationMethod = value

    @property
    def normal(
        self: Self,
    ) -> "_1089.TolerancedValueSpecification[FinishStockSpecification]":
        """mastapy.gears.gear_designs.cylindrical.TolerancedValueSpecification[mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash.FinishStockSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Normal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[FinishStockSpecification](
            temp
        )

    @property
    def tangent_to_reference_circle(
        self: Self,
    ) -> "_1089.TolerancedValueSpecification[FinishStockSpecification]":
        """mastapy.gears.gear_designs.cylindrical.TolerancedValueSpecification[mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash.FinishStockSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentToReferenceCircle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[FinishStockSpecification](
            temp
        )

    @property
    def cast_to(
        self: Self,
    ) -> "FinishStockSpecification._Cast_FinishStockSpecification":
        return self._Cast_FinishStockSpecification(self)
