#!/usr/bin/env python

import sys
from logging import Logger as PythonLogger
from typing import Type

#  --- Copied from logging module ---
if hasattr(sys, '_getframe'):
    def currentframe():
        return sys._getframe(3)
else:  # pragma: no cover
    def currentframe():
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except Exception:
            return sys.exc_info()[2].tb_frame.f_back


#  --- Copied from logging module ---


class KomoLogger(PythonLogger):
    def __init__(self, name: str):
        super().__init__(name)

    @staticmethod
    def logger_name_for_class(model_class: Type):
        return f"{model_class.__module__}.{model_class.__qualname__}"
