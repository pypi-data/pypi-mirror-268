from typing import Optional, List

import numpy as np

from .rooproc_output_action import RooProcOutputAction
from .auxiliary import register_action

from quickstats import module_exist
from quickstats.utils.common_utils import is_valid_file
from quickstats.interface.root import RDataFrameBackend

@register_action
class RooProcAsHDF(RooProcOutputAction):
    
    NAME = "AS_HDF"
    
    def __init__(self, filename:str, key:str,
                 columns:Optional[List[str]],
                 exclude:Optional[List[str]]=None):
        super().__init__(filename=filename,
                         columns=columns,
                         key=key)

    def _execute(self, rdf:"ROOT.RDataFrame", processor:"quickstats.RooProcessor", **params):
        filename = params['filename']
        key = params['key']
        if processor.cache and is_valid_file(filename):
            processor.stdout.info(f'Cached output from "{filename}".')
            return rdf, processor
        processor.stdout.info(f'Writing output to "{filename}".')
        import awkward as ak
        import pandas as pd
        columns = params.get('columns', None)
        exclude = params.get('exclude', None)
        save_columns = self.get_save_columns(rdf, processor, columns=columns,
                                             exclude=exclude,
                                             mode="REMOVE_NON_STANDARD_TYPE")
        array = None
        if module_exist('awkward'):
            try:
                import awkward as ak
                # NB: RDF Dask/Spark does not support GetColumnType yet
                if processor.backend in [RDataFrameBackend.DASK, RDataFrameBackend.SPARK]:
                    rdf.GetColumnType = rdf._headnode._localdf.GetColumnType
                array = ak.from_rdataframe(rdf, columns=save_columns)
                array = ak.to_numpy(array)
            except:
                array = None
                processor.stdout.warning("Failed to convert output to numpy arrays with awkward backend. "
                                         "Falling back to use ROOT instead")
        if array is None:
            array = rdf.AsNumpy(save_columns)
        df = pd.DataFrame(array)
        self.makedirs(filename)
        df.to_hdf(filename, key=key)
        return rdf, processor