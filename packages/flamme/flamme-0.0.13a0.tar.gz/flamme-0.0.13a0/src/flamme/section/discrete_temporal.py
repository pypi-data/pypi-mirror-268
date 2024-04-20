r"""Contain the implementation of a section to analyze the temporal
distribution of a column with discrete values."""

from __future__ import annotations

__all__ = ["ColumnTemporalDiscreteSection"]

import logging
from typing import TYPE_CHECKING

import numpy as np
from jinja2 import Template
from matplotlib import pyplot as plt
from pandas import DataFrame

from flamme.section.base import BaseSection
from flamme.section.utils import (
    GO_TO_TOP,
    render_html_toc,
    tags2id,
    tags2title,
    valid_h_tag,
)
from flamme.utils.figure import figure2html, readable_xticklabels
from flamme.utils.sorting import mixed_typed_sort

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = logging.getLogger(__name__)


class ColumnTemporalDiscreteSection(BaseSection):
    r"""Implement a section that analyzes the temporal distribution of a
    column with discrete values.

    Args:
        frame: The DataFrame to analyze.
        column: The column of the DataFrame to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or
            daily.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.
    """

    def __init__(
        self,
        frame: DataFrame,
        column: str,
        dt_column: str,
        period: str,
        figsize: tuple[float, float] | None = None,
    ) -> None:
        self._frame = frame
        self._column = column
        self._dt_column = dt_column
        self._period = period
        self._figsize = figsize

    @property
    def column(self) -> str:
        return self._column

    @property
    def dt_column(self) -> str:
        return self._dt_column

    @property
    def period(self) -> str:
        return self._period

    @property
    def figsize(self) -> tuple[float, float] | None:
        r"""tuple: The individual figure size in pixels. The first
        dimension is the width and the second is the height."""
        return self._figsize

    def get_statistics(self) -> dict:
        return {}

    def render_html_body(self, number: str = "", tags: Sequence[str] = (), depth: int = 0) -> str:
        logger.info(
            f"Analyzing the temporal discrete distribution of {self._column} | "
            f"datetime column: {self._dt_column} | period: {self._period}"
        )
        return Template(self._create_template()).render(
            {
                "go_to_top": GO_TO_TOP,
                "id": tags2id(tags),
                "depth": valid_h_tag(depth + 1),
                "title": tags2title(tags),
                "section": number,
                "column": self._column,
                "dt_column": self._dt_column,
                "period": self._period,
                "figure": create_temporal_figure(
                    frame=self._frame,
                    column=self._column,
                    dt_column=self._dt_column,
                    period=self._period,
                    figsize=self._figsize,
                ),
            }
        )

    def render_html_toc(
        self, number: str = "", tags: Sequence[str] = (), depth: int = 0, max_depth: int = 1
    ) -> str:
        return render_html_toc(number=number, tags=tags, depth=depth, max_depth=max_depth)

    def _create_template(self) -> str:
        return """
<h{{depth}} id="{{id}}">{{section}} {{title}} </h{{depth}}>

{{go_to_top}}

<p style="margin-top: 1rem;">
This section analyzes the temporal distribution of column <em>{{column}}</em>
by using the column <em>{{dt_column}}</em>.

{{figure}}

{{table}}
<p style="margin-top: 1rem;">
"""


def create_temporal_figure(
    frame: DataFrame,
    column: str,
    dt_column: str,
    period: str,
    figsize: tuple[float, float] | None = None,
) -> str:
    r"""Create a HTML representation of a figure with the temporal value
    distribution.

    Args:
        frame: The DataFrame to analyze.
        column: The column to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or
            daily.
        log_y (bool, optional): If ``True``, it represents the bars
            with a log scale. Default: ``False``
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Returns:
        The HTML representation of the figure.
    """
    if frame.shape[0] == 0:
        return "<span>&#9888;</span> No figure is generated because the column is empty"
    frame = frame[[column, dt_column]].copy()
    col_dt, col_count = "__datetime__", "__count__"
    frame[col_dt] = frame[dt_column].dt.to_period(period).astype(str)
    frame = frame[[column, col_dt]].groupby(by=[col_dt, column], dropna=False)[column].size()
    frame = DataFrame({col_count: frame}).reset_index().sort_values(by=[col_dt, column])
    frame = frame.pivot_table(
        index=col_dt, columns=column, values=col_count, fill_value=0, dropna=False
    )

    labels = mixed_typed_sort(frame.columns.tolist())
    num_labels = len(labels)
    steps = frame.index.tolist()
    x = np.arange(len(steps), dtype=int)
    bottom = np.zeros_like(x)
    width = 0.9 if len(steps) < 50 else 1
    fig, ax = plt.subplots(figsize=figsize)
    my_cmap = plt.get_cmap("viridis")
    for i, label in enumerate(labels):
        count = frame[label].to_numpy().astype(int)
        ax.bar(x, count, label=label, bottom=bottom, width=width, color=my_cmap(i / num_labels))
        bottom += count

    if len(labels) <= 10:
        ax.legend()
    ax.set_xticks(x, labels=steps)
    readable_xticklabels(ax, max_num_xticks=100)
    ax.set_xlim(-0.5, len(steps) - 0.5)
    ax.set_ylabel("Number of occurrences")
    ax.set_title(f"Temporal distribution for column {column}")
    return figure2html(fig, close_fig=True)
