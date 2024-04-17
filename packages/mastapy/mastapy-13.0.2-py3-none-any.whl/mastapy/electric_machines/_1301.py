"""RotorInternalLayerSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_INTERNAL_LAYER_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "RotorInternalLayerSpecification"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1288, _1317, _1318


__docformat__ = "restructuredtext en"
__all__ = ("RotorInternalLayerSpecification",)


Self = TypeVar("Self", bound="RotorInternalLayerSpecification")


class RotorInternalLayerSpecification(_0.APIBase):
    """RotorInternalLayerSpecification

    This is a mastapy class.
    """

    TYPE = _ROTOR_INTERNAL_LAYER_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RotorInternalLayerSpecification")

    class _Cast_RotorInternalLayerSpecification:
        """Special nested class for casting RotorInternalLayerSpecification to subclasses."""

        def __init__(
            self: "RotorInternalLayerSpecification._Cast_RotorInternalLayerSpecification",
            parent: "RotorInternalLayerSpecification",
        ):
            self._parent = parent

        @property
        def u_shaped_layer_specification(
            self: "RotorInternalLayerSpecification._Cast_RotorInternalLayerSpecification",
        ) -> "_1317.UShapedLayerSpecification":
            from mastapy.electric_machines import _1317

            return self._parent._cast(_1317.UShapedLayerSpecification)

        @property
        def v_shaped_magnet_layer_specification(
            self: "RotorInternalLayerSpecification._Cast_RotorInternalLayerSpecification",
        ) -> "_1318.VShapedMagnetLayerSpecification":
            from mastapy.electric_machines import _1318

            return self._parent._cast(_1318.VShapedMagnetLayerSpecification)

        @property
        def rotor_internal_layer_specification(
            self: "RotorInternalLayerSpecification._Cast_RotorInternalLayerSpecification",
        ) -> "RotorInternalLayerSpecification":
            return self._parent

        def __getattr__(
            self: "RotorInternalLayerSpecification._Cast_RotorInternalLayerSpecification",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RotorInternalLayerSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bridge_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BridgeThickness

        if temp is None:
            return 0.0

        return temp

    @bridge_thickness.setter
    @enforce_parameter_types
    def bridge_thickness(self: Self, value: "float"):
        self.wrapped.BridgeThickness = float(value) if value is not None else 0.0

    @property
    def central_bridge_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentralBridgeThickness

        if temp is None:
            return 0.0

        return temp

    @central_bridge_thickness.setter
    @enforce_parameter_types
    def central_bridge_thickness(self: Self, value: "float"):
        self.wrapped.CentralBridgeThickness = float(value) if value is not None else 0.0

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def magnets(self: Self) -> "_1288.MagnetForLayer":
        """mastapy.electric_machines.MagnetForLayer

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Magnets

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
    ) -> "RotorInternalLayerSpecification._Cast_RotorInternalLayerSpecification":
        return self._Cast_RotorInternalLayerSpecification(self)
