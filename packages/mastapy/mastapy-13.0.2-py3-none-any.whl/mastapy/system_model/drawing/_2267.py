"""SystemDeflectionViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.drawing import _2250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_VIEWABLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "SystemDeflectionViewable"
)

if TYPE_CHECKING:
    from mastapy.system_model.drawing import _2260


__docformat__ = "restructuredtext en"
__all__ = ("SystemDeflectionViewable",)


Self = TypeVar("Self", bound="SystemDeflectionViewable")


class SystemDeflectionViewable(_2250.AbstractSystemDeflectionViewable):
    """SystemDeflectionViewable

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemDeflectionViewable")

    class _Cast_SystemDeflectionViewable:
        """Special nested class for casting SystemDeflectionViewable to subclasses."""

        def __init__(
            self: "SystemDeflectionViewable._Cast_SystemDeflectionViewable",
            parent: "SystemDeflectionViewable",
        ):
            self._parent = parent

        @property
        def abstract_system_deflection_viewable(
            self: "SystemDeflectionViewable._Cast_SystemDeflectionViewable",
        ) -> "_2250.AbstractSystemDeflectionViewable":
            return self._parent._cast(_2250.AbstractSystemDeflectionViewable)

        @property
        def part_analysis_case_with_contour_viewable(
            self: "SystemDeflectionViewable._Cast_SystemDeflectionViewable",
        ) -> "_2260.PartAnalysisCaseWithContourViewable":
            from mastapy.system_model.drawing import _2260

            return self._parent._cast(_2260.PartAnalysisCaseWithContourViewable)

        @property
        def system_deflection_viewable(
            self: "SystemDeflectionViewable._Cast_SystemDeflectionViewable",
        ) -> "SystemDeflectionViewable":
            return self._parent

        def __getattr__(
            self: "SystemDeflectionViewable._Cast_SystemDeflectionViewable", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemDeflectionViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SystemDeflectionViewable._Cast_SystemDeflectionViewable":
        return self._Cast_SystemDeflectionViewable(self)
