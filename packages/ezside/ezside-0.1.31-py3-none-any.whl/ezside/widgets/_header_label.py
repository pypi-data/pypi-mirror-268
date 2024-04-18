"""HeaderLabel subclasses Label providing a widget suitable for headers.
It also implements an indicator for any unsaved changes. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from icecream import ic
from vistutils.fields import EmptyField

from ezside.settings import Defaults
from ezside.widgets import Label

ic.configureOutput(includeContext=True, )


class HeaderLabel(Label):
  """This subclass of Label turns a star on or off to indicate the
  presence of unsaved changes"""

  __inner_title__ = None
  __unsaved_changes__ = None

  title = EmptyField()

  @title.GET
  def _getTitle(self) -> str:
    """Getter-function for title"""
    return self.__inner_title__

  @title.SET
  def _setTitle(self, title: str) -> None:
    """Setter-function for title"""
    if self.__inner_title__ is not None:
      raise AttributeError('Title is already set!')
    self.__inner_title__ = title

  def __init__(self, *args, ) -> None:
    Label.__init__(self, *args, )
    for arg in args:
      if isinstance(arg, str):
        self.title = arg
        break
      title = getattr(arg, 'headerTitle', None)
      if isinstance(title, str):
        self.title = title
        break

  def getUnsavedState(self) -> bool:
    """Returns the unsaved state"""
    return True if self.__unsaved_changes__ else False

  def setUnsavedState(self, state: Any) -> None:
    """Sets the unsaved state"""
    self.__unsaved_changes__ = True if state else False

  def initUi(self) -> None:
    """Initializes the UI"""
    self.setFont(Defaults.getHeaderFont())
    self.setText(self.title)

  def update(self, ) -> None:
    """Updates the label"""
    if self.getUnsavedState():
      self.setText('*%s' % self.title)
    else:
      self.setText(self.title)
    Label.update(self)
