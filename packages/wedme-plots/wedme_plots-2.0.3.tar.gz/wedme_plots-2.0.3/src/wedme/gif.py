import tempfile
import subprocess
import matplotlib.pyplot as plt


def _run_command(command, silent=False, **kwargs):
    """Run a command while printing the live output"""
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            **kwargs,
        )
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if not silent:
                print(line.decode(), end="")
    except Exception as e:
        return None
    return process.returncode


def create_gif(frames, outname, resize_fac=1.0, frametime_ms=800):
    """
    Create a GIF from a list of frames.

    Args:
        frames (str): The path to the frames to be included in the GIF.
        outname (str): The path and filename of the output GIF.
        resize_fac (float, optional): The resize factor for the frames. Defaults to 1.0.
        frametime_ms (int, optional): The time (in milliseconds) between frames. Defaults to 800.

    Returns:
        None
    """

    delay_ms = round(frametime_ms / 10)
    _run_command(
        [
            "convert",
            "-resize",
            f"{resize_fac*100:.0f}%",
            "-delay",
            f"{delay_ms:.0f}",
            "-loop",
            "0",
            frames,
            outname,
        ]
    )


def _check_imagemagick():
    return _run_command(["convert", "-version"], silent=True) == 0


class GifMaker(object):
    """Class for creating GIFs from matplotlib figures using ImageMagick.

    Example usage:
    ```python
    import wedme
    import matplotlib.pyplot as plt

    gif = wedme.GifMaker()
    for i in range(10):
        plt.plot(range(10), [i]*10)
        gif.save_frame()

    gif.close("test.gif")
    ```
    """

    _is_open = False
    _frames = []
    _tempdir = None

    def __init__(self):
        self.clean()
        if not _check_imagemagick():
            raise RuntimeError(
                "Cannot create GIFs without ImageMagick installed. Download from https://imagemagick.org/script/download.php"
            )

    def clean(self):
        """Removes any currently saved frames and resets the object to a clean state"""
        if self._tempdir:
            self._tempdir.cleanup()
        else:
            self._tempdir = tempfile.TemporaryDirectory()

        self._frames = []
        self._is_open = True

    def save_frame(self, fig=None, name=None):
        """
        Save a frame of the given figure as a PNG image.

        Args:
            fig (matplotlib.figure.Figure, optional): The figure to save. If not provided, the current figure will be used.
            name (str, optional): The name of the saved image file. This will be used for ordering the frames in the GIF. If not provided, the order in which the frames are saved will be used.

        Returns:
            None

        Raises:
            None
        """
        if fig is None:
            fig = plt.gcf()

        if name is None:
            name = f"{len(self._frames):06d}"
        name += ".png"
        fig.savefig(f"{self._tempdir.name}/{name}")
        self._frames.append(f"{self._tempdir.name}/{name}")

    def save(self, outname, frametime_ms=800, resize_fac=1.0):
        """
        Save the GIF animation. NB: This does not close the object, so you can continue adding frames after saving.
        If this behaviour is not desired, call `close` instead.

        Args:
            outname (str): The output filename for the GIF.
            frametime_ms (int, optional): The time in milliseconds between frames. Defaults to 800.
            resize_fac (float, optional): The factor by which to resize the frames. Defaults to 1.0.
        """
        create_gif(f"{self._tempdir.name}/*.png", outname, resize_fac, frametime_ms)

    def close(self, outname):
        """
        Closes the GIF file by saving it and performing any necessary cleanup.

        Args:
            outname (str): The name of the output file.

        Returns:
            None
        """
        self.save(outname)
        self.clean()


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    gif = GifMaker()
    for i in range(10):
        plt.plot(range(10), [i] * 10)
        gif.save_frame(plt)

    gif.close("test.gif")
