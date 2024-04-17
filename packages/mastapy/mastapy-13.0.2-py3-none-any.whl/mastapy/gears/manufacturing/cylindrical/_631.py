"""GearManufacturingConfigurationViewModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "GearManufacturingConfigurationViewModel",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _632
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _677,
        _690,
        _704,
    )
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _757,
        _763,
        _773,
        _774,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearManufacturingConfigurationViewModel",)


Self = TypeVar("Self", bound="GearManufacturingConfigurationViewModel")


class GearManufacturingConfigurationViewModel(_0.APIBase):
    """GearManufacturingConfigurationViewModel

    This is a mastapy class.
    """

    TYPE = _GEAR_MANUFACTURING_CONFIGURATION_VIEW_MODEL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearManufacturingConfigurationViewModel"
    )

    class _Cast_GearManufacturingConfigurationViewModel:
        """Special nested class for casting GearManufacturingConfigurationViewModel to subclasses."""

        def __init__(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
            parent: "GearManufacturingConfigurationViewModel",
        ):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model_placeholder(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_632.GearManufacturingConfigurationViewModelPlaceholder":
            from mastapy.gears.manufacturing.cylindrical import _632

            return self._parent._cast(
                _632.GearManufacturingConfigurationViewModelPlaceholder
            )

        @property
        def hobbing_process_simulation_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_677.HobbingProcessSimulationViewModel":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _677,
            )

            return self._parent._cast(_677.HobbingProcessSimulationViewModel)

        @property
        def process_simulation_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_690.ProcessSimulationViewModel":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _690,
            )

            return self._parent._cast(_690.ProcessSimulationViewModel)

        @property
        def worm_grinding_process_simulation_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_704.WormGrindingProcessSimulationViewModel":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _704,
            )

            return self._parent._cast(_704.WormGrindingProcessSimulationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_757.ConventionalShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _757,
            )

            return self._parent._cast(_757.ConventionalShavingDynamicsViewModel)

        @property
        def plunge_shaving_dynamics_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_763.PlungeShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _763,
            )

            return self._parent._cast(_763.PlungeShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_773.ShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _773,
            )

            return self._parent._cast(_773.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "_774.ShavingDynamicsViewModelBase":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _774,
            )

            return self._parent._cast(_774.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
        ) -> "GearManufacturingConfigurationViewModel":
            return self._parent

        def __getattr__(
            self: "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "GearManufacturingConfigurationViewModel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "GearManufacturingConfigurationViewModel._Cast_GearManufacturingConfigurationViewModel":
        return self._Cast_GearManufacturingConfigurationViewModel(self)
