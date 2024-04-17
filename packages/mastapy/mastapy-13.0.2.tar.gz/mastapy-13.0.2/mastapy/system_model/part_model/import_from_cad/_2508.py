"""CylindricalRingGearFromCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.import_from_cad import _2506
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_RING_GEAR_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "CylindricalRingGearFromCAD"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.import_from_cad import _2505, _2511, _2502


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalRingGearFromCAD",)


Self = TypeVar("Self", bound="CylindricalRingGearFromCAD")


class CylindricalRingGearFromCAD(_2506.CylindricalGearInPlanetarySetFromCAD):
    """CylindricalRingGearFromCAD

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_RING_GEAR_FROM_CAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalRingGearFromCAD")

    class _Cast_CylindricalRingGearFromCAD:
        """Special nested class for casting CylindricalRingGearFromCAD to subclasses."""

        def __init__(
            self: "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD",
            parent: "CylindricalRingGearFromCAD",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_in_planetary_set_from_cad(
            self: "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD",
        ) -> "_2506.CylindricalGearInPlanetarySetFromCAD":
            return self._parent._cast(_2506.CylindricalGearInPlanetarySetFromCAD)

        @property
        def cylindrical_gear_from_cad(
            self: "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD",
        ) -> "_2505.CylindricalGearFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2505

            return self._parent._cast(_2505.CylindricalGearFromCAD)

        @property
        def mountable_component_from_cad(
            self: "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD",
        ) -> "_2511.MountableComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2511

            return self._parent._cast(_2511.MountableComponentFromCAD)

        @property
        def component_from_cad(
            self: "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD",
        ) -> "_2502.ComponentFromCAD":
            from mastapy.system_model.part_model.import_from_cad import _2502

            return self._parent._cast(_2502.ComponentFromCAD)

        @property
        def cylindrical_ring_gear_from_cad(
            self: "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD",
        ) -> "CylindricalRingGearFromCAD":
            return self._parent

        def __getattr__(
            self: "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalRingGearFromCAD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalRingGearFromCAD._Cast_CylindricalRingGearFromCAD":
        return self._Cast_CylindricalRingGearFromCAD(self)
