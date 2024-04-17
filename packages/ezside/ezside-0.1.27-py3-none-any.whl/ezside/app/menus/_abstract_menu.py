"""AbstractMenu provides the base class for the custom menus. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from PySide6.QtWidgets import QMenu, QMainWindow
from icecream import ic

from ezside.app.menus import Action

ic.configureOutput(includeContext=True, )


class AbstractMenu(QMenu):
  """AbstractMenu provides the base class for the custom menus. """

  def __init__(self, parent: QMainWindow) -> None:
    """Initializes the menu."""
    QMenu.__init__(self, parent)

  @abstractmethod
  def appendActions(self) -> None:
    """Appends the actions without setting them up"""

  @abstractmethod
  def setupActions(self, ) -> None:
    """Sets up the actions for the menu."""

  def applyParent(self) -> None:
    """Sets the parent on actions"""
    for action in self.actions():
      if isinstance(action, Action):
        action.setParent(self.parent())

  def initUi(self) -> None:
    """Collections append, setup and apply parent"""
    self.appendActions()
    self.setupActions()
    self.applyParent()
