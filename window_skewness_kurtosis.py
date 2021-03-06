import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from function_popup_message import popup_window
from class_statistical_backend import StatisticBackend
from function_data_check import data_preparation


class SkewnessKurtosis:
    # creates window of this class
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.check_b_l = None
        self.input_var = None
        self.check_list = None
        self.widget = None
        self.toolbar = None
        self.text_stat = None
        self.df = None
        self.mean = None
        self.median = None
        self.dominant = None
        self.figure = None
        self.a = None
        self.statistical_backend = None
        self.kde_value = None

        # creates labelframe for graph and data
        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.005, rely=0.01, relwidth=0.8, relheight=0.89)

        # creates labelframe for menu
        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.81, rely=0.91, relwidth=0.185, relheight=0.08)

        # creates labelframe to chose statistics
        self.stat_lf = tk.LabelFrame(self.master, text="Statistics",)
        self.stat_lf.place(relx=0.195, rely=0.91, relwidth=0.61, relheight=0.08)

        # creates methods to catch chosen statistics
        self.ch1 = tk.StringVar()
        self.ch2 = tk.StringVar()
        self.ch3 = tk.StringVar()
        self.ch4 = tk.StringVar()
        self.ch5 = tk.StringVar()
        self.ch6 = tk.StringVar()

        # creates check buttons
        self.ch_b1 = tk.Checkbutton(self.stat_lf, text="Skewness", variable=self.ch1,
                                    onvalue="Skewness", offvalue='', tristatevalue=0, state="disable", )

        self.ch_b2 = tk.Checkbutton(self.stat_lf, text="Kurtosis", variable=self.ch2,
                                    onvalue="Kurtosis", offvalue='', tristatevalue=0, state="disable", )

        self.ch_b3 = tk.Checkbutton(self.stat_lf, text="Mean", variable=self.ch3,
                                    onvalue="Mean", offvalue='', tristatevalue=0, )

        self.ch_b4 = tk.Checkbutton(self.stat_lf, text="Median", variable=self.ch4,
                                    onvalue="Median", offvalue='', tristatevalue=0, )

        self.ch_b5 = tk.Checkbutton(self.stat_lf, text="Dominant", variable=self.ch5,
                                    onvalue="Dominant", offvalue='', tristatevalue=0, )

        self.ch_b6 = tk.Checkbutton(self.stat_lf, text="Density", variable=self.ch6,
                                    onvalue="Density", offvalue='', tristatevalue=0, state="disable", )

        # positioning of the check buttons
        self.ch_b1.grid(row=0, column=0, sticky="W")
        self.ch_b2.grid(row=0, column=1, sticky="W")
        self.ch_b3.grid(row=0, column=2, sticky="W")
        self.ch_b4.grid(row=0, column=3, sticky="W")
        self.ch_b5.grid(row=0, column=4, sticky="W")
        self.ch_b6.grid(row=0, column=5, sticky="W")

        # creates quit button
        self.quit_b = tk.Button(self.menu_f, text="Close", command=self.close_window)
        self.quit_b.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        # creates load button
        self.load_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.load_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        # takes data from data object
        self.variables = list(data.columns)

        # creates label frame to text widget
        self.text_lf1 = tk.LabelFrame(self.master, text="Existing variables", relief="flat")
        self.text_lf1.place(relx=0.81, rely=0.01, relwidth=0.185, relheight=0.45)

        # creates text widget for display existing variables
        self.text_1 = tk.Text(self.text_lf1, bd=4, relief="groove", wrap="word")
        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1.configure(state='disabled')

        # creates label frame to text widget
        self.text_lf2 = tk.LabelFrame(self.master, text="Chosen variables", relief="flat")
        self.text_lf2.place(relx=0.81, rely=0.46, relwidth=0.185, relheight=0.45)

        # creates text widget to data insert
        self.text_2 = tk.Text(self.text_lf2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        # creates labelframe to switch between graph and report
        self.options_lf = tk.LabelFrame(self.master, text="Options")
        self.options_lf.place(relx=0.005, rely=0.91, relwidth=0.185, relheight=0.08)
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

        self.check_b_l = [
            self.ch1.get(), self.ch2.get(), self.ch3.get(),
            self.ch4.get(), self.ch5.get()
        ]

        self.check_b_l = [
            x for x in self.check_b_l if x
        ]

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

    # configure options when some of them are not allowed
    def config_var_options_for_graph(self):
        self.ch_b1.config(offvalue='', )
        self.ch_b2.config(offvalue='', )
        self.ch_b1.config(state="disabled")
        self.ch_b2.config(state="disabled")
        self.ch_b6.config(state="normal")

    # check is user insert one var for graph
    def check_if_only_one_var_for_graph(self):
        if len(self.input_var) == 1:
            return True
        else:
            popup_window("Information", "Only one variable can be displayed.")
            pass

    # add density curve on graph
    def add_density_to_graph(self):

        if self.ch6.get() == "Density":
            self.kde_value = True

        else:
            self.kde_value = False

        return self.kde_value

    # graph creator inside graph option
    def create_graph(self):
        self.df = self.data[self.input_var]
        self.figure = plt.figure()
        self.a = self.figure.add_subplot(111)
        sns.distplot(self.df, ax=self.a, kde=self.kde_value, rug=True, color='darkseagreen', )
        self.a.legend(loc="upper left", labels=self.input_var, )
        plt.xlabel("values", labelpad=2)
        plt.ylabel("frequency", labelpad=2)
        plt.title("Histogram")
        plt.grid()

    # adds basic statistics lines on graph
    def add_lines_to_graph(self):
        self.mean = np.mean(self.df)[0]
        self.median = np.median(self.df)
        self.dominant = self.df.mode(dropna=False).iloc[0][0]

        if self.ch3.get() == "Mean":
            self.a.axvline(self.mean, color='y', linestyle='solid', linewidth=1)
            min_y_lim, max_y_lim = plt.ylim()
            plt.text(self.mean * 1.1, max_y_lim * 0.9, 'Mean: {:.2f}'.format(self.mean), color='y', )

        if self.ch4.get() == "Median":
            self.a.axvline(self.median, color='r', linestyle='dashed', linewidth=1)
            min_y_lim, max_y_lim = plt.ylim()
            plt.text(self.median * 1.1, max_y_lim * 0.85, 'Median: {:.2f}'.format(self.median), color='r', )

        if self.ch5.get() == "Dominant":
            self.a.axvline(self.dominant, color='b', linestyle='dotted', linewidth=1)
            min_y_lim, max_y_lim = plt.ylim()
            plt.text(self.dominant * 1.1, max_y_lim * 0.8, 'Dominant: {:.2f}'.format(self.dominant), color='b', )

    # finally display of the graph
    def add_graph(self):
        canvas = FigureCanvasTkAgg(self.figure, master=self.graph_f)
        self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # reconfigure options between switch
    def config_var_options_for_data(self):
        self.ch_b6.config(offvalue='', )
        self.ch_b6.config(state="disable", )
        self.ch_b1.config(state="normal", )
        self.ch_b2.config(state="normal", )
        self.ch_b6.config(offvalue='', )

    # data creator inside report option
    def create_data(self):
        self.statistical_backend = StatisticBackend()
        self.text_stat = tk.Text(self.graph_f, bd=4, relief="groove", wrap="word")
        self.text_stat.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.text_stat.configure(state='normal')
        self.text_stat.insert(tk.END, self.statistical_backend.data_for_skewness_and_kurtosis(self.data, self.input_var, self.check_b_l))
        self.text_stat.configure(state='disabled')
        self.widget = None
        self.toolbar = None

    # method that supports radio buttons switching
    def chosen_data_insert(self):

        self.preparation_and_absorption_of_the_input()

        if self.check_if_all_input_correct():

            if self.ratio_var.get() == 0:

                if self.check_if_only_one_var_for_graph():
                    self.config_var_options_for_graph()
                    self.destroy_previous_objects()
                    self.add_density_to_graph()
                    self.create_graph()
                    self.add_lines_to_graph()
                    self.add_graph()

            elif self.ratio_var.get() == 1:

                self.config_var_options_for_data()
                self.destroy_previous_objects()
                self.create_data()
