import tkinter as tk
from window_simple_graphics import Graphics
from window_average_measures import AverageMeasures
from window_differentation_measures import DifferentiationMeasures
from window_skewness_kurtosis import SkewnessKurtosis
from function_popup_message import popup_window
from window_correlation import CorrelationWindow
from window_multicorrelation import MultiCorrelation
from class_data_manager import DataManager
from window_instruction import InstructionWindow


class StartPage:
    # creates main window
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.master.configure(bg="white")
        self.new = None

        # creates frame for data
        self.data_frame = tk.LabelFrame(self.master, bg="white", text="Data Frame")
        self.data_frame.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.94)

        # creates object to menage the data
        self.data_manager = DataManager(master, self.data_frame)

        # creates menu bar
        menu_bar = tk.Menu(self.master)

        opti = tk.Menu(menu_bar, tearoff=False)
        graph = tk.Menu(menu_bar, tearoff=False)
        corr = tk.Menu(menu_bar, tearoff=False)
        stat = tk.Menu(menu_bar, tearoff=False)
        other = tk.Menu(menu_bar, tearoff=False)
        instruction = tk.Menu(menu_bar, tearoff=False)

        opti.add_command(label="Load", command=lambda: self.data_manager.load_data(), )
        opti.add_command(label="Remove", command=lambda: self.data_manager.remove_data(), )
        opti.add_command(label="Exit", command=lambda: quit())

        graph.add_command(label="Graphics", command=lambda: self.new_window(
            Graphics, self.master,))
        corr.add_command(label="Correlation", command=lambda: self.new_window(
            CorrelationWindow, self.master,))
        corr.add_command(label="Multi correlation", command=lambda: self.new_window(
            MultiCorrelation, self.master,))
        stat.add_command(label="Average measures", command=lambda: self.new_window(
            AverageMeasures, self.master, ))
        stat.add_command(label="Differentiation measures", command=lambda: self.new_window(
            DifferentiationMeasures, self.master, ))
        other.add_command(label="Skewness and kurtosis", command=lambda: self.new_window(
            SkewnessKurtosis, self.master, ))
        instruction.add_command(label="Variables insert", command=lambda: InstructionWindow(
            tk.Toplevel(self.master,)))

        menu_bar.add_cascade(label="Options", menu=opti)
        menu_bar.add_cascade(label="Graphics", menu=graph, )
        menu_bar.add_cascade(label="Correlation", menu=corr, )
        menu_bar.add_cascade(label="Statistics", menu=stat, )
        menu_bar.add_cascade(label="Other", menu=other, )
        menu_bar.add_cascade(label="Instruction", menu=instruction)

        self.master.config(menu=menu_bar)

    # method to navigate between windows
    def new_window(self, _class, master):
        try:
            self.new = tk.Toplevel(master)
            _class(self.new, self.data_manager.data)
        except AttributeError:
            self.new.destroy()
            popup_window("Information", "No data have been loaded.")
            pass


# create and call mainloop
root = tk.Tk()
app = StartPage(root)
root.mainloop()
