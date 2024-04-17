"""The getIcon function creates and returns a QIcon of the given name."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from icecream import ic

ic.configureOutput(includeContext=True)


def getIconPath(name: str) -> str:
  """Creates and returns a QIcon of the given name."""

  name = name.lower().strip()
  name = name.replace(' ', '_')
  here = os.path.dirname(__file__)
  baseName = name.split('.')[0]
  iconPath = os.path.join(here, baseName + '.png')
  return iconPath
