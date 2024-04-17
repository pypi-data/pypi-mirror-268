"""HarmonicAnalysisRootAssemblyExportOptions"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5771
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_ROOT_ASSEMBLY_EXPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HarmonicAnalysisRootAssemblyExportOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisRootAssemblyExportOptions",)


Self = TypeVar("Self", bound="HarmonicAnalysisRootAssemblyExportOptions")


class HarmonicAnalysisRootAssemblyExportOptions(
    _5771.HarmonicAnalysisExportOptions[
        "_2663.IHaveRootHarmonicAnalysisResults", "_2481.RootAssembly"
    ]
):
    """HarmonicAnalysisRootAssemblyExportOptions

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_ROOT_ASSEMBLY_EXPORT_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HarmonicAnalysisRootAssemblyExportOptions"
    )

    class _Cast_HarmonicAnalysisRootAssemblyExportOptions:
        """Special nested class for casting HarmonicAnalysisRootAssemblyExportOptions to subclasses."""

        def __init__(
            self: "HarmonicAnalysisRootAssemblyExportOptions._Cast_HarmonicAnalysisRootAssemblyExportOptions",
            parent: "HarmonicAnalysisRootAssemblyExportOptions",
        ):
            self._parent = parent

        @property
        def harmonic_analysis_export_options(
            self: "HarmonicAnalysisRootAssemblyExportOptions._Cast_HarmonicAnalysisRootAssemblyExportOptions",
        ) -> "_5771.HarmonicAnalysisExportOptions":
            return self._parent._cast(_5771.HarmonicAnalysisExportOptions)

        @property
        def harmonic_analysis_root_assembly_export_options(
            self: "HarmonicAnalysisRootAssemblyExportOptions._Cast_HarmonicAnalysisRootAssemblyExportOptions",
        ) -> "HarmonicAnalysisRootAssemblyExportOptions":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisRootAssemblyExportOptions._Cast_HarmonicAnalysisRootAssemblyExportOptions",
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
        self: Self, instance_to_wrap: "HarmonicAnalysisRootAssemblyExportOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_all_fe_models(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAllFEModels

        if temp is None:
            return False

        return temp

    @include_all_fe_models.setter
    @enforce_parameter_types
    def include_all_fe_models(self: Self, value: "bool"):
        self.wrapped.IncludeAllFEModels = bool(value) if value is not None else False

    @property
    def include_all_shafts(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAllShafts

        if temp is None:
            return False

        return temp

    @include_all_shafts.setter
    @enforce_parameter_types
    def include_all_shafts(self: Self, value: "bool"):
        self.wrapped.IncludeAllShafts = bool(value) if value is not None else False

    @property
    def status_message_for_export(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatusMessageForExport

        if temp is None:
            return ""

        return temp

    @enforce_parameter_types
    def export_to_folder(self: Self, folder_path: "str") -> "List[str]":
        """List[str]

        Args:
            folder_path (str)
        """
        folder_path = str(folder_path)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.ExportToFolder(folder_path if folder_path else ""), str
        )

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisRootAssemblyExportOptions._Cast_HarmonicAnalysisRootAssemblyExportOptions":
        return self._Cast_HarmonicAnalysisRootAssemblyExportOptions(self)
