import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from function_popup_message import popup_window
import seaborn as sns
from function_data_check import data_preparation


class MultiCorrelation:
    # creates window of this class
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.corr_matrix = None
        self.figure = None
        self.a = None
        self.input_var = None
        self.check_list = None
        self.widget = None
        self.toolbar = None
        self.text_stat = None

        # creates labelframe for graph and data
        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.005, rely=0.01, relwidth=0.8, relheight=0.98)

        # creates labelframe for menu
        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.81, rely=0.91, relwidth=0.185, relheight=0.08)

        # creates button to quit window
        self.quit_b = tk.Button(self.menu_f, text="Close", command=self.close_window)
        self.quit_b.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        # creates load button
        self.load_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.load_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        # takes data from data object
        self.variables = list(data.columns)

        # creates label frame to text widget
        self.text_lf1 = tk.LabelFrame(self.master, text="Existing variables", relief="flat")
        self.text_lf1.place(relx=0.81, rely=0.01, relwidth=0.185, relheight=0.44)

        # creates text widget for display existing variables
        self.text_1 = tk.Text(self.text_lf1, bd=4, relief="groove", wrap="word")
        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1.configure(state='disabled')

        # creates label frame to text widget
        self.text_lf2 = tk.LabelFrame(self.master, text="Chosen variables", relief="flat")
        self.text_lf2.place(relx=0.81, rely=0.46, relwidth=0.185, relheight=0.37)

        # creates text widget to data insert
        self.text_2 = tk.Text(self.text_lf2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        # creates labelframe to switch between graph and report
        self.options_lf = tk.LabelFrame(self.master, text="Options")
        self.options_lf.place(relx=0.81, rely=0.83, relwidth=0.185, relheight=0.08)
        self.ratio_var = tk.IntVar()
        self.radio_b1 = tk.Radiobutton(self.options_lf, text="Report", value=1, variable=self.ratio_var)
        self.radio_b2 = tk.Radiobutton(self.options_lf, text="Graph", value=0, variable=self.ratio_var)
        self.radio_b1.grid(row=0, column=0, sticky="W")
        self.radio_b2.grid(row=0, column=1, sticky="W")

    # close window method
    def close_window(self):
        self.master.destroy()

    # takes and prepares data
    def preparation_and_absorption_of_the_input(self):
        self.input_var = data_preparation(self.text_2.get("1.0", "end"))
        self.check_list = all(item in self.variables for item in self.input_var)

    # checks if all insert data are correct
    def check_if_all_input_correct(self):
        if self.input_var:

            if self.check_list:
                return True
            else:
                popup_window("Information", "Incorrect variable name!")
                return False
        else:
            popup_window("Information", "No variables entered.")
            return False

    # destroys previous objects while user switch rapport and graph multiple times
    def destroy_previous_objects(self):

        if self.widget:
            self.widget.destroy()

        if self.toolbar:
            self.toolbar.destroy()

        if self.text_stat:
            self.text_stat.destroy()

    # graph creator inside graph option
    def create_graph(self):
        self.figure = plt.figure()
        self.a = self.figure.add_subplot(111)
        sns.heatmap(self.data[self.input_var].corr(method='pearson'),
                    ax=self.a, linecolor="lightgray", annot=True, center=0)
        plt.title("Correlogram")

        canvas = FigureCanvasTkAgg(self.figure, master=self.graph_f)
        self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # data creator inside report option
    def create_data(self):
        self.text_stat = tk.Text(self.graph_f, bd=4, relief="groove", wrap="word")
        self.text_stat.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.text_stat.configure(state='normal')
        self.corr_matrix = self.data[self.input_var].corr(method='pearson')
        self.text_stat.insert(tk.END, self.corr_matrix)
        self.text_stat.configure(state='disabled')
        self.widget = None
        self.toolbar = None

    # method that supports radio buttons switching
    def chosen_data_insert(self):
        self.preparation_and_absorption_of_the_input()

        if self.check_if_all_input_correct():

            if self.ratio_var.get() == 0:
                self.destroy_previous_objects()
                self.create_graph()

            elif self.ratio_var.get() == 1:
                self.destroy_previous_objects()
                self.create_data()
