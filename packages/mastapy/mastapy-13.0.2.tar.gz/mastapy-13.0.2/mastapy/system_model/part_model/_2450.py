"""BoltedJoint"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model import _2483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint")

if TYPE_CHECKING:
    from mastapy.bolts import _1485
    from mastapy.system_model.part_model import _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJoint",)


Self = TypeVar("Self", bound="BoltedJoint")


class BoltedJoint(_2483.SpecialisedAssembly):
    """BoltedJoint

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJoint")

    class _Cast_BoltedJoint:
        """Special nested class for casting BoltedJoint to subclasses."""

        def __init__(self: "BoltedJoint._Cast_BoltedJoint", parent: "BoltedJoint"):
            self._parent = parent

        @property
        def specialised_assembly(
            self: "BoltedJoint._Cast_BoltedJoint",
        ) -> "_2483.SpecialisedAssembly":
            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "BoltedJoint._Cast_BoltedJoint",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "BoltedJoint._Cast_BoltedJoint") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "BoltedJoint._Cast_BoltedJoint",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bolted_joint(self: "BoltedJoint._Cast_BoltedJoint") -> "BoltedJoint":
            return self._parent

        def __getattr__(self: "BoltedJoint._Cast_BoltedJoint", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def detailed_bolted_joint(self: Self) -> "_1485.DetailedBoltedJointDesign":
        """mastapy.bolts.DetailedBoltedJointDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DetailedBoltedJoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BoltedJoint._Cast_BoltedJoint":
        return self._Cast_BoltedJoint(self)
