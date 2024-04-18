"""MultiButton provides a layout containing any number of buttons arranged
in a grid layout. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from attribox import AttriBox

from ezside.widgets import BaseWidget, Grid


class MultiButton(BaseWidget):
  """MultiButton provides a layout containing any number of buttons arranged
  in a grid layout. """

  baseLayout = AttriBox[Grid]()
