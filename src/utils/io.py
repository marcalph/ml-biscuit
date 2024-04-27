#!/usr/bin/env python3
# coding: utf-8
##########################################
# authors                                #
# marcalph - https://github.com/marcalph #
##########################################
""" minimal data loading capabilities
"""
from pathlib import Path
from src.utils.log import logthis
from typing import Any


@logthis
def read(filepath: Path) -> None:
    """read the data"""
    raise NotImplementedError("todo implement this function")
