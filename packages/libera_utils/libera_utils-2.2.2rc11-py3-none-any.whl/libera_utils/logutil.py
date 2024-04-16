"""Logging utilities"""
# Standard
import copy
from datetime import date, datetime
import json
import logging
import logging.config
import logging.handlers
import traceback
from typing import Optional, Tuple, Mapping
import yaml
# Installed
from cloudpathlib import AnyPath
import watchtower
# Local
from libera_utils.config import config
from libera_utils.io.smart_open import smart_open

logger = logging.getLogger(__name__)


def _json_serialize_default(o):
    """
    A standard 'default' json serializer function.

    - Serializes datetime objects using their .isoformat() method.

    - Serializes all other objects using repr().
    """
    if isinstance(o, (date, datetime)):
        return o.isoformat()
    return repr(o)


class JsonLogFormatter(logging.Formatter):
    """Altered version of the CloudWatchLogFormatter provided in the watchtower library"""

    add_log_record_attrs = ('asctime', 'created', 'module', 'funcName', 'lineno', 'levelname')

    def __init__(
            self,
            *args,
            add_log_record_attrs: Optional[Tuple[str, ...]] = None,
            **kwargs,
    ):
        """

        Parameters
        ----------
        add_log_record_attrs : Optional, tuple
            Tuple of log record attributes to add to the resulting structured JSON structure that comes out of the
            logging formatter.
        """
        super().__init__(*args, **kwargs)
        if add_log_record_attrs is not None:
            self.add_log_record_attrs = add_log_record_attrs

    def format(self, record: logging.LogRecord) -> str:
        """Format log message to a string

        Parameters
        ----------
        record : logging.LogRecord
            Log record object containing the logged message, which may be a dict (Mapping) or a string
        """
        # Perform %-style string interpolation before we make the message into a dict
        if isinstance(record.msg, str) and record.args:
            record.msg = record.msg % record.args
            record.args = None

        # If we got a dict passed in, we don't want to mutate it as a side effect so we deepcopy it
        # This is a huge performance hit, but otherwise we are mutating our users' data and that's not cool
        msg = copy.deepcopy(record.msg) if isinstance(record.msg, Mapping) else {"msg": record.msg}

        if self.add_log_record_attrs:
            if "asctime" in self.add_log_record_attrs:
                msg["asctime"] = self.formatTime(record)
            for field in self.add_log_record_attrs:
                if field not in ("msg", "asctime"):
                    msg[field] = getattr(record, field)

        if record.exc_info:
            # Add the formatted traceback to the JSON object
            formatted_traceback = ''.join(traceback.format_exception(*record.exc_info))
            msg["traceback"] = formatted_traceback

        record.msg = msg
        return json.dumps(record.msg, default=_json_serialize_default)


def configure_static_logging(config_file: AnyPath or str):
    """Configure logging based on a static logging configuration yaml file.

    The yaml is interpreted as a dict configuration. There is no ability to customize this logging
    configuration at runtime.

    Parameters
    ----------
    config_file : cloudpathlib.anypath.AnyPath or str
        Location of config file.

    See Also
    --------
    configure_task_logging : Runtime modifiable logging configuration.
    """
    with smart_open(config_file) as log_config:
        config_yml = log_config.read()
        config_dict = yaml.safe_load(config_yml)
    logging.config.dictConfig(config_dict)
    logger.info(f"Logging configured statically according to {config_file}.")


