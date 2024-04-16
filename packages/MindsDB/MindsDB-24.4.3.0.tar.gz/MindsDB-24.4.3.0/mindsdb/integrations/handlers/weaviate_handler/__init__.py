from mindsdb.integrations.libs.const import HANDLER_TYPE

from .__about__ import __description__ as description
from .__about__ import __version__ as version

try:
    from .weaviate_handler import WeaviateDBHandler as Handler
    from .weaviate_handler import connection_args, connection_args_example

    import_error = None
except Exception as e:
    Handler = None
    import_error = e

title = "Weaviate"
name = "weaviate"
type = HANDLER_TYPE.DATA
icon_path = "icon.svg"

__all__ = [
    "Handler",
    "version",
    "name",
    "type",
    "title",
    "description",
    "connection_args",
    "connection_args_example",
    "import_error",
    "icon_path",
]
