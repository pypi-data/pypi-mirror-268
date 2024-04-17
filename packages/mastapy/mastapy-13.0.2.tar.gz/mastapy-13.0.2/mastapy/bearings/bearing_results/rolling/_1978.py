"""ForceAtLaminaReportable"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_AT_LAMINA_REPORTABLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ForceAtLaminaReportable"
)


__docformat__ = "restructuredtext en"
__all__ = ("ForceAtLaminaReportable",)


Self = TypeVar("Self", bound="ForceAtLaminaReportable")


class ForceAtLaminaReportable(_0.APIBase):
    """ForceAtLaminaReportable

    This is a mastapy class.
    """

    TYPE = _FORCE_AT_LAMINA_REPORTABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForceAtLaminaReportable")

    class _Cast_ForceAtLaminaReportable:
        """Special nested class for casting ForceAtLaminaReportable to subclasses."""

        def __init__(
            self: "ForceAtLaminaReportable._Cast_ForceAtLaminaReportable",
            parent: "ForceAtLaminaReportable",
        ):
            self._parent = parent

        @property
        def force_at_lamina_reportable(
            self: "ForceAtLaminaReportable._Cast_ForceAtLaminaReportable",
        ) -> "ForceAtLaminaReportable":
            return self._parent

        def __getattr__(
            self: "ForceAtLaminaReportable._Cast_ForceAtLaminaReportable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForceAtLaminaReportable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_equivalent_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def lamina_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LaminaIndex

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: Self) -> "ForceAtLaminaReportable._Cast_ForceAtLaminaReportable":
        return self._Cast_ForceAtLaminaReportable(self)
