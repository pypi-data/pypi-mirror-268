# -*- coding: utf-8 -*-
import logging

from coppyr import Context


# Module variables


LOGGERS_CACHE = {}

# Some example, basic formats.
COPPYR_FMT = "%(asctime)s [%(action_id)s] %(levelname)s \"%(message)s\""
COPPYR_FMT_WITH_TIME = "%(asctime)s [%(action_id)s] %(levelname)s " \
                       "\"%(message)s\" %(action_duration_str)s"

# Example/Default logging config
DEFAULT_CONFIG = {
    "version": 1,
    "formatters": {
        "coppyr": {
            "format": COPPYR_FMT
        },
        "coppyr-with-time": {
            "format": COPPYR_FMT_WITH_TIME
        }
    },
    "handlers": {
        "file-default": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "coppyr-with-time",
            "filename": f"/tmp/{Context().app_name}.log",
            "mode": "a"
        },
        "file-devnull": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "coppyr-with-time",
            "filename": "/dev/null",
            "mode": "a"
        },
        "stream-stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "coppyr-with-time",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "file": {
            "level": "DEBUG",
            "qualname": "default",
            "handlers": ["file-default"],
            "propagate": False
        },
        "devnull": {
            "level": "DEBUG",
            "qualname": "devnull",
            "handlers": ["file-devnull"],
            "propagate": False
        },
        "stdout": {
            "level": "DEBUG",
            "qualname": "stdout",
            "handlers": ["stream-stdout"],
            "propagate": False
        }
    },
    "root": {
        "level": "DEBUG",
        "formatter": "coppyr",
        "handlers": ["stream-stdout"]  # change this to file-default to have all
                                       # logs appear in the log file (including
                                       # logs from dependency libs)
    }
}


class CoppyrLogRecord(logging.LogRecord):
    """
    This log record class can consult `coppyr.Context` for more variables after
    normal `logging.LogRecord` init.  This is particularly useful for rich log
    contexts in complex services.

    The keys that are included/retrieved are configurable by modifying the
    `context.logging_keys` list.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = Context()
        for log_key in context.logging_keys:
            setattr(self, log_key, getattr(context, log_key))


class CoppyrLogger(logging.getLoggerClass()):
    """
    This is a custom logger class that simply users the custom log record above
    instead of the default one.
    """
    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None,
                   *arg, **kwargs):
        return CoppyrLogRecord(name, level, fn, lno, msg, args, exc_info, func)


def setup(dict_config=None, logger_class=CoppyrLogger):
    """
    Simple wrapper that accepts a dictionary and passes it to
    `logging.config.dictConfig`.

    WARNING: This method should only be called once as multiple calls to
    `logging.config.dictConfig` can cause errors.

    :param dict_config: Dict
        Dictionary following the configuration format of the logging built-in.
        For reference consult:
            https://docs.python.org/3/library/logging.config.html
    """
    if dict_config is None:
        dict_config = DEFAULT_CONFIG

    # Set the logging lib to use our logger and log record objects.
    logging.setLoggerClass(logger_class)

    from logging.config import dictConfig
    dictConfig(dict_config)


def get(name="file", level=None):
    """
    Creates logger object to specified log and caches it in `LOGGERS_CACHE`
    dict.

    :param name: String
        Log name.  `None` returns the "root" logger from `logging.getLogger()`.
    :param level: String
        Log level to set on logger. `None` uses the default log setting.
    :return: CoppyrLogger
        Logger object.
    """
    # If logger is not in cache, create a new one...
    if name not in LOGGERS_CACHE:
        logger = logging.getLogger(name)

        # Set log level if applicable.
        if level is not None:
            logger.setLevel(level)
        # TODO: We should sanity check level value first.

        # Cache logger.
        LOGGERS_CACHE[name] = logger

    return LOGGERS_CACHE[name]


def shutdown():
    """
    Call into `logging` to perform an orderly shutdown by flushing and closing
    all handlers.
    """
    logging.shutdown()
