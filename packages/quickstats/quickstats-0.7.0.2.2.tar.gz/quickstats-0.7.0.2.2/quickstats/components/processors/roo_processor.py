from typing import Optional, List, Dict, Union
import os
import glob
import json
import time
import ROOT

from .builtin_methods import BUILTIN_METHODS
from .actions import *
from .roo_process_config import RooProcessConfig

from quickstats import timer, AbstractObject, PathManager, GeneralEnum
from quickstats.interface.root import TFile, RDataFrame, RDataFrameBackend
from quickstats.interface.xrootd import get_cachedir, set_cachedir, switch_cachedir
from quickstats.utils.root_utils import declare_expression, close_all_root_files, set_multithread
from quickstats.utils.path_utils import is_remote_path
from quickstats.utils.common_utils import get_cpu_count

class RDFVerbosity(GeneralEnum):
    UNSET   = (0, 'kUnset')
    FATAL   = (1, 'kFatal')
    ERROR   = (2, 'kError')
    WARNING = (3, 'kWarning')
    INFO    = (4, 'kInfo')
    DEBUG   = (5, 'kDebug')

    def __new__(cls, value:int, key:str):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.key = key
        return obj

class RooProcessor(AbstractObject):

    @property
    def distributed(self):
        return self.backend != RDataFrameBackend.DEFAULT
        
    def __init__(self, config_source:Optional[Union[RooProcessConfig, str]]=None,
                 config_text:Optional[str]=None,
                 flags:Optional[List[str]]=None,
                 backend:Optional[str]=None,
                 backend_options:Optional[Dict]=None,
                 multithread:int=True,
                 cache:bool=False,
                 use_template:bool=False,
                 verbosity:Optional[Union[int, str]]="INFO"):
        super().__init__(verbosity=verbosity)
        self.cache = cache
        self.action_tree = None
        if flags is not None:
            self.flags = list(flags)
        else:
            self.flags = []
        self.rdf_frames = {}
        self.rdf = None
        self.global_variables = {}
        self.external_variables = {}
        self.default_treename = None
        self.use_template = use_template
        self.rdf_verbosity = None
        self.result_metadata = None
        if backend is None:
            self.backend = RDataFrameBackend.DEFAULT
        else:
            self.backend = RDataFrameBackend.parse(backend)
        self.backend_options = backend_options
        self.set_remote_file_options(localize=False,
                                     cachedir=get_cachedir())
        self.set_profile_options()
        self.load_buildin_functions()

        self.set_multithread(multithread)
        
        if config_source is not None:
            self.load_config(config_source)

    def set_multithread(self, num_threads:Optional[int]=None):
        if num_threads is None:
            num_threads = self.multithread
        num_threads = set_multithread(num_threads)
        if num_threads is None:
            self.stdout.info("Disabled multithreading.")
        else:
            self.stdout.info(f"Enabled multithreading with {num_threads} threads.")
        self.multithread = num_threads
            
    def set_cache(self, cache:bool=True):
        self.cache = cache
        
    def set_remote_file_options(self, localize:bool=False,
                                cache:bool=True, cachedir:Optional[str]="/tmp",
                                copy_options:Optional[Dict]=None):
        remote_file_options = {
            'localize': localize,
            'cache': cache,
            'cachedir': cachedir,
            'copy_options': copy_options
        }
        self.remote_file_options = remote_file_options

    def set_profile_options(self, throughput:bool=False):
        profile_options = {
            "throughput": throughput
        }
        self.profile_options = profile_options
            
    def load_buildin_functions(self):
        # bug of redefining module from ROOT
        try:
            import ROOT
            Internal = ROOT.Internal
        except:
            Internal = None
        distributed = self.distributed
        for name, definition in BUILTIN_METHODS.items():
            declare_expression(definition, name, distributed=distributed)
        if Internal is not None:
            if Internal != ROOT.Internal:
                ROOT.Internal = Internal
    
    def load_config(self, config_source:Union[RooProcessConfig, str]):
        if isinstance(config_source, RooProcessConfig):
            config = config_source
        else:
            config = RooProcessConfig.open(config_source)
        self.config = config
        action_tree = config.get_action_tree()
        action_tree.construct_actions(rdf_backend=self.backend)
        if not action_tree.root_node.has_child:
            raise RuntimeError("no actions found in the process card")
        first_action = action_tree.root_node.first_child.action
        if isinstance(first_action, RooProcTreeName):
            self.default_treename = first_action._params['treename']
        else:
            self.default_treename = None
        self.action_tree = action_tree
        
    def set_global_variables(self, **kwargs):
        self.global_variables.update(kwargs)
        
    def clear_global_variables(self):
        self.global_variables = {}
    
    def add_flags(self, flags:List[str]):
        self.flags += list(flags)
        
    def set_flags(self, flags:List[str]):
        self.flags = list(flags)        
        
    def cleanup(self, deepclean:bool=True):
        close_all_root_files()
        if deepclean:
            self.rdf_frames = {}
            self.rdf = None
            
    def shallow_cleanup(self):
        self.cleanup(deepclean=False)
    
    def run_action(self, action:RooProcBaseAction):
        if not self.rdf:
            raise RuntimeError("RDataFrame instance not initialized")
        if isinstance(action, RooProcRDFAction):
            self.rdf = action.execute(self.rdf, self.global_variables)
        elif isinstance(action, RooProcHelperAction):
            action.execute(self, self.global_variables)
        elif isinstance(action, RooProcHybridAction):
            self.rdf, _ = action.execute(self.rdf, self, self.global_variables)
        elif isinstance(action, RooProcNestedAction):
            return_code = action.execute(self, self.global_variables)
            return return_code
        else:
            raise RuntimeError("unknown action type")
        return RooProcReturnCode.NORMAL
            
    def run_all_actions(self, consider_child:bool=True):
        if not self.action_tree:
            raise RuntimeError("action tree not initialized")
        node = self.action_tree.get_next(consider_child=consider_child)
        if node is not None:
            source = node.try_get_data("source", None)
            self.stdout.debug(f'Executing node "{node.name}" defined at line {node.data["start_line_number"]}'
                             f' (source {source})')
            action = node.action
            return_code = self.run_action(action)
            if return_code == RooProcReturnCode.NORMAL:
                self.run_all_actions()
            elif return_code == RooProcReturnCode.SKIP_CHILD:
                self.run_all_actions(consider_child=False)
            else:
                raise RuntimeError("unknown return code")
        else:
            self.stdout.debug('All node executed')
            
    def sanity_check(self):
        if not self.action_tree:
            raise RuntimeError("action tree not initialized")        
        if not self.action_tree.root_node.has_child:
            self.stdout.warning("No actions to be performed.")
            return None

    @staticmethod
    def _has_remote_files(filenames:List[str]):
        return any(is_remote_path(filename) for filename in filenames)

    def list_files(self, filenames:List[str], resolve_cache:bool=True):
        cachedir = self.remote_file_options['cachedir']
        with switch_cachedir(cachedir):
            files = TFile.list_files(filenames, resolve_cache=resolve_cache,
                                     raise_on_error=False)
        return files

    def resolve_filenames(self, filenames:Union[List[str], str]):
        filenames = self.list_files(filenames, resolve_cache=True)
        if not filenames:
            return []
        has_remote_file = self._has_remote_files(filenames)
        # copy remote files to local storage
        if has_remote_file and self.remote_file_options['localize']:
            remote_files = [filename for filename in filenames if is_remote_path(filename)]
            self._copy_remote_files(remote_files)
            filenames = self.list_files(filenames, resolve_cache=True)
        return filenames

    def _copy_remote_files(self, filenames:List[str]):
        opts = self.remote_file_options
        copy_options = opts.get('copy_options', None)
        if copy_options is None:
            copy_options = {}
        TFile.copy_remote_files(filenames, cache=opts['cache'],
                                 cachedir=opts['cachedir'],
                                 **copy_options)
        
    def load_rdf(self,
                 filenames:Union[List[str], str],
                 treename:Optional[str]=None):
            
        filenames = self.resolve_filenames(filenames)
        if not filenames:
            self.stdout.info('No files to be processed. Skipping.')
            return None
        self._filenames = filenames

        if treename is None:
            treename = self.default_treename
        if treename is None:
            treename = TFile._get_main_treename(filenames[0])
            self.stdout.info(f"Using deduced treename: {treename}")

        if len(filenames) == 1:
            self.stdout.info(f'Processing file "{filenames[0]}".')
        else:
            self.stdout.info("Professing files")
            for filename in filenames:
                self.stdout.info(f'  "{filename}"', bare=True)
                
        rdf = RDataFrame.from_files(filenames, treename=treename,
                                    backend=self.backend,
                                    backend_options=self.backend_options,
                                    multithread_safe=self.multithread)
        self.rdf = rdf
        return self
    
    def run(self, filenames:Optional[Union[List[str], str]]=None):
        self.sanity_check()
        with timer() as t:
            if filenames is not None:
                self.load_rdf(filenames)
            self.action_tree.reset()
            self.run_all_actions()
            self.shallow_cleanup()
        self.stdout.info(f"Task finished. Total time taken: {t.interval:.3f} s.")
        result_metadata = {
            "files": list(self._filenames),
            "real_time": t.real_time_elapsed,
            "cpu_time": t.cpu_time_elapsed
        }
        self.result_metadata = result_metadata
        return self

    def get_rdf(self, frame:Optional[str]=None):
        rdf = self.rdf if frame is None else self.rdf_frames.get(frame, None)
        if rdf is None:
            raise RuntimeError('RDataFrame instance not initialized')
        return rdf

    def get_referenced_columns(self):
        action_tree = self.action_tree
        return action_tree.get_referenced_columns(self.global_variables)
        
    def awkward_array(self, frame:Optional[str]=None,
                      columns:Optional[List[str]]=None):
        rdf = self.get_rdf(frame)
        return RDataFrame._awkward_array(rdf, columns=columns)

    def display(self, frame:Optional[str]=None,
                columns:Union[str, List[str]]="",
                n_rows:int=5, n_max_collection_elements:int=10,
                lazy:bool=False):
        rdf = self.get_rdf(frame)
        result = self.rdf.Display(columns, n_rows, n_max_collection_elements)
        if not lazy:
            result.Print()
            return None
        return result

    def save_graph(self, frame:Optional[str]=None,
                   filename:Optional[str]=None):
        rdf = self.get_rdf(frame)
        if filename:
            ROOT.RDF.SaveGraph(rdf, filename)
        else:
            ROOT.RDF.SaveGraph(rdf)

    def set_rdf_verbosity(self, verbosity:str='INFO'):
        if isinstance(verbosity, str):
            verbosity = RDFVerbosity.parse(verbosity)
            loglevel = getattr(ROOT.Experimental.ELogLevel, verbosity.key)
        else:
            loglevel = verbosity
        verb = ROOT.Experimental.RLogScopedVerbosity(ROOT.Detail.RDF.RDFLogChannel(), loglevel)
        self.rdf_verbosity = verb