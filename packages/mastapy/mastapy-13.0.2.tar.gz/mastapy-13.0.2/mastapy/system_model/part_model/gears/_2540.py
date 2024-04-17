"""GearSetConfiguration"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "AbstractStaticLoadCaseGroup",
)
_GEAR_SET_MODES = python_net_import("SMT.MastaAPI.Gears", "GearSetModes")
_BOOLEAN = python_net_import("System", "Boolean")
_STATIC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "StaticLoadCase"
)
_GEAR_SET_CONFIGURATION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSetConfiguration"
)

if TYPE_CHECKING:
    from mastapy.gears import _331, _332
    from mastapy.system_model.part_model.gears import _2531, _2533, _2544, _2559
    from mastapy.system_model.analyses_and_results.load_case_groups import _5668
    from mastapy.gears.analysis import _1233
    from mastapy.system_model.analyses_and_results.static_loads import _6813


__docformat__ = "restructuredtext en"
__all__ = ("GearSetConfiguration",)


Self = TypeVar("Self", bound="GearSetConfiguration")


class GearSetConfiguration(_0.APIBase):
    """GearSetConfiguration

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_CONFIGURATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetConfiguration")

    class _Cast_GearSetConfiguration:
        """Special nested class for casting GearSetConfiguration to subclasses."""

        def __init__(
            self: "GearSetConfiguration._Cast_GearSetConfiguration",
            parent: "GearSetConfiguration",
        ):
            self._parent = parent

        @property
        def gear_set_configuration(
            self: "GearSetConfiguration._Cast_GearSetConfiguration",
        ) -> "GearSetConfiguration":
            return self._parent

        def __getattr__(
            self: "GearSetConfiguration._Cast_GearSetConfiguration", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetConfiguration.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_design_group(self: Self) -> "_331.GearSetDesignGroup":
        """mastapy.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesignGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_sets(self: Self) -> "List[_2531.ConicalGearSet]":
        """List[mastapy.system_model.part_model.gears.ConicalGearSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_sets(self: Self) -> "List[_2533.CylindricalGearSet]":
        """List[mastapy.system_model.part_model.gears.CylindricalGearSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_gear_sets(
        self: Self,
    ) -> "List[_2544.KlingelnbergCycloPalloidConicalGearSet]":
        """List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_sets(self: Self) -> "List[_2559.WormGearSet]":
        """List[mastapy.system_model.part_model.gears.WormGearSet]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def implementation_detail_results_for_group(
        self: Self,
        analysis_case: "_5668.AbstractStaticLoadCaseGroup",
        gear_set_mode: "_332.GearSetModes",
        run_all_planetary_meshes: "bool",
    ) -> "_1233.GearSetGroupDutyCycle":
        """mastapy.gears.analysis.GearSetGroupDutyCycle

        Args:
            analysis_case (mastapy.system_model.analyses_and_results.load_case_groups.AbstractStaticLoadCaseGroup)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ImplementationDetailResultsFor.Overloads[
            _ABSTRACT_STATIC_LOAD_CASE_GROUP, _GEAR_SET_MODES, _BOOLEAN
        ](
            analysis_case.wrapped if analysis_case else None,
            gear_set_mode,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def implementation_detail_results_for(
        self: Self,
        analysis_case: "_6813.StaticLoadCase",
        gear_set_mode: "_332.GearSetModes",
        run_all_planetary_meshes: "bool",
    ) -> "_1233.GearSetGroupDutyCycle":
        """mastapy.gears.analysis.GearSetGroupDutyCycle

        Args:
            analysis_case (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ImplementationDetailResultsFor.Overloads[
            _STATIC_LOAD_CASE, _GEAR_SET_MODES, _BOOLEAN
        ](
            analysis_case.wrapped if analysis_case else None,
            gear_set_mode,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def perform_implementation_detail_analysis_group(
        self: Self,
        static_load_case_group: "_5668.AbstractStaticLoadCaseGroup",
        gear_set_mode: "_332.GearSetModes",
        run_all_planetary_meshes: "bool" = True,
        perform_system_analysis_if_not_ready: "bool" = True,
    ):
        """Method does not return.

        Args:
            static_load_case_group (mastapy.system_model.analyses_and_results.load_case_groups.AbstractStaticLoadCaseGroup)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
            perform_system_analysis_if_not_ready (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        perform_system_analysis_if_not_ready = bool(
            perform_system_analysis_if_not_ready
        )
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _ABSTRACT_STATIC_LOAD_CASE_GROUP, _GEAR_SET_MODES, _BOOLEAN, _BOOLEAN
        ](
            static_load_case_group.wrapped if static_load_case_group else None,
            gear_set_mode,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
            (
                perform_system_analysis_if_not_ready
                if perform_system_analysis_if_not_ready
                else False
            ),
        )

    @enforce_parameter_types
    def perform_implementation_detail_analysis(
        self: Self,
        static_load: "_6813.StaticLoadCase",
        gear_set_mode: "_332.GearSetModes",
        run_all_planetary_meshes: "bool" = True,
        perform_system_analysis_if_not_ready: "bool" = True,
    ):
        """Method does not return.

        Args:
            static_load (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
            perform_system_analysis_if_not_ready (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        perform_system_analysis_if_not_ready = bool(
            perform_system_analysis_if_not_ready
        )
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _STATIC_LOAD_CASE, _GEAR_SET_MODES, _BOOLEAN, _BOOLEAN
        ](
            static_load.wrapped if static_load else None,
            gear_set_mode,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
            (
                perform_system_analysis_if_not_ready
                if perform_system_analysis_if_not_ready
                else False
            ),
        )

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
    def cast_to(self: Self) -> "GearSetConfiguration._Cast_GearSetConfiguration":
        return self._Cast_GearSetConfiguration(self)
