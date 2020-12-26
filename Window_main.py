import tkinter as tk
from Window_simple_graphics import Graphics
from Window_Average_measures import Average_measures
from Window_Differentation_measures import DifferentationMeasures
from Window_skewness_kurtosis import SkewnessKurtosis
from Window_popup_message import popup_window
from Window_correlation import Correlation
from Window_multicorrelation import MultiCorrelation
from Class_data_manager import Data_manager

FONT_label_title = []

# todo wywalić całego labelframa z ładowaniem danych do osobnej klasy dajesz 2 mastery i na dole czerwony pasek (data loaded)/(data unavalible)

class StartPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.master.configure(bg="white")

        self.data_frame = tk.LabelFrame(self.master, bg="white", text="Data Frame")
        self.data_frame.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.94)

        self.data_manager = Data_manager(master, self.data_frame)

        self.menubar = tk.Menu(self.master)

        opti = tk.Menu(self.menubar, tearoff=False)
        graph = tk.Menu(self.menubar, tearoff=False)
        stat = tk.Menu(self.menubar, tearoff=False)
        tut = tk.Menu(self.menubar, tearoff=False)

        opti.add_command(label="Load", command=lambda: self.data_manager.file_dialog(), )
        opti.add_command(label="Remove", command=lambda: self.data_manager.remove_data(), )
        opti.add_command(label="Exit", command=lambda: quit())

        graph.add_command(label="Graphics", command=lambda: self.new_window(Graphics))
        graph.add_command(label="Correlation", command=lambda: self.new_window(Correlation))
        graph.add_command(label="Multi correlation", command=lambda: self.new_window(MultiCorrelation))
        stat.add_command(label="Average measures", command=lambda: self.new_window(Average_measures))
        stat.add_command(label="Differentiation measures", command=lambda: self.new_window(DifferentationMeasures))
        stat.add_command(label="Skewness and kurtosis", command=lambda: self.new_window(SkewnessKurtosis))
        tut.add_command(label="Tutorials", command=lambda: popup_window("Information", "There may be some tutorials here in the future.", ))

        self.menubar.add_cascade(label="Options",menu=opti)
        self.menubar.add_cascade(label="Graphics", menu=graph,)
        self.menubar.add_cascade(label="Statistics", menu=stat,)
        self.menubar.add_cascade(label="Tutorials", menu=tut)

        self.master.config(menu=self.menubar)

    def new_window(self, _class,):
        try:
            self.new = tk.Toplevel(self.master)
            _class(self.new,self.data_manager.data) # tutaj ważne dodaję dane do funkcji która wrzuca te klasy
        except AttributeError:
            self.new.destroy()
            popup_window("Information", "No data have been loaded.")
            pass

root = tk.Tk()
app = StartPage(root)
root.mainloop()

