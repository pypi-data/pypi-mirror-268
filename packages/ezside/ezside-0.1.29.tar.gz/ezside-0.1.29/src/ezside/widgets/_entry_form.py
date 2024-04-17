"""EntryForm provides a header, a line-edit and a submit button. Instances
may be vertical or horizontal. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Signal, Qt
from attribox import AttriBox
from vistutils.fields import TextField
from vistutils.text import stringList, joinWords, monoSpace
from vistutils.waitaminute import typeMsg

from ezside.widgets import BaseWidget, Grid, Label, LineEdit, Button


class EntryForm(BaseWidget):
  """EntryForm provides a header, a line-edit and a submit button. Instances
  may be vertical or horizontal. """

  __variable_title__ = None
  __unsaved_changes__ = False
  __inner_widgets__ = None

  text = TextField('')

  baseLayout = AttriBox[Grid]()
  headerLabel = AttriBox[Label]()
  lineEdit = AttriBox[LineEdit]()
  submitButton = AttriBox[Button]()

  textApplied = Signal(str, str)  # oldText, newText
  newText = Signal(str)  # newText
  updated = Signal()  # Text has changed
  badKey = Signal()  # Bad key pressed
  selectedText = Signal(str)  # Text selected in line edit

  def __init__(self, *args, **kwargs) -> None:
    BaseWidget.__init__(self, *args, **kwargs)
    titleKeys = stringList("""title, key, name""")
    orientationKeys = stringList("""orientation, direction""")
    ORI = Qt.Orientation
    types = dict(title=(str,), orientation=(str, ORI))
    Keys = [titleKeys, orientationKeys]
    values = {k: None for (k, _) in types.items()}
    defaultValues = dict(orientation=ORI.Vertical)
    for (keys, (name, type_)) in zip(Keys, types.items()):
      for key in keys:
        if key in kwargs:
          val = kwargs[key]
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
          defVal = defaultValues.get(name, None)
          if defVal is None:
            e = """The '%s' constructor requires the argument named: '%s'! 
            This may be given as a positional argument or at any of the 
            following keyword arguments: %s"""
            keyList = joinWords(keys)
            clsName = self.__class__.__name__
            errorMessage = monoSpace(e % (clsName, name, keyList))
            raise ValueError(errorMessage)
          if isinstance(defVal, type_):
            values |= {name: defVal}
          else:
            e = typeMsg(name, defVal, type_)
            raise TypeError(e)
    self.__variable_title__ = values['title']
    self._row = 1 if values['orientation'] == ORI.Vertical else 0
    self._col = 1 if values['orientation'] == ORI.Horizontal else 0

  def _getTitle(self) -> str:
    if self.__variable_title__ is None:
      e = """EntryForm requires a title."""
      raise ValueError(e)
    if isinstance(self.__variable_title__, str):
      return self.__variable_title__
    e = typeMsg('title', self.__variable_title__, str)
    raise TypeError(e)

  def _getInnerWidgets(self, **kwargs) -> list[BaseWidget]:
    """Getter-function for list of inner widgets"""
    if self.__inner_widgets__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self.__inner_widgets__ = []
      return self._getInnerWidgets(_recursion=True)
    if isinstance(self.__inner_widgets__, list):
      for widget in self.__inner_widgets__:
        if not isinstance(widget, BaseWidget):
          e = typeMsg('innerWidget', widget, BaseWidget)
          raise TypeError(e)
      return self.__inner_widgets__
    e = typeMsg('inner_widgets', self.__inner_widgets__, list)
    raise TypeError(e)

  def __len__(self) -> int:
    return len(self._getInnerWidgets())

  def initUi(self) -> None:
    """Initializes the user interface"""
    self.headerLabel.setText(self._getTitle())
    self.lineEdit.setPlaceholderText('Enter text here')
    self.submitButton.setText('Submit')
    row, col = self._row * len(self), self._col * len(self)
    self.baseLayout.addWidget(self.headerLabel, row, col)
    self._getInnerWidgets().append(self.headerLabel)
    row, col = self._row * len(self), self._col * len(self)
    self.baseLayout.addWidget(self.lineEdit, row, col)
    self._getInnerWidgets().append(self.lineEdit)
    row, col = self._row * len(self), self._col * len(self)
    self.baseLayout.addWidget(self.submitButton, row, col)
    self._getInnerWidgets().append(self.submitButton)
    self.setLayout(self.baseLayout)

  def connectActions(self) -> None:
    """Connects the actions to the signals"""
    self.lineEdit.editingFinished.connect(self._resetLine)
    self.lineEdit.inputRejected.connect(self._badKey)
    self.lineEdit.selectionChanged.connect(self._selectLine)
    self.lineEdit.textEdited.connect(self._beginEdit)
    self.lineEdit.escapePressed.connect(self._resetLine)
    self.lineEdit.returnPressed.connect(self._applyText)
    self.submitButton.clicked.connect(self._applyText)

  def _resetLine(self, *_) -> None:
    """Resets the line-edit to show the current value"""
    self.lineEdit.setText(self.text)
    self._updateLabel()

  def _badKey(self, *_) -> None:
    """Emits the badKey signal"""
    self.badKey.emit()

  def _selectLine(self, *_) -> None:
    """Emits the selectedText signal"""
    self.selectedText.emit(self.lineEdit.selectedText())

  def _beginEdit(self) -> None:
    """Emits the newText signal"""
    self._updateLabel()

  def _applyText(self, *_) -> None:
    """Changes the current value to the text in the line-edit"""
    oldText = self.text
    self.text = self.lineEdit.text()
    self.textApplied.emit(oldText, self.text)

  def _updateLabel(self) -> None:
    """Updates the label with the current value"""
    if self.__unsaved_changes__:
      self.headerLabel.setText('%s*' % self._getTitle())
    self.headerLabel.setText(self._getTitle())
