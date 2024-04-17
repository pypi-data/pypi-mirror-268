"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._206 import ContactPairReporting
    from ._207 import CoordinateSystemReporting
    from ._208 import DegreeOfFreedomType
    from ._209 import ElasticModulusOrthotropicComponents
    from ._210 import ElementDetailsForFEModel
    from ._211 import ElementPropertiesBase
    from ._212 import ElementPropertiesBeam
    from ._213 import ElementPropertiesInterface
    from ._214 import ElementPropertiesMass
    from ._215 import ElementPropertiesRigid
    from ._216 import ElementPropertiesShell
    from ._217 import ElementPropertiesSolid
    from ._218 import ElementPropertiesSpringDashpot
    from ._219 import ElementPropertiesWithMaterial
    from ._220 import MaterialPropertiesReporting
    from ._221 import NodeDetailsForFEModel
    from ._222 import PoissonRatioOrthotropicComponents
    from ._223 import RigidElementNodeDegreesOfFreedom
    from ._224 import ShearModulusOrthotropicComponents
    from ._225 import ThermalExpansionOrthotropicComponents
else:
    import_structure = {
        "_206": ["ContactPairReporting"],
        "_207": ["CoordinateSystemReporting"],
        "_208": ["DegreeOfFreedomType"],
        "_209": ["ElasticModulusOrthotropicComponents"],
        "_210": ["ElementDetailsForFEModel"],
        "_211": ["ElementPropertiesBase"],
        "_212": ["ElementPropertiesBeam"],
        "_213": ["ElementPropertiesInterface"],
        "_214": ["ElementPropertiesMass"],
        "_215": ["ElementPropertiesRigid"],
        "_216": ["ElementPropertiesShell"],
        "_217": ["ElementPropertiesSolid"],
        "_218": ["ElementPropertiesSpringDashpot"],
        "_219": ["ElementPropertiesWithMaterial"],
        "_220": ["MaterialPropertiesReporting"],
        "_221": ["NodeDetailsForFEModel"],
        "_222": ["PoissonRatioOrthotropicComponents"],
        "_223": ["RigidElementNodeDegreesOfFreedom"],
        "_224": ["ShearModulusOrthotropicComponents"],
        "_225": ["ThermalExpansionOrthotropicComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactPairReporting",
    "CoordinateSystemReporting",
    "DegreeOfFreedomType",
    "ElasticModulusOrthotropicComponents",
    "ElementDetailsForFEModel",
    "ElementPropertiesBase",
    "ElementPropertiesBeam",
    "ElementPropertiesInterface",
    "ElementPropertiesMass",
    "ElementPropertiesRigid",
    "ElementPropertiesShell",
    "ElementPropertiesSolid",
    "ElementPropertiesSpringDashpot",
    "ElementPropertiesWithMaterial",
    "MaterialPropertiesReporting",
    "NodeDetailsForFEModel",
    "PoissonRatioOrthotropicComponents",
    "RigidElementNodeDegreesOfFreedom",
    "ShearModulusOrthotropicComponents",
    "ThermalExpansionOrthotropicComponents",
)
