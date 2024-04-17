"""ElementPropertiesBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_BASE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesBase",
)

if TYPE_CHECKING:
    from mastapy.fe_tools.enums import _1247
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
        _212,
        _213,
        _214,
        _215,
        _216,
        _217,
        _218,
        _219,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesBase",)


Self = TypeVar("Self", bound="ElementPropertiesBase")


class ElementPropertiesBase(_0.APIBase):
    """ElementPropertiesBase

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesBase")

    class _Cast_ElementPropertiesBase:
        """Special nested class for casting ElementPropertiesBase to subclasses."""

        def __init__(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
            parent: "ElementPropertiesBase",
        ):
            self._parent = parent

        @property
        def element_properties_beam(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_212.ElementPropertiesBeam":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _212

            return self._parent._cast(_212.ElementPropertiesBeam)

        @property
        def element_properties_interface(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_213.ElementPropertiesInterface":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _213

            return self._parent._cast(_213.ElementPropertiesInterface)

        @property
        def element_properties_mass(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_214.ElementPropertiesMass":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _214

            return self._parent._cast(_214.ElementPropertiesMass)

        @property
        def element_properties_rigid(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_215.ElementPropertiesRigid":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _215

            return self._parent._cast(_215.ElementPropertiesRigid)

        @property
        def element_properties_shell(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_216.ElementPropertiesShell":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _216

            return self._parent._cast(_216.ElementPropertiesShell)

        @property
        def element_properties_solid(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_217.ElementPropertiesSolid":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _217

            return self._parent._cast(_217.ElementPropertiesSolid)

        @property
        def element_properties_spring_dashpot(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_218.ElementPropertiesSpringDashpot":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _218

            return self._parent._cast(_218.ElementPropertiesSpringDashpot)

        @property
        def element_properties_with_material(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "_219.ElementPropertiesWithMaterial":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _219

            return self._parent._cast(_219.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase",
        ) -> "ElementPropertiesBase":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesBase._Cast_ElementPropertiesBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def class_(self: Self) -> "_1247.ElementPropertyClass":
        """mastapy.fe_tools.enums.ElementPropertyClass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Class

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.FETools.Enums.ElementPropertyClass"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.fe_tools.enums._1247", "ElementPropertyClass"
        )(value)

    @property
    def id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return 0

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
    def cast_to(self: Self) -> "ElementPropertiesBase._Cast_ElementPropertiesBase":
        return self._Cast_ElementPropertiesBase(self)
