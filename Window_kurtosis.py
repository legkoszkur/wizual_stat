import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
import numpy as np
from Function_message_window import popup_window
from Class_statistical_backend import StatisticBackend

class Kurtosis:#todo tutuaj będzie okienko do tworzenia wykresów
    def __init__(self, master,data):
        self.master = master
        self.data = data
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        self.graph_frame = tk.LabelFrame(self.master)
        self.graph_frame.place(relx=0.195, rely=0.01, relwidth=0.61, relheight=0.98)

        self.menu_frame = tk.LabelFrame(self.master, text="Menu")
        self.menu_frame.place(relx=0.81, rely=0.91, relwidth=0.185, relheight=0.08)

        self.average_measures = tk.LabelFrame(self.master, text="Average Measures", relief="flat")
        self.average_measures.place(relx=0.005, rely=0.01, relwidth=0.185, relheight=0.24)

        self.measures_of_differentiation = tk.LabelFrame(self.master, bg="white", text="Measures of differentiation",
                                                         relief="flat")
        self.measures_of_differentiation.place(relx=0.005, rely=0.31, relwidth=0.185, relheight=0.24)

        self.skewness_measures = tk.LabelFrame(self.master, bg="white", text="Skewness measures", relief="flat")
        self.skewness_measures.place(relx=0.005, rely=0.62, relwidth=0.185, relheight=0.155)

        self.CheckVar1 = tk.IntVar()
        self.CheckVar2 = tk.IntVar()
        self.CheckVar3 = tk.IntVar()
        self.CheckVar4 = tk.IntVar()
        self.CheckVar5 = tk.IntVar()
        self.CheckVar6 = tk.IntVar()
        self.CheckVar7 = tk.IntVar()
        self.CheckVar8 = tk.IntVar()
        self.CheckVar9 = tk.IntVar()
        self.CheckVar10 = tk.IntVar()
        self.CheckVar11 = tk.IntVar()
        self.CheckVar12 = tk.IntVar()
        self.CheckVar13 = tk.IntVar()

        self.check_b1 = tk.Checkbutton(self.average_measures, text="Mean", variable=self.CheckVar1, onvalue=1,
                                       offvalue=0,)
        self.check_b2 = tk.Checkbutton(self.average_measures, text="Dominant", variable=self.CheckVar2, onvalue=1,
                                       offvalue=0,)
        self.check_b3 = tk.Checkbutton(self.average_measures, text="Median", variable=self.CheckVar3, onvalue=1,
                                       offvalue=0,)
        self.check_b4 = tk.Checkbutton(self.average_measures, text="Quantile (0.25)", variable=self.CheckVar4, onvalue=1,
                                       offvalue=0,)
        self.check_b5 = tk.Checkbutton(self.average_measures, text="Quantile (0.75)", variable=self.CheckVar5, onvalue=1,
                                       offvalue=0,)
        self.check_b6 = tk.Checkbutton(self.measures_of_differentiation, text="Standard deviation",
                                       variable=self.CheckVar6, onvalue=1, offvalue=0, )
        self.check_b7 = tk.Checkbutton(self.measures_of_differentiation, text="Coefficient of variation",
                                       variable=self.CheckVar7, onvalue=1, offvalue=0, )
        self.check_b8 = tk.Checkbutton(self.measures_of_differentiation, text="Range", variable=self.CheckVar8,
                                       onvalue=1, offvalue=0, )
        self.check_b9 = tk.Checkbutton(self.measures_of_differentiation, text="Quarter range", variable=self.CheckVar9,
                                       onvalue=1, offvalue=0, )
        self.check_b10 = tk.Checkbutton(self.measures_of_differentiation, text="Quarter deviation",
                                        variable=self.CheckVar10, onvalue=1, offvalue=0, )
        self.check_b11 = tk.Checkbutton(self.skewness_measures, text="Edgeworth's",variable=self.CheckVar10, onvalue=1,
                                        offvalue=0, )
        self.check_b12 = tk.Checkbutton(self.skewness_measures, text="Pearson's",variable=self.CheckVar11, onvalue=1,
                                        offvalue=0, )
        self.check_b13 = tk.Checkbutton(self.skewness_measures, text="Yule-Kendall", variable=self.CheckVar12,onvalue=1,
                                        offvalue=0,)

        self.check_b1.grid(row=0,sticky="W")
        self.check_b2.grid(row=1,sticky="W")
        self.check_b3.grid(row=2,sticky="W")
        self.check_b4.grid(row=3,sticky="W")
        self.check_b5.grid(row=4,sticky="W")
        self.check_b6.grid(row=0, sticky="W")
        self.check_b7.grid(row=1, sticky="W")
        self.check_b8.grid(row=2, sticky="W")
        self.check_b9.grid(row=3, sticky="W")
        self.check_b10.grid(row=4, sticky="W")
        self.check_b11.grid(row=0, sticky="W")
        self.check_b12.grid(row=1, sticky="W")
        self.check_b13.grid(row=2, sticky="W")

        self.quit_button = tk.Button(self.menu_frame, text="Close", command=self.close_window)
        self.quit_button.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        self.refresh_graph_button = tk.Button(self.menu_frame, text="Load", command=lambda: self.chosen_data_insert())
        self.refresh_graph_button.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        self.variables = list(data.columns)

        self.text_label1 = tk.LabelFrame(self.master, bg="white", text="Existing variables", relief="flat")
        self.text_label1.place(relx=0.81, rely=0.01, relwidth=0.185, relheight=0.44)
        self.text_one = tk.Text(self.text_label1, bd=4, relief="groove", wrap="word")#warp word powoduje że przenosi całe słowo do następnej linijki
        self.text_one.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_one.configure(state='normal')
        self.text_one.insert(tk.END, self.variables)
        self.text_one .configure(state='disabled')

        self.text_label2 = tk.LabelFrame(self.master, bg="white", text="Variables on graph", relief="flat")
        self.text_label2.place(relx=0.81, rely=0.46, relwidth=0.185, relheight=0.44)
        self.text_two = tk.Text(self.text_label2, bd=4, relief="groove",wrap="word")
        self.text_two.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.options = tk.LabelFrame(self.master, text="Options")
        self.options.place(relx=0.005, rely=0.91, relwidth=0.185, relheight=0.08)

        self.ratio_var = tk.IntVar()
        self.radio_b1 = tk.Radiobutton(self.options, text="Report", value=1, variable=self.ratio_var)
        self.radio_b2 = tk.Radiobutton(self.options, text="Graph", value=0, variable=self.ratio_var)
        self.radio_b1.grid(row=0, column=0, sticky="W")
        self.radio_b2.grid(row=0, column=1, sticky="W")
        print(self.ratio_var)

        self.widget = None
        self.toolbar = None
        self.text_statistics = None

    def close_window(self):
        self.master.destroy()

    def chosen_data_insert(self):
        #todo tutaj trzeba poprawić ten try bo on nie sprawdza dla całego atrybutu czy to sa zmienne z listy tylko na podstawie errora
        self.input_variables = self.text_two.get("1.0", "end")
        self.input_variables = self.input_variables.split(" ")
        self.input_variables = [x for x in self.input_variables if x]  # to usuwa puste (w srodku ale nie na koncu)
        self.input_variables[-1] = self.input_variables[-1].strip()  # to usuwa \n
        if self.input_variables[-1] == '': #usuwa ostatnie puste miejsce jakby się pojawiło
            self.input_variables = self.input_variables[:-1]

        self.check_list = all(item in self.variables for item in self.input_variables)

        if self.check_list is True:#to sprawdza czy wszystkie wprowadzone zmienne sa poprawne

            if self.ratio_var.get() == 0:
                if self.widget:
                    self.widget.destroy()

                if self.toolbar:
                    self.toolbar.destroy()

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                order_numbers = []

                for i in range(len(self.data[self.input_variables])):
                    order_numbers.append(i)
                a.plot(order_numbers, self.data[self.input_variables])

                canvas = FigureCanvasTkAgg(f, master=self.graph_frame)
                self.toolbar = NavigationToolbar2Tk(canvas, self.graph_frame)
                self.widget = canvas.get_tk_widget()
                self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            elif self.ratio_var.get() == 1:

                if self.widget:
                    self.widget.destroy()

                if self.toolbar:
                    self.toolbar.destroy()

                if self.text_statistics:
                    _statistics = tk.Text(self.graph_frame, bd=4, relief="groove",
                                          wrap="word")  # warp word powoduje że przenosi całe słowo do następnej linijki
                self.text_statistics.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                self.text_statistics.configure(state='normal')
                self.text_statistics.insert(tk.END, self.data[self.input_variables])
                self.text_statistics.configure(state='disabled')

                self.input_statistics_list = ['sum', 'mean', 'min', 'max', 'std', 'median','skew','kurtosis',]
                #todo tutaj będzie klasa która utworzy ładny raport


        else:
            popup_window("Information", "Incorrect variable name!")









            #self.statistics_in_to_screen = Statistic_backend()

































