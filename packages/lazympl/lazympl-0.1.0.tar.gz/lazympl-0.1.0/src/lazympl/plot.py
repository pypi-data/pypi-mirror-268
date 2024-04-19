from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable, Sequence

    import matplotlib.axes as mpla

    from .figure import Figure


class Plot(ABC):
    @abstractmethod
    def draw_on(self, ax: mpla.Axes) -> None:
        """Draw plot onto provided axes."""


@dataclass(frozen=True)
class FigureTeePlot(Plot):
    plot: Plot
    make_figure: Callable[[Plot], Figure]
    file_name: str
    dpi: int = 200

    def draw_on(self, ax: mpla.Axes) -> None:
        # Do our job and draw the child plot
        self.plot.draw_on(ax)
        # Also save a side copy of the plot
        tee_fig = self.make_figure(self.plot).figure()
        tee_fig.savefig(self.file_name, dpi=self.dpi)


@dataclass(frozen=True, eq=False)
class PlotOnSameAxes(Plot):
    plots: Sequence[Plot]

    def draw_on(self, ax: mpla.Axes) -> None:
        for plot in reversed(self.plots):
            plot.draw_on(ax)


@dataclass(frozen=True)
class PlotIf(Plot):
    condition: bool
    plot: Plot

    def draw_on(self, ax: mpla.Axes) -> None:
        if self.condition:
            self.plot.draw_on(ax)


@dataclass(frozen=True)
class PlotIfElse(Plot):
    condition: bool
    plot_if: Plot
    plot_else: Plot

    def draw_on(self, ax: mpla.Axes) -> None:
        if self.condition:
            self.plot_if.draw_on(ax)
        else:
            self.plot_else.draw_on(ax)


@dataclass(frozen=True, eq=False)
class WithAxisLabels(Plot):
    plot: Plot
    xlabel: str
    ylabel: str

    def draw_on(self, ax: mpla.Axes) -> None:
        self.plot.draw_on(ax)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)


@dataclass(frozen=True, eq=False)
class WithPlotTitle(Plot):
    plot: Plot
    title: str

    def draw_on(self, ax: mpla.Axes) -> None:
        self.plot.draw_on(ax)
        ax.set_title(self.title)