def configure_task_logging(task_id: str, app_package_name: str,
                           console_log_level: str or int = None,
                           console_log_json: bool = False,
                           cloudwatch_log_group: str = None):
    """Configure logging based on runtime environment variables.

    Variables that control logging are LIBERA_LOG_DIR, LIBERA_CONSOLE_LOG_LEVEL, and LIBERA_LOG_GROUP. If these
    variables are unset, only INFO level console logging will be enabled.

    Parameters
    ----------
    task_id : str
        Unique identifier by which to name the log file and cloudwatch log stream.
    app_package_name : str
        This is the name of the top level package for which you want to instantiate logging. For example, if you are
        working on an application package called `my_app` and using module level logging, all your loggers will be
        named like `my_app.module_name.submodule_name`. We use this string to set the logging level of all loggers
        that inherit from the `my_app` logger (logger inheritance in python is expressed in dot notation). So by
        specifying `my_app` as the app_package_name, all your app logger handlers will log at your specified levels
        but all library loggers (e.g. those not inheriting from `my_app` logger) will only log at INFO level.
        This reduces debug spam from library loggers significantly, especially boto3.
    console_log_level : str or int, Optional
        Override environment variable log level configuration.
    console_log_json : bool, Optional
        If True, console logs will be JSON formatted. This is suitable for setting up loggers in AWS services that are
        automatically monitored by cloudwatch on stdout and stderr (e.g. Lambda or Batch)
    cloudwatch_log_group : str, Optional
        Override optional environment variable log group name. Default is None and will result in falling back to
        the LIBERA_LOG_GROUP environment variable. If that is not set, no cloudwatch JSON logging will be configured.

    Notes
    -----
    Even in the absence of cloudwatch JSON logging, all stdout/sterr messages generated by a Lambda will be logged to
    CloudWatch as string messages. Embedded JSON strings in log message text can still be queried in CloudWatch.

    See Also
    --------
    configure_static_logging : Static logging configuration based on yaml file.
    """
    def _str_bool(s: str):
        """Examines an environment variable string to determine if it is truthy or falsy"""
        if not bool(s):
            return False
        if s.lower() in ("false", "0", "none", "null"):
            return False
        return True

    handlers = {}
    setup_messages = []
    try:  # Try to establish console log level from config
        if not console_log_level:  # If not passed explicitly
            console_log_level_env = config.get("LIBERA_CONSOLE_LOG_LEVEL")
            if _str_bool(console_log_level_env):  # If it is truthy, then store it
                console_log_level = console_log_level_env.upper()

        if console_log_level:
            if isinstance(console_log_level, str):
                console_log_level = console_log_level.upper()
            console_handler = {
                "class": "logging.StreamHandler",
                "formatter": "json" if console_log_json else "plaintext",
                "level": console_log_level,
                "stream": "ext://sys.stdout"
            }
            handlers.update(console=console_handler)
            setup_messages.append(f"Console logging configured at level {console_log_level}.")
    except KeyError:
        pass

    try:  # Establish log directory from config
        log_dir = config.get("LIBERA_LOG_DIR")
        if _str_bool(log_dir):
            log_filepath = AnyPath(log_dir) / f"{task_id}.log"
            logfile_handler = {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "plaintext",
                "level": "DEBUG",
                "filename": str(log_filepath),
                "maxBytes": 10000000,  # 10MB
                "backupCount": 3
            }
            handlers.update(logfile=logfile_handler)
            setup_messages.append(f"File logging configured to log to {log_filepath}.")
    except KeyError:
        pass

    try:  # Establish cloudwatch log group from config
        if not cloudwatch_log_group:
            cloudwatch_log_group = config.get("LIBERA_LOG_GROUP")

        if _str_bool(cloudwatch_log_group):
            watchtower_handler = {
                "class": "watchtower.CloudWatchLogHandler",
                "formatter": "json",
                "level": "DEBUG",
                "log_group_name": cloudwatch_log_group,
                "log_stream_name": task_id,
                "send_interval": 10,
                "create_log_group": True
            }
            handlers.update(watchtower=watchtower_handler)
            setup_messages.append({"cloudwatch_log_handler_config": watchtower_handler})
    except KeyError:
        pass

    config_dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": "libera_utils.logutil.JsonLogFormatter",
            },
            "plaintext": {
                "format": "%(asctime)s %(levelname)-9.9s [%(filename)s:%(lineno)d in %(funcName)s()]: %(message)s"
            }
        },
        "handlers": handlers,
        "root": {
            "level": "INFO",
            "propagate": True,
            "handlers": list(handlers.keys())
        },
        "loggers": {
            app_package_name: {
                "level": "DEBUG",
                "handlers": []
            }
        }
    }

    logging.config.dictConfig(config_dict)
    for message in setup_messages:
        logger.info(message)


def flush_cloudwatch_logs():
    """Force flush of all cloudwatch logging handlers. For example at the end of a process just before it is killed.

    Returns
    -------
    None
    """
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        if isinstance(handler, watchtower.CloudWatchLogHandler):
            handler.flush()
