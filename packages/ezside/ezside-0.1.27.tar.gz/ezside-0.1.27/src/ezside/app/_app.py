"""App subclasses the QApplication class."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from vistutils.waitaminute import typeMsg

MenuFlag = Qt.ApplicationAttribute.AA_DontUseNativeMenuBar


class App(QApplication):
  """App is a subclass of QApplication."""

  __caller_id__ = None
  __main_window_class__ = None

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

  def exec(self) -> int:
    """Executes the application."""
    MainWindow = self._getMainWindowClass()
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.acceptQuit.connect(self.quit)
    return QApplication.exec_(self)
