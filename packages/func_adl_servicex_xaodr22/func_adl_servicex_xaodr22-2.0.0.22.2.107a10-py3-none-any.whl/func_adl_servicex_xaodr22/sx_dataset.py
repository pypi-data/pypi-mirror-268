from typing import Union
from func_adl_servicex.ServiceX import ServiceXSourceCPPBase
from servicex.servicex import ServiceXDataset
from servicex.utils import DatasetType
from .event_collection import Event


class SXDSAtlasxAODR22(ServiceXSourceCPPBase[Event]):
    def __init__(self, sx: Union[ServiceXDataset, DatasetType], backend="atlasr22"):
        """
        Create a servicex dataset sequence from a servicex dataset.
        """
        super().__init__(sx, backend, item_type=Event)


class SXDSAtlasxAODR22PHYS(ServiceXSourceCPPBase[Event]):
    def __init__(self, sx: Union[ServiceXDataset, DatasetType], backend="atlasr22"):
        """
        Create a servicex dataset sequence from a servicex dataset.
        """
        super().__init__(sx, backend, item_type=Event)
        # Do update-in-place to configure the calibration
        from .calibration_support import calib_tools
        new_sx = calib_tools.query_update(self, calib_tools.default_config("PHYS"))
        self._q_ast = new_sx._q_ast


class SXDSAtlasxAODR22PHYSLITE(ServiceXSourceCPPBase[Event]):
    def __init__(self, sx: Union[ServiceXDataset, DatasetType], backend="atlasr22"):
        """
        Create a servicex dataset sequence from a servicex dataset.
        """
        super().__init__(sx, backend, item_type=Event)
        # Do update-in-place to configure the calibration
        from .calibration_support import calib_tools
        new_sx = calib_tools.query_update(self, calib_tools.default_config("PHYSLITE"))
        self._q_ast = new_sx._q_ast
