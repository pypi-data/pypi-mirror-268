"""Brush class for the EZQt library."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor


class Brush(QBrush):
  """Brush class for the EZQt library."""

  def __init__(self, *args, **kwargs) -> None:
    QBrush.__init__(self, )
    intArgs = [arg for arg in args if isinstance(arg, int)]
    colorArgs = [arg for arg in args if isinstance(arg, QColor)]
    styleArgs = [arg for arg in args if isinstance(arg, Qt.BrushStyle)]
    color = None
    style = None
    if colorArgs:
      color = colorArgs[0]
    elif len(intArgs) in [3, 4]:
      color = QColor(*intArgs)
    else:
      color = QColor(255, 255, 255, 255)
    if styleArgs:
      style = styleArgs[0]
    else:
      style = Qt.BrushStyle.SolidPattern
    self.setColor(color)
    self.setStyle(style)
