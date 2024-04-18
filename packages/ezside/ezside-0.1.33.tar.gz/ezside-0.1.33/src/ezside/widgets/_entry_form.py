"""EntryForm provides a header, a line-edit and a submit button. Instances
may be vertical or horizontal. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Optional

from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtWidgets import QWidget, QFrame
from attribox import AttriBox
from icecream import ic
from vistutils.fields import TextField, EmptyField
from vistutils.text import stringList, joinWords, monoSpace
from vistutils.waitaminute import typeMsg

from ezside.core import VERTICAL, HORIZONTAL
from ezside.settings import Defaults
from ezside.widgets import BaseWidget, Grid, HeaderLabel, LineEdit, Button
from ezside.widgets import HorizontalSpacer, VerticalSpacer, AbstractSpacer

ORI = Qt.Orientation
ic.configureOutput(includeContext=True, )


class EntryForm(BaseWidget):
  """EntryForm provides a header, a line-edit and a submit button. Instances
  may be vertical or horizontal. """
  __variable_title__ = None
  __variable_value__ = None
  __unsaved_changes__ = False
  __inner_widgets__ = None
  __debug_flag__ = None

  value = EmptyField()

  baseLayout = AttriBox[Grid]()
  headerLabel = AttriBox[HeaderLabel]()
  lineEdit = AttriBox[LineEdit]()
  submitButton = AttriBox[Button]('Submit')
  hSpacer = AttriBox[HorizontalSpacer]()
  vSpacer = AttriBox[VerticalSpacer]()

  newTextFrom = Signal(str, str)  # oldText, newText
  newText = Signal(str)  # newText
  updated = Signal()  # Text has changed
  edited = Signal(str)  # Text is being edited, but not updated yet.
  cancelled = Signal(str)  # Text edit was cancelled

  def __init__(self, *args, **kwargs) -> None:
    BaseWidget.__init__(self, *args, **kwargs)
    self._ori = None
    types = dict(title=str, orientation=ORI, debug=bool, )
    values = dict(title=None, orientation=None, debug=None, )
    defVals = dict(title=None, orientation=HORIZONTAL, debug=False, )
    titleKeys = stringList("""title, header, name, variable""")
    oriKeys = stringList("""orientation, ori, direction, dir""")
    debugKeys = stringList("""debug, dbg, debugFlag, dbgFlag""")
    KEYS = [titleKeys, oriKeys, debugKeys, ]
    for ((name, type_), Keys) in zip(types.items(), KEYS):
      for key in Keys:
        if key in kwargs:
          val = kwargs.get(key)
          if isinstance(val, type_):
            values[name] = val
            break
          e = typeMsg(name, val, type_)
          raise TypeError(e)
      else:
        for arg in args:
          if isinstance(arg, type_):
            values[name] = arg
            break
        else:
          values[name] = defVals[name]
    self.__variable_title__ = values['title']
    self._ori = values['orientation']
    self.__debug_flag__ = values['debug']

  @value.SET
  def _setValue(self, value: Any) -> None:
    """Setter-function for value"""
    self.__variable_value__ = value

  @value.GET
  def _getValue(self) -> Any:
    """Getter-function for value"""
    return self.__variable_value__

  def _getTitle(self) -> str:
    if self.__variable_title__ is None:
      e = """EntryForm requires a title."""
      raise ValueError(e)
    if isinstance(self.__variable_title__, str):
      return self.__variable_title__
    e = typeMsg('title', self.__variable_title__, str)
    raise TypeError(e)

  def _getInnerWidgets(self, **kwargs) -> list[QWidget]:
    """Getter-function for list of inner widgets"""
    return [self.headerLabel, self.lineEdit, self.submitButton,
            self.hSpacer, ]

  def __len__(self) -> int:
    return len(self._getInnerWidgets())

  def _getOrientation(self) -> Qt.Orientation:
    """Getter-function for orientation"""
    if self._ori in [VERTICAL, HORIZONTAL]:
      return self._ori
    e = """Orientation must be one of: '%s', but received: '%s'!"""
    horName = str(HORIZONTAL.name)
    verName = str(VERTICAL.name)
    oriNames = joinWords(horName, verName, )
    raise ValueError(monoSpace(e % (oriNames, str(self._ori))))

  def isVertical(self) -> bool:
    """Returns True if the orientation is vertical"""
    return True if self._getOrientation() == VERTICAL else False

  def isHorizontal(self) -> bool:
    """Returns True if the orientation is horizontal"""
    return True if self._getOrientation() == HORIZONTAL else False

  def _getRowCol(self, widget: QWidget) -> tuple[int, int]:
    """Getter-function for row and column based on orientation"""
    for (i, w) in enumerate(self._getInnerWidgets()):
      if w == widget:
        if self.isVertical():
          return i, 0
        elif self.isHorizontal():
          return 0, i
    e = """Widget not found in inner widgets!"""
    raise ValueError(e)

  def _getSpacer(self) -> AbstractSpacer:
    """Getter-function for the spacer widget based on orientation"""
    if self.isVertical():
      return self.vSpacer
    elif self.isHorizontal():
      return self.hSpacer

  def _getStrut(self) -> AbstractSpacer:
    """Getter-function for the strut widget based on orientation"""
    if self.isVertical():
      return self.hSpacer
    elif self.isHorizontal():
      return self.vSpacer

  def _getStrutArgs(self) -> tuple[int, int, int, int]:
    """Getter-function for the strut spans based on orientation"""
    if self.isVertical():
      return 0, 1, len(self), 1
    elif self.isHorizontal():
      return 1, 0, 1, len(self)

  def _getSizes(self) -> list[QSize]:
    """Getter-function for preferred sizes"""
    return [w.sizeHint() for w in self._getInnerWidgets()]

  def _getWidths(self) -> list[int]:
    """Getter-function for the widths of the inner widgets"""
    return [s.width() for s in self._getSizes()]

  def _getHeights(self) -> list[int]:
    """Getter-function for the heights of the inner widgets"""
    return [s.height() for s in self._getSizes()]

  def _getSizeSum(self) -> QSize:
    """Getter-function for the sum of the sizes of the inner widgets"""
    width, height = None, None
    layoutSpaces = (len(self) - 1) * Defaults.getLayoutSpacing()
    if self.isVertical():
      width = max(self._getWidths())
      height = sum(self._getHeights()) + layoutSpaces
    elif self.isHorizontal():
      width = sum(self._getWidths()) + layoutSpaces
      height = max(self._getHeights())
    if isinstance(width, int) and isinstance(height, int):
      return QSize(width, height)

  def initUi(self) -> None:
    """Initializes the user interface"""
    self.headerLabel.initUi()
    self.headerLabel.title = self._getTitle()
    self.headerLabel.setFrameShadow(QFrame.Shadow.Sunken)
    self.headerLabel.setFrameShape(QFrame.Shape.Panel)
    header = self.headerLabel
    self.lineEdit.initUi()
    self.lineEdit.setFont(Defaults.getMonospacedFont())
    self.lineEdit.setPlaceholderText('Enter text here')
    lineEdit = self.lineEdit
    self.submitButton.initUi()
    self.submitButton.setText('Submit')
    button = self.submitButton
    spacer = self._getSpacer()
    spacer.setDebugFlag(self.__debug_flag__)
    strut = self._getStrut()
    strut.setDebugFlag(self.__debug_flag__)
    self.setMinimumSize(self._getSizeSum())
    self.baseLayout.addWidget(header, *self._getRowCol(header))
    self.baseLayout.addWidget(lineEdit, *self._getRowCol(lineEdit))
    self.baseLayout.addWidget(button, *self._getRowCol(button))
    self.baseLayout.addWidget(spacer, *self._getRowCol(spacer))
    self.baseLayout.addWidget(strut, *self._getStrutArgs())
    self.setLayout(self.baseLayout)
    self._updateUnsavedChanges()

  def connectActions(self) -> None:
    """Connects the actions to the signals"""
    self.lineEdit.keyPressed.connect(self._updateUnsavedChanges)
    self.lineEdit.keyReleased.connect(self._updateUnsavedChanges)
    self.lineEdit.textChanged.connect(self._textEditedFunc)
    self.lineEdit.escapePressed.connect(self._cancelEditFunc)
    self.lineEdit.returnPressed.connect(self._updateTextFunc)
    self.submitButton.clicked.connect(self._updateTextFunc)

  def _textEditedFunc(self, newText: str) -> None:
    """Slot for textEdited signal"""
    self.edited.emit(newText)
    self._updateUnsavedChanges()

  def _cancelEditFunc(self) -> None:
    """Slot for escapePressed signal"""
    text = self.lineEdit.getText()
    self.cancelled.emit(text)
    if text:
      self.lineEdit.setText('')
    else:
      self.lineEdit.setText(self.value)

  def _updateTextFunc(self) -> None:
    """This method updates the text field on the EntryForm instance to
    that of the lineEdit field."""
    oldText = self.value
    newText = self.lineEdit.getText()
    self.value = newText
    self.newTextFrom.emit(oldText, newText)
    self.newText.emit(newText)
    self.updated.emit()
    self._updateUnsavedChanges()

  def _updateUnsavedChanges(self, *_) -> None:
    """Updates the unsaved changes state"""
    unsavedFlag = self.value != self.lineEdit.displayText()
    self.headerLabel.setUnsavedState(unsavedFlag)
    self.headerLabel.update()
    self.submitButton.setEnabled(unsavedFlag)
    self.submitButton.update()
