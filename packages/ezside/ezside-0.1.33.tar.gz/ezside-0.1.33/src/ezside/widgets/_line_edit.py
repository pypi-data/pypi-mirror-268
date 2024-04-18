"""LineEdit wrapper.  """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from PySide6.QtCore import Signal, Qt, QEvent
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from attribox import AttriBox
from icecream import ic
from vistutils.fields import TextField
from vistutils.text import stringList
from vistutils.waitaminute import typeMsg

from ezside.core import SHIFT, Tight
from ezside.widgets import Horizontal
from ezside.widgets import BaseWidget

ic.configureOutput(includeContext=True, )


class LineEdit(QLineEdit):
  """LineEdit wrapper.  """
  keyValue = Signal(int)
  keyName = Signal(str)
  keyPressed = Signal(QKeyEvent)
  keyReleased = Signal(QKeyEvent)
  escapePressed = Signal()
  escapeReleased = Signal()
  shiftEnter = Signal()
  shiftEnterRelease = Signal()

  def event(self, event_: QEvent) -> bool:
    """Reimplementation triggering the signal"""
    if isinstance(event_, QKeyEvent):
      key = event_.keyCombination().key()
      if event_.modifiers() == SHIFT and key.value == Qt.Key.Key_Return:
        if event_.type() == QEvent.Type.KeyPress:
          self.shiftEnter.emit()
        if event_.type() == QEvent.Type.KeyRelease:
          self.shiftEnterRelease.emit()
        return True
    return QLineEdit.event(self, event_)

  def keyPressEvent(self, event: QKeyEvent) -> Any:
    """Reimplementation triggering the signal"""
    key = event.keyCombination().key()
    self.keyValue.emit(key.value)
    self.keyName.emit(key.name)
    self.keyPressed.emit(event)
    if event.key() == Qt.Key.Key_Escape:
      self.escapePressed.emit()
    if event.modifiers() == SHIFT and event.key() == Qt.Key.Key_Return:
      self.shiftEnter.emit()
      return False
    return QLineEdit.keyPressEvent(self, event)

  def keyReleaseEvent(self, event: QKeyEvent) -> Any:
    """Reimplementation triggering the signal"""
    key = event.keyCombination().key()
    self.keyValue.emit(key.value)
    self.keyName.emit(key.name)
    self.keyReleased.emit(event)
    if event.key() == Qt.Key.Key_Escape:
      self.escapeReleased.emit()
    if event.modifiers() == SHIFT and key.value == Qt.Key.Key_Return:
      self.shiftEnterRelease.emit()
      return False
    return QLineEdit.keyReleaseEvent(self, event)

  def initUi(self) -> None:
    """Initialize the user interface."""
    self.setSizePolicy(Tight, Tight)

  def connectActions(self) -> None:
    """Initialize the actions."""

  def getText(self) -> str:
    """Getter-function for the text field"""
    return self.text()

#
# class LineEdit(BaseWidget):
#   """LineEdit wrapper.  """
#   __fallback_placeholder__ = 'Enter text here'
#   __placeholder_text__ = None
#
#   baseLayout = AttriBox[Horizontal]()
#   lineEdit = AttriBox[_LineEdit]()
#   text = TextField()
#
#   cursorPositionChanged = Signal(int, int)
#   editingFinished = Signal()
#   inputRejected = Signal()
#   returnPressed = Signal()
#   selectionChanged = Signal()
#   textChanged = Signal(str)
#   textEdited = Signal(str)
#   keyNumber = Signal(int)
#   keyName = Signal(str)
#   keyPressed = Signal(QKeyEvent)
#   keyReleased = Signal(QKeyEvent)
#   escapePressed = Signal()
#   escapeReleased = Signal()
#   shiftEnter = Signal()
#   shiftEnterRelease = Signal()
#
#   def __init__(self, *args, **kwargs) -> None:
#     """Initialize the widget."""
#     BaseWidget.__init__(self, *args, **kwargs)
#     placeholderKeys = stringList("""placeholder, defaultText""")
#     for key in placeholderKeys:
#       if key in kwargs:
#         val = kwargs.get(key, )
#         if isinstance(key, str):
#           self.__placeholder_text__ = val
#           break
#         e = typeMsg('placeholderText', val, str)
#         raise TypeError(e)
#     else:
#       for arg in args:
#         if isinstance(arg, str):
#           self.__placeholder_text__ = arg
#           break
#       else:
#         self.__placeholder_text__ = self.__fallback_placeholder__
#
#   def initUi(self) -> None:
#     """Initialize the user interface."""
#     self.lineEdit.setPlaceholderText(self.__placeholder_text__)
#     self.baseLayout.addWidget(self.lineEdit)
#     self.setLayout(self.baseLayout)
#
#   def connectActions(self) -> None:
#     """Initialize the actions."""
#     self.lineEdit.cursorPositionChanged.connect(self.cursorPositionChanged)
#     self.lineEdit.editingFinished.connect(self.editingFinished)
#     self.lineEdit.inputRejected.connect(self.inputRejected)
#     self.lineEdit.returnPressed.connect(self.returnPressed)
#     self.lineEdit.selectionChanged.connect(self.selectionChanged)
#     self.lineEdit.textChanged.connect(self.textChanged)
#     self.lineEdit.textEdited.connect(self.textEdited)
#     self.lineEdit.textChanged.connect(self.update)
#     self.lineEdit.keyValue.connect(self.keyNumber)
#     self.lineEdit.keyName.connect(self.keyName)
#     self.lineEdit.keyPressed.connect(self.keyPressed)
#     self.lineEdit.keyReleased.connect(self.keyReleased)
#     self.lineEdit.escapePressed.connect(self.escapePressed)
#     self.lineEdit.escapeReleased.connect(self.escapeReleased)
#     self.lineEdit.shiftEnter.connect(self.shiftEnter)
#     self.lineEdit.shiftEnterRelease.connect(self.shiftEnterRelease)
#     self.shiftEnter.connect(self.insertLineBreak)
#     self.escapePressed.connect(self.clearSelection)
#
#   def insertLineBreak(self) -> None:
#     """Insert a line break."""
#     self.text += '\n'
#
#   def setPlaceholderText(self, text: str) -> None:
#     """Set the placeholder text."""
#     self.__placeholder_text__ = text
#     self.lineEdit.setPlaceholderText(text)
#
#   def update(self) -> None:
#     """Update the widget."""
#     if not self.lineEdit.text():
#       self.lineEdit.setPlaceholderText(self.__placeholder_text__)
#     self.text = self.lineEdit.text()
#     return BaseWidget.update(self)
#
#   def clearSelection(self) -> None:
#     """If any text is selected, it is unselected. If no text is selected,
#     the text is cleared."""
#     if self.lineEdit.selectedText():
#       return self.lineEdit.deselect()
#     return self.lineEdit.clear()
#
#   def selectedText(self) -> str:
#     """Return the selected text."""
#     return self.lineEdit.selectedText()
#
#   def setText(self, text: str) -> None:
#     """Set the text."""
#     self.lineEdit.setText(text)
#     self.text = text
#     self.update()
