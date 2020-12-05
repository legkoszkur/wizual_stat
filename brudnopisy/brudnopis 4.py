import tkinter as tk
from tkinter import ttk, Canvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class application():

    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Emetor')
        self.win.geometry('700x650+230+30')
        self.win.configure(background='pale green')
        self.createWidgets()

    def createWidgets(self):
        self.var1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.win, text='1',command= self.mat, variable=self.var1)
        self.check1.grid(row=1,column=0)

    def mat(self):
        data=[{'a':1,'b':2},{'a':1,'b':4},{'a':1,'b':6},{'a':1,'b':8}]
        index=['1','2','3','4']

        fig=Figure(figsize=(4,5), facecolor='white')
        a=fig.add_subplot(111)

        df = pd.DataFrame(data, index=index)
        df.plot(kind='bar', ax=a)

        canvas=FigureCanvasTkAgg(fig, self.win)
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4)
        canvas.draw()

if __name__ == '__main__':
    app = application()
    app.win.mainloop()
