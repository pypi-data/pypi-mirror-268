r"""Contain utility functions to manage matplotlib figures."""

from __future__ import annotations

__all__ = ["figure2html"]

import base64
import io
import math
from typing import TYPE_CHECKING

from matplotlib import pyplot as plt

if TYPE_CHECKING:
    from matplotlib.axes import Axes


def figure2html(fig: plt.Figure, close_fig: bool = False) -> str:
    r"""Convert a matplotlib figure to a string that can be used in a
    HTML file.

    Args:
        fig: The figure to convert.
        close_fig: If ``True``, the figure is closed after it is
            converted to HTML format.

    Returns:
        The converted figure to a string.

    Example usage:

    ```pycon
    >>> from matplotlib import pyplot as plt
    >>> from flamme.utils.figure import figure2html
    >>> fig, ax = plt.subplots()
    >>> string = figure2html(fig)

    ```
    """
    fig.tight_layout()
    img = io.BytesIO()
    fig.savefig(img, format="png", bbox_inches="tight")
    img.seek(0)
    data = base64.b64encode(img.getvalue()).decode("utf-8")
    if close_fig:
        plt.close(fig)
    return f'<img src="data:image/png;charset=utf-8;base64, {data}">'


def readable_xticklabels(
    ax: Axes,
    max_num_xticks: int = 100,
    xticklabel_max_len: int = 20,
    xticklabel_min: int = 10,
) -> None:
    r"""Update the tick labels to make them easier to read, in particular
    if the tick labels are dense.

    Args:
        ax: The figure axes to update.
        max_num_xticks: The maximum number of ticks to show in the
            figure.
        xticklabel_max_len: If a tick label has a length greater than
            this value, the tick labels are rotated vertically.
        xticklabel_min: If the number of ticks is lower than this
            number the tick labels are rotated vertically.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> from matplotlib import pyplot as plt
    >>> from flamme.utils.figure import readable_xticklabels
    >>> fig, ax = plt.subplots()
    >>> ax.hist(np.arange(10), bins=10)
    >>> readable_xticklabels(ax)

    ```
    """
    xticks = ax.get_xticks()
    if len(xticks) > max_num_xticks:
        n = math.ceil(len(xticks) / max_num_xticks)
        xticks = xticks[::n]
        ax.set_xticks(xticks)
    if len(xticks) > xticklabel_min or any(
        len(str(label)) > xticklabel_max_len for label in ax.get_xticklabels()
    ):
        ax.tick_params(axis="x", labelrotation=90)
