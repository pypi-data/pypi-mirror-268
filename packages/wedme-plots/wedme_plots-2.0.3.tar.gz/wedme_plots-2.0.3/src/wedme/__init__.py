"""We Don't Make Embarrassing Plots

Import the `wedme` module to apply styles:

    >>> import wedme
    >>> wedme.paper()

"""

# Standard library imports
from wedme.util import imshow, colorbar, get_colormap_norm, unique_legend
from wedme.styledefs import reset, dev, paper, poster, slide, thesis, a0
from wedme.shorthands import figure, subplots, apply
from wedme.const import *

from wedme.gif import GifMaker
