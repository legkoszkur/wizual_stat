import tkinter as tk
from matplotlib.figure import Figure
import scipy.stats
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Window_popup_message import popup_window

class Correlation:#todo tutuaj będzie okienko do tworzenia wykresów
    def __init__(self, master,data):
        self.master = master
        self.data = data
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        self.graph_f = tk.LabelFrame(self.master)
        self.graph_f.place(relx=0.005, rely=0.01, relwidth=0.75, relheight=0.98)

        self.menu_f = tk.LabelFrame(self.master, text="Menu")
        self.menu_f.place(relx=0.76, rely=0.91, relwidth=0.23, relheight=0.08)

        self.quit_b = tk.Button(self.menu_f, text="Close", command=self.close_window)
        self.quit_b.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        self.load_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.load_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        self.variables = list(data.columns)

        self.text_l1 = tk.LabelFrame(self.master, bg="white", text="Existing variables", relief="flat")
        self.text_l1.place(relx=0.76, rely=0.01, relwidth=0.23, relheight=0.45)
        self.text_1 = tk.Text(self.text_l1, bd=4, relief="groove", wrap="word")#warp word powoduje że przenosi całe słowo do następnej linijki
        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1 .configure(state='disabled')

        self.text_l2 = tk.LabelFrame(self.master, bg="white", text="Variable one", relief="flat")
        self.text_l2.place(relx=0.76, rely=0.47, relwidth=0.23, relheight=0.1)
        self.text_2 = tk.Text(self.text_l2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.text_l3 = tk.LabelFrame(self.master, bg="white", text="Variable two", relief="flat")
        self.text_l3.place(relx=0.76, rely=0.58, relwidth=0.23, relheight=0.1)
        self.text_3 = tk.Text(self.text_l3, bd=4, relief="groove", wrap="word")
        self.text_3.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.text_l4 = tk.LabelFrame(self.master, bg="white", text="Correlation ", relief="flat")
        self.text_l4.place(relx=0.76, rely=0.69, relwidth=0.23, relheight=0.1)
        self.text_4 = tk.Entry(self.text_l4, bd=4, relief="groove", )
        self.text_4.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_4.configure(state='disabled')

        self.widget = None
        self.toolbar = None

    def close_window(self):
        self.master.destroy()

    def chosen_data_insert(self):
        if self.widget:
            self.widget.destroy()

        if self.toolbar:
            self.toolbar.destroy()

        self.input_var1 = self.text_2.get("1.0", "end")
        self.input_var1 = self.input_var1.split(" ")
        self.input_var1 = [x for x in self.input_var1 if x]  # to usuwa puste
        self.input_var1[-1] = self.input_var1[-1].strip()  # to usuwa \n

        self.input_var2 = self.text_3.get("1.0", "end")
        self.input_var2 = self.input_var2.split(" ")
        self.input_var2 = [x for x in self.input_var2 if x]  # to usuwa puste
        self.input_var2[-1] = self.input_var2[-1].strip()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        a.scatter(self.data[self.input_var1], self.data[self.input_var2], )

        canvas = FigureCanvasTkAgg(f, master=self.graph_f)
        self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        print(self.data[self.input_var2])
        print(self.data[self.input_var1])
        print(type(self.data[self.input_var1]))

        self.correlation = scipy.stats.pearsonr(self.data.loc[[self.input_var1, self.input_var2]], )
        print(self.correlation)
        """
        self.text_4.configure(state='normal')
        self.text_4.insert(tk.END, self.correlation[0])
        self.text_4.configure(state='disabled')
        """
























