import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Window_popup_message import popup_window
from Class_statistical_backend import StatisticBackend


class SkewnessKurtosis:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.195, rely=0.01, relwidth=0.61, relheight=0.98)

        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.81, rely=0.91, relwidth=0.185, relheight=0.08)

        self.stat_lf = tk.LabelFrame(self.master, text="Statistics", relief="flat")
        self.stat_lf.place(relx=0.005, rely=0.01, relwidth=0.185, relheight=0.37)

        self.ch1 = tk.StringVar()
        self.ch2 = tk.StringVar()
        self.ch3 = tk.StringVar()
        self.ch4 = tk.StringVar()
        self.ch5 = tk.StringVar()

        self.ch_b1 = tk.Checkbutton(self.stat_lf, text="Skewness", variable=self.ch1,
                                    onvalue="Skewness", tristatevalue=0, )
        self.ch_b2 = tk.Checkbutton(self.stat_lf, text="Kurtosis", variable=self.ch2,
                                    onvalue="Kurtosis", tristatevalue=0, )
        self.ch_b3 = tk.Checkbutton(self.stat_lf, text="Mean", variable=self.ch3,
                                    onvalue="Mean", tristatevalue=0, )
        self.ch_b4 = tk.Checkbutton(self.stat_lf, text="Median", variable=self.ch4,
                                    onvalue="Median", tristatevalue=0, )
        self.ch_b5 = tk.Checkbutton(self.stat_lf, text="Dominant", variable=self.ch5,
                                    onvalue="Dominant", tristatevalue=0, )

        self.ch_b1.grid(row=0, sticky="W")
        self.ch_b2.grid(row=1, sticky="W")
        self.ch_b3.grid(row=2, sticky="W")
        self.ch_b4.grid(row=3, sticky="W")
        self.ch_b5.grid(row=4, sticky="W")

        self.quit_b = tk.Button(self.menu_f, text="Close", command=self.close_window)
        self.quit_b.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        self.load_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.load_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        self.variables = list(data.columns)

        self.text_lf1 = tk.LabelFrame(self.master, text="Existing variables", relief="flat")
        self.text_lf1.place(relx=0.81, rely=0.01, relwidth=0.185, relheight=0.44)
        self.text_1 = tk.Text(self.text_lf1, bd=4, relief="groove", wrap="word")

        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1.configure(state='disabled')

        self.text_lf2 = tk.LabelFrame(self.master, text="Variable on graph (Max 1)", relief="flat")
        self.text_lf2.place(relx=0.81, rely=0.46, relwidth=0.185, relheight=0.08)
        self.text_2 = tk.Text(self.text_lf2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.options_lf = tk.LabelFrame(self.master, text="Options")
        self.options_lf.place(relx=0.005, rely=0.91, relwidth=0.185, relheight=0.08)
        self.ratio_var = tk.IntVar()
        self.radio_b1 = tk.Radiobutton(self.options_lf, text="Report", value=1, variable=self.ratio_var)
        self.radio_b2 = tk.Radiobutton(self.options_lf, text="Graph", value=0, variable=self.ratio_var)
        self.radio_b1.grid(row=0, column=0, sticky="W")
        self.radio_b2.grid(row=0, column=1, sticky="W")

        self.widget = None
        self.toolbar = None
        self.text_stat = None

    def close_window(self):
        self.master.destroy()

    def chosen_data_insert(self):
        self.input_var = self.text_2.get("1.0", "end")
        self.input_var = self.input_var.split(" ")
        self.input_var = [x for x in self.input_var if x]  # to usuwa puste (w srodku ale nie na koncu)
        self.input_var[-1] = self.input_var[-1].strip()  # to usuwa \n
        if self.input_var[-1] == '':  # usuwa ostatnie puste miejsce jakby się pojawiło
            self.input_var = self.input_var[:-1]
        self.check_list = all(item in self.variables for item in self.input_var)
        self.check_b_l = [self.ch1.get(),self.ch2.get()]
        # to usuwa puste pola żeby można było załadować odpowiednie nazywy
        self.check_b_l = [x for x in self.check_b_l if x]

        self.statistical_backend = StatisticBackend(self.data, self.input_var, self.check_b_l, 2, )

        if self.check_list is True:

            if self.ratio_var.get() == 0:

                if self.widget:
                    self.widget.destroy()

                if self.toolbar:
                    self.toolbar.destroy()

                if self.text_stat:
                    self.text_stat.destroy()

                self.df = self.data[self.input_var]
                self.figure = plt.figure()  # figura to jest to miejsce przestrzen na którą można wrzućac wiele wykresów
                self.a = self.figure.add_subplot(111)  # to jest jeden z wykresów
                self.bar_g = sns.distplot(self.df, ax=self.a, color='darkseagreen',bins=int(len(self.data[self.input_var])/3))
                # tu przypisuję do mojej figury plot który jest barem i wpisuję go w ax=a czyli jakby dopiero tutaj określam gdzie
                plt.legend(loc="upper left")
                plt.xlabel("values", labelpad=5)
                plt.ylabel("frequency", labelpad=5)
                plt.title("Histogram")
                canvas = FigureCanvasTkAgg(self.figure , master=self.graph_f)
                self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
                self.widget = canvas.get_tk_widget()
                self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                #todo tutaj jest kilka rzeczy do zrobienie
                #1. zrobić żeby wykres był dokładniejszy
                #2. zrobić opcje dodawania sredniej itp
                #3. zrobić żeby można było zmieniać skew i kurt
                #https://dfrieds.com/math/skewness.html
                #https://seaborn.pydata.org/generated/seaborn.distplot.html


            elif self.ratio_var.get() == 1:

                if self.widget:
                    self.widget.destroy()

                if self.toolbar:
                    self.toolbar.destroy()

                if self.text_stat:
                    self.text_stat.destroy()

                self.text_stat = tk.Text(self.graph_f, bd=4, relief="groove", wrap="word")
                self.text_stat.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                self.text_stat.configure(state='normal')
                self.text_stat.insert(tk.END, self.statistical_backend.skew_kurt_df)
                self.text_stat.configure(state='disabled')

        else:
            popup_window("Information", "Incorrect variable name!")






































