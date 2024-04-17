"""ConnectorFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.import_from_cad import _2511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "ConnectorFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import (
        _2510,
        _2503,
        _2514,
        _2515,
        _2502,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorFromCAD",)


Self = TypeVar("Self", bound="ConnectorFromCAD")


class ConnectorFromCAD(_2511.MountableComponentFromCAD):
    """ConnectorFromCAD

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorFromCAD")

    class _Cast_ConnectorFromCAD:
        """Special nested class for casting ConnectorFromCAD to subclasses."""

        def __init__(
            self: "ConnectorFromCAD._Cast_ConnectorFromCAD", parent: "ConnectorFromCAD"
        ):
            self._parent = parent

        @property
        def mountable_component_from_cad(
            self: "ConnectorFromCAD._Cast_ConnectorFromCAD",
        ) -> "_2511.MountableComponentFromCAD":
            return self._parent._cast(_2511.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "ConnectorFromCAD._Cast_ConnectorFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def concept_bearing_from_cad(
            self: "ConnectorFromCAD._Cast_ConnectorFromCAD",
        ) -> "_2503.ConceptBearingFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2503

            return self._parent._cast(_2503.ConceptBearingFromCAD)

        @property
        def rigid_connector_from_cad(
            self: "ConnectorFromCAD._Cast_ConnectorFromCAD",
        ) -> "_2514.RigidConnectorFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2514

            return self._parent._cast(_2514.RigidConnectorFromCAD)

        @property
        def rolling_bearing_from_cad(
            self: "ConnectorFromCAD._Cast_ConnectorFromCAD",
        ) -> "_2515.RollingBearingFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2515

            return self._parent._cast(_2515.RollingBearingFromCAD)

        @property
        def connector_from_cad(
            self: "ConnectorFromCAD._Cast_ConnectorFromCAD",
        ) -> "ConnectorFromCAD":
            return self._parent

        def __getattr__(self: "ConnectorFromCAD._Cast_ConnectorFromCAD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mounting(self: Self) -> "_2510.HousedOrMounted":
        """mastapy.system_model.part_model.import_from_cad.HousedOrMounted"""
        temp = self.wrapped.Mounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD.HousedOrMounted"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.import_from_cad._2510", "HousedOrMounted"
        )(value)

    @mounting.setter
    @enforce_parameter_types
    def mounting(self: Self, value: "_2510.HousedOrMounted"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD.HousedOrMounted"
        )
        self.wrapped.Mounting = value

    @property
    def cast_to(self: Self) -> "ConnectorFromCAD._Cast_ConnectorFromCAD":
        return self._Cast_ConnectorFromCAD(self)
