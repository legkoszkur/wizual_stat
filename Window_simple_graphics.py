import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Window_popup_message import popup_window
import matplotlib.pyplot as plt

class Graphics:#todo tutuaj będzie okienko do tworzenia wykresów
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

        self.refresh_b = tk.Button(self.menu_f, text="Load", command=lambda: self.chosen_data_insert())
        self.refresh_b.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        # Here im importing data from Window_main
        self.variables = list(data.columns)

        self.text_l1 = tk.LabelFrame(self.master, bg="white", text="Existing variables", relief="flat")
        self.text_l1.place(relx=0.76, rely=0.01, relwidth=0.23, relheight=0.44)
        self.text_1 = tk.Text(self.text_l1, bd=4, relief="groove", wrap="word")#warp word powoduje że przenosi całe słowo do następnej linijki
        self.text_1.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_1.configure(state='normal')
        self.text_1.insert(tk.END, self.variables)
        self.text_1 .configure(state='disabled')

        self.text_l2 = tk.LabelFrame(self.master, bg="white", text="Variables on graph", relief="flat")
        self.text_l2.place(relx=0.76, rely=0.46, relwidth=0.23, relheight=0.44)
        self.text_2 = tk.Text(self.text_l2, bd=4, relief="groove", wrap="word")
        self.text_2.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.widget = None
        self.toolbar = None

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
            if self.check_list is True:

                if self.widget:
                    self.widget.destroy()

                if self.toolbar:
                    self.toolbar.destroy()

                f = Figure(figsize=(5, 5), dpi=100)
                self.a = f.add_subplot(111)
                order_numbers = []

                for i in range(len(self.data[self.input_var])):
                    order_numbers.append(i)
                self.a.plot(order_numbers, self.data[self.input_var])

                canvas = FigureCanvasTkAgg(f, master=self.graph_f)
                self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
                self.widget = canvas.get_tk_widget()
                self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            else:
                popup_window("Information", "Incorrect variable name!")
        else:
            popup_window("Information", "No variables entered")






















