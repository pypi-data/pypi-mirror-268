r"""Contain the implementation of a section to count the number of rows
for a given temporal window."""

from __future__ import annotations

__all__ = ["TemporalRowCountSection"]

import logging
from typing import TYPE_CHECKING

from jinja2 import Template
from matplotlib import pyplot as plt

from flamme.section.base import BaseSection
from flamme.section.utils import (
    GO_TO_TOP,
    render_html_toc,
    tags2id,
    tags2title,
    valid_h_tag,
)
from flamme.utils.figure import figure2html, readable_xticklabels

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pandas import DataFrame

logger = logging.getLogger(__name__)


class TemporalRowCountSection(BaseSection):
    r"""Implement a section to analyze the number of rows per temporal
    window.

    Args:
        frame: The DataFrame to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.
    """

    def __init__(
        self,
        frame: DataFrame,
        dt_column: str,
        period: str,
        figsize: tuple[float, float] | None = None,
    ) -> None:
        if dt_column not in frame:
            msg = (
                f"Datetime column {dt_column} is not in the DataFrame "
                f"(columns:{sorted(frame.columns)})"
            )
            raise ValueError(msg)
        self._frame = frame
        self._dt_column = dt_column
        self._period = period
        self._figsize = figsize

    @property
    def frame(self) -> DataFrame:
        r"""The DataFrame to analyze."""
        return self._frame

    @property
    def dt_column(self) -> str:
        r"""The datetime column."""
        return self._dt_column

    @property
    def period(self) -> str:
        r"""The temporal period used to analyze the data."""
        return self._period

    @property
    def figsize(self) -> tuple[float, float] | None:
        r"""The individual figure size in pixels.

        The first dimension is the width and the second is the height.
        """
        return self._figsize

    def get_statistics(self) -> dict:
        return {}

    def render_html_body(self, number: str = "", tags: Sequence[str] = (), depth: int = 0) -> str:
        logger.info(
            "Rendering the number of rows per temporal window "
            f"| datetime column: {self._dt_column} | period: {self._period}"
        )
        return Template(self._create_template()).render(
            {
                "go_to_top": GO_TO_TOP,
                "id": tags2id(tags),
                "depth": valid_h_tag(depth + 1),
                "title": tags2title(tags),
                "section": number,
                "dt_column": self._dt_column,
                "figure": create_temporal_count_figure(
                    frame=self._frame,
                    dt_column=self._dt_column,
                    period=self._period,
                    figsize=self._figsize,
                ),
                "table": create_temporal_count_table(
                    frame=self._frame,
                    dt_column=self._dt_column,
                    period=self._period,
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
This section analyzes the number of rows per temporal window.
The column <em>{{dt_column}}</em> is used as the temporal column.

{{figure}}

{{table}}
<p style="margin-top: 1rem;">
"""


def create_temporal_count_figure(
    frame: DataFrame,
    dt_column: str,
    period: str,
    figsize: tuple[float, float] | None = None,
) -> str:
    r"""Return a HTML representation of a figure with number of rows per
    temporal windows.

    Args:
        frame: The DataFrame to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Returns:
        The HTML representation of the figure.
    """
    if frame.shape[0] == 0:
        return "<span>&#9888;</span> No figure is generated because there is no data"

    counts, labels = prepare_data(frame=frame, dt_column=dt_column, period=period)
    fig, ax = plt.subplots(figsize=figsize)
    ax.bar(x=labels, height=counts, color="tab:blue")
    ax.set_ylabel("number of rows")
    ax.set_xlim(-0.5, len(labels) - 0.5)
    readable_xticklabels(ax, max_num_xticks=100)
    return figure2html(fig, close_fig=True)


def create_temporal_count_table(frame: DataFrame, dt_column: str, period: str) -> str:
    r"""Return a HTML representation of a figure with number of rows per
    temporal windows.

    Args:
        frame: The DataFrame to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.

    Returns:
        The HTML representation of the table.
    """
    if frame.shape[0] == 0:
        return ""
    counts, labels = prepare_data(frame=frame, dt_column=dt_column, period=period)
    rows = []
    for label, num_rows in zip(labels, counts):
        rows.append(create_temporal_count_table_row(label=label, num_rows=num_rows))
    return Template(
        """
<details>
    <summary>Statistics per period</summary>

    <p>The following table shows some statistics for each period.

    <table class="table table-hover table-responsive w-auto" >
        <thead class="thead table-group-divider">
            <tr>
                <th>period</th>
                <th>number of rows</th>
            </tr>
        </thead>
        <tbody class="tbody table-group-divider">
            {{rows}}
            <tr class="table-group-divider"></tr>
        </tbody>
    </table>
</details>
"""
    ).render({"rows": "\n".join(rows), "period": period})


def create_temporal_count_table_row(label: str, num_rows: int) -> str:
    r"""Return the HTML code of a table row.

    Args:
        label: The label i.e. temporal window.
        num_rows: The number of rows for the given temporal
            window.

    Returns:
        The HTML code of a row.
    """
    return Template("<tr><th>{{label}}</th><td {{num_style}}>{{num_rows}}</td></tr>").render(
        {
            "num_style": 'style="text-align: right;"',
            "label": label,
            "num_rows": f"{num_rows:,}",
        }
    )


def prepare_data(
    frame: DataFrame,
    dt_column: str,
    period: str,
) -> tuple[list[int], list[str]]:
    r"""Prepare the data to create the figure and table.

    Args:
        frame: The DataFrame to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.

    Returns:
        A tuple with the counts and the temporal window labels.
    """
    if frame.shape[0] == 0:
        return [], []

    frame = frame[[dt_column]].copy()
    columns = frame.columns.tolist()
    dt_col = "__datetime__"
    frame[dt_col] = frame[dt_column].dt.to_period(period)

    frame_count = frame.groupby(dt_col)[columns].size()
    count = frame_count.to_numpy().astype(int).tolist()
    labels = [str(dt) for dt in frame_count.index]
    return count, labels
