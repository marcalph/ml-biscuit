#!/usr/bin/env python3
# coding: utf-8
##########################################
# authors                                #
# marcalph - https://github.com/marcalph #
##########################################
""" log utilities
"""

# import functools
import logging
import os
import time
from functools import wraps
from inspect import getframeinfo, stack
from typing import Any, Callable, TypeVar

import pandas as pd
from typing_extensions import ParamSpec

P = ParamSpec("P")
T = TypeVar("T")


class CustomFormatter(logging.Formatter):
    """Custom formatter, overrides funcname and filename if provided"""

    def get_header_length(self, record: logging.LogRecord) -> int:
        """Get the header length of a given record."""
        return len(
            super().format(
                logging.LogRecord(
                    name=record.name,
                    level=record.levelno,
                    pathname=record.pathname,
                    lineno=record.lineno,
                    msg="",
                    args=(),
                    exc_info=None,
                )
            )
        )

    def format(self, record: logging.LogRecord) -> str:
        if hasattr(record, "name_override"):
            record.funcName = record.name_override
        if hasattr(record, "file_override"):
            record.filename = record.file_override

        indent = " " * self.get_header_length(record)
        head, *trailing = super().format(record).splitlines(True)
        return head + "".join(indent + line for line in trailing)


def logthis(fn: Callable[P, T]) -> Callable[P, T]:
    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        py_file_caller = getframeinfo(stack()[1][0])
        extra_args = {
            "name_override": fn.__name__,
            "file_override": os.path.basename(py_file_caller.filename),
            "line_override": py_file_caller.lineno,
        }
        logger.info("started", extra=extra_args)
        t = time.time()
        function = fn(*args, **kwargs)
        logger.info(f"ended in {time.time()-t:.1f} sec", extra=extra_args)
        return function

    return wrapper


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler("./journal.log")
formatter = CustomFormatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(funcName)s - %(message)s",
    "%Y-%m-%d %H:%M",
)
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
