from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import matplotlib.figure as mplf

if TYPE_CHECKING:
    from os import PathLike
    from typing import Any, Sequence, Union

    from .plot import Plot


class Figure(ABC):
    @abstractmethod
    def figure(self) -> mplf.Figure:
        """Build the matplotlib figure"""

    def save_to(self, file_name: Union[str, PathLike]) -> None:
        """Save the figure to provided image file name"""
        self.figure().savefig(file_name)


@dataclass(frozen=True)
class SinglePlotFigure(Figure):
    plot: Plot
    figsize: tuple[float, float] = (6.0, 6.0)

    def figure(self) -> mplf.Figure:
        fig = mplf.Figure(figsize=self.figsize, constrained_layout=True)
        ax = fig.add_subplot()
        self.plot.draw_on(ax)
        return fig


@dataclass(frozen=True)
class MatrixOfPlotsFigure(Figure):
    plots: Sequence[Plot]
    nrows: int = 3
    ncols: int = 3
    individual_plot_size: tuple[float, float] = (5.0, 5.0)
    title: str = ""
    subplots_kwargs: dict[str, Any] = field(default_factory=dict)

    def figure(self) -> mplf.Figure:
        fig = mplf.Figure(
            figsize=(
                self.individual_plot_size[0] * self.ncols,
                self.individual_plot_size[1] * self.nrows,
            ),
            constrained_layout=True,
        )
        axs = fig.subplots(
            nrows=self.nrows, ncols=self.ncols, squeeze=False, **self.subplots_kwargs
        )

        for p, ax in zip(self.plots, axs.flat):
            p.draw_on(ax)

        for ax in axs[:-1, :].flat:
            ax.set_xlabel(None)

        for ax in axs[:, 1:].flat:
            ax.set_ylabel(None)

        if self.title:
            fig.suptitle(self.title)

        return fig
