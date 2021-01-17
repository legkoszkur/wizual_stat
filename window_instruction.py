from tkinter import Label, LabelFrame, Text, END


# this class create window with short instruction
class InstructionWindow:

    def __init__(self, master, ):

        self.master = master
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        self.text = "1. To enter more than one variable name you must use one space as described on below example:"

        self.text_1 = Text(self.master, wrap="word" )
        self.text_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)

        self.text_1.configure(state='normal')
        self.text_1.insert(END, self.text)
        self.text_1.configure(state='disabled')

        self.text_lf1 = LabelFrame(self.master, text="Existing variables", relief="flat")
        self.text_lf1.place(relx=0.35, rely=0.21, relwidth=0.3, relheight=0.5)

        self.example_variables = "x1 x2 x3"

        self.text_2 = Text(self.text_lf1, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_2.configure(state='normal')
        self.text_2.insert(END, self.example_variables)
        self.text_2.configure(state='disabled')

        self.text2 = "2. In order for the data to be correctly imported, it should be in CSV, XLSX or XLS formats." \
            " In addition, all variable names should be on the first row and assigned values vertically below them."

        self.text_3 = Text(self.master, wrap="word")
        self.text_3.place(relx=0.05, rely=0.7, relwidth=0.9, relheight=0.25)
        self.text_3.configure(state='normal')
        self.text_3.insert(END, self.text2)
        self.text_3.configure(state='disabled')
