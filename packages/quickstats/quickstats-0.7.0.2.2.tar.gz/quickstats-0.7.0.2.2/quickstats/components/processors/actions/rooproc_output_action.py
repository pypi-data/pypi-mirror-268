from typing import Optional, List, Dict
import fnmatch

import numpy as np

from .rooproc_hybrid_action import RooProcHybridAction
from .formatter import ListFormatter
from quickstats.interface.root import RDataFrameBackend

from quickstats.utils.common_utils import is_valid_file, filter_by_wildcards
from quickstats.utils.data_conversion import root_datatypes, get_rdf_column_type, ConversionMode, reduce_vector_types

class RooProcOutputAction(RooProcHybridAction):

    PARAM_FORMATS = {
        'columns': ListFormatter,
        'exclude': ListFormatter
    }
    
    def __init__(self, filename:str, 
                 columns:Optional[List[str]]=None,
                 exclude:Optional[List[str]]=None,
                 **kwargs):
        super().__init__(filename=filename,
                         columns=columns,
                         **kwargs)
        
    @classmethod
    def parse(cls, main_text:str, block_text:Optional[str]=None):
        kwargs = cls.parse_as_kwargs(main_text)
        return cls._try_create(**kwargs)
    
    def get_save_columns(self, rdf, processor,
                         columns:Optional[List[str]]=None,
                         exclude:Optional[List[str]]=None,
                         mode:ConversionMode=ConversionMode.REMOVE_NON_STANDARD_TYPE):
        all_columns = list([str(col) for col in rdf.GetColumnNames()])
        
        save_columns = filter_by_wildcards(all_columns, columns)
        save_columns = filter_by_wildcards(save_columns, exclude, exclusion=True)
        save_columns = list(set(save_columns))
        
        if columns is None:
            columns = list(all_columns)
        if exclude is None:
            exclude = []

        save_columns = filter_by_wildcards(all_columns, columns)
        save_columns = filter_by_wildcards(save_columns, exclude, exclusion=True)

        mode = ConversionMode.parse(mode)
        if mode in [ConversionMode.REMOVE_NON_STANDARD_TYPE,
                    ConversionMode.REMOVE_NON_ARRAY_TYPE]:
            column_types = np.array([get_rdf_column_type(rdf, col) for col in save_columns])
            if mode == ConversionMode.REMOVE_NON_ARRAY_TYPE:
                column_types = reduce_vector_types(column_types)
            new_columns = list(np.array(save_columns)[np.where(np.isin(column_types, root_datatypes))])
            removed_columns = np.setdiff1d(save_columns, new_columns)
            if len(removed_columns) > 0:
                col_str = ", ".join(removed_columns)
                processor.stdout.warning("The following column(s) will be excluded from the output as they have "
                                         f"data types incompatible with the output format: {col_str}")
            save_columns = new_columns
        return save_columns

    def get_referenced_columns(self, global_vars:Optional[Dict]=None):
        params = self.get_formatted_parameters(global_vars, strict=False)
        columns = params.get("columns", None)
        if columns is None:
            columns = ["*"]
        exclude = params.get("exclude", None)
        if exclude is not None:
            self.stdout.warning("Column exclusion will not be applied when inferring referenced columns")
        return columns