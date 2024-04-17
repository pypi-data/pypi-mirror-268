"""DegreeOfFreedomBoundaryConditionLinear"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.fe import _2377
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEGREE_OF_FREEDOM_BOUNDARY_CONDITION_LINEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "DegreeOfFreedomBoundaryConditionLinear"
)


__docformat__ = "restructuredtext en"
__all__ = ("DegreeOfFreedomBoundaryConditionLinear",)


Self = TypeVar("Self", bound="DegreeOfFreedomBoundaryConditionLinear")


class DegreeOfFreedomBoundaryConditionLinear(_2377.DegreeOfFreedomBoundaryCondition):
    """DegreeOfFreedomBoundaryConditionLinear

    This is a mastapy class.
    """

    TYPE = _DEGREE_OF_FREEDOM_BOUNDARY_CONDITION_LINEAR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DegreeOfFreedomBoundaryConditionLinear"
    )

    class _Cast_DegreeOfFreedomBoundaryConditionLinear:
        """Special nested class for casting DegreeOfFreedomBoundaryConditionLinear to subclasses."""

        def __init__(
            self: "DegreeOfFreedomBoundaryConditionLinear._Cast_DegreeOfFreedomBoundaryConditionLinear",
            parent: "DegreeOfFreedomBoundaryConditionLinear",
        ):
            self._parent = parent

        @property
        def degree_of_freedom_boundary_condition(
            self: "DegreeOfFreedomBoundaryConditionLinear._Cast_DegreeOfFreedomBoundaryConditionLinear",
        ) -> "_2377.DegreeOfFreedomBoundaryCondition":
            return self._parent._cast(_2377.DegreeOfFreedomBoundaryCondition)

        @property
        def degree_of_freedom_boundary_condition_linear(
            self: "DegreeOfFreedomBoundaryConditionLinear._Cast_DegreeOfFreedomBoundaryConditionLinear",
        ) -> "DegreeOfFreedomBoundaryConditionLinear":
            return self._parent

        def __getattr__(
            self: "DegreeOfFreedomBoundaryConditionLinear._Cast_DegreeOfFreedomBoundaryConditionLinear",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "DegreeOfFreedomBoundaryConditionLinear.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def displacement(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Displacement

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @displacement.setter
    @enforce_parameter_types
    def displacement(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Displacement = value

    @property
    def force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Force

        if temp is None:
            return 0.0

        return temp

    @force.setter
    @enforce_parameter_types
    def force(self: Self, value: "float"):
        self.wrapped.Force = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "DegreeOfFreedomBoundaryConditionLinear._Cast_DegreeOfFreedomBoundaryConditionLinear":
        return self._Cast_DegreeOfFreedomBoundaryConditionLinear(self)
