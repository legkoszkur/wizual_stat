from tkinter import *
from tkinter import colorchooser
colors_list = ["red", "blue", "green", "brown", "yellow", "pink", "gold", "cyan"]
input_var = ["x1","x2","x3","x4","x5","x6","x7","x8",]
# todo ta klasa będzie zwracać wektor z nowymi kodami kolorów
#https://www.youtube.com/watch?v=NDCirUTTrhg&ab_channel=Codemy.com
#todo będzie przymować zmienne zmiennych zeby wiedzieć o ile kolorów zapytać
#to będzie okno w którym będą przyciski w zależności od tego ile będzie zmiennych podanych tyle przycisków i pod kazdym przyciskiem będzie wyskakiwać
root = Tk()
root.geometry("1000x600")
root.resizable(False, False)

class AskColors:
    def __init__(self, master, input_v, colors_l):
        self.master = master
        self.input_var = input_v
        self.color_list = colors_l

        self.color_lf = LabelFrame(self.master, text="Change color", )
        self.color_lf.place(relx=0.005, rely=0.375, relwidth=0.185, relheight=0.08)

        self.type_b = Button(self.color_lf, text="Type", command=lambda: self.color_backend())
        self.type_b.place(relx=0.05, rely=0.05, relwidth=0.35, relheight=0.8)

        self.text_1 = Entry(self.color_lf, bd=4, relief="groove")
        self.text_1.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.88)

        #self.text_1.configure(state='normal') #po kliknięciu w przycisk zmiany powinno zamrozić możliwość zmiany zmiennej
        #self.text_1.insert(END, self.variables)
        #self.text_1.configure(state='disabled')

    def color_backend(self):
        if self.text_1.get() in self.input_var:
            self.c_chooser = colorchooser.askcolor()
            self.my_color = self.c_chooser[1]





mm = AskColors(root, input_var, colors_list)


root.mainloop()







