__software__ = "Barkshark Lib"
"Name of the library"

__version_info__ = (0, 1, 0)
"Version of the library"

__version__ = ".".join(str(v) for v in __version_info__)
"Version of the library in string form"


from .application import Application
from .transport import AsyncTransport

from .enums import (
	Enum,
	IntEnum,
	IntFlagEnum,
	StrEnum,
	FileSizeUnit,
	FileType,
	HttpMethod,
	HttpStatus,
	ProtocolPort,
	XdgDir
)

from .errors import (
	Error,
	ErrorCode,
	FileError
)

# todo: convert these errors to use the new Error class
from .errors import (
	HttpError

)

from .misc import (
	catch_errors,
	convert_to_boolean,
	convert_to_bytes,
	convert_to_string,
	deprecated,
	get_object_name,
	get_object_properties,
	get_top_domain,
	http_request,
	is_loop_running,
	random_str,
	time_function,
	time_function_pprint,
	DictProperty,
	Env,
	FileSize,
	HttpDate,
	JsonBase,
	NamedTuple,
	RunData

)

from .objects import (
	Object,
	Signal
)

from .path import (
	File,
	Path
)

from .router import (
	Match,
	Route,
	Router
)

from .url import (
	Query,
	Url
)
