"""ElectricMachineMechanicalAnalysisMeshingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.electric_machines import _1272
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MECHANICAL_ANALYSIS_MESHING_OPTIONS = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "ElectricMachineMechanicalAnalysisMeshingOptions"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _61


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineMechanicalAnalysisMeshingOptions",)


Self = TypeVar("Self", bound="ElectricMachineMechanicalAnalysisMeshingOptions")


class ElectricMachineMechanicalAnalysisMeshingOptions(
    _1272.ElectricMachineMeshingOptionsBase
):
    """ElectricMachineMechanicalAnalysisMeshingOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MECHANICAL_ANALYSIS_MESHING_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineMechanicalAnalysisMeshingOptions"
    )

    class _Cast_ElectricMachineMechanicalAnalysisMeshingOptions:
        """Special nested class for casting ElectricMachineMechanicalAnalysisMeshingOptions to subclasses."""

        def __init__(
            self: "ElectricMachineMechanicalAnalysisMeshingOptions._Cast_ElectricMachineMechanicalAnalysisMeshingOptions",
            parent: "ElectricMachineMechanicalAnalysisMeshingOptions",
        ):
            self._parent = parent

        @property
        def electric_machine_meshing_options_base(
            self: "ElectricMachineMechanicalAnalysisMeshingOptions._Cast_ElectricMachineMechanicalAnalysisMeshingOptions",
        ) -> "_1272.ElectricMachineMeshingOptionsBase":
            return self._parent._cast(_1272.ElectricMachineMeshingOptionsBase)

        @property
        def fe_meshing_options(
            self: "ElectricMachineMechanicalAnalysisMeshingOptions._Cast_ElectricMachineMechanicalAnalysisMeshingOptions",
        ) -> "_61.FEMeshingOptions":
            from mastapy.nodal_analysis import _61

            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def electric_machine_mechanical_analysis_meshing_options(
            self: "ElectricMachineMechanicalAnalysisMeshingOptions._Cast_ElectricMachineMechanicalAnalysisMeshingOptions",
        ) -> "ElectricMachineMechanicalAnalysisMeshingOptions":
            return self._parent

        def __getattr__(
            self: "ElectricMachineMechanicalAnalysisMeshingOptions._Cast_ElectricMachineMechanicalAnalysisMeshingOptions",
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
        self: Self,
        instance_to_wrap: "ElectricMachineMechanicalAnalysisMeshingOptions.TYPE",
    ):
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
    def cast_to(
        self: Self,
    ) -> "ElectricMachineMechanicalAnalysisMeshingOptions._Cast_ElectricMachineMechanicalAnalysisMeshingOptions":
        return self._Cast_ElectricMachineMechanicalAnalysisMeshingOptions(self)
