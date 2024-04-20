import importlib_resources as _resources
import matplotlib.pyplot as _plt
import matplotlib as _mpl
from wedme.const import *


## Functions for applying the wedme styles
def _apply_style(stylename):
    with _resources.files(
        "wedme"
    ) / "stylesheets" / f"{stylename}.mplstyle" as file_path:
        _plt.style.use(file_path)


def reset():
    _mpl.rcParams.update(_mpl.rcParamsDefault)


def dev():
    paper()
    _mpl.rcParams["figure.dpi"] = 200


def _common():
    _apply_style("common")


def slide():
    _common()
    _apply_style("slides")


def paper():
    _common()
    _apply_style("elspaper")


def poster():
    _common()
    _apply_style("a0")


def a0():
    _common()
    _apply_style("a0")


def thesis():
    _common()
    _apply_style("thesis")


_styles = {
    "DEV": dev,
    "RESET": reset,
    "PAPER": paper,
    "SLIDE": slide,
    "A0": a0,
    "THESIS": thesis,
}

_aliases = {
    "SLIDES": "SLIDE",
    "POSTER": "A0",
}

# List of available styles and aliases
_available_styles = [x.lower() for x in list(_styles.keys())]  # + list(_aliases.keys())


def get_style(stylename):
    stylename = stylename.upper()
    if stylename in _aliases:
        stylename = _aliases[stylename]
    if stylename in _styles:
        return _styles[stylename]
    else:
        raise ValueError(
            f"Unknown figure style `{stylename.lower()}`. Available styles are: {', '.join(_available_styles)}."
        )


def apply_style(stylename):
    # Call the appropriate figure type
    get_style(stylename)()
