from tkinter import *
from tkinter import colorchooser
from Window_popup_message import popup_window



def color_backend(self):
    if self.text_1.get() in self.input_var:
        self.text_1.configure(state='disabled')
        self.c_chooser = colorchooser.askcolor()
        self.my_color = self.c_chooser[1] # chosen color
        self.index_of_variable = self.input_var.index(self.text_1.get()) # color index
        self.text_1.configure(state='normal')
    else:
        popup_window("Warning","Un correct variable name. Please insert one correct variable name.")










