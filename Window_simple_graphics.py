import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Function_message_window import popup_window

class Graphics:#todo tutuaj będzie okienko do tworzenia wykresów
    def __init__(self, master,data):
        self.master = master
        self.data = data
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        self.graph_frame = tk.LabelFrame(self.master)
        self.graph_frame.place(relx=0.005, rely=0.01, relwidth=0.75, relheight=0.98)

        self.menu_frame = tk.LabelFrame(self.master, text="Menu")
        self.menu_frame.place(relx=0.76, rely=0.91, relwidth=0.23, relheight=0.08)

        self.quit_button = tk.Button(self.menu_frame, text="Close", command=self.close_window)
        self.quit_button.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.8)

        self.refresh_graph_button = tk.Button(self.menu_frame, text="Load", command=lambda: self.chosen_data_insert())
        self.refresh_graph_button.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        # Here im importing data from Window_main
        self.variables = list(data.columns)

        self.text_label1 = tk.LabelFrame(self.master, bg="white", text="Existing variables", relief="flat")
        self.text_label1.place(relx=0.76, rely=0.01, relwidth=0.23, relheight=0.44)
        self.text_one = tk.Text(self.text_label1, bd=4, relief="groove",wrap="word")#warp word powoduje że przenosi całe słowo do następnej linijki
        self.text_one.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)
        self.text_one.configure(state='normal')
        self.text_one.insert(tk.END, self.variables)
        self.text_one .configure(state='disabled')

        self.text_label2 = tk.LabelFrame(self.master, bg="white", text="Variables on graph", relief="flat")
        self.text_label2.place(relx=0.76, rely=0.46, relwidth=0.23, relheight=0.44)
        self.text_two = tk.Text(self.text_label2, bd=4, relief="groove",wrap="word")
        self.text_two.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.widget = None
        self.toolbar = None

    def close_window(self):
        self.master.destroy()

    def chosen_data_insert(self):
        try:
            if self.widget:
                self.widget.destroy()

            if self.toolbar:
                self.toolbar.destroy()

            self.input_variables = self.text_two.get("1.0", "end")
            self.input_variables = self.input_variables.split(" ")
            self.input_variables = [x for x in self.input_variables if x]# to usuwa puste
            self.input_variables[-1] = self.input_variables[-1].strip()# to usuwa \n

            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            order_numbers = []

            for i in range(len(self.data[self.input_variables])):
                order_numbers.append(i)
            a.plot(order_numbers, self.data[self.input_variables])

            canvas = FigureCanvasTkAgg(f, master=self.graph_frame)
            self.toolbar = NavigationToolbar2Tk(canvas,self.graph_frame)
            self.widget = canvas.get_tk_widget()
            self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        except KeyError:
            popup_window("Information", "Incorrect variable name!")























