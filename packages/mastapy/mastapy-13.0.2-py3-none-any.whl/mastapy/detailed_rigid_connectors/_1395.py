"""DetailedRigidConnectorHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_RIGID_CONNECTOR_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors", "DetailedRigidConnectorHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import (
        _1396,
        _1399,
        _1403,
        _1406,
        _1414,
        _1421,
        _1426,
    )
    from mastapy.detailed_rigid_connectors.keyed_joints import _1446
    from mastapy.detailed_rigid_connectors.interference_fits import _1453


__docformat__ = "restructuredtext en"
__all__ = ("DetailedRigidConnectorHalfDesign",)


Self = TypeVar("Self", bound="DetailedRigidConnectorHalfDesign")


class DetailedRigidConnectorHalfDesign(_0.APIBase):
    """DetailedRigidConnectorHalfDesign

    This is a mastapy class.
    """

    TYPE = _DETAILED_RIGID_CONNECTOR_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedRigidConnectorHalfDesign")

    class _Cast_DetailedRigidConnectorHalfDesign:
        """Special nested class for casting DetailedRigidConnectorHalfDesign to subclasses."""

        def __init__(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
            parent: "DetailedRigidConnectorHalfDesign",
        ):
            self._parent = parent

        @property
        def custom_spline_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1396.CustomSplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1396

            return self._parent._cast(_1396.CustomSplineHalfDesign)

        @property
        def din5480_spline_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1399.DIN5480SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1399

            return self._parent._cast(_1399.DIN5480SplineHalfDesign)

        @property
        def gbt3478_spline_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1403.GBT3478SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1403

            return self._parent._cast(_1403.GBT3478SplineHalfDesign)

        @property
        def iso4156_spline_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1406.ISO4156SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1406

            return self._parent._cast(_1406.ISO4156SplineHalfDesign)

        @property
        def sae_spline_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1414.SAESplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1414

            return self._parent._cast(_1414.SAESplineHalfDesign)

        @property
        def spline_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1421.SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1421

            return self._parent._cast(_1421.SplineHalfDesign)

        @property
        def standard_spline_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1426.StandardSplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1426

            return self._parent._cast(_1426.StandardSplineHalfDesign)

        @property
        def keyway_joint_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1446.KeywayJointHalfDesign":
            from mastapy.detailed_rigid_connectors.keyed_joints import _1446

            return self._parent._cast(_1446.KeywayJointHalfDesign)

        @property
        def interference_fit_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "_1453.InterferenceFitHalfDesign":
            from mastapy.detailed_rigid_connectors.interference_fits import _1453

            return self._parent._cast(_1453.InterferenceFitHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
        ) -> "DetailedRigidConnectorHalfDesign":
            return self._parent

        def __getattr__(
            self: "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedRigidConnectorHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def non_contacting_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NonContactingDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @non_contacting_diameter.setter
    @enforce_parameter_types
    def non_contacting_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NonContactingDiameter = value

    @property
    def tensile_yield_strength(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TensileYieldStrength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tensile_yield_strength.setter
    @enforce_parameter_types
    def tensile_yield_strength(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TensileYieldStrength = value

    @property
    def ultimate_tensile_strength(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UltimateTensileStrength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @ultimate_tensile_strength.setter
    @enforce_parameter_types
    def ultimate_tensile_strength(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UltimateTensileStrength = value

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
    ) -> "DetailedRigidConnectorHalfDesign._Cast_DetailedRigidConnectorHalfDesign":
        return self._Cast_DetailedRigidConnectorHalfDesign(self)
