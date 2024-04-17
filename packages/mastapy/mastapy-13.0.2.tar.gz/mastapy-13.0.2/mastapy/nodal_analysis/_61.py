"""FEMeshingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MESHING_OPTIONS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "FEMeshingOptions"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _58, _95, _62, _77, _88
    from mastapy.electric_machines import _1270, _1271, _1272


__docformat__ = "restructuredtext en"
__all__ = ("FEMeshingOptions",)


Self = TypeVar("Self", bound="FEMeshingOptions")


class FEMeshingOptions(_0.APIBase):
    """FEMeshingOptions

    This is a mastapy class.
    """

    TYPE = _FE_MESHING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEMeshingOptions")

    class _Cast_FEMeshingOptions:
        """Special nested class for casting FEMeshingOptions to subclasses."""

        def __init__(
            self: "FEMeshingOptions._Cast_FEMeshingOptions", parent: "FEMeshingOptions"
        ):
            self._parent = parent

        @property
        def meshing_options(
            self: "FEMeshingOptions._Cast_FEMeshingOptions",
        ) -> "_77.MeshingOptions":
            from mastapy.nodal_analysis import _77

            return self._parent._cast(_77.MeshingOptions)

        @property
        def shaft_fe_meshing_options(
            self: "FEMeshingOptions._Cast_FEMeshingOptions",
        ) -> "_88.ShaftFEMeshingOptions":
            from mastapy.nodal_analysis import _88

            return self._parent._cast(_88.ShaftFEMeshingOptions)

        @property
        def electric_machine_mechanical_analysis_meshing_options(
            self: "FEMeshingOptions._Cast_FEMeshingOptions",
        ) -> "_1270.ElectricMachineMechanicalAnalysisMeshingOptions":
            from mastapy.electric_machines import _1270

            return self._parent._cast(
                _1270.ElectricMachineMechanicalAnalysisMeshingOptions
            )

        @property
        def electric_machine_meshing_options(
            self: "FEMeshingOptions._Cast_FEMeshingOptions",
        ) -> "_1271.ElectricMachineMeshingOptions":
            from mastapy.electric_machines import _1271

            return self._parent._cast(_1271.ElectricMachineMeshingOptions)

        @property
        def electric_machine_meshing_options_base(
            self: "FEMeshingOptions._Cast_FEMeshingOptions",
        ) -> "_1272.ElectricMachineMeshingOptionsBase":
            from mastapy.electric_machines import _1272

            return self._parent._cast(_1272.ElectricMachineMeshingOptionsBase)

        @property
        def fe_meshing_options(
            self: "FEMeshingOptions._Cast_FEMeshingOptions",
        ) -> "FEMeshingOptions":
            return self._parent

        def __getattr__(self: "FEMeshingOptions._Cast_FEMeshingOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEMeshingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_order(self: Self) -> "_58.ElementOrder":
        """mastapy.nodal_analysis.ElementOrder"""
        temp = self.wrapped.ElementOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._58", "ElementOrder"
        )(value)

    @element_order.setter
    @enforce_parameter_types
    def element_order(self: Self, value: "_58.ElementOrder"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )
        self.wrapped.ElementOrder = value

    @property
    def element_shape(self: Self) -> "_95.VolumeElementShape":
        """mastapy.nodal_analysis.VolumeElementShape"""
        temp = self.wrapped.ElementShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.VolumeElementShape"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._95", "VolumeElementShape"
        )(value)

    @element_shape.setter
    @enforce_parameter_types
    def element_shape(self: Self, value: "_95.VolumeElementShape"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.VolumeElementShape"
        )
        self.wrapped.ElementShape = value

    @property
    def maximum_chord_height(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumChordHeight

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_chord_height.setter
    @enforce_parameter_types
    def maximum_chord_height(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumChordHeight = value

    @property
    def maximum_edge_altitude_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumEdgeAltitudeRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_edge_altitude_ratio.setter
    @enforce_parameter_types
    def maximum_edge_altitude_ratio(self: Self, value: "float"):
        self.wrapped.MaximumEdgeAltitudeRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_growth_rate(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumGrowthRate

        if temp is None:
            return 0.0

        return temp

    @maximum_growth_rate.setter
    @enforce_parameter_types
    def maximum_growth_rate(self: Self, value: "float"):
        self.wrapped.MaximumGrowthRate = float(value) if value is not None else 0.0

    @property
    def maximum_spanning_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumSpanningAngle

        if temp is None:
            return 0.0

        return temp

    @maximum_spanning_angle.setter
    @enforce_parameter_types
    def maximum_spanning_angle(self: Self, value: "float"):
        self.wrapped.MaximumSpanningAngle = float(value) if value is not None else 0.0

    @property
    def minimum_element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_element_size.setter
    @enforce_parameter_types
    def minimum_element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumElementSize = value

    @property
    def minimum_triangle_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumTriangleAngle

        if temp is None:
            return 0.0

        return temp

    @minimum_triangle_angle.setter
    @enforce_parameter_types
    def minimum_triangle_angle(self: Self, value: "float"):
        self.wrapped.MinimumTriangleAngle = float(value) if value is not None else 0.0

    @property
    def preserve_edge_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PreserveEdgeAngle

        if temp is None:
            return 0.0

        return temp

    @preserve_edge_angle.setter
    @enforce_parameter_types
    def preserve_edge_angle(self: Self, value: "float"):
        self.wrapped.PreserveEdgeAngle = float(value) if value is not None else 0.0

    @property
    def preserve_node_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PreserveNodeAngle

        if temp is None:
            return 0.0

        return temp

    @preserve_node_angle.setter
    @enforce_parameter_types
    def preserve_node_angle(self: Self, value: "float"):
        self.wrapped.PreserveNodeAngle = float(value) if value is not None else 0.0

    @property
    def meshing_problems(self: Self) -> "List[_62.FEMeshingProblem]":
        """List[mastapy.nodal_analysis.FEMeshingProblem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshingProblems

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
    def cast_to(self: Self) -> "FEMeshingOptions._Cast_FEMeshingOptions":
        return self._Cast_FEMeshingOptions(self)
