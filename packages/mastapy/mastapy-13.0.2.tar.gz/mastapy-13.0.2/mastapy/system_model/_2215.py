"""ElectricMachineGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel", "ElectricMachineGroup"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1268, _1274, _1293
    from mastapy.electric_machines.load_cases_and_analyses import _1367


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineGroup",)


Self = TypeVar("Self", bound="ElectricMachineGroup")


class ElectricMachineGroup(_0.APIBase):
    """ElectricMachineGroup

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineGroup")

    class _Cast_ElectricMachineGroup:
        """Special nested class for casting ElectricMachineGroup to subclasses."""

        def __init__(
            self: "ElectricMachineGroup._Cast_ElectricMachineGroup",
            parent: "ElectricMachineGroup",
        ):
            self._parent = parent

        @property
        def electric_machine_group(
            self: "ElectricMachineGroup._Cast_ElectricMachineGroup",
        ) -> "ElectricMachineGroup":
            return self._parent

        def __getattr__(
            self: "ElectricMachineGroup._Cast_ElectricMachineGroup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_details(self: Self) -> "List[_1268.ElectricMachineDetail]":
        """List[mastapy.electric_machines.ElectricMachineDetail]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def electric_machine_load_case_groups(
        self: Self,
    ) -> "List[_1367.ElectricMachineLoadCaseGroup]":
        """List[mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineLoadCaseGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def add_electric_machine_detail(
        self: Self, type_: "_1274.ElectricMachineType", name: "str" = "Motor"
    ) -> "_1293.NonCADElectricMachineDetail":
        """mastapy.electric_machines.NonCADElectricMachineDetail

        Args:
            type_ (mastapy.electric_machines.ElectricMachineType)
            name (str, optional)
        """
        type_ = conversion.mp_to_pn_enum(
            type_, "SMT.MastaAPI.ElectricMachines.ElectricMachineType"
        )
        name = str(name)
        method_result = self.wrapped.AddElectricMachineDetail(
            type_, name if name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def add_load_case_group(
        self: Self, name: "str" = "New Load Case Group"
    ) -> "_1367.ElectricMachineLoadCaseGroup":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup

        Args:
            name (str, optional)
        """
        name = str(name)
        method_result = self.wrapped.AddLoadCaseGroup(name if name else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def duplicate_electric_machine_detail(
        self: Self, detail: "_1268.ElectricMachineDetail"
    ) -> "_1268.ElectricMachineDetail":
        """mastapy.electric_machines.ElectricMachineDetail

        Args:
            detail (mastapy.electric_machines.ElectricMachineDetail)
        """
        method_result = self.wrapped.DuplicateElectricMachineDetail(
            detail.wrapped if detail else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def electric_machine_detail_named(
        self: Self, name: "str", has_non_linear_dq_model: "bool"
    ) -> "_1268.ElectricMachineDetail":
        """mastapy.electric_machines.ElectricMachineDetail

        Args:
            name (str)
            has_non_linear_dq_model (bool)
        """
        name = str(name)
        has_non_linear_dq_model = bool(has_non_linear_dq_model)
        method_result = self.wrapped.ElectricMachineDetailNamed(
            name if name else "",
            has_non_linear_dq_model if has_non_linear_dq_model else False,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def load_case_group_named(
        self: Self, load_case_group_name: "str"
    ) -> "_1367.ElectricMachineLoadCaseGroup":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup

        Args:
            load_case_group_name (str)
        """
        load_case_group_name = str(load_case_group_name)
        method_result = self.wrapped.LoadCaseGroupNamed(
            load_case_group_name if load_case_group_name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def remove_all_electric_machine_details(self: Self):
        """Method does not return."""
        self.wrapped.RemoveAllElectricMachineDetails()

    def remove_all_load_case_groups(self: Self):
        """Method does not return."""
        self.wrapped.RemoveAllLoadCaseGroups()

    @enforce_parameter_types
    def remove_electric_machine_detail(
        self: Self, motor: "_1268.ElectricMachineDetail"
    ) -> "bool":
        """bool

        Args:
            motor (mastapy.electric_machines.ElectricMachineDetail)
        """
        method_result = self.wrapped.RemoveElectricMachineDetail(
            motor.wrapped if motor else None
        )
        return method_result

    @enforce_parameter_types
    def remove_electric_machine_detail_named(
        self: Self, name: "str", has_non_linear_dq_model: "bool"
    ) -> "bool":
        """bool

        Args:
            name (str)
            has_non_linear_dq_model (bool)
        """
        name = str(name)
        has_non_linear_dq_model = bool(has_non_linear_dq_model)
        method_result = self.wrapped.RemoveElectricMachineDetailNamed(
            name if name else "",
            has_non_linear_dq_model if has_non_linear_dq_model else False,
        )
        return method_result

    @enforce_parameter_types
    def remove_load_case_group_named(self: Self, name: "str") -> "bool":
        """bool

        Args:
            name (str)
        """
        name = str(name)
        method_result = self.wrapped.RemoveLoadCaseGroupNamed(name if name else "")
        return method_result

    @enforce_parameter_types
    def try_remove_load_case_group(
        self: Self, load_case_group: "_1367.ElectricMachineLoadCaseGroup"
    ) -> "bool":
        """bool

        Args:
            load_case_group (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup)
        """
        method_result = self.wrapped.TryRemoveLoadCaseGroup(
            load_case_group.wrapped if load_case_group else None
        )
        return method_result

    @property
    def cast_to(self: Self) -> "ElectricMachineGroup._Cast_ElectricMachineGroup":
        return self._Cast_ElectricMachineGroup(self)
