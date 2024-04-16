from mindsdb.integrations.libs.const import HANDLER_TYPE

from .__about__ import __version__ as version, __description__ as description
try:
    from .byom_handler import BYOMHandler as Handler, connection_args
    import_error = None
except Exception as e:
    Handler = None
    import_error = e


title = 'BYOM'
name = 'byom'
type = HANDLER_TYPE.ML
icon_path = "icon.svg"

__all__ = [
    'Handler', 'version', 'name', 'type', 'title', 'description', 'connection_args'
]

