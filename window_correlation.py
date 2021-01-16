import tkinter as tk
from function_data_check import data_preparation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from function_popup_message import popup_window


class CorrelationWindow:
    # creates window of this class
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.input_var1 = None
        self.input_var2 = None
        self.check_list1 = None
        self.check_list2 = None
        self.figure = None
        self.corr_df = None
        self.correlation = None
        self.a = None

        # creates labelframe for graph and data
        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.005, rely=0.01, relwidth=0.75, relheight=0.98)

        # creates labelframe for menu
        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.76, rely=0.91, relwidth=0.23, relheight=0.08)

        # creates quit button
        self.quit_b = tk.Button(self.menu_f, text="Close", command=self.close_window)
        self.quit_b.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        # creates load button
        self.load_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.load_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        # takes data from data object
        self.variables = list(data.columns)

        # creates text widget for display existing variables
        self.text_l1 = tk.LabelFrame(self.master, text="Existing variables", relief="flat")
        self.text_l1.place(relx=0.76, rely=0.01, relwidth=0.23, relheight=0.45)
        self.text_1 = tk.Text(self.text_l1, bd=4, relief="groove", wrap="word")
        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1 .configure(state='disabled')

        # creates label frame to text widget and text widget inside to let insert first variable
        self.text_l2 = tk.LabelFrame(self.master, text="Variable one", relief="flat")
        self.text_l2.place(relx=0.76, rely=0.47, relwidth=0.23, relheight=0.1)
        self.text_2 = tk.Text(self.text_l2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        # creates label frame to text widget and text widget inside to let insert second variable
        self.text_l3 = tk.LabelFrame(self.master, text="Variable two", relief="flat")
        self.text_l3.place(relx=0.76, rely=0.58, relwidth=0.23, relheight=0.1)
        self.text_3 = tk.Text(self.text_l3, bd=4, relief="groove", wrap="word")
        self.text_3.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        # creates label frame to text widget and text widget inside to print correlation amount
        self.text_l4 = tk.LabelFrame(self.master,  text="Pearson correlation ", relief="flat")
        self.text_l4.place(relx=0.76, rely=0.69, relwidth=0.23, relheight=0.1)
        self.text_4 = tk.Text(self.text_l4, bd=4, bg="silver", relief="groove", state='disabled')
        self.text_4.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.widget = None
        self.toolbar = None

    # close window method
    def close_window(self):
        self.master.destroy()

    # takes and prepares data
    def preparation_and_absorption_of_the_input(self):
        self.input_var1 = data_preparation(self.text_2.get("1.0", "end"))
        self.input_var2 = data_preparation(self.text_3.get("1.0", "end"))

        self.check_list1 = all(item in self.variables for item in self.input_var1)
        self.check_list2 = all(item in self.variables for item in self.input_var2)

    # checks if all insert data are correct
    def check_if_all_input_correct(self):
        if self.input_var1:

            if self.input_var2:

                if self.check_list1:

                    if self.check_list2:
                        return True
                    else:
                        popup_window("Information", "Incorrect variable name on second entry!")
                        return False
                else:
                    popup_window("Information", "Incorrect variable name on first entry!")
                    return False
            else:
                popup_window("Information", "No variables entered on second entry!")
                return False
        else:
            popup_window("Information", "No variables entered on first entry!")
            return False

    # destroys previous objects while user switch rapport and graph multiple times
    def destroy_previous_objects(self):

        if self.widget:
            self.widget.destroy()

        if self.toolbar:
            self.toolbar.destroy()

    # graph creator inside graph option
    def create_graph(self):
        self.figure = plt.Figure()
        self.a = self.figure.add_subplot(111)

        self.a.scatter(self.data[self.input_var1[0]], self.data[self.input_var2[0]], )
        self.a.set_xlabel(self.input_var1[0], labelpad=0)
        self.a.set_ylabel(self.input_var2[0], labelpad=0)
        self.a.set_title("Correlogram")

        canvas = FigureCanvasTkAgg(self.figure, master=self.graph_f)
        self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # data creator inside report option
    def create_data(self):
        self.text_4.configure(state='normal')
        self.text_4.delete("1.0", "end")
        self.corr_df = self.data[[self.input_var1[0], self.input_var2[0]]]
        self.correlation = self.corr_df.corr(method='pearson').iloc[0][1]
        self.text_4.insert(tk.END, round(self.correlation, 6))
        self.text_4.configure(state='disabled')

    # method that supports radio buttons switching
    def chosen_data_insert(self):
        self.preparation_and_absorption_of_the_input()
        if self.check_if_all_input_correct():
            self.destroy_previous_objects()
            self.create_graph()
            self.create_data()
