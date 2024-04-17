"""FrequencyResponseAnalysisOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FREQUENCY_RESPONSE_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "FrequencyResponseAnalysisOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("FrequencyResponseAnalysisOptions",)


Self = TypeVar("Self", bound="FrequencyResponseAnalysisOptions")


class FrequencyResponseAnalysisOptions(_7544.AbstractAnalysisOptions["_6812.LoadCase"]):
    """FrequencyResponseAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _FREQUENCY_RESPONSE_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FrequencyResponseAnalysisOptions")

    class _Cast_FrequencyResponseAnalysisOptions:
        """Special nested class for casting FrequencyResponseAnalysisOptions to subclasses."""

        def __init__(
            self: "FrequencyResponseAnalysisOptions._Cast_FrequencyResponseAnalysisOptions",
            parent: "FrequencyResponseAnalysisOptions",
        ):
            self._parent = parent

        @property
        def abstract_analysis_options(
            self: "FrequencyResponseAnalysisOptions._Cast_FrequencyResponseAnalysisOptions",
        ) -> "_7544.AbstractAnalysisOptions":
            return self._parent._cast(_7544.AbstractAnalysisOptions)

        @property
        def frequency_response_analysis_options(
            self: "FrequencyResponseAnalysisOptions._Cast_FrequencyResponseAnalysisOptions",
        ) -> "FrequencyResponseAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "FrequencyResponseAnalysisOptions._Cast_FrequencyResponseAnalysisOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FrequencyResponseAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_gear_mesh_harmonics(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfGearMeshHarmonics

        if temp is None:
            return 0

        return temp

    @number_of_gear_mesh_harmonics.setter
    @enforce_parameter_types
    def number_of_gear_mesh_harmonics(self: Self, value: "int"):
        self.wrapped.NumberOfGearMeshHarmonics = int(value) if value is not None else 0

    @property
    def number_of_input_shaft_harmonics(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfInputShaftHarmonics

        if temp is None:
            return 0

        return temp

    @number_of_input_shaft_harmonics.setter
    @enforce_parameter_types
    def number_of_input_shaft_harmonics(self: Self, value: "int"):
        self.wrapped.NumberOfInputShaftHarmonics = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_shaft_harmonics(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfShaftHarmonics

        if temp is None:
            return 0

        return temp

    @number_of_shaft_harmonics.setter
    @enforce_parameter_types
    def number_of_shaft_harmonics(self: Self, value: "int"):
        self.wrapped.NumberOfShaftHarmonics = int(value) if value is not None else 0

    @property
    def reference_power_load(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ReferencePowerLoad

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @reference_power_load.setter
    @enforce_parameter_types
    def reference_power_load(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ReferencePowerLoad = value

    @property
    def threshold_for_significant_kinetic_energy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThresholdForSignificantKineticEnergy

        if temp is None:
            return 0.0

        return temp

    @threshold_for_significant_kinetic_energy.setter
    @enforce_parameter_types
    def threshold_for_significant_kinetic_energy(self: Self, value: "float"):
        self.wrapped.ThresholdForSignificantKineticEnergy = (
            float(value) if value is not None else 0.0
        )

    @property
    def threshold_for_significant_strain_energy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThresholdForSignificantStrainEnergy

        if temp is None:
            return 0.0

        return temp

    @threshold_for_significant_strain_energy.setter
    @enforce_parameter_types
    def threshold_for_significant_strain_energy(self: Self, value: "float"):
        self.wrapped.ThresholdForSignificantStrainEnergy = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "FrequencyResponseAnalysisOptions._Cast_FrequencyResponseAnalysisOptions":
        return self._Cast_FrequencyResponseAnalysisOptions(self)
