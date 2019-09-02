import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from . import curveFunc as cf
from . import colors


class Curve:
    """Creates beautiful plots from data points

    This class is used as a higher level approach to plot polynomial graphs
    using matplotlib. The graph is

    Only sensible defaults are asssumed and wherever possible, they are
    over-rideable by passing them as attributes.

    If you only need some neat and tidy functions to generate the numpy ranges,
    polynomial values etc, check curveFunc.py


    Attributes:
        data: data of orignal x, y
        curve: contains the list returned by getCurve()
            first element is x values over numpy range
            second element is y values for polynomial over numpy range
            third element are the polynomial constants, higher first
        polyDeg: Number, Degree of the polynomial to be plotted
        colors: List of colors used for coloring the plot
        fig, ax: objects of the plt.subplots(), can be used to hack and do
            cool stuff not yet _easified_ in this package
    """

    def __init__(
        self,
        x, y,
        polyDeg=1,
        depth=1000,
        extend=1,
        colors=colors
    ):
        """Initialize the data and metadata for Plotting

        The data and other minor settings are initialized here. The different
        matplotlib objects are separated and stored as class attributes. They can
        be accessed outside and are welcome for hacking.


        Args:
            x: List of data points for the x axis.
            y: List of data points for the y axis.
            polyDeg: Number, Degree of the polynomial to be plotted
            depth: _optional_ Integer >= 1, Number of divisions for numpy
                array
            extend: _optional_ Fraction, A factor with which the range is
                increased in both directions beyond the largest and smallest
                x data set points
            colors: _optional_ A list of colors used to color the graph.
                First value is used for Data, the last for Plot.

        """
        self.data = x, y
        self.curve = cf.getCurve(x, y, polyDeg, depth, extend)
        self.polyDeg = polyDeg
        self.colors = colors
        self.fig, self.ax = plt.subplots()

    def createPlot(
        self,
        plotData=True,
        plotLabel='',
        dataLabel='',
        legend=False,
        grid=True,
        path='',
        dpi=300
    ):
        """Create the plot

        The plot is plotted through this method!
        All parameters are optional

        Args:
            plotData: Bool, Plot data points as a scatter plot if True (default).
            plotLabel: string, Label for plot
            dataLabel: string, Label for data points
            legend: Bool, Whether to display the legend,
                if plotLabel or dataLabel are set, they override this.
            grid: Bool, whether to display grid or not. By default yes!
            path: string, path of file to be saved
            dpi: Number, used as dpi for saving the figure
        """
        self.ax.plot(self.curve[0], self.curve[1],
                     color=self.colors[len(self.colors)-1], label=plotLabel)

        if plotData:
            self.ax.scatter(self.data[0], self.data[1],
                            color=self.colors[0],
                            label=dataLabel)

        self.ax.grid()
        if plotLabel or dataLabel or legend:
            self.ax.legend()

        if path:
            self.fig.savefig(path)

        return self.fig

    def set(self, *args, **kwargs):
        """Set the labels etc for the plot

        This function accepts all arguments that can set to ax.set

        Args:
            xlabel: String, Label for x axis
            ylabel: String, Label for y axis
            title: String, title for graph

            ...others that can be passed to ax.set()
        """
        self.ax.set(*args, **kwargs)

    def save(self, path, dpi=300):
        """Save the plot

        The plot is saved through this method!
        All parameters except **path** are optional

        Args:
            path: string, path of file to be saved
            dpi: Number, used as dpi for saving the figure
        """
        if path:
            self.fig.savefig(path, dpi=300)
