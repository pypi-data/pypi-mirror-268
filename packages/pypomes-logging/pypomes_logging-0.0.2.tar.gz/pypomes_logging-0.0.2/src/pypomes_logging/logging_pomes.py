import json
import logging
from datetime import datetime, timedelta
from flask import Request, Response, send_file
from io import BytesIO
from pathlib import Path
from typing import Final, Literal, TextIO

from pypomes_core import (
    APP_PREFIX, DATETIME_FORMAT_INV, TEMP_DIR, DATETIME_FORMAT_COMPACT,
    env_get_str, env_get_path, datetime_parse
)
from pypomes_http import http_get_parameters


def __get_logging_level(level: Literal["debug", "info", "warning", "error", "critical"]) -> int:
    """
    Translate the log severity string *level* into the logging's internal severity value.

    :param level: the string log severity
    :return: the internal logging severity value
    """
    result: int | None
    match level:
        case "debug":
            result = logging.DEBUG          # 10
        case "info":
            result = logging.INFO           # 20
        case "warning":
            result = logging.WARN           # 30
        case "error":
            result = logging.ERROR          # 40
        case "critical":
            result = logging.CRITICAL       # 50
        case _:
            result = logging.NOTSET         # 0

    return result


LOGGING_ID: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_ID", f"{APP_PREFIX}")
LOGGING_FORMAT: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_FORMAT",
                                         "{asctime} {levelname:1.1} {thread:5d} "
                                         "{module:20.20} {funcName:20.20} {lineno:3d} {message}")
