import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import colorchooser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Window_popup_message import popup_window
from Class_statistical_backend import StatisticBackend


class Average_measures:#todo tutuaj będzie okienko do tworzenia wykresów
    def __init__(self, master,data):
        self.master = master
        self.data = data
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.195, rely=0.01, relwidth=0.61, relheight=0.98)

        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.81, rely=0.91, relwidth=0.185, relheight=0.08)

        self.stat_lf = tk.LabelFrame(self.master, text="Average Measures", relief="flat")
        self.stat_lf.place(relx=0.005, rely=0.01, relwidth=0.185, relheight=0.37)

        self.ch1 = tk.StringVar()
        self.ch2 = tk.StringVar()
        self.ch3 = tk.StringVar()
        self.ch4 = tk.StringVar()
        self.ch5 = tk.StringVar()
        self.ch6 = tk.StringVar()
        self.ch7 = tk.StringVar()
        self.ch8 = tk.StringVar()

        self.ch_b1 = tk.Checkbutton(self.stat_lf, text="Sum", variable=self.ch1,
                                    onvalue="Sum",offvalue='', tristatevalue=0, )
        self.ch_b2 = tk.Checkbutton(self.stat_lf, text="Mean", variable=self.ch2,
                                    onvalue="Mean",offvalue='', tristatevalue=0, )
        self.ch_b3 = tk.Checkbutton(self.stat_lf, text="Max", variable=self.ch3,
                                    onvalue="Max",offvalue='', tristatevalue=0, )
        self.ch_b4 = tk.Checkbutton(self.stat_lf, text="Min", variable=self.ch4,
                                    onvalue="Min",offvalue='', tristatevalue=0, )
        self.ch_b5 = tk.Checkbutton(self.stat_lf, text="Median", variable=self.ch5,
                                    onvalue="Median",offvalue='', tristatevalue=0, )
        self.ch_b6 = tk.Checkbutton(self.stat_lf, text="Quantile_25", variable=self.ch6,
                                    onvalue="Quantile_25",offvalue='', tristatevalue=0, )
        self.ch_b7 = tk.Checkbutton(self.stat_lf, text="Quantile_75", variable=self.ch7,
                                    onvalue="Quantile_75",offvalue='', tristatevalue=0, )
        self.ch_b8 = tk.Checkbutton(self.stat_lf, text="Dominant", variable=self.ch8,
                                    onvalue="Dominant",offvalue='', tristatevalue=0, )

        self.ch_b1.grid(row=0,column=1, sticky="W")
        self.ch_b2.grid(row=1,column=1, sticky="W")
        self.ch_b3.grid(row=2,column=1, sticky="W")
        self.ch_b4.grid(row=3,column=1, sticky="W")
        self.ch_b5.grid(row=4,column=1, sticky="W")
        self.ch_b6.grid(row=5,column=1, sticky="W")
        self.ch_b7.grid(row=6,column=1, sticky="W")
        self.ch_b8.grid(row=7,column=1, sticky="W")

        self.quit_b = tk.Button(self.menu_f, text="Close", command=self.close_window)
        self.quit_b.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        self.load_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.load_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        self.variables = list(data.columns)

        self.text_lf1 = tk.LabelFrame(self.master, text="Existing variables", relief="flat")
        self.text_lf1.place(relx=0.81, rely=0.01, relwidth=0.185, relheight=0.44)
        self.text_1 = tk.Text(self.text_lf1, bd=4, relief="groove", wrap="word")
        # warp word powoduje że przenosi całe słowo do następnej linijki
        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1 .configure(state='disabled')

        self.text_lf2 = tk.LabelFrame(self.master, text="Variables on graph", relief="flat")
        self.text_lf2.place(relx=0.81, rely=0.46, relwidth=0.185, relheight=0.44)
        self.text_2 = tk.Text(self.text_lf2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.options_lf = tk.LabelFrame(self.master, text="Options")
        self.options_lf.place(relx=0.005, rely=0.91, relwidth=0.185, relheight=0.08)
        self.ratio_var = tk.IntVar()
        self.radio_b1 = tk.Radiobutton(self.options_lf, text="Report", value=1, variable=self.ratio_var)
        self.radio_b2 = tk.Radiobutton(self.options_lf, text="Graph", value=0, variable=self.ratio_var)
        self.radio_b1.grid(row=0, column=0, sticky="W")
        self.radio_b2.grid(row=0, column=1, sticky="W")

        self.color_lf = tk.LabelFrame(self.master, text="Change color", )
        self.color_lf.place(relx=0.005, rely=0.375, relwidth=0.185, relheight=0.08)

        self.type_b = tk.Button(self.color_lf, text="Type", command=lambda: self.color_backend())
        self.type_b.place(relx=0.05, rely=0.05, relwidth=0.35, relheight=0.8)

        self.text_c = tk.Entry(self.color_lf, bd=4, relief="groove")
        self.text_c.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.88)
        self.text_c.configure(state='disabled')

        self.widget = None
        self.toolbar = None
        self.text_stat = None

    def color_backend(self):
        if self.text_c.get() in self.input_var:
            self.text_c.configure(state='disabled')
            self.c_chooser = colorchooser.askcolor()
            self.my_color = self.c_chooser[1]  # chosen color
            self.index_of_variable = self.input_var.index(self.text_c.get())  # color index
            self.text_c.configure(state='normal')
        else:
            popup_window("Warning","Please insert correct variable name.")

    def close_window(self):
        self.master.destroy()

    def chosen_data_insert(self):
        self.input_var = self.text_2.get("1.0", "end")
        self.input_var = self.input_var.split(" ")
        self.input_var = [x for x in self.input_var if x]  # to usuwa puste (w srodku ale nie na koncu)
        self.input_var[-1] = self.input_var[-1].strip()  # to usuwa \n
        if self.input_var[-1] == '': #usuwa ostatnie puste miejsce jakby się pojawiło
            self.input_var = self.input_var[:-1]
        self.check_list = all(item in self.variables for item in self.input_var)

        self.input_stat_l = [self.ch1.get(), self.ch2.get(), self.ch3.get(), self.ch4.get(), self.ch5.get(), self.ch6.get(),
                             self.ch7.get(), self.ch8.get(), ]
        # to usuwa puste pola żeby można było załadować odpowiednie nazywy
        self.input_stat_l = [x for x in self.input_stat_l if x]

        self.statistical_backend = StatisticBackend(self.data, self.input_var, self.input_stat_l, 0, )

        if self.check_list is True:
            # to sprawdza czy wszystkie wprowadzone zmienne sa poprawne

            if self.ratio_var.get() == 0:
                if self.widget:
                    self.widget.destroy()

                if self.toolbar:
                    self.toolbar.destroy()

                if self.text_stat:
                    self.text_stat.destroy()

                df = self.statistical_backend.average_measures_df
                figure = plt.figure()#figura to jest to miejsce przestrzen na którą można wrzućac wiele wykresów
                a = figure.add_subplot(111)#to jest jeden z wykresów
                x = df.plot(kind="bar",ax=a) #tu przypisuję do mojej figury plot który jest barem i wpisuję go w ax=a czyli jakby dopiero tutaj określam gdzie
                #znajdzie się mój wykres w tym przypadku w "a"
                #potem renderuje go za pomoca

                canvas = FigureCanvasTkAgg(figure, master=self.graph_f)
                self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
                self.widget = canvas.get_tk_widget()
                self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                self.text_c.configure(state='normal')

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
                self.text_stat.insert(tk.END, self.statistical_backend.average_measures_df)
                self.text_stat.configure(state='disabled')

        else:
            popup_window("Information", "Incorrect variable name!")







































