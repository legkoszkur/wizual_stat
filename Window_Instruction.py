from tkinter import Label, LabelFrame, Text, END


class InstructionWindow:

    def __init__(self, master, ):

        self.master = master
        self.master.geometry("400x200")
        self.master.resizable(False, False)

        self.text = "To enter more than one variable names you must \n use one space as described on below example:"
        self. example_variables = "x1 x2 x3"

        self.label = Label(self.master, text=self.text, justify='left', bg="white", )
        self.label.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

        self.text_lf1 = LabelFrame(self.master, text="Existing variables", relief="flat")
        self.text_lf1.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.7)
        self.text_1 = Text(self.text_lf1, bd=4, relief="groove", wrap="word")

        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(END, self.example_variables)
        self.text_1.configure(state='disabled')
