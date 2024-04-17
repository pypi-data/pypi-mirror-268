"""MeshingOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.nodal_analysis import _61
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESHING_OPTIONS = python_net_import("SMT.MastaAPI.NodalAnalysis", "MeshingOptions")


__docformat__ = "restructuredtext en"
__all__ = ("MeshingOptions",)


Self = TypeVar("Self", bound="MeshingOptions")


class MeshingOptions(_61.FEMeshingOptions):
    """MeshingOptions

    This is a mastapy class.
    """

    TYPE = _MESHING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshingOptions")

    class _Cast_MeshingOptions:
        """Special nested class for casting MeshingOptions to subclasses."""

        def __init__(
            self: "MeshingOptions._Cast_MeshingOptions", parent: "MeshingOptions"
        ):
            self._parent = parent

        @property
        def fe_meshing_options(
            self: "MeshingOptions._Cast_MeshingOptions",
        ) -> "_61.FEMeshingOptions":
            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def meshing_options(
            self: "MeshingOptions._Cast_MeshingOptions",
        ) -> "MeshingOptions":
            return self._parent

        def __getattr__(self: "MeshingOptions._Cast_MeshingOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_size.setter
    @enforce_parameter_types
    def element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementSize = value

    @property
    def cast_to(self: Self) -> "MeshingOptions._Cast_MeshingOptions":
        return self._Cast_MeshingOptions(self)
