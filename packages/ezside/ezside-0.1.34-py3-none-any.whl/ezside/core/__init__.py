"""The 'ezside.core' package provides a limited selection from the Qt
namespace in much shorter named versions. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._qt_names import *
from ._colors import *

from ._pen import Pen
from ._brush import Brush
from ._parse_parent import parseParent
from ._font_family import Font

from ._color_factory import parseColor
from ._pen_factory import parsePen, stylePen, emptyPen, solidPen
from ._pen_factory import dashPen, dotPen, dashDotPen
from ._brush_factory import parseBrush, emptyBrush, solidBrush
