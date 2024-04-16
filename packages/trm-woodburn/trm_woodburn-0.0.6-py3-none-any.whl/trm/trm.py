"""
Copyright 2024 David Woodburn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__author__ = "David Woodburn"
__license__ = "MIT"
__date__ = "2024-04-15"
__maintainer__ = "David Woodburn"
__email__ = "david.woodburn@icloud.com"
__status__ = "Development"

import os
import time
import math
import numpy as np


class config:
    uni = True # flag to use unicode characters
    cols = 60 # default column width
    rows = 20 # default row height


def plot(x, y=None, label='', rows=1, cols=1):
    """
    Create a text-based plot of the path defined by (`x`, `y`) using characters.
    If the size of the terminal can be found, that will be used for sizing the
    plot. Otherwise, the default dimensions (config.cols, config.rows) will be
    used. Note that this function does not plot connecting lines, only the
    points specified by the (`x`, `y`) pairs.

    Parameters
    ----------
    x : (K,) or (J, K) np.ndarray
        Array of x-axis values or matrix of rows of x-axis values.
    y : (K,) or (J, K) np.ndarray, default None
        Array of y-axis values or matrix of rows of y-axis values. If `y` is not
        provided, `x` will be used as the `y` array and `x` will be defined to
        be an array of indices.
    label : str, default ''
        Text to place at top of the plot, centered in the border.
    rows : int, default 1
        Desired number of rows if greater than 1 or fraction of existing rows if
        less than 1.
    cols : int, default 1
        Desired number of columns if greater than 1 or fraction of existing
        columns if less than 1.
    """

    # Get the terminal window size.
    try: # Try to get the true size.
        term_cols, term_rows = os.get_terminal_size()
        use_color = True
    except: # If getting terminal size fails, use default values.
        term_cols = config.cols
        term_rows = config.rows
        use_color = False
    term_rows -= 1 # Account for the prompt line.

    # Convert a fractional canvas size to columns and rows.
    if cols <= 1:
        cols = max(round(term_cols * cols), 3)
    if rows <= 1:
        rows = max(round(term_rows * rows), 3)

    # Adjust for the bounding box and ensure integer type.
    rows = int(rows) - 2
    cols = int(cols) - 2

    # Define the sub-columns and sub-rows.
    if config.uni:
        subcols = 2
        subrows = 4
    else:
        subcols = 1
        subrows = 3

    # If only `x` is provided, copy to `y`
    # and make `x` an array of integers.
    if y is None:
        y = x + 0
        if np.ndim(y) == 0:
            x = 1.0
        elif np.ndim(y) == 1:
            x = np.arange(len(y)) + 1
        elif np.ndim(y) == 2:
            J, K = y.shape
            x = np.arange(K) + 1
            x = np.outer(np.ones(J), x)

    # Get the limits.
    eps = 1e-16
    x_min = np.nanmin(x)
    x_max = np.nanmax(x)
    if x_min == x_max:
        x_min -= eps
        x_max += eps
    y_min = np.nanmin(y)
    y_max = np.nanmax(y)
    if y_min == y_max:
        y_min -= eps
        y_max += eps

    # Expand the limits to align zero with the nearest half row so that the zero
    # marker is true.
    if (y_min < 0) and (y_max > 0):
        idx_zero = round((rows - 1.0/subrows)
            * y_max/(y_max - y_min) - 0.5)*subrows + subrows/2
        slope = max((subrows*rows - 1 - idx_zero)/y_min,
            -idx_zero/y_max)
        y_min = (subrows*rows - 1 - idx_zero)/slope
        y_max = -idx_zero/slope
    if y_min == y_max:
        row_zero = -1
    else:
        row_zero = math.floor((rows - 1/subrows)*(y_max)/(y_max - y_min))

    # Ensure x and y are both 2D arrays.
    x = np.array(x)
    y = np.array(y)
    if np.ndim(x) == 0:
        x = np.array([[x]])
    elif np.ndim(x) == 1:
        x = np.array([x])
    if np.ndim(y) == 0:
        y = np.array([[y]])
    elif np.ndim(y) == 1:
        y = np.array([y])

    # Ensure x and y have compatible shapes.
    Jx, Kx = x.shape
    Jy, Ky = y.shape
    if Jx != Jy:
        if Jx == 1 and Jy > 1:
            x = np.outer(np.ones(Jy), x)
            Jx = Jy
        elif Jx > 1 and Jy == 1:
            y = np.outer(np.ones(Jx), y)
            Jy = Jx
        else:
            raise ValueError("x and y must have 1 or the same number of rows.")
    if Kx != Ky:
        raise ValueError("x and y must have the same number of columns.")
    J = Jx
    K = Kx

    # Scale the data to dots.
    X_jk = (subcols*cols - 1)*(x - x_min)/(x_max - x_min)
    Y_jk = (subrows*rows - 1)*(y_max - y)/(y_max - y_min)

    # Get the ranges text.
    x_min_str = f"{x_min:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    x_max_str = f"{x_max:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    y_min_str = f"{y_min:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    y_max_str = f"{y_max:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    ranges = f"({x_min_str}:{x_max_str}, {y_min_str}:{y_max_str})"

    # Map locations to a large matrix.
    M = np.zeros((subrows*rows, subcols*cols), dtype=int)
    X = np.round(X_jk).astype(int)
    Y = np.round(Y_jk).astype(int)
    M[Y, X] = 1 # Puts a 1 wherever the curve coordinates are.

    # Scale the data to dots.
    if (J > 1) and (use_color):
        color_list = [39, 40, 220, 208, 201]
        u = X//subcols
        v = Y//subrows
        F = np.zeros((rows, cols), dtype=int)
        for j in range(J):
            F[v[j], u[j]] = color_list[j % 5]
    else:
        F = None

    # Convert the large matrix to a smaller matrix of character values.
    C = matrix_to_braille(M) if config.uni else matrix_to_ascii(M)

    # Draw the plot.
    draw_graph(C, ranges, label, F, row_zero)


def draw_graph(C, left=None, right=None, F=None, row_zero=-1):
    """
    Parameters
    ----------
    C : (I, J) int np.ndarray
        Matrix of character values.
    left : string, default None
        String to place on the left of the box.
    right : string, default None
        String to place on the right of the box.
    F : (I, J) int np.ndarray, default None
        Matrix of foreground 8-bit color values.
    """

    # Define the box drawing characters.
    if config.uni:
        b = ["\u250C", "\u2500", "\u2510", "\u2502", "\u2502",
                "\u251C", "\u2524", "\u2514", "\u2518"]
    else:
        b = [".", "-", ".", "|", "|", "+", "+", "'", "'"]

    # Replace zeros with spaces.
    C = np.where(C == 0, 0x20, C)

    # Draw the top edge of the box.
    rows, cols = C.shape
    print(f"{b[0]}{b[1]*cols}{b[2]}")

    # Draw the contents and two sides of the box.
    if F is None:
        for row in range(rows):
            string = b[3] if row != row_zero else b[5]
            string += ''.join(list(map(chr, C[row])))
            string += b[4] if row != row_zero else b[6]
            print(string)
    else:
        # For each row of the matrix, draw.
        for row in range(rows):
            # Get this row of data.
            F_row = F[row]
            C_row = C[row]

            # Draw this row.
            chars = ''.join(list(map(chr, C_row)))
            string = b[3] if row != row_zero else b[5]
            f = 0
            for col in range(cols):
                if f != F_row[col]:
                    f = F_row[col]
                    if f == 0:
                        string += "\x1b[0m"
                    else:
                        string += f"\x1b[38;5;{f}m"
                string += chars[col]
            if f != 0:
                string += "\x1b[0m"
            string += b[4] if row != row_zero else b[6]
            print(string)

    # Draw the bottom of the box and the left and right strings.
    mid_dashes = cols - 2 - len(left) - 2 - len(right) - 2*(right != '')
    if mid_dashes >= 0:
        right = f" {right} " if right != '' else ''
        print(f"{b[7]}{b[1]} {left} {b[1]*mid_dashes}{right}{b[1]}{b[8]}")
    else:
        print(f"{b[7]}{b[1]*cols}{b[8]}")
        print(left + (', ' + right)*(right != ''))


def matrix_to_braille(M):
    # Pad the matrix with zeros.
    I, J = M.shape
    II = math.ceil(I/4)*4
    JJ = math.ceil(J/2)*2
    MM = np.zeros((II, JJ), dtype=int)
    MM[:I, :J] = M

    # Convert the matrix of ones and zeros to braille characters.
    C = (0x2800 + MM[::4, ::2] +   8*MM[::4, 1::2]
            +  2*MM[1::4, ::2] +  16*MM[1::4, 1::2]
            +  4*MM[2::4, ::2] +  32*MM[2::4, 1::2]
            + 64*MM[3::4, ::2] + 128*MM[3::4, 1::2])
    return C


def matrix_to_ascii(M):
    # Pad the matrix with zeros.
    I, J = M.shape
    II = math.ceil(I/3)*3
    MM = np.zeros((II, J), dtype=int)
    MM[:I, :J] = M

    # Convert the matrix of ones and zeros to braille characters.
    glyphs = np.array([ # " `-'.!:|"
        0x20, 0x60, 0x2D, 0x27, 0x2E, 0x21, 0x3A, 0x7C])
    C = glyphs[M[::3] + 2*M[1::3] + 4*M[2::3]]
    return C


def matrix_to_stars(M):
    I, J = M.shape
    C = 0x20*np.ones((I, 2*J + 1), dtype=int)
    C[:, 1:-1:2] += 0xA*M
    return C


def bars(x, names=None, width=config.cols, show_zero=True):
    # Get the name space.
    name_space = 0
    if names is not None:
        lens = [len(s) for s in names]
        name_space = max(lens)

    # Adjust the total width to make room for names.
    width -= name_space
    if width < 4:
        width = 4

    # Get min and max.
    if show_zero:
        x_min = 0
    else:
        x_min = min(x)
    x_max = max(x)

    # For each value of x, print the bar.
    k = (width - 3)/(x_max - x_min)
    for n in range(len(x)):
        blen = round((x[n] - x_min) * k)
        bstr = "=" * blen
        estr = ' ' * (width - 3 - blen)
        if names is None:
            print(f" |{bstr}{estr}|")
        else:
            sstr = " " * (name_space - len(names[n]))
            print(f"{sstr}{names[n]} |{bstr}{estr}|")


def heat(matrix):
    """
    Create a surface plot using the input `matrix`. The rows are printed in
    reverse order.
    """

    # Scale the matrix.
    m_min = np.min(matrix)
    m_max = np.max(matrix)
    M = np.round((matrix - m_min)/(m_max - m_min)*23).astype(int) + 232
    rows, cols = M.shape

    # Print the matrix.
    if config.uni:
        for row in range(0, (rows - rows%2), 2):
            for col in range(cols):
                print("\x1b[38;5;%dm\x1b[48;5;%dm\u2580" %
                        (M[row, col], M[row + 1, col]), end="")
            print("\x1b[39m\x1b[49m")
        if rows % 2 == 1:
            for col in range(cols):
                print("\x1b[38;5;%dm\u2580" % (M[-1, col]), end="")
            print("\x1b[39m")
    else:
        for row in range(rows):
            for col in range(cols):
                print("\x1b[48;5;%dm  " % (M[row, col]), end="")
            print("\x1b[49m")


def table(matrix, head=None, left=None, width=10, sep='  '):
    """
    Print a table to the terminal.

    Parameters
    ----------
    matrix : list of lists of values
        Table of values.
    head : list of strings, default []
        List of header labels.
    left : list of strings, default []
        List of left-most column labels.
    width : int, default 10
        Width in characters of each cell.
    sep : string, default '   '
        String separating columns.
    """

    # -----------------
    # Check the inputs.
    # -----------------

    # Check the type of matrix.
    if isinstance(matrix, (str, float, int)):
        matrix = [[matrix]]
    elif isinstance(matrix, list):
        is_2d = False
        for n, datum in enumerate(matrix):
            if isinstance(datum, np.ndarray):
                is_2d = True
                matrix[n] = datum.tolist()
            elif isinstance(datum, list):
                is_2d = True
        if not is_2d:
            matrix = [matrix]
    elif isinstance(matrix, np.ndarray):
        matrix = matrix.tolist()
        if not isinstance(matrix[0], list):
            matrix = [matrix]
    else:
        raise Exception('print_table: matrix must be a list!')

    # Check the type of head.
    if head is None:
        head = []
    elif isinstance(head, (str, float, int)):
        head = [head]
    elif isinstance(head, np.ndarray):
        head = head.tolist()
    elif not isinstance(head, list):
        raise Exception('print_table: head must be a list!')

    # Check the type of left.
    if left is None:
        left = []
    elif isinstance(left, (str, float, int)):
        left = [left]
    elif isinstance(left, np.ndarray):
        left = left.tolist()
    elif not isinstance(left, list):
        raise Exception('print_table: left must be a list!')

    # Check that width is within 3 to 30.
    if width < 6:
        width = 6
    elif width > 30:
        width = 30

    # -------------
    # Print header.
    # -------------

    def f2str(num, width=6):
        """
        Convert a floating-point number, `num`, to a string, keeping the total
        width in characters equal to `width`.
        """

        # Ensure width is not less than 6, and check if padding should not be
        # used (i.e., width was negative).
        if width < 0:
            width = -width
            skip_padding = True
        else:
            skip_padding = False
        if width < 6:
            width = 6

        # Make num non-negative by remember the minus.
        if num < 0:
            sw = 1
            s = "-"
            num = -num
            ei = int(np.floor(np.log10(num))) # integer exponent
        elif num > 0:
            sw = 0
            s = ""
            ei = int(np.floor(np.log10(num))) # integer exponent
        else:
            sw = 0
            s = ""
            ei = 0

        # Build number string without leading spaces.
        if ei >= 4:     # 10000 to inf
            f_str = s + "%.*g" % (width - 2 - len(str(ei)) - sw,
                    num*(10**(-ei)))
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
            f_str += "e%d" % (ei)
        elif ei >= 0:   # 1 to 10-
            f_str = s + "%.*f" % (width - 2 - ei - sw, num)
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
        elif ei >= -3:  # 0.001 to 1-
            f_str = s + "%.*f" % (width - 2 - sw, num)
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
        else:           # -inf to 0.001-
            f_str = s + "%.*g" % (width - 3 - len(str(-ei)) - sw,
                    num*(10**(-ei)))
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
            f_str += "e%d" % (ei)

        # Add leading spaces for padding.
        if not skip_padding:
            f_str = " "*(width - len(f_str)) + f_str

        return f_str

    def fixed_width_string(C, width=6):
        """
        Convert a string or numeric value, `C`, to a string, keeping the total
        width in characters equal to `width`.
        """

        if isinstance(C, str):
            L = len(C)
            if L > width:
                L = width - 3
                return C[:L] + '...'
            elif L == width:
                return C
            else:
                return ' '*(width-L) + C
        elif isinstance(C, float):
            return f2str(C, width)
        else:
            return f2str(float(C), width)

    if len(head) > 0:
        row_str = ""
        if len(left) > 0:
            row_str += " "*width + " | "
        for n_col, val in enumerate(head):
            if n_col > 0:
                row_str += sep
            row_str += fixed_width_string(val, width)
        print(row_str)

        row_str = ""
        if len(left) > 0:
            row_str += "-"*width + " | "
        for n_col in range(len(head)):
            if n_col > 0:
                row_str += sep
            row_str += "-"*width
        print(row_str)

    # -------------
    # Print matrix.
    # -------------

    for n_row, vals in enumerate(matrix):
        row_str = ""
        if len(left) > n_row:
            row_str += fixed_width_string(left[n_row], width) + " | "
        elif len(left) > 0:
            row_str += " "*width + " | "
        for n_col, val in enumerate(vals):
            if n_col > 0:
                row_str += sep
            row_str += fixed_width_string(val, width)
        print(row_str)


def sparsity(matrix, label=''):
    # Convert matrix to zeros and ones.
    M = (np.abs(matrix) > 1e-30).astype(int)

    # Convert the large matrix to a smaller matrix of character values.
    C = matrix_to_braille(M) if config.uni else matrix_to_stars(M)

    # Create the shape string.
    shape_str = f"{matrix.shape[0]}x{matrix.shape[1]}"

    # Draw the plot.
    draw_graph(C, shape_str, label)


def time_str(t_seconds):
    """ Convert time in seconds to a clock string of the form
    `HH:MM:SS.S`. """
    t_seconds = abs(t_seconds)
    hours = int(t_seconds/3600)
    minutes = int((t_seconds - hours*3600)//60)
    seconds = (t_seconds % 60)
    clock_str = "%02d:%02d:%04.1f" % (hours, minutes, seconds)
    return clock_str


def progress(k, K, tic=None, width=None):
    """
    Output a simple progress bar with percent complete to the terminal. When `k`
    equals `K - 1`, the progress bar will complete and start a new line.

    Parameters
    ----------
    k : int
        Index which should grow monotonically from 0 to K - 1.
    K : int
        Final index value of `k` plus 1.
    tic : float, default None
        Starting time (s). If provided, an estimated time remaining will be
        displayed. If left as None, no time will be shown. When the progress bar
        completes, the total duration will be shown.
    width : int, default None
        Width of the full string, including the percent complete, the bar, and
        the clock. If not given, the width of the terminal window will be used.
    """

    # Default the width to the terminal width or config.cols.
    if width is None:
        try: # Try to get the true size.
            width, _ = os.get_terminal_size()
        except: # If getting terminal size fails, use default values.
            width = config.cols

    # Get the ratio.
    ratio = (k + 1)/K

    # Get the clock string.
    if tic is not None:
        t_elapsed = time.perf_counter() - tic
        if k + 1 == K:
            clk_str = "  " + time_str(t_elapsed)
        else:
            t_remaining = t_elapsed*(1.0 - ratio)/ratio
            clk_str = " -" + time_str(t_remaining)
    else:
        clk_str = ""

    # Build the progress bar.
    N = width - 8 - len(clk_str) # maximum length of bar within the brackets
    if k + 1 == K:
        print(f"\r100% [{'/'*N}]{clk_str}", flush=True)
    elif (K < N) or (k % int(K/N) == 0):
        bar_len = int(N*ratio)
        print(f"\r{int(100*ratio):3d}% "
            + f"[{'/'*bar_len}{'-'*(N - bar_len)}]{clk_str}",
            end="", flush=True)
