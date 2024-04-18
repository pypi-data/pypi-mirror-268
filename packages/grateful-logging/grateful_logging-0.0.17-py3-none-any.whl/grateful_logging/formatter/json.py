import json
import logging
from typing import Iterable, TypeAlias


TDefaultKey: TypeAlias = str 
TAlisKey: TypeAlias = str


class JSONFormatter(logging.Formatter):
    def __init__(
        self, 
        *,
        include_keys: "dict[TAlisKey, TDefaultKey]",
        always_keys: "Iterable[str]" = tuple(),
        is_use_time: bool = True,
        **kwargs,
    ):
        self._is_use_time = is_use_time
        self._include_fields = include_keys 
        self._always_keys = always_keys
        super().__init__(**kwargs)

    def format(self, record: "logging.LogRecord") -> str:
        if self._is_use_time:
            record.asctime = self.formatTime(record, self.datefmt)
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record: "logging.LogRecord"):
        message = {
            alias: value
            for alias, key in self._include_fields.items()
            if (
                (value := record.__dict__.get(key)) is not None
                or (key in self._always_keys)
            )
        }

        return message
