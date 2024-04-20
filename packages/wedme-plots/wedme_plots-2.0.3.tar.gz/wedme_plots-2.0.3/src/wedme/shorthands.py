from wedme.styledefs import *
import matplotlib.pyplot as _plt
import matplotlib as _mpl


def _get_size_for_style(style: str, sizename: str):
    size_const_name = f"{style}_{sizename}"
    if size_const_name not in globals():
        raise ValueError(
            f"Style `{style.lower()}` does not have a size named `{sizename}`"
        )
    return globals()[size_const_name]


def _get_style_and_figsize(name: str):
    nameparts = name.upper().split("_")
    stylename = nameparts[0]
    assert get_style(stylename)

    if len(nameparts) == 2 or len(nameparts) > 3:
        # Not of the form `STYLE_WIDTH_HEIGHT` or `STYLE`
        raise ValueError(
            f"Invalid figure type: {name}. The correct form is `STYLE_WIDTH_HEIGHT` or `STYLE`"
        )
    elif len(nameparts) == 1:
        # If the name is of the form `STYLE`, we assume that the figure size is not specified
        figsize = None
    else:
        # Otherwise, we assume it is of the form `TYPE_WIDTH_HEIGHT`
        # Extract the type, width, and height
        wname, hname = nameparts[1:]

        if wname.endswith("H"):
            hname, wname = nameparts[1:]

        h = _get_size_for_style(stylename, hname)
        w = _get_size_for_style(stylename, wname)
        figsize = (w, h)
    return stylename, figsize


class _metafigure(type):
    @classmethod
    def _callfun(cls, *args, **kws):
        raise NotImplementedError("This method should be overridden by the child class")

    # Catch-all for figure types. Any method call to this class will get intercepted here.
    def __getattr__(cls, name: str):
        # `name` is the name of the method that was called
        stylename, figsize = _get_style_and_figsize(name)

        # Define a new function that calls the `figure` method with the appropriate arguments
        def myfig(*args, stylename=stylename, **kwargs):
            # Update the keyword arguments with the figure size
            kws = {}
            if figsize is not None:
                kws.update(figsize=figsize)

                if "figsize" in kwargs:
                    raise ValueError(
                        f"Cannot specify `figsize` in the keyword arguments when calling `{name}`"
                    )
            kws.update(kwargs)

            apply_style(stylename)

            # Call the figure method with the updated arguments
            return cls._callfun(*args, **kws)

        # Return the new function handle. When one calls `wedme.figure.TYPE_WIDTH_HEIGHT()`,
        # `wedme.figure.TYPE_WIDTH_HEIGHT` returns the function handle `myfig`
        return myfig


class apply(metaclass=_metafigure):
    def _callfun(*args, **kws):
        if "figsize" in kws:
            _mpl.rcParams["figure.figsize"] = kws["figsize"]


class figure(metaclass=_metafigure):
    def _callfun(*args, **kws):
        return _plt.figure(*args, **kws)


class subplots(metaclass=_metafigure):
    def _callfun(*args, **kws):
        return _plt.subplots(*args, **kws)
