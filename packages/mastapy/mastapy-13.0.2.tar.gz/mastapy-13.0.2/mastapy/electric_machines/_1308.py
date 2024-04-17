"""StatorRotorMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials import _272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_ROTOR_MATERIAL = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "StatorRotorMaterial"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1283, _1264
    from mastapy.utility_gui.charts import _1874
    from mastapy.materials import _251
    from mastapy.utility import _1597
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("StatorRotorMaterial",)


Self = TypeVar("Self", bound="StatorRotorMaterial")


class StatorRotorMaterial(_272.Material):
    """StatorRotorMaterial

    This is a mastapy class.
    """

    TYPE = _STATOR_ROTOR_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StatorRotorMaterial")

    class _Cast_StatorRotorMaterial:
        """Special nested class for casting StatorRotorMaterial to subclasses."""

        def __init__(
            self: "StatorRotorMaterial._Cast_StatorRotorMaterial",
            parent: "StatorRotorMaterial",
        ):
            self._parent = parent

        @property
        def material(
            self: "StatorRotorMaterial._Cast_StatorRotorMaterial",
        ) -> "_272.Material":
            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "StatorRotorMaterial._Cast_StatorRotorMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def stator_rotor_material(
            self: "StatorRotorMaterial._Cast_StatorRotorMaterial",
        ) -> "StatorRotorMaterial":
            return self._parent

        def __getattr__(
            self: "StatorRotorMaterial._Cast_StatorRotorMaterial", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StatorRotorMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def annealing(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Annealing

        if temp is None:
            return ""

        return temp

    @annealing.setter
    @enforce_parameter_types
    def annealing(self: Self, value: "str"):
        self.wrapped.Annealing = str(value) if value is not None else ""

    @property
    def coefficient_specification_method(
        self: Self,
    ) -> "_1283.IronLossCoefficientSpecificationMethod":
        """mastapy.electric_machines.IronLossCoefficientSpecificationMethod"""
        temp = self.wrapped.CoefficientSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.IronLossCoefficientSpecificationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1283", "IronLossCoefficientSpecificationMethod"
        )(value)

    @coefficient_specification_method.setter
    @enforce_parameter_types
    def coefficient_specification_method(
        self: Self, value: "_1283.IronLossCoefficientSpecificationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.IronLossCoefficientSpecificationMethod",
        )
        self.wrapped.CoefficientSpecificationMethod = value

    @property
    def country(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Country

        if temp is None:
            return ""

        return temp

    @country.setter
    @enforce_parameter_types
    def country(self: Self, value: "str"):
        self.wrapped.Country = str(value) if value is not None else ""

    @property
    def electrical_resistivity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ElectricalResistivity

        if temp is None:
            return 0.0

        return temp

    @electrical_resistivity.setter
    @enforce_parameter_types
    def electrical_resistivity(self: Self, value: "float"):
        self.wrapped.ElectricalResistivity = float(value) if value is not None else 0.0

    @property
    def grade_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.GradeName

        if temp is None:
            return ""

        return temp

    @grade_name.setter
    @enforce_parameter_types
    def grade_name(self: Self, value: "str"):
        self.wrapped.GradeName = str(value) if value is not None else ""

    @property
    def lamination_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LaminationThickness

        if temp is None:
            return 0.0

        return temp

    @lamination_thickness.setter
    @enforce_parameter_types
    def lamination_thickness(self: Self, value: "float"):
        self.wrapped.LaminationThickness = float(value) if value is not None else 0.0

    @property
    def loss_curves(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LossCurves

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def manufacturer(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Manufacturer

        if temp is None:
            return ""

        return temp

    @manufacturer.setter
    @enforce_parameter_types
    def manufacturer(self: Self, value: "str"):
        self.wrapped.Manufacturer = str(value) if value is not None else ""

    @property
    def material_category(self: Self) -> "str":
        """str"""
        temp = self.wrapped.MaterialCategory

        if temp is None:
            return ""

        return temp

    @material_category.setter
    @enforce_parameter_types
    def material_category(self: Self, value: "str"):
        self.wrapped.MaterialCategory = str(value) if value is not None else ""

    @property
    def stacking_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.StackingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @stacking_factor.setter
    @enforce_parameter_types
    def stacking_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.StackingFactor = value

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
    def core_loss_coefficients(self: Self) -> "_1264.CoreLossCoefficients":
        """mastapy.electric_machines.CoreLossCoefficients

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoreLossCoefficients

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def loss_curve_flux_densities(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LossCurveFluxDensities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def loss_curve_frequencies(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LossCurveFrequencies

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def loss_curve_losses(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LossCurveLosses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def set_loss_curve_data(
        self: Self,
        frequencies: "List[float]",
        flux_densities: "List[float]",
        loss: "List[float]",
    ):
        """Method does not return.

        Args:
            frequencies (List[float])
            flux_densities (List[float])
            loss (List[float])
        """
        frequencies = conversion.mp_to_pn_list_float(frequencies)
        flux_densities = conversion.mp_to_pn_list_float(flux_densities)
        loss = conversion.mp_to_pn_list_float(loss)
        self.wrapped.SetLossCurveData(frequencies, flux_densities, loss)

    def try_update_coefficients_from_loss_curve_data(
        self: Self,
    ) -> "_1597.MethodOutcome":
        """mastapy.utility.MethodOutcome"""
        method_result = self.wrapped.TryUpdateCoefficientsFromLossCurveData()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "StatorRotorMaterial._Cast_StatorRotorMaterial":
        return self._Cast_StatorRotorMaterial(self)
