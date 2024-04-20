import matplotlib.pyplot as _plt
import matplotlib as _mpl
import numpy as _np


def colorbar(mappable=None, label="", labelpad=10, labelkwargs={}, **kwargs):
    cax = _plt.colorbar(mappable=mappable, **kwargs)
    cax.set_label(label, rotation=270, labelpad=labelpad, **labelkwargs)
    return cax


def imshow(
    data,
    vmin_percentile=None,
    vmax_percentile=None,
    vmin=None,
    vmax=None,
    *args,
    **kwargs,
):
    if vmin_percentile is not None:
        vmin = _np.nanpercentile(data, vmin_percentile)
    if vmax_percentile is not None:
        vmax = _np.nanpercentile(data, vmax_percentile)
    return _plt.imshow(data, *args, vmin=vmin, vmax=vmax, *args, **kwargs)


def get_colormap_norm(cmap="viridis", X=None, min=None, max=None):
    if not X is None:
        min = _np.nanmin(_np.array(X))
        max = _np.nanmax(_np.array(X))

    cmap = _plt.cm.get_cmap(cmap)
    norm = _mpl.colors.Normalize(vmin=min, vmax=max)

    return lambda x: cmap(norm(x))


def get_colormap_norm_for_colorbar(cmap="viridis", X=None, min=None, max=None):
    """Generates a colormap and a scalar mappable for use in a colorbar.
    This might be useful when plotting multiple lines with different colors based on a parameter.

    Example usage:
        cmap, scalarmappable = wedme.util.get_colormap_norm_for_colorbar("nipy_spectral", min=340, max=386)

        for i, result in enumerate(myresults):
            plt.plot(result.x, result.y, color=cmap(delay), label=f"{delay}ns")

        wedme.colorbar(scalarmappable, label="Q-switch delay [ns]")
    """
    if not X is None:
        min = _np.nanmin(_np.array(X))
        max = _np.nanmax(_np.array(X))

    cmap = _plt.cm.get_cmap(cmap)
    norm = _mpl.colors.Normalize(vmin=min, vmax=max)
    fun = lambda x: cmap(norm(x))
    scalar_mappable = _mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

    return fun, scalar_mappable


def unique_legend(ax=None, **kwargs):
    if ax is None:
        ax = _plt.gca()

    handles, labels = ax.get_legend_handles_labels()
    unique_labels, unique_handles = _np.unique(labels, return_index=True)
    unique_handles = [handles[i] for i in unique_handles]
    return _plt.legend(unique_handles, unique_labels, **kwargs)
