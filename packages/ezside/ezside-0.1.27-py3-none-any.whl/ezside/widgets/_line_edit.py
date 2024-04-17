"""LineEdit wrapper.  """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit
from attribox import AttriBox
from icecream import ic
from vistutils.fields import TextField
from vistutils.text import stringList
from vistutils.waitaminute import typeMsg

from ezside.widgets import Horizontal
from ezside.widgets import BaseWidget

ic.configureOutput(includeContext=True, )


class LineEdit(BaseWidget):
  """LineEdit wrapper.  """
  __fallback_placeholder__ = 'Enter text here'
  __placeholder_text__ = None

  baseLayout = AttriBox[Horizontal]()
  lineEdit = AttriBox[QLineEdit]()
  text = TextField()

  cursorPositionChanged = Signal(int, int)
  editingFinished = Signal()
  inputRejected = Signal()
  returnPressed = Signal()
  selectionChanged = Signal()
  textChanged = Signal(str)
  textEdited = Signal(str)

  def __init__(self, *args, **kwargs) -> None:
    """Initialize the widget."""
    BaseWidget.__init__(self, *args, **kwargs)
    placeholderKeys = stringList("""placeholder, defaultText""")
    for key in placeholderKeys:
      if key in kwargs:
        val = kwargs.get(key, )
        if isinstance(key, str):
          self.__placeholder_text__ = val
          break
        e = typeMsg('placeholderText', val, str)
        raise TypeError(e)
    else:
      for arg in args:
        if isinstance(arg, str):
          self.__placeholder_text__ = arg
          break
      else:
        self.__placeholder_text__ = self.__fallback_placeholder__

  def initUi(self) -> None:
    """Initialize the user interface."""
    self.lineEdit.setPlaceholderText(self.__placeholder_text__)
    self.baseLayout.addWidget(self.lineEdit)
    self.setLayout(self.baseLayout)

  def connectActions(self) -> None:
    """Initialize the actions."""
    self.lineEdit.cursorPositionChanged.connect(self.cursorPositionChanged)
    self.lineEdit.editingFinished.connect(self.editingFinished)
    self.lineEdit.inputRejected.connect(self.inputRejected)
    self.lineEdit.returnPressed.connect(self.returnPressed)
    self.lineEdit.selectionChanged.connect(self.selectionChanged)
    self.lineEdit.textChanged.connect(self.textChanged)
    self.lineEdit.textEdited.connect(self.textEdited)
    self.lineEdit.textChanged.connect(self.update)

  def setPlaceholderText(self, text: str) -> None:
    """Set the placeholder text."""
    self.__placeholder_text__ = text
    self.lineEdit.setPlaceholderText(text)

  def update(self) -> None:
    """Update the widget."""
    if not self.lineEdit.text():
      self.lineEdit.setPlaceholderText(self.__placeholder_text__)
    self.text = self.lineEdit.text()
    return BaseWidget.update(self)
