"""Label prints centered text"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt, QRect, QRectF
from PySide6.QtGui import QPainter, \
  QPaintEvent, \
  QFontMetrics
from PySide6.QtWidgets import QLabel
from attribox import AttriBox
from icecream import ic
from vistutils.fields import TextField, EmptyField
from vistutils.parse import maybe
from vistutils.text import joinWords, monoSpace
from vistutils.waitaminute import typeMsg

from ezside.core import emptyPen, \
  emptyBrush, \
  AlignLeft, \
  Tight, \
  AlignFlag, \
  AlignHCenter, \
  AlignRight, \
  AlignTop, \
  AlignBottom, \
  Center, \
  parseParent
from ezside.core import AlignVCenter
from ezside.settings import Defaults
from ezside.widgets import BaseWidget, \
  Vertical, \
  VerticalSpacer, \
  HorizontalSpacer, Horizontal

ic.configureOutput(includeContext=True, )


class Label(QLabel):
  """Subclass of QLabel"""
  __fallback_alignment__ = Center
  __fallback_text__ = 'Label'
  __alignment_flags__ = None
  __inner_text__ = None
  innerText = EmptyField()

  def __init__(self, *args, ) -> None:
    parent = parseParent(*args, )
    QLabel.__init__(self, parent)
    textArg = None
    alignArg = None
    for arg in args:
      if isinstance(arg, str):
        textArg = arg
      if isinstance(arg, AlignFlag):
        if alignArg is None:
          alignArg = arg
        else:
          alignArg |= arg
    self.__inner_text__ = maybe(textArg, self.__fallback_text__)
    self.__alignment_flags__ = maybe(alignArg, self.__fallback_alignment__)

  def initUi(self) -> None:
    """The initUi method initializes the user interface."""
    self.setAlignment(self.__alignment_flags__)
    self.setText(self.__inner_text__)
    self.setMargin(Defaults.getLabelMargin())
    self.setSizePolicy(Tight, Tight)

  def connectActions(self) -> None:
    """Initialize the actions."""

  @innerText.SET
  def setText(self, newText: str) -> None:
    """Set the text of the label"""
    self.__inner_text__ = newText
    QLabel.setText(self, newText)

  @innerText.GET
  def getText(self, ) -> str:
    """Getter-function for the text field"""
    return self.__inner_text__
