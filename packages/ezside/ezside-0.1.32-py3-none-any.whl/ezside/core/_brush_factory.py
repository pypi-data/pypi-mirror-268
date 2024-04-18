"""The brushFactory function creates images of QBrush."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from vistutils.text import stringList
from vistutils.parse import maybe

from ezside.core import parseColor


def _createBrush(*args, **kwargs) -> QBrush:
  """Creates a QBrush instance."""
  errors = []
  colorDefault = QColor(0, 0, 0, 255)
  styleDefault = Qt.BrushStyle.SolidPattern
  colorArg, styleArg = None, None
  colorKeys = stringList("""color, col, brushColor, rgb, RGBA""")
  styleKeys = stringList("""style, brushStyle""")
  for arg in args:
    if isinstance(arg, QColor) and colorArg is None:
      colorArg = arg
    elif isinstance(arg, Qt.BrushStyle) and styleArg is None:
      styleArg = arg
  colorKwarg, styleKwarg = None, None
  for key in colorKeys:
    if key in kwargs and colorKwarg is None:
      val = kwargs[key]
      try:
        colorKwarg = parseColor(val)
      except ValueError as valueError:
        errors.append(valueError)
  for key in styleKeys:
    if key in kwargs and styleKwarg is None:
      val = kwargs[key]
      if isinstance(val, Qt.BrushStyle):
        styleKwarg = val
  color = maybe(colorKwarg, colorArg, colorDefault)
  style = maybe(styleKwarg, styleArg, styleDefault)
  brush = QBrush()
  brush.setColor(color)
  brush.setStyle(style)
  return brush


def parseBrush(*args, **kwargs) -> QBrush:
  """Parses a QBrush instance."""
  return _createBrush(*args, **kwargs)


def emptyBrush() -> QBrush:
  """Creates an empty QBrush instance."""
  return _createBrush(QColor(0, 0, 0, 0), Qt.BrushStyle.NoBrush, )


def solidBrush(*args, **kwargs) -> QBrush:
  """Creates a solid QBrush instance."""
  color = parseColor(*args, **kwargs)
  return _createBrush(color, Qt.BrushStyle.SolidPattern, )
