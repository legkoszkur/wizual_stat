import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from function_popup_message import popup_window
from function_data_check import data_preparation


class Graphics:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.figure = None
        self.a = None
        self.df = None
        self.input_var = None
        self.check_list = None
        self.widget = None
        self.toolbar = None

        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.005, rely=0.01, relwidth=0.75, relheight=0.98)

        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.76, rely=0.91, relwidth=0.23, relheight=0.08)

        self.quit_b = tk.Button(self.menu_f, text="Close", command=self.close_window)
        self.quit_b.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        self.refresh_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.refresh_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        self.variables = list(data.columns)

        self.text_l1 = tk.LabelFrame(self.master, bg="white", text="Existing variables", relief="flat")
        self.text_l1.place(relx=0.76, rely=0.01, relwidth=0.23, relheight=0.44)
        self.text_1 = tk.Text(self.text_l1, bd=4, relief="groove", wrap="word")
        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1 .configure(state='disabled')

        self.text_l2 = tk.LabelFrame(self.master, bg="white", text="Variables on graph", relief="flat")
        self.text_l2.place(relx=0.76, rely=0.46, relwidth=0.23, relheight=0.44)
        self.text_2 = tk.Text(self.text_l2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

    def close_window(self):
        self.master.destroy()

    def preparation_and_absorption_of_the_input(self):

        self.input_var = data_preparation(self.text_2.get("1.0", "end"))

        self.check_list = all(item in self.variables for item in self.input_var)

    def check_if_all_input_correct(self):

        if self.input_var:

            if self.check_list is True:
                return True
            else:
                popup_window("Information", "Incorrect variable name!")
                return False
        else:
            popup_window("Information", "No variables entered")
            return False

    def destroy_previous_objects(self):
        if self.widget:
            self.widget.destroy()

        if self.toolbar:
            self.toolbar.destroy()

    def create_graph(self):
        self.figure = plt.figure()
        self.a = self.figure.add_subplot(111)
        self.df = self.data[self.input_var]
        self.df.plot(ax=self.a, )
        plt.xlabel("Periods", labelpad=1.3)
        plt.title("Amounts")

        canvas = FigureCanvasTkAgg(self.figure, master=self.graph_f)
        self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def chosen_data_insert(self):
        self.preparation_and_absorption_of_the_input()
        if self.check_if_all_input_correct():
            self.destroy_previous_objects()
            self.create_graph()
