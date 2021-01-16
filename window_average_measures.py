import tkinter as tk
import matplotlib.pyplot as plt
from function_data_check import data_preparation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from function_popup_message import popup_window
from class_statistical_backend import StatisticBackend


class AverageMeasures:
    # creates window of this class
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.input_var = None
        self.check_list = None
        self.df = None
        self.figure = None
        self.a = None
        self.bar_g = None
        self.input_s_l = None
        self.statistical_backend = None
        self.widget = None
        self.toolbar = None
        self.text_stat = None

        # creates labelframe for graph and data
        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.005, rely=0.01, relwidth=0.8, relheight=0.89)

        # creates labelframe for menu
        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.81, rely=0.91, relwidth=0.185, relheight=0.08)

        # creates labelframe to chose statistics
        self.stat_lf = tk.LabelFrame(self.master, text="Average Measures",)
        self.stat_lf.place(relx=0.195, rely=0.91, relwidth=0.61, relheight=0.08)

        # creates methods to catch chosen statistics
        self.ch1 = tk.StringVar()
        self.ch2 = tk.StringVar()
        self.ch3 = tk.StringVar()
        self.ch4 = tk.StringVar()
        self.ch5 = tk.StringVar()
        self.ch6 = tk.StringVar()
        self.ch7 = tk.StringVar()
        self.ch8 = tk.StringVar()

        # creates check buttons
        self.ch_b1 = tk.Checkbutton(self.stat_lf, text="Sum", variable=self.ch1,
                                    onvalue="Sum", offvalue='', tristatevalue=0, )
        self.ch_b2 = tk.Checkbutton(self.stat_lf, text="Mean", variable=self.ch2,
                                    onvalue="Mean", offvalue='', tristatevalue=0, )
        self.ch_b3 = tk.Checkbutton(self.stat_lf, text="Max", variable=self.ch3,
                                    onvalue="Max", offvalue='', tristatevalue=0, )
        self.ch_b4 = tk.Checkbutton(self.stat_lf, text="Min", variable=self.ch4,
                                    onvalue="Min", offvalue='', tristatevalue=0, )
        self.ch_b5 = tk.Checkbutton(self.stat_lf, text="Median", variable=self.ch5,
                                    onvalue="Median", offvalue='', tristatevalue=0, )
        self.ch_b6 = tk.Checkbutton(self.stat_lf, text="Quantile_25%", variable=self.ch6,
                                    onvalue="Q_25%", offvalue='', tristatevalue=0, )
        self.ch_b7 = tk.Checkbutton(self.stat_lf, text="Quantile_75%", variable=self.ch7,
                                    onvalue="Q_75%", offvalue='', tristatevalue=0, )
        self.ch_b8 = tk.Checkbutton(self.stat_lf, text="Dominant", variable=self.ch8,
                                    onvalue="Dominant", offvalue='', tristatevalue=0, )

        # positioning of the check buttons
        self.ch_b1.grid(row=0, column=0, sticky="W")
        self.ch_b2.grid(row=0, column=1, sticky="W")
        self.ch_b3.grid(row=0, column=2, sticky="W")
        self.ch_b4.grid(row=0, column=3, sticky="W")
        self.ch_b5.grid(row=0, column=4, sticky="W")
        self.ch_b6.grid(row=0, column=5, sticky="W")
        self.ch_b7.grid(row=0, column=6, sticky="W")
        self.ch_b8.grid(row=0, column=7, sticky="W")

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
        self.text_1 .configure(state='disabled')

        # creates label frame to text widget
        self.text_lf2 = tk.LabelFrame(self.master, text="Variables on graph", relief="flat")
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

        self.input_s_l = [
            self.ch1.get(), self.ch2.get(), self.ch3.get(), self.ch4.get(),
            self.ch5.get(), self.ch6.get(), self.ch7.get(), self.ch8.get(),
        ]

        self.input_s_l = [
            x for x in self.input_s_l if x
        ]

    # checks if all insert data are correct
    def check_if_all_input_correct(self):

        if self.input_s_l:

            if self.input_var:

                if self.check_list:
                    self.statistical_backend = StatisticBackend()
                    return True
                else:
                    popup_window("Information", "Incorrect variable name!")
                    return False
            else:
                popup_window("Information", "No variables entered.")
                return False
        else:
            popup_window("Information", "No statistic chosen.")
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
        self.df = self.statistical_backend.data_for_average_measures(self.data, self.input_var, self.input_s_l)
        self.figure = plt.figure()
        self.a = self.figure.add_subplot(111)
        self.bar_g = self.df.plot(kind="bar", ax=self.a, rot=True)
        self.a.set_title("Average measures")

        canvas = FigureCanvasTkAgg(self.figure, master=self.graph_f)
        self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # data creator inside report option
    def create_data(self):
        self.text_stat = tk.Text(self.graph_f, bd=4, relief="groove", wrap="word")
        self.text_stat.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.text_stat.configure(state='normal')
        self.text_stat.insert(tk.END, self.statistical_backend.data_for_average_measures(
            self.data, self.input_var, self.input_s_l))
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
