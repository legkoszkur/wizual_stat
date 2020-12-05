from tkinter import *
from tkinter import colorchooser
import random
from Window_popup_message import popup_window

input_var = ["x1","x2","x3","x4","x5","x6","x7","x8",]

root = Tk()
root.geometry("1000x600")
root.resizable(False, False)

input_var = ["x1","x3","x67","x7","x9"]
random_colors = ["#"+''.join([random.choice('0123456789ABCDEF')for j in range(6)]) for i in range(len(input_var))]

class AskColors:
    def __init__(self, master, input_v, colors):
        self.master = master
        self.input_var = input_v
        self.colors = colors

        self.color_lf = LabelFrame(self.master, text="Change color", )
        self.color_lf.place(relx=0.005, rely=0.375, relwidth=0.185, relheight=0.08)

        self.type_b = Button(self.color_lf, text="Type", command=lambda: self.color_backend())
        self.type_b.place(relx=0.05, rely=0.05, relwidth=0.35, relheight=0.8)

        self.text_1 = Entry(self.color_lf, bd=4, relief="groove")
        self.text_1.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.88)

        self.colorhh = Label(self.master, text="",bg="white" )
        self.colorhh.place(relx=0.3, rely=0.6, relwidth=0.3, relheight=0.3)
# todo trzeba zrobić tak że po wybraniu już zmiennych ładowało te kolory teraz juz nie mam siły jutro
        for i in range(len(input_v)):
            print(i)
            Button(self.master, text="Type", bg=self.colors[i]).place(relx=0.15+0.1*i, rely=0.15, relwidth=0.1, relheight=0.1)


    def color_backend(self):
        if self.text_1.get() in self.input_var:
            self.text_1.configure(state='disabled')
            self.c_chooser = colorchooser.askcolor()
            self.my_color = self.c_chooser[1]
            self.index_of_variable = self.input_var.index(self.text_1.get())
            print(self.colors)
            print(self.my_color)
            self.colors[self.index_of_variable] = self.my_color
            print(self.colors)
            self.text_1.configure(state='normal')



        else:
            popup_window("Warning","Un correct variable name. Please insert one correct variable name.")


mm = AskColors(root, input_var,random_colors)

root.mainloop()







