"""EditMenu provides the edit menu for the main application window."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMainWindow

from attribox import AttriBox
from ezside.app.menus import AbstractMenu, Action


class EditMenu(AbstractMenu):
  """EditMenu provides the edit menu for the main application window."""

  undo = AttriBox[Action]('undo')
  redo = AttriBox[Action]('redo')
  cut = AttriBox[Action]('cut')
  copy = AttriBox[Action]('copy')
  paste = AttriBox[Action]('paste')
  delete = AttriBox[Action]('delete')
  select_all = AttriBox[Action]('select_all')

  def __init__(self, parent: QMainWindow) -> None:
    """EditMenu provides the edit menu for the main application window."""
    AbstractMenu.__init__(self, parent)
    self.setTitle('Edit')

  def appendActions(self) -> None:
    """Appends the actions without setting them up"""
    self.addAction(self.undo)
    self.addAction(self.redo)
    self.addSeparator()
    self.addAction(self.cut)
    self.addAction(self.copy)
    self.addAction(self.paste)
    self.addAction(self.delete)
    self.addSeparator()
    self.addAction(self.select_all)

  def setupActions(self, ) -> None:
    """Sets up the actions for the edit menu."""
    self.undo.setupAction()
    self.redo.setupAction()
    self.cut.setupAction()
    self.copy.setupAction()
    self.paste.setupAction()
    self.delete.setupAction()
    self.select_all.setupAction()
