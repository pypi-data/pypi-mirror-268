"""AdvancedSystemDeflectionViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.drawing import _2250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_SYSTEM_DEFLECTION_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "AdvancedSystemDeflectionViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2260


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedSystemDeflectionViewable",)


Self = TypeVar("Self", bound="AdvancedSystemDeflectionViewable")


class AdvancedSystemDeflectionViewable(_2250.AbstractSystemDeflectionViewable):
    """AdvancedSystemDeflectionViewable

    This is a mastapy class.
    """

    TYPE = _ADVANCED_SYSTEM_DEFLECTION_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AdvancedSystemDeflectionViewable")

    class _Cast_AdvancedSystemDeflectionViewable:
        """Special nested class for casting AdvancedSystemDeflectionViewable to subclasses."""

        def __init__(
            self: "AdvancedSystemDeflectionViewable._Cast_AdvancedSystemDeflectionViewable",
            parent: "AdvancedSystemDeflectionViewable",
        ):
            self._parent = parent

        @property
        def abstract_system_deflection_viewable(
            self: "AdvancedSystemDeflectionViewable._Cast_AdvancedSystemDeflectionViewable",
        ) -> "_2250.AbstractSystemDeflectionViewable":
            return self._parent._cast(_2250.AbstractSystemDeflectionViewable)

        @property
        def part_analysis_case_with_contour_viewable(
            self: "AdvancedSystemDeflectionViewable._Cast_AdvancedSystemDeflectionViewable",
        ) -> "_2260.PartAnalysisCaseWithContourViewable":
            from mastapy.system_model.drawing import _2260

            return self._parent._cast(_2260.PartAnalysisCaseWithContourViewable)

        @property
        def advanced_system_deflection_viewable(
            self: "AdvancedSystemDeflectionViewable._Cast_AdvancedSystemDeflectionViewable",
        ) -> "AdvancedSystemDeflectionViewable":
            return self._parent

        def __getattr__(
            self: "AdvancedSystemDeflectionViewable._Cast_AdvancedSystemDeflectionViewable",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AdvancedSystemDeflectionViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AdvancedSystemDeflectionViewable._Cast_AdvancedSystemDeflectionViewable":
        return self._Cast_AdvancedSystemDeflectionViewable(self)
