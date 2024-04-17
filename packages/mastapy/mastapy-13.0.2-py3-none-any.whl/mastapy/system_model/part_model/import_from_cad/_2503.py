"""ConceptBearingFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_BEARING_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "ConceptBearingFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import _2511, _2502


__docformat__ = "restructuredtext en"
__all__ = ("ConceptBearingFromCAD",)


Self = TypeVar("Self", bound="ConceptBearingFromCAD")


class ConceptBearingFromCAD(_2504.ConnectorFromCAD):
    """ConceptBearingFromCAD

    This is a mastapy class.
    """

    TYPE = _CONCEPT_BEARING_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptBearingFromCAD")

    class _Cast_ConceptBearingFromCAD:
        """Special nested class for casting ConceptBearingFromCAD to subclasses."""

        def __init__(
            self: "ConceptBearingFromCAD._Cast_ConceptBearingFromCAD",
            parent: "ConceptBearingFromCAD",
        ):
            self._parent = parent

        @property
        def connector_from_cad(
            self: "ConceptBearingFromCAD._Cast_ConceptBearingFromCAD",
        ) -> "_2504.ConnectorFromCAD":
            return self._parent._cast(_2504.ConnectorFromCAD)

        @property
        def mountable_component_from_cad(
            self: "ConceptBearingFromCAD._Cast_ConceptBearingFromCAD",
        ) -> "_2511.MountableComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2511

            return self._parent._cast(_2511.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "ConceptBearingFromCAD._Cast_ConceptBearingFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def concept_bearing_from_cad(
            self: "ConceptBearingFromCAD._Cast_ConceptBearingFromCAD",
        ) -> "ConceptBearingFromCAD":
            return self._parent

        def __getattr__(
            self: "ConceptBearingFromCAD._Cast_ConceptBearingFromCAD", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptBearingFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConceptBearingFromCAD._Cast_ConceptBearingFromCAD":
        return self._Cast_ConceptBearingFromCAD(self)
