"""RollingBearingFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.import_from_cad import _2504
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_BEARING_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "RollingBearingFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import _2511, _2502


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingFromCAD",)


Self = TypeVar("Self", bound="RollingBearingFromCAD")


class RollingBearingFromCAD(_2504.ConnectorFromCAD):
    """RollingBearingFromCAD

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingBearingFromCAD")

    class _Cast_RollingBearingFromCAD:
        """Special nested class for casting RollingBearingFromCAD to subclasses."""

        def __init__(
            self: "RollingBearingFromCAD._Cast_RollingBearingFromCAD",
            parent: "RollingBearingFromCAD",
        ):
            self._parent = parent

        @property
        def connector_from_cad(
            self: "RollingBearingFromCAD._Cast_RollingBearingFromCAD",
        ) -> "_2504.ConnectorFromCAD":
            return self._parent._cast(_2504.ConnectorFromCAD)

        @property
        def mountable_component_from_cad(
            self: "RollingBearingFromCAD._Cast_RollingBearingFromCAD",
        ) -> "_2511.MountableComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2511

            return self._parent._cast(_2511.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "RollingBearingFromCAD._Cast_RollingBearingFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def rolling_bearing_from_cad(
            self: "RollingBearingFromCAD._Cast_RollingBearingFromCAD",
        ) -> "RollingBearingFromCAD":
            return self._parent

        def __getattr__(
            self: "RollingBearingFromCAD._Cast_RollingBearingFromCAD", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingBearingFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "float"):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "RollingBearingFromCAD._Cast_RollingBearingFromCAD":
        return self._Cast_RollingBearingFromCAD(self)