LOGGING_STYLE: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_STYLE", "{")

LOGGING_FILE_PATH: Final[Path] = env_get_path(f"{APP_PREFIX}_LOGGING_FILE_PATH",
                                              TEMP_DIR / f"{APP_PREFIX}.log")
LOGGING_FILE_MODE: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_FILE_MODE", "a")

# define and configure the logger
PYPOMES_LOGGER: Final[logging.Logger] = logging.getLogger(LOGGING_ID)

# define the logging severity level
# noinspection PyTypeChecker
LOGGING_LEVEL: Final[int] = __get_logging_level(env_get_str(f"{APP_PREFIX}_LOGGING_LEVEL"))

# configure the logger
# noinspection PyTypeChecker
logging.basicConfig(filename=LOGGING_FILE_PATH,
                    filemode=LOGGING_FILE_MODE,
                    format=LOGGING_FORMAT,
                    datefmt=DATETIME_FORMAT_INV,
                    style=LOGGING_STYLE,
                    level=LOGGING_LEVEL)
for _handler in logging.root.handlers:
    _handler.addFilter(logging.Filter(LOGGING_ID))


def logging_get_entries(errors: list[str],
                        log_level: Literal["debug", "info", "warning", "error", "critical"] = None,
                        log_from: datetime = None,
                        log_to: datetime = None,
                        log_path: Path | str = LOGGING_FILE_PATH) -> BytesIO:
    """
    Extract and return all entries in the logging file *log_path*.

    It is expected for this logging file to be compliant with *PYPOMES_LOGGER*'s default format.
    The extraction meets the criteria specified by *log_level*, and by the inclusive interval *[log_from, log_to]*.

    :param errors: incidental error messages
    :param log_level: the logging level (defaults to all levels)
    :param log_from: the initial timestamp (defaults to unspecified)
    :param log_to: the finaL timestamp (defaults to unspecified)
    :param log_path: the path of the log file
    :return: the logging entries meeting the specified criteria
    """
    # inicializa variável de retorno
    result: BytesIO | None = None

    # obtain the logging level
    # noinspection PyTypeChecker
    logging_level: int = __get_logging_level(log_level)

    filepath: Path = Path(log_path)
    # does the log file exist ?
    if not Path.exists(filepath):
        # no, report the error
        errors.append(f"File '{filepath}' not found")

    # any error ?
    if len(errors) == 0:
        # no, proceed
        result = BytesIO()
        with filepath.open() as f:
            line: str = f.readline()
            while line:
                items: list[str] = line.split(maxsplit=3)
                # noinspection PyTypeChecker
                msg_level: int = __get_logging_level(items[2])
                if msg_level >= logging_level:
                    if log_from or log_to:
                        timestamp: datetime = datetime_parse(f"{items[0]} {items[1]}")
                        if (not log_from or timestamp >= log_from) and \
                           (not log_to or timestamp <= log_to):
                            result.write(line.encode())
                    else:
                            result.write(line.encode())
                line = f.readline()

    return result


def logging_send_entries(request: Request) -> Response:
    """
    Retrieve from the log file, and send in response, the entries matching the criteria specified.

    These criteria are specified as imput parameters of the HTTP request, according to the pattern
    *attach=<[t,true,f,false]>&log-path=<log-path>&level=<log-level>&
     from=YYYYMMDDhhmmss&to=YYYYMMDDhhmmss&last-days=<n>&last-hours=<n>>*

    All criteria are optional:
        - attach: whether browser should display or save file (defaults to True - save it)
        - log-path: the path of the log file (defaults to LOGGING_FILE_PATH)
        - level: the logging level of the entries
        - from: the start timestamp
        - to: the finish timestamp
        - last-days: how many days before current date
        - last-hours: how may hours before current time

    :param request: the 'Request' object
    :return: file containing the log entries requested on success, or incidental errors on fail
    """
    # declare the return variable
    result: Response

    # initialize the error messages list
    errors: list[str] = []

    # obtain the request parameters
    scheme: dict = http_get_parameters(request=request)

    # obtain the logging level
    log_level: str = scheme.get("level")

    # obtain the initial and final timestamps
    log_from: datetime = datetime_parse(scheme.get("from"))
    log_to: datetime = datetime_parse(scheme.get("to"))

    # if 'from' and 'to' were not specified, try 'last-days' and 'last-hours'
    if log_from is None and log_to is None:
        last_days: str = scheme.get("last-days", "0")
        last_hours: str = scheme.get("last-hours", "0")
        offset_days: int = int(last_days) if last_days.isdigit() else 0
        offset_hours: int = int(last_hours) if last_hours.isdigit() else 0
        if offset_days or offset_hours:
            log_from = datetime.now() - timedelta(days=offset_days, hours=offset_hours)

    # obtain the path for the log file
    log_path: Path | str = scheme.get("log-path", LOGGING_FILE_PATH)

    # retrieve the log entries
    # noinspection PyTypeChecker
    log_entries: BytesIO = logging_get_entries(errors, log_level, log_from, log_to, log_path)

    # any error ?
    if len(errors) == 0:
        # no, return the log entries requested
        base: str = "entries"
        if log_from:
           base += f"-from_{log_from.strftime(DATETIME_FORMAT_COMPACT)}"
        if log_to:
           base += f"-to_{log_to.strftime(DATETIME_FORMAT_COMPACT)}"
        log_file = f"log_{base}.log"
        param: str = scheme.get("attach", "true")
        attach: bool = not (isinstance(param, str) and param.lower() in ["0", "f", "false"])
        log_entries.seek(0)
        result = send_file(path_or_file=log_entries,
                           mimetype="text/plain",
                           as_attachment=attach,
                           download_name=log_file)
    else:
        # yes, report the failure
        result = Response(json.dumps({"errors": errors}), status=400,  mimetype="application/json")

    return result


def logging_log_msgs(msgs: list[str],
                     output_dev: TextIO = None,
                     log_level: Literal["debug", "info", "warning", "error", "critical"] = "error",
                     logger: logging.Logger = PYPOMES_LOGGER) -> None:
    """
    Write all messages in *msgs* to *logger*'s logging file, and to *output_dev*.

    The output device is tipically *sys.stdout* or *sys.stderr*.

    :param msgs: the messages list
    :param output_dev: output device where the message is to be printed (None for no device printing)
    :param log_level: the logging level, defaults to 'error' (None for no logging)
    :param logger: the logger to use
    """
    # define the log writer
    log_writer: callable = None
    match log_level:
        case "debug":
            log_writer = logger.debug
        case "info":
            log_writer = logger.info
        case "warning":
            log_writer = logger.warning
        case "error":
            log_writer = logger.error
        case "critical":
            log_writer = logger.critical

    # traverse the messages list
    for msg in msgs:
        # has the log writer been defined ?
        if log_writer:
            # yes, log the message
            log_writer(msg)

        # write to output
        __write_to_output(msg, output_dev)


def logging_log_debug(msg: str, output_dev: TextIO = None,
                      logger: logging.Logger = PYPOMES_LOGGER) -> None:
    """
    Write debug-level message *msg* to *logger*'s logging file, and to *output_dev*.

    The output device is tipically *sys.stdout* or *sys.stderr*.

    :param msg: the message to log
    :param output_dev: output device where the message is to be printed (None for no device printing)
    :param logger: the logger to use
    """
    # log the message
    logger.debug(msg)
    __write_to_output(msg, output_dev)


def logging_log_info(msg: str,
                     output_dev: TextIO = None,
                     logger: logging.Logger = PYPOMES_LOGGER) -> None:
    """
    Write info-level message *msg* to *logger*'s logging file, and to *output_dev*.

    The output device is tipically *sys.stdout* or *sys.stderr*.

    :param msg: the message to log
    :param output_dev: output device where the message is to be printed (None for no device printing)
    :param logger: the logger to use
    """
    # log the message
    logger.info(msg)
    __write_to_output(msg, output_dev)


def logging_log_warning(msg: str,
                        output_dev: TextIO = None,
                        logger: logging.Logger = PYPOMES_LOGGER) -> None:
    """
    Write warning-level message *msg* to *logger*'s logging file, and to *output_dev*.

    The output device is tipically *sys.stdout* or *sys.stderr*.

    :param msg: the message to log
    :param output_dev: output device where the message is to be printed (None for no device printing)
    :param logger: the logger to use
    """
    # log the message
    logger.warning(msg)
    __write_to_output(msg, output_dev)


def logging_log_error(msg: str,
                      output_dev: TextIO = None,
                      logger: logging.Logger = PYPOMES_LOGGER) -> None:
    """
    Write error-level message *msg* to *logger*'s logging file, and to *output_dev*.

    The output device is tipically *sys.stdout* or *sys.stderr*.

    :param msg: the message to log
    :param output_dev: output device where the message is to be printed (None for no device printing)
    :param logger: the logger to use
    """
    # log the message
    logger.error(msg)
    __write_to_output(msg, output_dev)


def logging_log_critical(msg: str,
                         output_dev: TextIO = None,
                         logger: logging.Logger = PYPOMES_LOGGER) -> None:
    """
    Write critical-level message *msg* to *logger*'s logging file, and to *output_dev*.

    The output device is tipically *sys.stdout* or *sys.stderr*.

    :param msg: the message to log
    :param output_dev: output device where the message is to be printed (None for no device printing)
    :param logger: the logger to use
    """
    # log the message
    logger.critical(msg)
    __write_to_output(msg, output_dev)


def __write_to_output(msg: str,
                      output_dev: TextIO) -> None:

    # has the output device been defined ?
    if output_dev:
        # yes, write the message to it
        output_dev.write(msg)

        # is the output device 'stderr' ou 'stdout' ?
        if output_dev.name.startswith("<std"):
            # yes, skip to the next line
            output_dev.write("\n")
