"""StatusBar provides a status bar for the main application window."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
  """StatusBar provides a status bar for the main application window."""

  def initUi(self, ) -> None:
    """Initializes the user interface for the status bar."""
    self.showMessage('Ready')
    self.setStyleSheet("""background-color: #f0f0f0; color: #000000;
    border-top: 1px solid #000000; border-left: 1px solid #000000;""")
