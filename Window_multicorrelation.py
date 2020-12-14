import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Window_popup_message import popup_window
import seaborn as sns



class MultiCorrelation:  # todo tutuaj będzie okienko do tworzenia wykresów
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.005, rely=0.01, relwidth=0.8, relheight=0.98)

        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.81, rely=0.91, relwidth=0.185, relheight=0.08)

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
        self.text_1.configure(state='disabled')

        self.text_lf2 = tk.LabelFrame(self.master,text="Chosen variables", relief="flat")
        self.text_lf2.place(relx=0.81, rely=0.46, relwidth=0.185, relheight=0.37)
        self.text_2 = tk.Text(self.text_lf2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.options_lf = tk.LabelFrame(self.master, text="Options")
        self.options_lf.place(relx=0.81, rely=0.83, relwidth=0.185, relheight=0.08)
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

        if self.input_var:

            if self.check_list:

                if self.ratio_var.get() == 0:
                    if self.widget:
                        self.widget.destroy()

                    if self.toolbar:
                        self.toolbar.destroy()

                    if self.text_stat:
                        self.text_stat.destroy()

                    self.figure = plt.figure()
                    self.a = self.figure.add_subplot(111)
                    sns.heatmap(self.data[self.input_var].corr(method='pearson'), ax=self.a,)
                    plt.title("Correlogram")
                    #todo poprawic korelogram
                    #https://stackoverflow.com/questions/43507756/python-seaborn-how-to-replicate-corrplot

                    canvas = FigureCanvasTkAgg(self.figure, master=self.graph_f)
                    self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
                    self.widget = canvas.get_tk_widget()
                    self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


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
                    self.corr_matrix = self.data[self.input_var].corr(method='pearson')
                    self.text_stat.insert(tk.END,self.corr_matrix)
                    self.text_stat.configure(state='disabled')
                    self.widget = None
                    self.toolbar = None






            else:
                popup_window("Information", "Incorrect variable name!")
        else:
            popup_window("Information", "No variables entered.")











































