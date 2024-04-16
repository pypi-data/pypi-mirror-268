# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nested_config']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8,<3.0.0',
 'single-version>=1.6.0,<2.0.0',
 'typing-extensions>=4.6.0,<5.0.0']

extras_require = \
{':python_version < "3.11"': ['tomli>=2.0.0,<3.0.0'],
 'yaml': ['pyyaml>=5.1.0,<7.0.0']}

setup_kwargs = {
    'name': 'nested-config',
    'version': '2.0.3.post0',
    'description': 'Parse configuration files that include paths to other config files into Pydantic modelinstances. Also support pathlib.PurePath on Pydantic 1.8+.',
    'long_description': '# nested-config README\n\n**nested-config** provides for parsing configuration files that include paths to other\nconfig files into [Pydantic](https://github.com/samuelcolvin/pydantic/) model instances.\nIt also supports validating and JSON-encoding `pathlib.PurePath` on Pydantic 1.8+.\n\n## Usage\n\n### Config loading\n\n**nested-config** may be used in your project in two main ways.\n\n1. You may simply call `nested_config.validate_config()` with a config file path and a\n   Pydantic model which may or may not include nested Pydantic models. If there are nested\n   models and the config file has string values for those fields, those values are\n   interpreted as paths to other config files and those are recursively read into their\n   respective Pydantic models using `validate_config()`. The `default_suffix` kwarg allows\n   for specifying the file suffix (extension) to assume if the config file has no suffix\n   or its suffix is not in the `nested_config.config_dict_loaders` dict.\n\n   Example including mixed configuration file types and `default_suffix` (Note that PyYAML\n   is an extra dependency required for parsing yaml files):\n\n   **house.yaml**\n\n   ```yaml\n   name: my house\n   dimensions: dimensions\n   ```\n\n   **dimensions** (TOML type)\n\n   ```toml\n   length = 10\n   width = 20\n   ```\n\n   **parse_house.py**\n\n   ```python\n   import pydantic\n   import yaml\n\n   from nested_config import validate_config\n\n   class Dimensions(pydantic.BaseModel):\n       length: int\n       width: int\n\n\n   class House(pydantic.BaseModel):\n       name: str\n       dimensions: Dimensions\n\n\n   house = validate_config("house.yaml", House, default_suffix=".toml")\n   house  # House(name=\'my house\', dimensions=Dimensions(length=10, width=20))\n   ```\n\n2. Alternatively, you can use `nested_config.BaseModel` which subclasses\n   `pydantic.BaseModel` and adds a `from_config` classmethod:\n\n   **house.toml**\n\n   ```toml\n   name = "my house"\n   dimensions = "dimensions.toml"\n   ```\n\n   **dimensions.toml**\n\n   ```toml\n   length = 12.6\n   width = 25.3\n   ```\n\n   **parse_house.py**\n\n   ```python\n   import nested_config\n\n   class Dimensions(nested_config.BaseModel):\n       length: float\n       width: float\n\n\n   class House(nested_config.BaseModel):\n       name: str\n       dimensions: Dimensions\n\n\n   house = House.from_config("house.toml", House)\n   house  # House(name=\'my house\', dimensions=Dimensions(length=12.6, width=25.3))\n   ```\n\n   In this case, if you need to specify a default loader, just use\n   `nested_config.set_default_loader(suffix)` before using `BaseModel.from_config()`.\n\nSee [tests](https://gitlab.com/osu-nrsg/nested-config/-/tree/master/tests) for more\ndetailed use-cases, such as where the root pydantic model contains lists or dicts of other\nmodels and when those may be included in the root config file or specified as paths to\nsub-config files.\n\n### Included loaders\n\n**nested-config** automatically loads the following files based on extension:\n\n| Format | Extensions(s) | Library                                    |\n| ------ | ------------- | ------------------------------------------ |\n| JSON   | .json         | `json` (stdlib)                            |\n| TOML   | .toml         | `tomllib` (Python 3.11+ stdlib) or `tomli` |\n| YAML   | .yaml, .yml   | `pyyaml` (extra dependency[^yaml-extra])   |\n\n### Adding loaders\n\nTo add a loader for another file extension, simply update the `config_dict_loaders` dict:\n\n```python\nimport nested_config\nfrom nested_config import ConfigDict  # alias for dict[str, Any]\n\ndef dummy_loader(config_path: Path) -> ConfigDict:\n    return {"a": 1, "b": 2}\n\nnested_config.config_dict_loaders[".dmy"] = dummy_loader\n\n# or add another extension for an existing loader\nnested_config.config_dict_loaders[".jsn"] = nested_config.config_dict_loaders[".json"]\n```\n\n### `PurePath` handling\n\nA bonus feature of **nested-config** is that it provides for validation and JSON encoding\nof `pathlib.PurePath` and its subclasses in Pydantic <2.0 (this is built into Pydantic\n2.0+). All that is needed is an import of `nested_config`. Example:\n\n```python\nfrom pathlib import PurePosixPath\n\nimport nested_config\nimport pydantic\n\n\nclass RsyncDestination(pydantic.BaseModel):\n    remote_server: str\n    remote_path: PurePosixPath\n\n\ndest = RsyncDestination(remote_server="rsync.example.com", remote_path="/data/incoming")\n\ndest  # RsyncDestination(remote_server=\'rsync.example.com\', remote_path=PurePosixPath(\'/data/incoming\'))\ndest.json()  # \'{"remote_server":"rsync.example.com","remote_path":"/data/incoming"}\'\n\n```\n\n## Pydantic 1.0/2.0 Compatibility\n\nnested-config is runtime compatible with Pydantic 1.8+ and Pydantic 2.0.\n\nThe follow table gives info on how to configure the [mypy](https://www.mypy-lang.org/) and\n[Pyright](https://microsoft.github.io/pyright) type checkers to properly work, depending\non the version of Pydantic you are using.\n\n| Pydantic Version | [mypy config][1]            | mypy cli                    | [Pyright config][2]                         |\n|------------------|-----------------------------|-----------------------------|---------------------------------------------|\n| 2.0+             | `always_false = PYDANTIC_1` | `--always-false PYDANTIC_1` | `defineConstant = { "PYDANTIC_1" = false }` |\n| 1.8-1.10         | `always_true = PYDANTIC_1`  | `--always-true PYDANTIC_1`  | `defineConstant = { "PYDANTIC_1" = true }`  |\n\n## Footnotes\n\n[^yaml-extra]: Install `pyyaml` separately with `pip` or install **nested-config** with\n               `pip install nested-config[yaml]`.\n\n[1]: https://mypy.readthedocs.io/en/latest/config_file.html\n[2]: https://microsoft.github.io/pyright/#/configuration\n',
    'author': 'Randall Pittman',
    'author_email': 'pittmara@oregonstate.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/osu-nrsg/nested-config',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
