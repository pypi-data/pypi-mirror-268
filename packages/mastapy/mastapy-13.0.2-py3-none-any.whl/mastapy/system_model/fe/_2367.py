"""BaseFEWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASE_FE_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "BaseFEWithSelection"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _188, _181, _197, _196
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.fe import _2397, _2398, _2399, _2400, _2401, _2415


__docformat__ = "restructuredtext en"
__all__ = ("BaseFEWithSelection",)


Self = TypeVar("Self", bound="BaseFEWithSelection")


class BaseFEWithSelection(_0.APIBase):
    """BaseFEWithSelection

    This is a mastapy class.
    """

    TYPE = _BASE_FE_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BaseFEWithSelection")

    class _Cast_BaseFEWithSelection:
        """Special nested class for casting BaseFEWithSelection to subclasses."""

        def __init__(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
            parent: "BaseFEWithSelection",
        ):
            self._parent = parent

        @property
        def fe_substructure_with_selection(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
        ) -> "_2397.FESubstructureWithSelection":
            from mastapy.system_model.fe import _2397

            return self._parent._cast(_2397.FESubstructureWithSelection)

        @property
        def fe_substructure_with_selection_components(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
        ) -> "_2398.FESubstructureWithSelectionComponents":
            from mastapy.system_model.fe import _2398

            return self._parent._cast(_2398.FESubstructureWithSelectionComponents)

        @property
        def fe_substructure_with_selection_for_harmonic_analysis(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
        ) -> "_2399.FESubstructureWithSelectionForHarmonicAnalysis":
            from mastapy.system_model.fe import _2399

            return self._parent._cast(
                _2399.FESubstructureWithSelectionForHarmonicAnalysis
            )

        @property
        def fe_substructure_with_selection_for_modal_analysis(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
        ) -> "_2400.FESubstructureWithSelectionForModalAnalysis":
            from mastapy.system_model.fe import _2400

            return self._parent._cast(_2400.FESubstructureWithSelectionForModalAnalysis)

        @property
        def fe_substructure_with_selection_for_static_analysis(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
        ) -> "_2401.FESubstructureWithSelectionForStaticAnalysis":
            from mastapy.system_model.fe import _2401

            return self._parent._cast(
                _2401.FESubstructureWithSelectionForStaticAnalysis
            )

        @property
        def race_bearing_fe_with_selection(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
        ) -> "_2415.RaceBearingFEWithSelection":
            from mastapy.system_model.fe import _2415

            return self._parent._cast(_2415.RaceBearingFEWithSelection)

        @property
        def base_fe_with_selection(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection",
        ) -> "BaseFEWithSelection":
            return self._parent

        def __getattr__(
            self: "BaseFEWithSelection._Cast_BaseFEWithSelection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BaseFEWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_selected_faces(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfSelectedFaces

        if temp is None:
            return 0

        return temp

    @property
    def number_of_selected_nodes(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfSelectedNodes

        if temp is None:
            return 0

        return temp

    @property
    def selected_component(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedComponent

        if temp is None:
            return ""

        return temp

    @property
    def component_draw_style(self: Self) -> "_188.FEModelComponentDrawStyle":
        """mastapy.nodal_analysis.dev_tools_analyses.FEModelComponentDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def draw_style(self: Self) -> "_181.DrawStyleForFE":
        """mastapy.nodal_analysis.dev_tools_analyses.DrawStyleForFE

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def node_selection(self: Self) -> "_197.FENodeSelectionDrawStyle":
        """mastapy.nodal_analysis.dev_tools_analyses.FENodeSelectionDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeSelection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transparency_draw_style(self: Self) -> "_196.FEModelTransparencyDrawStyle":
        """mastapy.nodal_analysis.dev_tools_analyses.FEModelTransparencyDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransparencyDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def select_component(self: Self, component: "_2451.Component"):
        """Method does not return.

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        self.wrapped.SelectComponent(component.wrapped if component else None)

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
    def cast_to(self: Self) -> "BaseFEWithSelection._Cast_BaseFEWithSelection":
        return self._Cast_BaseFEWithSelection(self)
