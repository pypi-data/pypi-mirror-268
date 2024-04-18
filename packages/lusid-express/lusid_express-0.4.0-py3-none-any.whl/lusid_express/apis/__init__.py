import os as __os
from lumipy.client import Client as __Client
import lusid.api as __apis
from lusid.utilities import ApiClientFactory as __ApiClientFactory
from lusidjam import RefreshingToken as __RefreshingToken

def __camel_to_snake(name):
    import re
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()



__secrets_path = __os.getenv("FBN_SECRETS_PATH")

__api_factory = __ApiClientFactory(
    token=__RefreshingToken(),
    api_secrets_filename=__secrets_path,
    app_name="LusidJupyterNotebook",
)
__api_exports = []

def __create_api_variables(api_factory, module):
    """
    Create and export variables for each API class in the given module.
    The variables will be named in the format <name>_api where <name> is the lowercase class name.
    Adds each variable name to the __all__ list for module exports.
    """
    global __api_exports
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and attr_name.endswith('Api'):
            variable_name = __camel_to_snake(attr_name[:-3]) + '_api'
            globals()[variable_name] = api_factory.build(attr)
            __api_exports.append(variable_name)


__create_api_variables(__api_factory, __apis)


__api_exports.append(__Client(api_secrets_filename=__os.environ.get('FBN_SECRETS_PATH',None)))
__all__ = __api_exports