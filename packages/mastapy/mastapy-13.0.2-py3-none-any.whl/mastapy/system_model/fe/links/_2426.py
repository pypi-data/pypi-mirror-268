"""ElectricMachineStatorFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.fe.links import _2432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "ElectricMachineStatorFELink"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2381
    from mastapy.system_model.fe.links import _2425


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorFELink",)


Self = TypeVar("Self", bound="ElectricMachineStatorFELink")


class ElectricMachineStatorFELink(_2432.MultiNodeFELink):
    """ElectricMachineStatorFELink

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_FE_LINK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineStatorFELink")

    class _Cast_ElectricMachineStatorFELink:
        """Special nested class for casting ElectricMachineStatorFELink to subclasses."""

        def __init__(
            self: "ElectricMachineStatorFELink._Cast_ElectricMachineStatorFELink",
            parent: "ElectricMachineStatorFELink",
        ):
            self._parent = parent

        @property
        def multi_node_fe_link(
            self: "ElectricMachineStatorFELink._Cast_ElectricMachineStatorFELink",
        ) -> "_2432.MultiNodeFELink":
            return self._parent._cast(_2432.MultiNodeFELink)

        @property
        def fe_link(
            self: "ElectricMachineStatorFELink._Cast_ElectricMachineStatorFELink",
        ) -> "_2425.FELink":
            from mastapy.system_model.fe.links import _2425

            return self._parent._cast(_2425.FELink)

        @property
        def electric_machine_stator_fe_link(
            self: "ElectricMachineStatorFELink._Cast_ElectricMachineStatorFELink",
        ) -> "ElectricMachineStatorFELink":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorFELink._Cast_ElectricMachineStatorFELink",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineStatorFELink.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_dynamic_load_data(
        self: Self,
    ) -> "_2381.ElectricMachineDynamicLoadData":
        """mastapy.system_model.fe.ElectricMachineDynamicLoadData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDynamicLoadData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorFELink._Cast_ElectricMachineStatorFELink":
        return self._Cast_ElectricMachineStatorFELink(self)
