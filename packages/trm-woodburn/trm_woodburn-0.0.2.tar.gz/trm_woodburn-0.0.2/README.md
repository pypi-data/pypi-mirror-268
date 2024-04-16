# Console Information Explorer

This library provides several functions for nicely printing data to the
terminal. MatPlotLib is a very nice library, but it can be a bit tedious at
times when all you want is something quick and dirty.

-   Every separate plot needs to be introduced with a `plt.figure()` statement.
-   Large sets of data can be slow to render.
-   If you are working in full screen on the terminal, plots can pull you to
    another window.
-   The entire python program and the terminal is locked up after any
    `plt.show()` command until you close all figure windows.
-   Unless you save the figures to individual files, there is no buffer to show
    plots from past runs.

These are all excuses to use this library. But, the biggest reason to use this
library is that the terminal is cool, and the more you can do you work in the
terminal the better.

## Plots

```python
trm.plot(x, y=None, label='', cols=1, rows=1)
```

The plot function will render all the data points defined by `x` and `y` to the
terminal. The inputs `x` and `y` can be vectors or matrices. If they are
matrices, each row is treated as a separate curve.

The shapes of `x` and `y` do not have to be the same, but they must be
compatible. So, `x` could be a vector and `y` could be a matrix as long as the
length of `x` equals the number of columns of `y`.

If only `x` is given, it will be interpreted as the `y` values, and the `x`
values will be the array of indices.

When the plot is printed, the graph is rendered within a box and the ranges of
`x` and `y` are listed in the bottom left corner. So,

```
(0:99, -1.5:1.5)
```

means that `x` ranges from `0` to `99` and `y` ranges from `-1.5` to `1.5`.

If a `label` is given, this will be printed in the bottom right of the plot box.

The `cols` and `rows` parameters let you specify the number of terminal text
columns and rows to use for the plot, respectively. For each of these, if the
value is less than or equal to 1, it represents a portion of the available space
to use. For example, if `cols` is `0.5`, then half the number of columns of the
current terminal window will be used for the plot. If the value is greater than
1, it represents the absolute number of columns or rows to use. Also, if the
size of the current terminal cannot be obtained, the available space will
default to `60` columns and `20` rows.

By default, this library will use unicode symbols (specifically braille) for
plotting. A good font to use for this is JuliaMono. However, if your font does
not support the necessary unicode symbols, you can tell the library to not use
them by setting `trm.UNI` to `False` before calling the `trm.plot` function.

If only one curve is being plotted, the characters will be written in whatever
the default font color is set to in your terminal. If more than one curve is
plotted, color will be used. The color map is blue, green, yellow, red, and
magenta. If you have more than 5 curves (This is just a terminal-based plot; why
would you do that?), then the colors will recyle.

## Bars

```python
trm.bars(x, labels=None, width=COLS, show_zero=True)
```

It can be convenient to plot a simple bar graph. The `x` input is the vector of
values. The `labels` input is a list of strings corresponding to the labels to
print before the bar of each value in `x`. The `width` input is the total width
of characters including the labels.

## Heat maps

```python
trm.heat(matrix)
```

The `heat` function will generate a heat map of the `matrix` input using 24
shades of gray. Black is used for the lowest value and white for the highest
value. If `trm.UNI` is `True`, half-block characters from the unicode table will
be used. If it is `False`, two spaces per element of the matrix will be used.

## Tables

```python
trm.table(matrix, head=None, left=None, width=10, sep='  ')
```

You can print a nicely spaced table of the `matrix` data. The `head` and `left`
inputs are lists of header and left-most column labels, respectively, to print
around the `matrix`.

## Sparsity

```python
trm.sparsity(matrix, label='')
```

If all you want to see is the sparsity of a matrix, use this function. The
`label` input will be placed in the bottom-right corner of the render.

## Progress bars

```python
trm.progress(k, K, tic=None, width=None)
```

There are many progress bar libraries available for Python. But, many of them
seem to be extremely over-complicated. TQDM, for example, includes over 20
source files. This library's implementation of a progress bar is a single,
one-page function. The `k` input is the counter of whatever for loop the
progress bar is reporting on. The `K` input is one greater than the largest
possible value of `k`, as in `for k in range(K):`. If `tic` is provided, the
estimated time remaining to complete the process based on the initial time
stored in `tic` will be displayed. When the process is completed, the total
elapsed time since `tic` will be displayed. If `width` is not provided, the full
width of the current terminal window will be used.
