"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2272 import AbstractShaftToMountableComponentConnection
    from ._2273 import BearingInnerSocket
    from ._2274 import BearingOuterSocket
    from ._2275 import BeltConnection
    from ._2276 import CoaxialConnection
    from ._2277 import ComponentConnection
    from ._2278 import ComponentMeasurer
    from ._2279 import Connection
    from ._2280 import CVTBeltConnection
    from ._2281 import CVTPulleySocket
    from ._2282 import CylindricalComponentConnection
    from ._2283 import CylindricalSocket
    from ._2284 import DatumMeasurement
    from ._2285 import ElectricMachineStatorSocket
    from ._2286 import InnerShaftSocket
    from ._2287 import InnerShaftSocketBase
    from ._2288 import InterMountableComponentConnection
    from ._2289 import MountableComponentInnerSocket
    from ._2290 import MountableComponentOuterSocket
    from ._2291 import MountableComponentSocket
    from ._2292 import OuterShaftSocket
    from ._2293 import OuterShaftSocketBase
    from ._2294 import PlanetaryConnection
    from ._2295 import PlanetarySocket
    from ._2296 import PlanetarySocketBase
    from ._2297 import PulleySocket
    from ._2298 import RealignmentResult
    from ._2299 import RollingRingConnection
    from ._2300 import RollingRingSocket
    from ._2301 import ShaftSocket
    from ._2302 import ShaftToMountableComponentConnection
    from ._2303 import Socket
    from ._2304 import SocketConnectionOptions
    from ._2305 import SocketConnectionSelection
else:
    import_structure = {
        "_2272": ["AbstractShaftToMountableComponentConnection"],
        "_2273": ["BearingInnerSocket"],
        "_2274": ["BearingOuterSocket"],
        "_2275": ["BeltConnection"],
        "_2276": ["CoaxialConnection"],
        "_2277": ["ComponentConnection"],
        "_2278": ["ComponentMeasurer"],
        "_2279": ["Connection"],
        "_2280": ["CVTBeltConnection"],
        "_2281": ["CVTPulleySocket"],
        "_2282": ["CylindricalComponentConnection"],
        "_2283": ["CylindricalSocket"],
        "_2284": ["DatumMeasurement"],
        "_2285": ["ElectricMachineStatorSocket"],
        "_2286": ["InnerShaftSocket"],
        "_2287": ["InnerShaftSocketBase"],
        "_2288": ["InterMountableComponentConnection"],
        "_2289": ["MountableComponentInnerSocket"],
        "_2290": ["MountableComponentOuterSocket"],
        "_2291": ["MountableComponentSocket"],
        "_2292": ["OuterShaftSocket"],
        "_2293": ["OuterShaftSocketBase"],
        "_2294": ["PlanetaryConnection"],
        "_2295": ["PlanetarySocket"],
        "_2296": ["PlanetarySocketBase"],
        "_2297": ["PulleySocket"],
        "_2298": ["RealignmentResult"],
        "_2299": ["RollingRingConnection"],
        "_2300": ["RollingRingSocket"],
        "_2301": ["ShaftSocket"],
        "_2302": ["ShaftToMountableComponentConnection"],
        "_2303": ["Socket"],
        "_2304": ["SocketConnectionOptions"],
        "_2305": ["SocketConnectionSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)
