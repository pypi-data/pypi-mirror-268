"""ShaftSystemDeflectionSectionsReport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SYSTEM_DEFLECTION_SECTIONS_REPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting",
    "ShaftSystemDeflectionSectionsReport",
)

if TYPE_CHECKING:
    from mastapy.utility.enums import _1827
    from mastapy.utility.report import _1776, _1777, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSystemDeflectionSectionsReport",)


Self = TypeVar("Self", bound="ShaftSystemDeflectionSectionsReport")


class ShaftSystemDeflectionSectionsReport(_1763.CustomReportChart):
    """ShaftSystemDeflectionSectionsReport

    This is a mastapy class.
    """

    TYPE = _SHAFT_SYSTEM_DEFLECTION_SECTIONS_REPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSystemDeflectionSectionsReport")

    class _Cast_ShaftSystemDeflectionSectionsReport:
        """Special nested class for casting ShaftSystemDeflectionSectionsReport to subclasses."""

        def __init__(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
            parent: "ShaftSystemDeflectionSectionsReport",
        ):
            self._parent = parent

        @property
        def custom_report_chart(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
        ) -> "_1763.CustomReportChart":
            return self._parent._cast(_1763.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
        ) -> "_1776.CustomReportMultiPropertyItem":
            pass

            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def shaft_system_deflection_sections_report(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
        ) -> "ShaftSystemDeflectionSectionsReport":
            return self._parent

        def __getattr__(
            self: "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport",
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
        self: Self, instance_to_wrap: "ShaftSystemDeflectionSectionsReport.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display(self: Self) -> "_1827.TableAndChartOptions":
        """mastapy.utility.enums.TableAndChartOptions"""
        temp = self.wrapped.Display

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.enums._1827", "TableAndChartOptions"
        )(value)

    @display.setter
    @enforce_parameter_types
    def display(self: Self, value: "_1827.TableAndChartOptions"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Enums.TableAndChartOptions"
        )
        self.wrapped.Display = value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ShaftSystemDeflectionSectionsReport._Cast_ShaftSystemDeflectionSectionsReport"
    ):
        return self._Cast_ShaftSystemDeflectionSectionsReport(self)
