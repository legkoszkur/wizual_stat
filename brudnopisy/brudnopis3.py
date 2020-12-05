import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import pandas as pd

x = [[-4632.0, -52.6364, 1.0, -99.0, -56.0, -78.00, -28.50, -65.0,],
     [4723.0, 53.6705, 99.0, 1.0, 52.5, 33.50, 79.25, 24.0],
     [4938.0, 56.1136, 100.0, 2.0, 64.0, 29.75, 81.25, 68.0],
     [4119.0, 46.8068, 99.0, 1.0, 42.5, 22.00, 73.25, 81.0]]
inde = ["x1", "x2", "x3", "x4"]
kolumn = ["Sum", "Mean", "Max", "Min", "Median", "Quantile_25", "Quantile_75", "Dominant",]
df = pd.DataFrame(x, index=inde, columns=kolumn)


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot().plot(df,kind="bar")

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.dest