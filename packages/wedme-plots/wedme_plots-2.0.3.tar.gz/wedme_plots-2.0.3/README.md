# 👗 wedme-plots: We Don't Make Embarrassing Plots

Matplotlib styles for papers, posters, presentations and theses. Tailored for academic use.

## Too long; didn't read
1. Pick a style from `paper`, `slide`, `a0`, `thesis`.
2. Decide the final size of the figure on the chosen medium. 
For example, the column width (`cw`) and default height (`dh`) for the `paper` style.
3. Import `wedme`
4. Before using matplotlib, apply the style using `wedme.apply.[style]_[width]_[height]()`. In the above example, `wedme.apply.paper_cw_dh()`.


## Installation
Install from [PyPI](https://pypi.org/project/wedme-plots/) using PIP:
```
pip install wedme-plots
```

For Anaconda users:
- Open an Anaconda Prompt
- Optional: if you use an environment other than `base`, open it using `conda activate [my environment]`
- Install pip using `conda install pip`
- Install wedme-plots using `pip install wedme-plots`

## Styling
Wedme offers multiple styles:
- `paper`: compatible with most journals (Nature, Science, Elsevier). 
- `slide`: compatible with a (16:9) Microsoft Powerpoint presentation. 
- `a0`: A0 poster.
- `thesis`: (work-in-progress) similar to `paper` but for the B5 page format.

## Usage
There are two ways of applying a wedme style. 

### 1. Global styling and sizing

Import the `wedme` module and apply the desired style, e.g. `wedme.apply.paper()`. 
This applies the specified style and its default size to every subsequent figure.

Example:
```python
import wedme

# These commands apply a style to subsequent Matplotlib figures.

# Pick one:
wedme.apply.paper()  # For Elsevier-compatible paper styles
wedme.apply.slide()  # For a 16:9 Powerpoint slide
wedme.apply.a0()     # For A0 posters
wedme.apply.thesis() # For B5-paper thesis

# Optionally, change the default size:
wedme.apply.slide_tw_hh()

# Proceed with plotting as usual
import matplotlib.pyplot as plt

plt.figure()
plt.plot([1, 2, 3, 4])
plt.show()
```

### 2. Local styling and sizing

Alternatively, one can open figures in a specified style and size using the `wedme` drop-in replacements for `plt.figure()` and `plt.subplots()` as follows:

```python
import wedme
import matplotlib.pyplot as plt

# Open a figure in the `a0` style, 
# with a size corresponding to half-width and half-height
wedme.figure.a0_hw_hh()
plt.plot([1, 2, 3, 4])

# Open a figure with two subplots in the `slide` style,
# with the figure size corresponding to half-width and half-height
fig, (ax1, ax2) = wedme.subplots.slide_hw_hh(1, 2)

ax1.plot([1, 2, 3, 4])
ax2.plot([1, 2, 3, 4])
```

Any arguments passed to `wedme.figure.[style]()` and `wedme.subplots.[style]()` are passed on to the equivalent matplotlib functions.

## Sizing
Matching the matplotlib figure size to the final display size of the figure is critically important: scaling to a different height will change font sizes and line widths.

We include the following breakpoints, with respect to the available width and height (`H`) of the chosen medium:
| Breakpoint | Ratio |
| -- | -- |
| `F` | 100% _("full")_ |
| `TT` | 2/3 _("two-thirds")_ |
| `H` | 1/2 _("half")_ |
| `FT` | 5/12 _("five-twelfth")_ |
| `T` | 1/3 _("third")_ |
| `Q` | 1/4 _("quarter")_ |
| `R` | 1/5 |
| `S` | 1/6 |

To specify the size using a breakpoint, append `W` (width) or `H` (height). For example, `wedme.figure.a0_hw_hh()` specifies the `a0` style, with a size of half the A0 width and height.

In addition to the breakpoints, some styles include custom sizes:
- `paper`: `CW` (column width) for two-column papers. `GH` is the height that corresponds to the golden-ratio of `CW`.
- `thesis`: `LFW` and `LFH` for the landscape full-width and full-height.
The default width and height `DW` and `DH` correspond to `CW` and `GH` of the `paper` style

</br>

When no size is specified, the following defaults sizes are used:
- `paper`: `(wedme.PAPER_CW, wedme.paper_GH)`
- `slide`: `(wedme.SLIDE_TW, wedme.slide_HH)`
- `a0`:  `(wedme.A0_TW, ...)`
- `thesis`: `(wedme.THESIS_DW, wedme.paper_DH)`


## Powerpoint
Powerpoint automatically resizes artwork to a size that is different from the export size. To undo this:
- Insert the figure in Powerpoint.
- Picture Format > Reset Picture > Reset Picture & Size.

## Fonts
Sans-serif fonts are the standards for figures because they remain readable even when small or pixelated. Helvetica or Arial fonts are preferred by Nature, Science and Elsevier. 

We try to find Helvetica, Arial, Verdana, Inter, Nimbus Sans on your system, in that order. The first font found will be applied to the figures.

## Exporting
`wedme` sets the `pdf.fonttype` parameter to `42` as recommended by Nature. This ensures that the text is editable even after exporting a pdf. `wedme` also changes the parameters `figure.autolayout` and `savefig.bbox` such that the specified sizes are respected.

For saving figures, consider using [pypdfplot](https://github.com/dcmvdbekerom/pypdfplot) to maintain the ability to later change how data is displayed. Of course, we don't make embarassing plots to begin with.

## Examples
<img src="https://github.com/mruijzendaal/wedme-plots/blob/main/img/calibration_curve_rot.png?raw=true" width="512">

## Utilities
Other than style sheets, wedme also includes utilities for commonly used operations.
- Creating animated GIF images from multiple plots. See `wedme.gif`
- Creating a legend only for unique entries. See `wedme.util.unique_legend()`
- Specifying the colorbar label easily. See `wedme.util.colorbar()`
- Specifying the minimum and maximum of the colorbar as a function of percentiles of the shown field. See `wedme.util.imshow()`
- Making plot colors dependent on some variable. See `weme.util.get_colormap_norm()`