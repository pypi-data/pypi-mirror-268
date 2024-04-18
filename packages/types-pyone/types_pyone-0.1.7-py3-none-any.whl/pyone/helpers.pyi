# Stub file for the helpers module within the PyONE library

from typing import Any, Dict, Optional

from . import OneException

# Extend the base exception for specific helper errors
class OneHelperException(OneException): ...

# Typing details for the function interacting with XMLRPC server
def marketapp_export(one: Any, appid: int, dsid: Optional[int] = None, name: Optional[str] = None, vmtemplate_name: Optional[str] = None) -> Dict[str, int]: ...
