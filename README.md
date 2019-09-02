<div align="center">
    <h1>
        xyplot 📈
    </h1>
   	<p>
        Plotting with python made easy
    </p>
</div>



![Meme representing lines of code required to make a matplotlib graph](https://i.redd.it/zhscjhjr3nb21.jpg)

Are you tired of replicating common steps that are needed to plot even a simple polynomial functions in python's infamous Matplotlib?

Worry no more! Presenting xyplot! Plot polynomials easily and more importantly, pythonically!

For example, to plot a polynomial best fit curve you only need to:

```python
import Curve from xyplot
x, y  = [x1, x2, ...], [y1, y2, ...]

curve = Curve(x, y, 2)

curve.setLabels(
  xlabel='time (s)', ylabel='voltage (mV)',
  title='About as simple as it gets, folks'
)

curve.save('MyPlot.png')
```

Makes sense right?

> **Fair Warning**
> This is just a high level sensible wrapper to the matplotlib and numpy package. Its aim is to reduce the workload necessary to make very basic plots.
> To make more extensive and customizable plots, refer to [matplotlib](https://matplotlib.org/)

## Why this effort?

Some of the more inquistive and experienced would be asking why the hell did I create an entire package that can only plot polynomials. Because there was nothing similar in matplotlib and I wanted to help those who have only little knowledge of python plot amazing graphs in as few lines and headaches as possible.

For those who still like control, you always have the fig, ax attributes of the curve class available for exploitation! And then, if you are not satisfied, try the OG matplotlib!



## Documentation?

> Documentation is like sex: when it is good, it is very, very good;                            and when it is bad, it is better than nothing. — *Dick B.*

With that said, the documentation can be found here: 