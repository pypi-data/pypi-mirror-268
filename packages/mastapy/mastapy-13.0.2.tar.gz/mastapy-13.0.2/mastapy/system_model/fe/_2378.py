"""DegreeOfFreedomBoundaryConditionAngular"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.fe import _2377
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DEGREE_OF_FREEDOM_BOUNDARY_CONDITION_ANGULAR = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "DegreeOfFreedomBoundaryConditionAngular"
)


__docformat__ = "restructuredtext en"
__all__ = ("DegreeOfFreedomBoundaryConditionAngular",)


Self = TypeVar("Self", bound="DegreeOfFreedomBoundaryConditionAngular")


class DegreeOfFreedomBoundaryConditionAngular(_2377.DegreeOfFreedomBoundaryCondition):
    """DegreeOfFreedomBoundaryConditionAngular

    This is a mastapy class.
    """

    TYPE = _DEGREE_OF_FREEDOM_BOUNDARY_CONDITION_ANGULAR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DegreeOfFreedomBoundaryConditionAngular"
    )

    class _Cast_DegreeOfFreedomBoundaryConditionAngular:
        """Special nested class for casting DegreeOfFreedomBoundaryConditionAngular to subclasses."""

        def __init__(
            self: "DegreeOfFreedomBoundaryConditionAngular._Cast_DegreeOfFreedomBoundaryConditionAngular",
            parent: "DegreeOfFreedomBoundaryConditionAngular",
        ):
            self._parent = parent

        @property
        def degree_of_freedom_boundary_condition(
            self: "DegreeOfFreedomBoundaryConditionAngular._Cast_DegreeOfFreedomBoundaryConditionAngular",
        ) -> "_2377.DegreeOfFreedomBoundaryCondition":
            return self._parent._cast(_2377.DegreeOfFreedomBoundaryCondition)

        @property
        def degree_of_freedom_boundary_condition_angular(
            self: "DegreeOfFreedomBoundaryConditionAngular._Cast_DegreeOfFreedomBoundaryConditionAngular",
        ) -> "DegreeOfFreedomBoundaryConditionAngular":
            return self._parent

        def __getattr__(
            self: "DegreeOfFreedomBoundaryConditionAngular._Cast_DegreeOfFreedomBoundaryConditionAngular",
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
        self: Self, instance_to_wrap: "DegreeOfFreedomBoundaryConditionAngular.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Angle = value

    @property
    def torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @torque.setter
    @enforce_parameter_types
    def torque(self: Self, value: "float"):
        self.wrapped.Torque = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "DegreeOfFreedomBoundaryConditionAngular._Cast_DegreeOfFreedomBoundaryConditionAngular":
        return self._Cast_DegreeOfFreedomBoundaryConditionAngular(self)
