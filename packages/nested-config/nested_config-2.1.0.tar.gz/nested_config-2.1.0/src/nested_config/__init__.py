"""nested_config - This package does two things:

1. It adds the ability to parse config files into Pydantic model instances, including
   config files that include string path references to other config files in place of
   sub-model instances.

       my_obj = validate_config("my_config.toml", MyConfigModel, loader=toml.load)

2. It adds PurePath, PurePosixPath, and PureWindowsPath validation and JSON-encoding to
   Pydantic v1 (these are already included in Pydantic 2.)
"""

try:
    # Don't require pydantic
    from nested_config._pydantic import (
        BaseModel,
        validate_config,
    )
except ImportError:
    pass

from nested_config.expand import expand_config
from nested_config.loaders import (
    ConfigLoaderError,
    NoLoaderError,
    config_dict_loaders,
)
from nested_config.version import __version__
