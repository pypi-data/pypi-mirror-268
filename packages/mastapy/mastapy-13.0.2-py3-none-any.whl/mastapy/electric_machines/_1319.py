"""WindingConductor"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WINDING_CONDUCTOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "WindingConductor"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1252, _1278


__docformat__ = "restructuredtext en"
__all__ = ("WindingConductor",)


Self = TypeVar("Self", bound="WindingConductor")


class WindingConductor(_0.APIBase):
    """WindingConductor

    This is a mastapy class.
    """

    TYPE = _WINDING_CONDUCTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WindingConductor")

    class _Cast_WindingConductor:
        """Special nested class for casting WindingConductor to subclasses."""

        def __init__(
            self: "WindingConductor._Cast_WindingConductor", parent: "WindingConductor"
        ):
            self._parent = parent

        @property
        def cad_conductor(
            self: "WindingConductor._Cast_WindingConductor",
        ) -> "_1252.CADConductor":
            from mastapy.electric_machines import _1252

            return self._parent._cast(_1252.CADConductor)

        @property
        def hairpin_conductor(
            self: "WindingConductor._Cast_WindingConductor",
        ) -> "_1278.HairpinConductor":
            from mastapy.electric_machines import _1278

            return self._parent._cast(_1278.HairpinConductor)

        @property
        def winding_conductor(
            self: "WindingConductor._Cast_WindingConductor",
        ) -> "WindingConductor":
            return self._parent

        def __getattr__(self: "WindingConductor._Cast_WindingConductor", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WindingConductor.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conductor_dimension_for_dq_model_ac_winding_loss_scaling_for_skin_depth(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ConductorDimensionForDQModelACWindingLossScalingForSkinDepth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @conductor_dimension_for_dq_model_ac_winding_loss_scaling_for_skin_depth.setter
    @enforce_parameter_types
    def conductor_dimension_for_dq_model_ac_winding_loss_scaling_for_skin_depth(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ConductorDimensionForDQModelACWindingLossScalingForSkinDepth = (
            value
        )

    @property
    def layer_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LayerIndex

        if temp is None:
            return 0

        return temp

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
    def cast_to(self: Self) -> "WindingConductor._Cast_WindingConductor":
        return self._Cast_WindingConductor(self)
