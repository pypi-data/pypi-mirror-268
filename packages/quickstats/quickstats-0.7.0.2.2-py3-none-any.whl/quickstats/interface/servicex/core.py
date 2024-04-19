from typing import Optional
from functools import partial

import httpx
from servicex.configuration import Configuration

read_bak = Configuration.read
AsyncClient_bak = httpx.AsyncClient

__all__ = ["set_cache_path", "set_async_client_timeout"]

def set_cache_path(cache_path:Optional[str]=None):
    def overwrite_read(cls, config_path: Optional[str] = None):
        if config_path:
            yaml_config = Configuration._add_from_path(Path(config_path), walk_up_tree=False)
        else:
            yaml_config = Configuration._add_from_path(walk_up_tree=True)

        if yaml_config:
            yaml_config['cache_path'] = cache_path
            return Configuration(**yaml_config)
        else:
            path_extra = f"in {config_path}" if config_path else ""
            raise NameError(
                "Can't find .servicex or servicex.yaml config file " + path_extra
            )
    if cache_path is None:
        Configuration.read = read_bak
    else:
        Configuration.read = classmethod(overwrite_read)

def set_async_client_timeout(timeout:Optional[float]=None,
                             connect:Optional[float]=None,
                             read:Optional[float]=None,
                             write:Optional[float]=None,
                             pool:Optional[float]=None,):
    timeout_spec = {}
    if connect is not None:
        timeout_spec['connect'] = connect
    if read is not None:
        timeout_spec['read'] = read
    if write is not None:
        timeout_spec['write'] = write
    if pool is not None:
        timeout_spec['pool'] = pool        
    timeout = httpx.Timeout(timeout, **timeout_spec)
    httpx.AsyncClient = partial(AsyncClient_bak, timeout=timeout)