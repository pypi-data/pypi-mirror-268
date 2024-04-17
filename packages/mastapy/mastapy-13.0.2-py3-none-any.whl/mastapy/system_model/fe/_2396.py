"""FESubstructureWithBatchOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_BATCH_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureWithBatchOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2390


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureWithBatchOptions",)


Self = TypeVar("Self", bound="FESubstructureWithBatchOptions")


class FESubstructureWithBatchOptions(_0.APIBase):
    """FESubstructureWithBatchOptions

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_BATCH_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FESubstructureWithBatchOptions")

    class _Cast_FESubstructureWithBatchOptions:
        """Special nested class for casting FESubstructureWithBatchOptions to subclasses."""

        def __init__(
            self: "FESubstructureWithBatchOptions._Cast_FESubstructureWithBatchOptions",
            parent: "FESubstructureWithBatchOptions",
        ):
            self._parent = parent

        @property
        def fe_substructure_with_batch_options(
            self: "FESubstructureWithBatchOptions._Cast_FESubstructureWithBatchOptions",
        ) -> "FESubstructureWithBatchOptions":
            return self._parent

        def __getattr__(
            self: "FESubstructureWithBatchOptions._Cast_FESubstructureWithBatchOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FESubstructureWithBatchOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_substructure(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FESubstructure

        if temp is None:
            return ""

        return temp

    @property
    def load_mesh_and_vectors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LoadMeshAndVectors

        if temp is None:
            return False

        return temp

    @load_mesh_and_vectors.setter
    @enforce_parameter_types
    def load_mesh_and_vectors(self: Self, value: "bool"):
        self.wrapped.LoadMeshAndVectors = bool(value) if value is not None else False

    @property
    def load_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LoadMesh

        if temp is None:
            return False

        return temp

    @load_mesh.setter
    @enforce_parameter_types
    def load_mesh(self: Self, value: "bool"):
        self.wrapped.LoadMesh = bool(value) if value is not None else False

    @property
    def load_vectors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LoadVectors

        if temp is None:
            return False

        return temp

    @load_vectors.setter
    @enforce_parameter_types
    def load_vectors(self: Self, value: "bool"):
        self.wrapped.LoadVectors = bool(value) if value is not None else False

    @property
    def run_condensation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RunCondensation

        if temp is None:
            return False

        return temp

    @run_condensation.setter
    @enforce_parameter_types
    def run_condensation(self: Self, value: "bool"):
        self.wrapped.RunCondensation = bool(value) if value is not None else False

    @property
    def unload_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UnloadMesh

        if temp is None:
            return False

        return temp

    @unload_mesh.setter
    @enforce_parameter_types
    def unload_mesh(self: Self, value: "bool"):
        self.wrapped.UnloadMesh = bool(value) if value is not None else False

    @property
    def unload_vectors(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UnloadVectors

        if temp is None:
            return False

        return temp

    @unload_vectors.setter
    @enforce_parameter_types
    def unload_vectors(self: Self, value: "bool"):
        self.wrapped.UnloadVectors = bool(value) if value is not None else False

    @property
    def fe(self: Self) -> "_2390.FESubstructure":
        """mastapy.system_model.fe.FESubstructure

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FE

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FESubstructureWithBatchOptions._Cast_FESubstructureWithBatchOptions":
        return self._Cast_FESubstructureWithBatchOptions(self)
