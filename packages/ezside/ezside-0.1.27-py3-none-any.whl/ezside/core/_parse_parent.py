"""The parseParent function parses positional arguments and returns the
first instance of QWidget encountered if any."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Optional

from PySide6.QtWidgets import QWidget
from vistutils.text import stringList


def parseParent(*args, **kwargs) -> Optional[QWidget]:
  """The parseParent function parses positional arguments and returns the
  first instance of QWidget encountered if any."""
  parentKeys = stringList("""parent, main, window""")
  for key in parentKeys:
    if key in kwargs:
      val = kwargs.get(key)
      if isinstance(val, QWidget):
        return val
  for arg in args:
    if isinstance(arg, QWidget):
      return arg
