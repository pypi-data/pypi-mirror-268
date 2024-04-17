"""GearFEModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.analysis import _1227
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_GEAR_FLANKS = python_net_import("SMT.MastaAPI.Gears", "GearFlanks")
_GEAR_FE_MODEL = python_net_import("SMT.MastaAPI.Gears.FEModel", "GearFEModel")

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1205
    from mastapy import _7567
    from mastapy.gears import _329
    from mastapy.gears.fe_model.cylindrical import _1207
    from mastapy.gears.fe_model.conical import _1210
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("GearFEModel",)


Self = TypeVar("Self", bound="GearFEModel")


class GearFEModel(_1227.GearImplementationDetail):
    """GearFEModel

    This is a mastapy class.
    """

    TYPE = _GEAR_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearFEModel")

    class _Cast_GearFEModel:
        """Special nested class for casting GearFEModel to subclasses."""

        def __init__(self: "GearFEModel._Cast_GearFEModel", parent: "GearFEModel"):
            self._parent = parent

        @property
        def gear_implementation_detail(
            self: "GearFEModel._Cast_GearFEModel",
        ) -> "_1227.GearImplementationDetail":
            return self._parent._cast(_1227.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "GearFEModel._Cast_GearFEModel",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearFEModel._Cast_GearFEModel",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_fe_model(
            self: "GearFEModel._Cast_GearFEModel",
        ) -> "_1207.CylindricalGearFEModel":
            from mastapy.gears.fe_model.cylindrical import _1207

            return self._parent._cast(_1207.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "GearFEModel._Cast_GearFEModel",
        ) -> "_1210.ConicalGearFEModel":
            from mastapy.gears.fe_model.conical import _1210

            return self._parent._cast(_1210.ConicalGearFEModel)

        @property
        def gear_fe_model(self: "GearFEModel._Cast_GearFEModel") -> "GearFEModel":
            return self._parent

        def __getattr__(self: "GearFEModel._Cast_GearFEModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_bore(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FEBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @fe_bore.setter
    @enforce_parameter_types
    def fe_bore(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FEBore = value

    @property
    def include_all_teeth_in_the_fe_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeAllTeethInTheFEMesh

        if temp is None:
            return False

        return temp

    @include_all_teeth_in_the_fe_mesh.setter
    @enforce_parameter_types
    def include_all_teeth_in_the_fe_mesh(self: Self, value: "bool"):
        self.wrapped.IncludeAllTeethInTheFEMesh = (
            bool(value) if value is not None else False
        )

    @property
    def element_settings(self: Self) -> "_1205.GearMeshingElementOptions":
        """mastapy.gears.fe_model.GearMeshingElementOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def calculate_stiffness_from_fe(self: Self):
        """Method does not return."""
        self.wrapped.CalculateStiffnessFromFE()

    @enforce_parameter_types
    def calculate_stiffness_from_fe_with_progress(
        self: Self, progress: "_7567.TaskProgress"
    ):
        """Method does not return.

        Args:
            progress (mastapy.TaskProgress)
        """
        self.wrapped.CalculateStiffnessFromFE.Overloads[_TASK_PROGRESS](
            progress.wrapped if progress else None
        )

    @enforce_parameter_types
    def get_stress_influence_coefficients_from_fe(self: Self, flank: "_329.GearFlanks"):
        """Method does not return.

        Args:
            flank (mastapy.gears.GearFlanks)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        self.wrapped.GetStressInfluenceCoefficientsFromFE.Overloads[_GEAR_FLANKS](flank)

    @enforce_parameter_types
    def get_stress_influence_coefficients_from_fe_with_progress(
        self: Self, flank: "_329.GearFlanks", progress: "_7567.TaskProgress"
    ):
        """Method does not return.

        Args:
            flank (mastapy.gears.GearFlanks)
            progress (mastapy.TaskProgress)
        """
        flank = conversion.mp_to_pn_enum(flank, "SMT.MastaAPI.Gears.GearFlanks")
        self.wrapped.GetStressInfluenceCoefficientsFromFE.Overloads[
            _GEAR_FLANKS, _TASK_PROGRESS
        ](flank, progress.wrapped if progress else None)

    @property
    def cast_to(self: Self) -> "GearFEModel._Cast_GearFEModel":
        return self._Cast_GearFEModel(self)
