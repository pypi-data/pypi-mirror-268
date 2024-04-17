"""ConicalGearFEModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.fe_model import _1203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Conical", "ConicalGearFEModel"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1227, _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearFEModel",)


Self = TypeVar("Self", bound="ConicalGearFEModel")


class ConicalGearFEModel(_1203.GearFEModel):
    """ConicalGearFEModel

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearFEModel")

    class _Cast_ConicalGearFEModel:
        """Special nested class for casting ConicalGearFEModel to subclasses."""

        def __init__(
            self: "ConicalGearFEModel._Cast_ConicalGearFEModel",
            parent: "ConicalGearFEModel",
        ):
            self._parent = parent

        @property
        def gear_fe_model(
            self: "ConicalGearFEModel._Cast_ConicalGearFEModel",
        ) -> "_1203.GearFEModel":
            return self._parent._cast(_1203.GearFEModel)

        @property
        def gear_implementation_detail(
            self: "ConicalGearFEModel._Cast_ConicalGearFEModel",
        ) -> "_1227.GearImplementationDetail":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalGearFEModel._Cast_ConicalGearFEModel",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearFEModel._Cast_ConicalGearFEModel",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def conical_gear_fe_model(
            self: "ConicalGearFEModel._Cast_ConicalGearFEModel",
        ) -> "ConicalGearFEModel":
            return self._parent

        def __getattr__(self: "ConicalGearFEModel._Cast_ConicalGearFEModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalGearFEModel._Cast_ConicalGearFEModel":
        return self._Cast_ConicalGearFEModel(self)
