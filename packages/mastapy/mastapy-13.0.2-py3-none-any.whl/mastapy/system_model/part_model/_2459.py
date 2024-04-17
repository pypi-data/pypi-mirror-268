"""ExternalCADModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model import _2451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModel",)


Self = TypeVar("Self", bound="ExternalCADModel")


class ExternalCADModel(_2451.Component):
    """ExternalCADModel

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModel")

    class _Cast_ExternalCADModel:
        """Special nested class for casting ExternalCADModel to subclasses."""

        def __init__(
            self: "ExternalCADModel._Cast_ExternalCADModel", parent: "ExternalCADModel"
        ):
            self._parent = parent

        @property
        def component(
            self: "ExternalCADModel._Cast_ExternalCADModel",
        ) -> "_2451.Component":
            return self._parent._cast(_2451.Component)

        @property
        def part(self: "ExternalCADModel._Cast_ExternalCADModel") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "ExternalCADModel._Cast_ExternalCADModel",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def external_cad_model(
            self: "ExternalCADModel._Cast_ExternalCADModel",
        ) -> "ExternalCADModel":
            return self._parent

        def __getattr__(self: "ExternalCADModel._Cast_ExternalCADModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalCADModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def draw_two_sided(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawTwoSided

        if temp is None:
            return False

        return temp

    @draw_two_sided.setter
    @enforce_parameter_types
    def draw_two_sided(self: Self, value: "bool"):
        self.wrapped.DrawTwoSided = bool(value) if value is not None else False

    @property
    def opacity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Opacity

        if temp is None:
            return 0.0

        return temp

    @opacity.setter
    @enforce_parameter_types
    def opacity(self: Self, value: "float"):
        self.wrapped.Opacity = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ExternalCADModel._Cast_ExternalCADModel":
        return self._Cast_ExternalCADModel(self)
