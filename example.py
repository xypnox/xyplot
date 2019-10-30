from xyplot import Curve

# Our data
x, y = [0, 2, 4, 6, 8], [0, 2, 4, 6, 17]

# A simple curve object with data and degree of polynomial
curve = Curve(x, y, 2)

# Set the x, y axis labels and Title
curve.set(
    xlabel = "Labels are fun and easy",
    ylabel = "Oooh see him Go!",
    title = "I am an easy Graph"
)

# Label our data and curve
curve.createPlot(
    plotLabel="Label for the Curve",
    dataLabel="Label for our DATA",
)
curve.get_linear()

curve.save("sample.png") # Save our graph in