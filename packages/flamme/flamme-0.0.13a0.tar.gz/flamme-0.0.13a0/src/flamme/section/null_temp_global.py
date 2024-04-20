r"""Contain the implementation of a section to analyze the temporal
distribution of null values for all columns."""

from __future__ import annotations

__all__ = ["GlobalTemporalNullValueSection"]

import logging
from typing import TYPE_CHECKING

from jinja2 import Template
from matplotlib import pyplot as plt

from flamme.section.base import BaseSection
from flamme.section.null import plot_temporal_null_total
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

    import numpy as np
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class GlobalTemporalNullValueSection(BaseSection):
    r"""Implement a section to analyze the temporal distribution of null
    values for all columns.

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
        r"""``pandas.DataFrame``: The DataFrame to analyze."""
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
        r"""tuple: The individual figure size in pixels. The first
        dimension is the width and the second is the height."""
        return self._figsize

    def get_statistics(self) -> dict:
        return {}

    def render_html_body(self, number: str = "", tags: Sequence[str] = (), depth: int = 0) -> str:
        logger.info(
            "Rendering the temporal distribution of null values for all columns "
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
                "figure": create_temporal_null_figure(
                    frame=self._frame,
                    dt_column=self._dt_column,
                    period=self._period,
                    figsize=self._figsize,
                ),
                "table": create_temporal_null_table(
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
This section analyzes the temporal distribution of null values in all columns.
The column <em>{{dt_column}}</em> is used as the temporal column.

{{figure}}

{{table}}
<p style="margin-top: 1rem;">
"""


def create_temporal_null_figure(
    frame: DataFrame,
    dt_column: str,
    period: str,
    figsize: tuple[float, float] | None = None,
) -> str:
    r"""Create a HTML representation of a figure with the temporal null
    value distribution.

    Args:
        frame: The DataFrame to analyze.
        dt_column: The datetime column used to analyze the
            temporal distribution.
        period: The temporal period e.g. monthly or daily.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Returns:
        The HTML representation of the figure.
    """
    if frame.shape[0] == 0:
        return ""

    num_nulls, total, labels = prepare_data(frame=frame, dt_column=dt_column, period=period)

    fig, ax = plt.subplots(figsize=figsize)
    plot_temporal_null_total(ax=ax, labels=labels, num_nulls=num_nulls, total=total)
    readable_xticklabels(ax, max_num_xticks=100)
    return figure2html(fig, close_fig=True)


def create_temporal_null_table(frame: DataFrame, dt_column: str, period: str) -> str:
    r"""Create a HTML representation of a table with the temporal
    distribution of null values.

    Args:
        frame: The DataFrame to analyze.
        dt_column: The datetime column used to analyze the
            temporal distribution.
        period: The temporal period e.g. monthly or daily.

    Returns:
        The HTML representation of the table.
    """
    if frame.shape[0] == 0:
        return ""
    num_nulls, totals, labels = prepare_data(frame=frame, dt_column=dt_column, period=period)
    rows = []
    for label, num_null, total in zip(labels, num_nulls, totals):
        rows.append(create_temporal_null_table_row(label=label, num_nulls=num_null, total=total))
    return Template(
        """
<details>
    <summary>Statistics per period</summary>

    <p>The following table shows some statistics for each period.

    <table class="table table-hover table-responsive w-auto" >
        <thead class="thead table-group-divider">
            <tr>
                <th>period</th>
                <th>number of null values</th>
                <th>number of non-null values</th>
                <th>total number of values</th>
                <th>percentage of null values</th>
                <th>percentage of non-null values</th>
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


def create_temporal_null_table_row(label: str, num_nulls: int, total: int) -> str:
    r"""Create the HTML code of a new table row.

    Args:
        label: The label of the row.
        num_nulls: The number of null values.
        total: The total number of values.

    Returns:
        The HTML code of a row.
    """
    num_non_nulls = total - num_nulls
    return Template(
        """<tr>
    <th>{{label}}</th>
    <td {{num_style}}>{{num_nulls}}</td>
    <td {{num_style}}>{{num_non_nulls}}</td>
    <td {{num_style}}>{{total}}</td>
    <td {{num_style}}>{{num_nulls_pct}}</td>
    <td {{num_style}}>{{num_non_nulls_pct}}</td>
</tr>"""
    ).render(
        {
            "num_style": 'style="text-align: right;"',
            "label": label,
            "num_nulls": f"{num_nulls:,}",
            "num_non_nulls": f"{num_non_nulls:,}",
            "total": f"{total:,}",
            "num_nulls_pct": f"{100 * num_nulls / total:.2f}%",
            "num_non_nulls_pct": f"{100 * num_non_nulls / total:.2f}%",
        }
    )


def prepare_data(
    frame: DataFrame,
    dt_column: str,
    period: str,
) -> tuple[np.ndarray, np.ndarray, list]:
    r"""Prepare the data to create the figure and table.

    Args:
        frame: The DataFrame to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.

    Returns:
        A tuple with 3 values. The first value is a numpy NDArray
            that contains the number of null values per period. The
            second value is a numpy NDArray that contains the total
            number of values. The third value is a list that contains
            the label of each period.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.section.null_temp_global import prepare_data
    >>> num_nulls, total, labels = prepare_data(
    ...     frame=pd.DataFrame(
    ...         {
    ...             "col1": np.array([np.nan, 1, 0, 1]),
    ...             "col2": np.array([np.nan, 1, 0, np.nan]),
    ...             "datetime": pd.to_datetime(
    ...                 ["2020-01-03", "2020-02-03", "2020-03-03", "2020-04-03"]
    ...             ),
    ...         }
    ...     ),
    ...     dt_column="datetime",
    ...     period="M",
    ... )
    >>> num_nulls
    array([2, 0, 0, 1])
    >>> total
    array([2, 2, 2, 2])
    >>> labels
    ['2020-01', '2020-02', '2020-03', '2020-04']

    ```
    """
    frame = frame.copy()
    columns = frame.columns.tolist()
    columns.remove(dt_column)
    dt_col = "__datetime__"
    frame[dt_col] = frame[dt_column].dt.to_period(period)
    frame.loc[:, columns] = frame[columns].isna().astype(float)

    num_nulls = frame.groupby(dt_col)[columns].sum().sum(axis=1).sort_index()
    total = frame.groupby(dt_col)[columns].count().sum(axis=1).sort_index()
    labels = [str(dt) for dt in num_nulls.index]
    return num_nulls.to_numpy().astype(int), total.to_numpy().astype(int), labels
