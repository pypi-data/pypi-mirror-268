"""This module provides expanding spacers preventing widgets from being
spread to fill up available space. Three versions are provided,
HorizontalSpacer, VerticalSpacer, and GridSpacer, expanding in the
horizontal, vertical, and both directions respectively. The spacers are
intended to be invisible except for during development. Use the visibility
flag in the settings."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtGui import QPainter, QPaintEvent, QPen, QColor

from ezside.core import solidBrush, Yellow, Expand, Tight, SolidLine
from ezside.core import dashPen
from ezside.widgets import BaseWidget


class AbstractSpacer(BaseWidget):
  """AbstractSpacer class provides a base class for the spacers."""
  __debug_flag__ = None

  def __init__(self, *args, **kwargs) -> None:
    BaseWidget.__init__(self, *args, **kwargs)
    self.setContentsMargins(0, 0, 0, 0)

  def setDebugFlag(self, flag: bool) -> None:
    """Set the debug flag."""
    self.__debug_flag__ = flag

  def paintEvent(self, event: QPaintEvent) -> None:
    """Paint the spacer."""
    if self.__debug_flag__:
      painter = QPainter()
      painter.begin(self)
      viewRect = painter.viewport()
      painter.setPen(dashPen())
      painter.setBrush(solidBrush(Yellow))
      painter.drawRect(viewRect)
      painter.end()


class HorizontalSpacer(AbstractSpacer):
  """HorizontalSpacer class provides a horizontal spacer."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractSpacer.__init__(self, *args, **kwargs)
    self.setSizePolicy(Expand, Tight)
    self.setMinimumHeight(32)


class VerticalSpacer(AbstractSpacer):
  """VerticalSpacer class provides a vertical spacer."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractSpacer.__init__(self, *args, **kwargs)
    self.setSizePolicy(Tight, Expand)
    self.setMinimumWidth(32)


class GridSpacer(AbstractSpacer):
  """GridSpacer class provides a grid spacer."""

  def __init__(self, *args, **kwargs) -> None:
    AbstractSpacer.__init__(self, *args, **kwargs)
    self.setSizePolicy(Expand, Expand)


class HorizontalSeparator(HorizontalSpacer):
  """HorizontalSeparator class provides a horizontal separator."""

  def paintEvent(self, event: QPaintEvent) -> None:
    """Paint the separator."""
    painter = QPainter()
    painter.begin(self)
    viewRect = painter.viewport()
    pen = QPen()
    pen.setWidth(1)
    pen.setStyle(SolidLine)
    pen.setColor(QColor(0, 0, 0, 255))
    painter.setPen(pen)
    y = viewRect.center().y()
    left, right = viewRect.left(), viewRect.right()
    painter.drawLine(left, y, right, y)
    painter.end()


class VerticalSeparator(VerticalSpacer):
  """VerticalSeparator class provides a vertical separator."""

  def paintEvent(self, event: QPaintEvent) -> None:
    """Paint the separator."""
    painter = QPainter()
    painter.begin(self)
    viewRect = painter.viewport()
    pen = QPen()
    pen.setWidth(1)
    pen.setStyle(SolidLine)
    pen.setColor(QColor(0, 0, 0, 255))
    painter.setPen(pen)
    x = viewRect.center().x()
    top, bottom = viewRect.top(), viewRect.bottom()
    painter.drawLine(x, top, x, bottom)
    painter.end()
