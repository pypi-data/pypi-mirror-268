"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2349 import ClutchConnection
    from ._2350 import ClutchSocket
    from ._2351 import ConceptCouplingConnection
    from ._2352 import ConceptCouplingSocket
    from ._2353 import CouplingConnection
    from ._2354 import CouplingSocket
    from ._2355 import PartToPartShearCouplingConnection
    from ._2356 import PartToPartShearCouplingSocket
    from ._2357 import SpringDamperConnection
    from ._2358 import SpringDamperSocket
    from ._2359 import TorqueConverterConnection
    from ._2360 import TorqueConverterPumpSocket
    from ._2361 import TorqueConverterTurbineSocket
else:
    import_structure = {
        "_2349": ["ClutchConnection"],
        "_2350": ["ClutchSocket"],
        "_2351": ["ConceptCouplingConnection"],
        "_2352": ["ConceptCouplingSocket"],
        "_2353": ["CouplingConnection"],
        "_2354": ["CouplingSocket"],
        "_2355": ["PartToPartShearCouplingConnection"],
        "_2356": ["PartToPartShearCouplingSocket"],
        "_2357": ["SpringDamperConnection"],
        "_2358": ["SpringDamperSocket"],
        "_2359": ["TorqueConverterConnection"],
        "_2360": ["TorqueConverterPumpSocket"],
        "_2361": ["TorqueConverterTurbineSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClutchConnection",
    "ClutchSocket",
    "ConceptCouplingConnection",
    "ConceptCouplingSocket",
    "CouplingConnection",
    "CouplingSocket",
    "PartToPartShearCouplingConnection",
    "PartToPartShearCouplingSocket",
    "SpringDamperConnection",
    "SpringDamperSocket",
    "TorqueConverterConnection",
    "TorqueConverterPumpSocket",
    "TorqueConverterTurbineSocket",
)
