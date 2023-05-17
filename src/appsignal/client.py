from __future__ import annotations
from typing import TYPE_CHECKING
import logging
from logging import Logger, ERROR, WARNING, INFO, DEBUG
from .agent import start_agent
from .opentelemetry import start_opentelemetry
from .config import Config, Options

if TYPE_CHECKING:
    from typing import Unpack


class Client:
    _logger: Logger
    _config: Config

    LOG_LEVELS = dict(error=ERROR, warning=WARNING, info=INFO, debug=DEBUG, trace=DEBUG)

    def __init__(self, **options: Unpack[Options]):
        self._config = Config(options)
        self.start_logger()

        if not self._config.option("active"):
            self._logger.info("AppSignal not starting: no active config found")

    def start(self):
        if self._config.option("active"):
            start_agent(self._config)
            start_opentelemetry(self._config)

    def start_logger(self):
        log_file_path = self._config.log_file_path()
        if log_file_path:
            self._logger = logging.getLogger("appsignal")
            handler = logging.FileHandler(log_file_path)
            handler.setFormatter(
                logging.Formatter(
                    "[%(asctime)s (process) #%(process)d][%(levelname)s] %(message)s",
                    "%Y-%m-%dT%H:%M:%S",
                )
            )
            self._logger.addHandler(handler)
            self._logger.setLevel(self.LOG_LEVELS[self._config.option("log_level")])
        else:
            print(
                "[appsignal][ERROR] Could not initialize file logger. "
                "Logger is inactive."
            )
