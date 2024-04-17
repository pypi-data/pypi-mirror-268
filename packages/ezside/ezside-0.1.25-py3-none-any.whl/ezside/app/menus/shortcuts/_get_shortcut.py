"""KeyMap provides named instances of QKeySequence for use in the main
application."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from warnings import warn

from PySide6.QtGui import QKeySequence
from icecream import ic
from vistutils.text import monoSpace

ic.configureOutput(includeContext=True, )


def _getKeyboardShortcuts() -> dict:
  """
  Returns a dictionary of common keyboard shortcuts
  categorized by Files, Edit, View, and Help actions.
  """
  return {
    "new": "CTRL+N",
    "open": "CTRL+O",
    "save": "CTRL+S",
    "save_as": "CTRL+SHIFT+S",
    "close": "CTRL+W",
    "undo": "CTRL+Z",
    "redo": "CTRL+Y",
    "cut": "CTRL+X",
    "copy": "CTRL+C",
    "paste": "CTRL+V",
    "select_all": "CTRL+A",
    "about_qt": "F12",
    "exit": "ALT+F4",
  }


def getShortcut(name: str) -> QKeySequence:
  """
  Returns a QKeySequence for the given name.
  """
  name = name.lower().strip()
  name = name.replace(' ', '_')
  if 'debug' in name:
    for char in name:
      if char.isnumeric():
        return QKeySequence('F%s' % char)
  base = _getKeyboardShortcuts()
  shortcut = base.get(name, '')
  sequence = QKeySequence.fromString(shortcut)
  if not sequence:
    warn(f'No keyboard shortcut found for {monoSpace(name)}')
    return QKeySequence()
  return sequence
