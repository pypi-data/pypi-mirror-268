"""FilesMenu provides the file menu for the main application window."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QMainWindow
from icecream import ic

from attribox import AttriBox
from ezside.app.menus import AbstractMenu, Action

ic.configureOutput(includeContext=True, )


class FilesMenu(AbstractMenu):
  """FilesMenu provides the file menu for the main application window."""

  new = AttriBox[Action]('new')
  open = AttriBox[Action]('open')
  save = AttriBox[Action]('save')
  save_as = AttriBox[Action]('save_as')
  exit = AttriBox[Action]('exit')

  def __init__(self, parent: QMainWindow) -> None:
    """FilesMenu provides the file menu for the main application window."""
    AbstractMenu.__init__(self, parent)
    self.setTitle('File')

  def appendActions(self) -> None:
    """Appends the actions without setting them up"""
    self.addAction(self.new)
    self.addAction(self.open)
    self.addAction(self.save)
    self.addAction(self.save_as)
    Action(self.addSeparator())
    self.addAction(self.exit)

  def setupActions(self, ) -> None:
    """Sets up the actions for the file menu."""
    self.new.setupAction()
    self.open.setupAction()
    self.save.setupAction()
    self.save_as.setupAction()
    self.exit.setupAction()
