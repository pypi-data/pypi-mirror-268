"""CustomReportText"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.report import _1767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_TEXT = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportText"
)

if TYPE_CHECKING:
    from mastapy.html import _307
    from mastapy.utility.report import _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportText",)


Self = TypeVar("Self", bound="CustomReportText")


class CustomReportText(_1767.CustomReportDefinitionItem):
    """CustomReportText

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_TEXT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportText")

    class _Cast_CustomReportText:
        """Special nested class for casting CustomReportText to subclasses."""

        def __init__(
            self: "CustomReportText._Cast_CustomReportText", parent: "CustomReportText"
        ):
            self._parent = parent

        @property
        def custom_report_definition_item(
            self: "CustomReportText._Cast_CustomReportText",
        ) -> "_1767.CustomReportDefinitionItem":
            return self._parent._cast(_1767.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(
            self: "CustomReportText._Cast_CustomReportText",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportText._Cast_CustomReportText",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_text(
            self: "CustomReportText._Cast_CustomReportText",
        ) -> "CustomReportText":
            return self._parent

        def __getattr__(self: "CustomReportText._Cast_CustomReportText", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportText.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bold(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Bold

        if temp is None:
            return False

        return temp

    @bold.setter
    @enforce_parameter_types
    def bold(self: Self, value: "bool"):
        self.wrapped.Bold = bool(value) if value is not None else False

    @property
    def cad_text_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CADTextSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @cad_text_size.setter
    @enforce_parameter_types
    def cad_text_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CADTextSize = value

    @property
    def heading_type(self: Self) -> "_307.HeadingType":
        """mastapy.html.HeadingType"""
        temp = self.wrapped.HeadingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.HTML.HeadingType")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.html._307", "HeadingType")(value)

    @heading_type.setter
    @enforce_parameter_types
    def heading_type(self: Self, value: "_307.HeadingType"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.HTML.HeadingType")
        self.wrapped.HeadingType = value

    @property
    def is_heading(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsHeading

        if temp is None:
            return False

        return temp

    @is_heading.setter
    @enforce_parameter_types
    def is_heading(self: Self, value: "bool"):
        self.wrapped.IsHeading = bool(value) if value is not None else False

    @property
    def show_symbol(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowSymbol

        if temp is None:
            return False

        return temp

    @show_symbol.setter
    @enforce_parameter_types
    def show_symbol(self: Self, value: "bool"):
        self.wrapped.ShowSymbol = bool(value) if value is not None else False

    @property
    def show_unit(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowUnit

        if temp is None:
            return False

        return temp

    @show_unit.setter
    @enforce_parameter_types
    def show_unit(self: Self, value: "bool"):
        self.wrapped.ShowUnit = bool(value) if value is not None else False

    @property
    def text(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Text

        if temp is None:
            return ""

        return temp

    @text.setter
    @enforce_parameter_types
    def text(self: Self, value: "str"):
        self.wrapped.Text = str(value) if value is not None else ""

    @property
    def cast_to(self: Self) -> "CustomReportText._Cast_CustomReportText":
        return self._Cast_CustomReportText(self)
