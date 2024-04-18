"""Pen wraps the QPen class."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor
from vistutils.parse import maybe

from ezside.core import BevelJoin, FlatCap, SolidLine, Black


class Pen(QPen):
  """Pen wraps the QPen class."""

  def __init__(self, *args, **kwargs) -> None:
    QPen.__init__(self, )
    intArgs = [arg for arg in args if isinstance(arg, int)]
    colorArgs = [arg for arg in args if isinstance(arg, QColor)]
    styleArgs = [arg for arg in args if isinstance(arg, Qt.PenStyle)]
    capStyleArgs = [arg for arg in args if isinstance(arg, Qt.PenCapStyle)]
    joinStyleArgs = [arg for arg in args if isinstance(arg, Qt.PenJoinStyle)]
    width = None
    color = None
    if not colorArgs:
      if len(intArgs) in [4, 5]:
        width = intArgs.pop(0)
        color = QColor(*intArgs)
      elif len(intArgs) > 5:
        raise ValueError
      elif intArgs:
        width = 1
    color = maybe(color, Black)
    width = maybe(width, 1)
    penStyle = styleArgs[0] if styleArgs else SolidLine
    capStyle = capStyleArgs[0] if capStyleArgs else FlatCap
    joinStyle = joinStyleArgs[0] if joinStyleArgs else BevelJoin
    self.setWidth(width)
    self.setColor(color)
    self.setStyle(penStyle)
    self.setCapStyle(capStyle)
    self.setJoinStyle(joinStyle)
