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
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.master.configure(bg="white")
        self.new = None

        self.data_frame = tk.LabelFrame(self.master, bg="white", text="Data Frame")
        self.data_frame.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.94)

        self.data_manager = DataManager(master, self.data_frame)

        self.menu_bar = tk.Menu(self.master)

        opti = tk.Menu(self.menu_bar, tearoff=False)
        graph = tk.Menu(self.menu_bar, tearoff=False)
        corr = tk.Menu(self.menu_bar, tearoff=False)
        stat = tk.Menu(self.menu_bar, tearoff=False)
        other = tk.Menu(self.menu_bar, tearoff=False)
        instruction = tk.Menu(self.menu_bar, tearoff=False)

        opti.add_command(label="Load", command=lambda: self.data_manager.file_dialog(), )
        opti.add_command(label="Remove", command=lambda: self.data_manager.remove_data(), )
        opti.add_command(label="Exit", command=lambda: quit())

        graph.add_command(label="Graphics", command=lambda: self.new_window(Graphics))
        corr.add_command(label="Correlation", command=lambda: self.new_window(CorrelationWindow))
        corr.add_command(label="Multi correlation", command=lambda: self.new_window(MultiCorrelation))
        stat.add_command(label="Average measures", command=lambda: self.new_window(AverageMeasures))
        stat.add_command(label="Differentiation measures", command=lambda: self.new_window(DifferentiationMeasures))
        other.add_command(label="Skewness and kurtosis", command=lambda: self.new_window(SkewnessKurtosis))
        instruction.add_command(label="Variables insert", command=lambda: InstructionWindow(tk.Toplevel(self.master)))

        self.menu_bar.add_cascade(label="Options", menu=opti)
        self.menu_bar.add_cascade(label="Graphics", menu=graph, )
        self.menu_bar.add_cascade(label="Correlation", menu=corr, )
        self.menu_bar.add_cascade(label="Statistics", menu=stat, )
        self.menu_bar.add_cascade(label="Other", menu=other, )
        self.menu_bar.add_cascade(label="Instruction", menu=instruction)

        self.master.config(menu=self.menu_bar)

    def new_window(self, _class,):
        try:
            self.new = tk.Toplevel(self.master)
            _class(self.new, self.data_manager.data)
        except AttributeError:
            self.new.destroy()
            popup_window("Information", "No data have been loaded.")
            pass


root = tk.Tk()
app = StartPage(root)
root.mainloop()
