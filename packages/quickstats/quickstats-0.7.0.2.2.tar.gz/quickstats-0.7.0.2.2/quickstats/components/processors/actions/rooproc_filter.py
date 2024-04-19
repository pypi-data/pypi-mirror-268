from typing import Optional
import re

from .rooproc_rdf_action import RooProcRDFAction
from .auxiliary import register_action

@register_action
class RooProcFilter(RooProcRDFAction):
    
    NAME = "FILTER"
    
    def __init__(self, expression:str, name:Optional[str]=None):
        super().__init__(expression=expression,
                         name=name)
        
    @classmethod
    def parse(cls, main_text:str, block_text:Optional[str]=None):
        name_literals = re.findall(r"@{([^{}]+)}", main_text)
        if len(name_literals) == 0:
            name = main_text.strip()
            expression = name
        elif len(name_literals) == 1:
            name = name_literals[0]
            expression = main_text.replace("@{" + name + "}", "").strip()
        else:
            raise RuntimeError(f"multiple filter names detected in the expression `{main_text}`")
        return cls(name=name, expression=expression)
        
    def _execute(self, rdf:"ROOT.RDataFrame", **params):
        expression = params['expression']
        name = params.get("name", None)
        if name is not None:
            rdf_next = rdf.Filter(expression, name)
        else:
            rdf_next = rdf.Filter(expression)
        return rdf_next