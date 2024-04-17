"""NodalMatrixEditorWrapperColumn"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_MATRIX_EDITOR_WRAPPER_COLUMN = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "NodalMatrixEditorWrapperColumn"
)


__docformat__ = "restructuredtext en"
__all__ = ("NodalMatrixEditorWrapperColumn",)


Self = TypeVar("Self", bound="NodalMatrixEditorWrapperColumn")


class NodalMatrixEditorWrapperColumn(_0.APIBase):
    """NodalMatrixEditorWrapperColumn

    This is a mastapy class.
    """

    TYPE = _NODAL_MATRIX_EDITOR_WRAPPER_COLUMN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalMatrixEditorWrapperColumn")

    class _Cast_NodalMatrixEditorWrapperColumn:
        """Special nested class for casting NodalMatrixEditorWrapperColumn to subclasses."""

        def __init__(
            self: "NodalMatrixEditorWrapperColumn._Cast_NodalMatrixEditorWrapperColumn",
            parent: "NodalMatrixEditorWrapperColumn",
        ):
            self._parent = parent

        @property
        def nodal_matrix_editor_wrapper_column(
            self: "NodalMatrixEditorWrapperColumn._Cast_NodalMatrixEditorWrapperColumn",
        ) -> "NodalMatrixEditorWrapperColumn":
            return self._parent

        def __getattr__(
            self: "NodalMatrixEditorWrapperColumn._Cast_NodalMatrixEditorWrapperColumn",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalMatrixEditorWrapperColumn.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def node_1_theta_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node1ThetaX

        if temp is None:
            return 0.0

        return temp

    @node_1_theta_x.setter
    @enforce_parameter_types
    def node_1_theta_x(self: Self, value: "float"):
        self.wrapped.Node1ThetaX = float(value) if value is not None else 0.0

    @property
    def node_1_theta_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node1ThetaY

        if temp is None:
            return 0.0

        return temp

    @node_1_theta_y.setter
    @enforce_parameter_types
    def node_1_theta_y(self: Self, value: "float"):
        self.wrapped.Node1ThetaY = float(value) if value is not None else 0.0

    @property
    def node_1_theta_z(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node1ThetaZ

        if temp is None:
            return 0.0

        return temp

    @node_1_theta_z.setter
    @enforce_parameter_types
    def node_1_theta_z(self: Self, value: "float"):
        self.wrapped.Node1ThetaZ = float(value) if value is not None else 0.0

    @property
    def node_1x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node1X

        if temp is None:
            return 0.0

        return temp

    @node_1x.setter
    @enforce_parameter_types
    def node_1x(self: Self, value: "float"):
        self.wrapped.Node1X = float(value) if value is not None else 0.0

    @property
    def node_1y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node1Y

        if temp is None:
            return 0.0

        return temp

    @node_1y.setter
    @enforce_parameter_types
    def node_1y(self: Self, value: "float"):
        self.wrapped.Node1Y = float(value) if value is not None else 0.0

    @property
    def node_1z(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node1Z

        if temp is None:
            return 0.0

        return temp

    @node_1z.setter
    @enforce_parameter_types
    def node_1z(self: Self, value: "float"):
        self.wrapped.Node1Z = float(value) if value is not None else 0.0

    @property
    def node_2_theta_x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node2ThetaX

        if temp is None:
            return 0.0

        return temp

    @node_2_theta_x.setter
    @enforce_parameter_types
    def node_2_theta_x(self: Self, value: "float"):
        self.wrapped.Node2ThetaX = float(value) if value is not None else 0.0

    @property
    def node_2_theta_y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node2ThetaY

        if temp is None:
            return 0.0

        return temp

    @node_2_theta_y.setter
    @enforce_parameter_types
    def node_2_theta_y(self: Self, value: "float"):
        self.wrapped.Node2ThetaY = float(value) if value is not None else 0.0

    @property
    def node_2_theta_z(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node2ThetaZ

        if temp is None:
            return 0.0

        return temp

    @node_2_theta_z.setter
    @enforce_parameter_types
    def node_2_theta_z(self: Self, value: "float"):
        self.wrapped.Node2ThetaZ = float(value) if value is not None else 0.0

    @property
    def node_2x(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node2X

        if temp is None:
            return 0.0

        return temp

    @node_2x.setter
    @enforce_parameter_types
    def node_2x(self: Self, value: "float"):
        self.wrapped.Node2X = float(value) if value is not None else 0.0

    @property
    def node_2y(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node2Y

        if temp is None:
            return 0.0

        return temp

    @node_2y.setter
    @enforce_parameter_types
    def node_2y(self: Self, value: "float"):
        self.wrapped.Node2Y = float(value) if value is not None else 0.0

    @property
    def node_2z(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Node2Z

        if temp is None:
            return 0.0

        return temp

    @node_2z.setter
    @enforce_parameter_types
    def node_2z(self: Self, value: "float"):
        self.wrapped.Node2Z = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "NodalMatrixEditorWrapperColumn._Cast_NodalMatrixEditorWrapperColumn":
        return self._Cast_NodalMatrixEditorWrapperColumn(self)
