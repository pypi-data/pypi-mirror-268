"""App subclasses the QApplication class."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from vistutils.fields import EmptyField
from vistutils.waitaminute import typeMsg

MenuFlag = Qt.ApplicationAttribute.AA_DontUseNativeMenuBar


class App(QApplication):
  """App is a subclass of QApplication."""

  __caller_id__ = None
  __main_window_class__ = None
  __main_window_instance__ = None

  mainWindow = EmptyField()

  def __init__(self, mainWindowClass: type) -> None:
    """Initializes the App instance."""
    QApplication.__init__(self, )
    self.setAttribute(MenuFlag, True)
    if isinstance(mainWindowClass, type):
      self._setMainWindowClass(mainWindowClass)
    else:
      e = typeMsg('mainWindowClass', mainWindowClass, type)
      raise TypeError(e)

  def _setMainWindowClass(self, mainWindowClass: type) -> None:
    """Set the main window class."""
    self.__main_window_class__ = mainWindowClass

  def _getMainWindowClass(self) -> type:
    """Get the main window class."""
    return self.__main_window_class__

  def _createMainWindowInstance(self) -> None:
    """Create the main window."""
    MainWindow = self._getMainWindowClass()
    self.__main_window_instance__ = MainWindow()
    self.__main_window_instance__.show()
    self.__main_window_instance__.acceptQuit.connect(self.quit)

  @mainWindow.GET
  def _getMainWindowInstance(self, **kwargs) -> Any:
    """Getter-function for the main window instance."""
    if self.__main_window_instance__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createMainWindowInstance()
      return self._getMainWindowInstance(_recursion=True)
    mainWindowClass = self._getMainWindowClass()
    if isinstance(self.__main_window_instance__, mainWindowClass):
      return self.__main_window_instance__
    e = typeMsg('mainWindowInstance',
                self.__main_window_instance__,
                mainWindowClass)
    raise TypeError(e)

  def exec(self) -> int:
    """Executes the application."""
    if isinstance(self.mainWindow, QMainWindow):
      self.mainWindow.show()
    else:
      e = typeMsg('mainWindow', self.mainWindow, QMainWindow)
      raise TypeError(e)
    return QApplication.exec_(self)
