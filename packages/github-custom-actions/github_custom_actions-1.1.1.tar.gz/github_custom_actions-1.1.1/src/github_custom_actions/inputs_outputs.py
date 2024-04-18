"""Github Actions helper functions.

We want to support Python 3.7 that you still have on some self-hosted action runners.
So no fancy features like walrus operator, @cached_property, etc.
"""

import os
import typing
from collections.abc import MutableMapping
from pathlib import Path
from typing import Dict, Iterator, Union, List, Optional, Any

INPUT_PREFIX = "INPUT_"


class DocumentedEnvVars:
    """Documented environment variables.

    Lazy load attributes from environment variables.
    Only described attributes are loaded.
    Attributes with type Path converted accordingly, it the value is "" set to None.
    """

    # todo: should be readonly
    _type_hints_cache: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def _get_type_hints(cls) -> Dict[str, Any]:
        # Use cls.__name__ to ensure each subclass uses its own cache entry
        if cls.__name__ not in cls._type_hints_cache:
            cls._type_hints_cache[cls.__name__] = typing.get_type_hints(cls)
        return cls._type_hints_cache[cls.__name__]

    def attribute_to_env_var(self, name: str) -> str:
        """Convert attribute name to environment variable name."""
        return name.upper()

    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except AttributeError as exc:
            type_hints = self.__class__._get_type_hints()
            if name not in type_hints:
                raise AttributeError(f"Unknown {name}") from exc
            env_var_name = self.attribute_to_env_var(name)
            if env_var_name in os.environ:
                value: Optional[Union[str, Path]] = os.environ[env_var_name]

                # If the type hint is Path, convert the value to Path
                if type_hints[name] is Path:
                    value = Path(value) if value else None
                self.__dict__[name] = value
                return value
            raise


class ActionInputs(DocumentedEnvVars):  # pylint: disable=too-few-public-methods
    """GitHub Action input variables.

    Usage:
        class MyAction:
            @property
            def inputs(self):
                return InputProxy()

        action = MyAction()
        # to get action input `my-input` from environment var `INPUT_MY-INPUT`
        print(action.inputs.my_input)
    """

    def attribute_to_env_var(self, name: str) -> str:
        return INPUT_PREFIX + name.upper().replace("_", "-")


class ActionOutputs(MutableMapping):  # type: ignore
    """GitHub Actions output variables.

    Usage:
        class MyAction:
            @property
            def output(self):
                return OutputProxy()

        action = MyAction()
        action.output["my-output"] = "value"
    """

    def __init__(self) -> None:
        self.output_file_path: Path = Path(os.environ["GITHUB_OUTPUT"])
        self._output_keys: Optional[Dict[str, str]] = None

    def __getitem__(self, key: str) -> str:
        return self._get_output_keys[key]

    def __setitem__(self, key: str, value: str) -> None:
        self._get_output_keys[key] = value
        self._save_output_file()

    def __delitem__(self, key: str) -> None:
        del self._get_output_keys[key]
        self._save_output_file()

    def __iter__(self) -> Iterator[str]:
        return iter(self._get_output_keys)

    def __len__(self) -> int:
        return len(self._get_output_keys)

    def __contains__(self, key: object) -> bool:
        return key in self._get_output_keys

    @property
    def _get_output_keys(self) -> Dict[str, str]:
        """Load key-value pairs from a file, returning {} if the file does not exist."""
        if self._output_keys is None:
            try:
                content = self.output_file_path.read_text(encoding="utf-8")
                self._output_keys = dict(
                    (line.split("=", 1) for line in content.splitlines() if "=" in line)
                )
            except FileNotFoundError:
                self._output_keys = {}
        return self._output_keys

    def _save_output_file(self) -> None:
        self.output_file_path.parent.mkdir(parents=True, exist_ok=True)
        lines: List[str] = [f"{key}={value}" for key, value in self._get_output_keys.items()]
        self.output_file_path.write_text("\n".join(lines), encoding="utf-8")
