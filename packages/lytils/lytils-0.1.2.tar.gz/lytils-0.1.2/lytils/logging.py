import logging
import traceback
from inspect import currentframe


def get_line_number():
    cf = currentframe()
    return cf.f_back.f_lineno


def setup_logging():
    filename = "debug.log"
    encoding = "utf-8"
    formatting = "%(asctime)s - [%(levelname)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    level = logging.INFO
    logging.basicConfig(
        filename=filename,
        encoding=encoding,
        format=formatting,
        datefmt=date_format,
        level=level,
    )


def log_error_trace():
    trace = traceback.format_exc()
    logging.error(trace)
