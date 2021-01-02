def close_window(self):
    self.master.destroy()


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


def check_if_all_input_correct(self):
    if self.input_s_l:

        if self.input_var:

            if self.check_list:
                self.statistical_backend = StatisticBackend(self.data, self.input_var, self.input_s_l)
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


def destroy_previous_objects(self):
    if self.widget:
        self.widget.destroy()

    if self.toolbar:
        self.toolbar.destroy()

    if self.text_stat:
        self.text_stat.destroy()


def create_graph(self):
    self.df = self.statistical_backend.data_for_average_measures()
    self.figure = plt.figure()
    self.a = self.figure.add_subplot(111)
    self.bar_g = self.df.plot(kind="bar", ax=self.a, rot=True)
    self.a.set_title("Average measures")

    canvas = FigureCanvasTkAgg(self.figure, master=self.graph_f)
    self.toolbar = NavigationToolbar2Tk(canvas, self.graph_f)
    self.widget = canvas.get_tk_widget()
    self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def create_data(self):
    self.text_stat = tk.Text(self.graph_f, bd=4, relief="groove", wrap="word")
    self.text_stat.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    self.text_stat.configure(state='normal')
    self.text_stat.insert(tk.END, self.statistical_backend.data_for_average_measures())
    self.text_stat.configure(state='disabled')
    self.widget = None
    self.toolbar = None


def chosen_data_insert(self):
    self.preparation_and_absorption_of_the_input()

    if self.check_if_all_input_correct():

        if self.ratio_var.get() == 0:
            self.destroy_previous_objects()
            self.create_graph()

        elif self.ratio_var.get() == 1:
            self.destroy_previous_objects()
            self.create_data()
