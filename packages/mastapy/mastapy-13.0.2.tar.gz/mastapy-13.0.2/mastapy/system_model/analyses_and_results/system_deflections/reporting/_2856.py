"""RigidlyConnectedComponentGroupSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results import _2660
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGIDLY_CONNECTED_COMPONENT_GROUP_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting",
    "RigidlyConnectedComponentGroupSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1525
    from mastapy.system_model.analyses_and_results.system_deflections import _2723


__docformat__ = "restructuredtext en"
__all__ = ("RigidlyConnectedComponentGroupSystemDeflection",)


Self = TypeVar("Self", bound="RigidlyConnectedComponentGroupSystemDeflection")


class RigidlyConnectedComponentGroupSystemDeflection(_2660.DesignEntityGroupAnalysis):
    """RigidlyConnectedComponentGroupSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RIGIDLY_CONNECTED_COMPONENT_GROUP_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RigidlyConnectedComponentGroupSystemDeflection"
    )

    class _Cast_RigidlyConnectedComponentGroupSystemDeflection:
        """Special nested class for casting RigidlyConnectedComponentGroupSystemDeflection to subclasses."""

        def __init__(
            self: "RigidlyConnectedComponentGroupSystemDeflection._Cast_RigidlyConnectedComponentGroupSystemDeflection",
            parent: "RigidlyConnectedComponentGroupSystemDeflection",
        ):
            self._parent = parent

        @property
        def design_entity_group_analysis(
            self: "RigidlyConnectedComponentGroupSystemDeflection._Cast_RigidlyConnectedComponentGroupSystemDeflection",
        ) -> "_2660.DesignEntityGroupAnalysis":
            return self._parent._cast(_2660.DesignEntityGroupAnalysis)

        @property
        def rigidly_connected_component_group_system_deflection(
            self: "RigidlyConnectedComponentGroupSystemDeflection._Cast_RigidlyConnectedComponentGroupSystemDeflection",
        ) -> "RigidlyConnectedComponentGroupSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RigidlyConnectedComponentGroupSystemDeflection._Cast_RigidlyConnectedComponentGroupSystemDeflection",
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
        instance_to_wrap: "RigidlyConnectedComponentGroupSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_properties(self: Self) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def components(self: Self) -> "List[_2723.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Components

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RigidlyConnectedComponentGroupSystemDeflection._Cast_RigidlyConnectedComponentGroupSystemDeflection":
        return self._Cast_RigidlyConnectedComponentGroupSystemDeflection(self)
