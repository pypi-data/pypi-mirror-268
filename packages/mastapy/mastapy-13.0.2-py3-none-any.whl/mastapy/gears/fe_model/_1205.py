"""GearMeshingElementOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESHING_ELEMENT_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.FEModel", "GearMeshingElementOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshingElementOptions",)


Self = TypeVar("Self", bound="GearMeshingElementOptions")


class GearMeshingElementOptions(_0.APIBase):
    """GearMeshingElementOptions

    This is a mastapy class.
    """

    TYPE = _GEAR_MESHING_ELEMENT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshingElementOptions")

    class _Cast_GearMeshingElementOptions:
        """Special nested class for casting GearMeshingElementOptions to subclasses."""

        def __init__(
            self: "GearMeshingElementOptions._Cast_GearMeshingElementOptions",
            parent: "GearMeshingElementOptions",
        ):
            self._parent = parent

        @property
        def gear_meshing_element_options(
            self: "GearMeshingElementOptions._Cast_GearMeshingElementOptions",
        ) -> "GearMeshingElementOptions":
            return self._parent

        def __getattr__(
            self: "GearMeshingElementOptions._Cast_GearMeshingElementOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshingElementOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def body_elements(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.BodyElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @body_elements.setter
    @enforce_parameter_types
    def body_elements(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.BodyElements = value

    @property
    def face_elements(self: Self) -> "int":
        """int"""
        temp = self.wrapped.FaceElements

        if temp is None:
            return 0

        return temp

    @face_elements.setter
    @enforce_parameter_types
    def face_elements(self: Self, value: "int"):
        self.wrapped.FaceElements = int(value) if value is not None else 0

    @property
    def fillet_elements(self: Self) -> "int":
        """int"""
        temp = self.wrapped.FilletElements

        if temp is None:
            return 0

        return temp

    @fillet_elements.setter
    @enforce_parameter_types
    def fillet_elements(self: Self, value: "int"):
        self.wrapped.FilletElements = int(value) if value is not None else 0

    @property
    def profile_elements(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ProfileElements

        if temp is None:
            return 0

        return temp

    @profile_elements.setter
    @enforce_parameter_types
    def profile_elements(self: Self, value: "int"):
        self.wrapped.ProfileElements = int(value) if value is not None else 0

    @property
    def radial_elements(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RadialElements

        if temp is None:
            return 0

        return temp

    @radial_elements.setter
    @enforce_parameter_types
    def radial_elements(self: Self, value: "int"):
        self.wrapped.RadialElements = int(value) if value is not None else 0

    @property
    def rim_elements(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.RimElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @rim_elements.setter
    @enforce_parameter_types
    def rim_elements(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.RimElements = value

    @property
    def tip_elements(self: Self) -> "int":
        """int"""
        temp = self.wrapped.TipElements

        if temp is None:
            return 0

        return temp

    @tip_elements.setter
    @enforce_parameter_types
    def tip_elements(self: Self, value: "int"):
        self.wrapped.TipElements = int(value) if value is not None else 0

    @property
    def web_elements(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.WebElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @web_elements.setter
    @enforce_parameter_types
    def web_elements(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.WebElements = value

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
    ) -> "GearMeshingElementOptions._Cast_GearMeshingElementOptions":
        return self._Cast_GearMeshingElementOptions(self)
