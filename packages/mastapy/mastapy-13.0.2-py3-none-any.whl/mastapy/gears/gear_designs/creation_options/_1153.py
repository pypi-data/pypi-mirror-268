"""GearSetCreationOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_CREATION_OPTIONS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.CreationOptions", "GearSetCreationOptions"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _954
    from mastapy.gears.gear_designs.creation_options import _1152, _1154, _1155


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCreationOptions",)


Self = TypeVar("Self", bound="GearSetCreationOptions")
T = TypeVar("T", bound="_954.GearSetDesign")


class GearSetCreationOptions(_0.APIBase, Generic[T]):
    """GearSetCreationOptions

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GEAR_SET_CREATION_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCreationOptions")

    class _Cast_GearSetCreationOptions:
        """Special nested class for casting GearSetCreationOptions to subclasses."""

        def __init__(
            self: "GearSetCreationOptions._Cast_GearSetCreationOptions",
            parent: "GearSetCreationOptions",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_pair_creation_options(
            self: "GearSetCreationOptions._Cast_GearSetCreationOptions",
        ) -> "_1152.CylindricalGearPairCreationOptions":
            from mastapy.gears.gear_designs.creation_options import _1152

            return self._parent._cast(_1152.CylindricalGearPairCreationOptions)

        @property
        def hypoid_gear_set_creation_options(
            self: "GearSetCreationOptions._Cast_GearSetCreationOptions",
        ) -> "_1154.HypoidGearSetCreationOptions":
            from mastapy.gears.gear_designs.creation_options import _1154

            return self._parent._cast(_1154.HypoidGearSetCreationOptions)

        @property
        def spiral_bevel_gear_set_creation_options(
            self: "GearSetCreationOptions._Cast_GearSetCreationOptions",
        ) -> "_1155.SpiralBevelGearSetCreationOptions":
            from mastapy.gears.gear_designs.creation_options import _1155

            return self._parent._cast(_1155.SpiralBevelGearSetCreationOptions)

        @property
        def gear_set_creation_options(
            self: "GearSetCreationOptions._Cast_GearSetCreationOptions",
        ) -> "GearSetCreationOptions":
            return self._parent

        def __getattr__(
            self: "GearSetCreationOptions._Cast_GearSetCreationOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCreationOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def gear_set_design(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesign

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
    def cast_to(self: Self) -> "GearSetCreationOptions._Cast_GearSetCreationOptions":
        return self._Cast_GearSetCreationOptions(self)
