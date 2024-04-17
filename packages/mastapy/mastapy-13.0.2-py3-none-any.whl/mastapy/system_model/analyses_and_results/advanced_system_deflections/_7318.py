"""ContactChartPerToothPass"""

from __future__ import annotations

from typing import TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTACT_CHART_PER_TOOTH_PASS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ContactChartPerToothPass",
)


__docformat__ = "restructuredtext en"
__all__ = ("ContactChartPerToothPass",)


Self = TypeVar("Self", bound="ContactChartPerToothPass")


class ContactChartPerToothPass(_0.APIBase):
    """ContactChartPerToothPass

    This is a mastapy class.
    """

    TYPE = _CONTACT_CHART_PER_TOOTH_PASS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ContactChartPerToothPass")

    class _Cast_ContactChartPerToothPass:
        """Special nested class for casting ContactChartPerToothPass to subclasses."""

        def __init__(
            self: "ContactChartPerToothPass._Cast_ContactChartPerToothPass",
            parent: "ContactChartPerToothPass",
        ):
            self._parent = parent

        @property
        def contact_chart_per_tooth_pass(
            self: "ContactChartPerToothPass._Cast_ContactChartPerToothPass",
        ) -> "ContactChartPerToothPass":
            return self._parent

        def __getattr__(
            self: "ContactChartPerToothPass._Cast_ContactChartPerToothPass", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ContactChartPerToothPass.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max_pressure(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaxPressure

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

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
    def cast_to(
        self: Self,
    ) -> "ContactChartPerToothPass._Cast_ContactChartPerToothPass":
        return self._Cast_ContactChartPerToothPass(self)
