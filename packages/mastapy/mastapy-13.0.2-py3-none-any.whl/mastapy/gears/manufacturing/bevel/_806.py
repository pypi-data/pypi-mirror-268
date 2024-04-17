"""PinionConcave"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_CONCAVE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "PinionConcave"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel.basic_machine_settings import _826
    from mastapy.gears.manufacturing.bevel import _809


__docformat__ = "restructuredtext en"
__all__ = ("PinionConcave",)


Self = TypeVar("Self", bound="PinionConcave")


class PinionConcave(_0.APIBase):
    """PinionConcave

    This is a mastapy class.
    """

    TYPE = _PINION_CONCAVE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PinionConcave")

    class _Cast_PinionConcave:
        """Special nested class for casting PinionConcave to subclasses."""

        def __init__(
            self: "PinionConcave._Cast_PinionConcave", parent: "PinionConcave"
        ):
            self._parent = parent

        @property
        def pinion_concave(
            self: "PinionConcave._Cast_PinionConcave",
        ) -> "PinionConcave":
            return self._parent

        def __getattr__(self: "PinionConcave._Cast_PinionConcave", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PinionConcave.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_concave_ob_configuration(
        self: Self,
    ) -> "_826.BasicConicalGearMachineSettingsGenerated":
        """mastapy.gears.manufacturing.bevel.basic_machine_settings.BasicConicalGearMachineSettingsGenerated

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_cutter_parameters_concave(
        self: Self,
    ) -> "_809.PinionFinishMachineSettings":
        """mastapy.gears.manufacturing.bevel.PinionFinishMachineSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionCutterParametersConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PinionConcave._Cast_PinionConcave":
        return self._Cast_PinionConcave(self)
