import tkinter as tk
from Window_simple_graphics import Graphics
from Window_Average_measures import Average_measures
from Window_Differentation_measures import DifferentationMeasures
from Window_skewness import Skewness
from Window_kurtosis import Kurtosis
from Window_models import Models
from Window_settings import Settings
from Window_popup_message import popup_window
from Window_corelation import Correlation
from Class_data_manager import Data_manager


FONT_label_title = []




# todo wywalić całego labelframa z ładowaniem danych do osobnej klasy dajesz 2 mastery i na dole czerwony pasek (data loaded)/(data unavalible)

class StartPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        data_frame = tk.LabelFrame(self.master, bg="white", text="Data Frame")
        data_frame.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.74)

        self.data_manager = Data_manager(master, data_frame)

        menubar = tk.Menu(self.master)

        opti = tk.Menu(menubar, tearoff=False)
        graph = tk.Menu(menubar, tearoff=False,)
        stat = tk.Menu(menubar, tearoff=False)
        models = tk.Menu(menubar, tearoff=False)
        tut = tk.Menu(menubar, tearoff=False)

        opti.add_command(label="Settings", command=lambda: self.new_window(Settings),)
        opti.add_command(label="Exit", command=lambda: quit())

        graph.add_command(label="Graphics", command=lambda: self.new_window(Graphics))
        graph.add_command(label="Correlation", command=lambda: self.new_window(Correlation))
        stat.add_command(label="Average measures", command=lambda: self.new_window(Average_measures))
        stat.add_command(label="Differentiation measures", command=lambda: self.new_window(DifferentationMeasures))
        stat.add_command(label="Skewness", command=lambda: self.new_window(Skewness))
        stat.add_command(label="Kurtosis", command=lambda: self.new_window(Kurtosis))
        models.add_command(label="Models", command=lambda: self.new_window(Models))
        tut.add_command(label="Tutorials", command=lambda: print("here will be some youtube tutorials"))

        menubar.add_cascade(label="Options",menu=opti)
        menubar.add_cascade(label="Graphics", menu=graph)
        menubar.add_cascade(label="Statistics", menu=stat)
        menubar.add_cascade(label="Models", menu=models)
        menubar.add_cascade(label="Tutorials", menu=tut)

        self.master.config(menu=menubar)

        buttons_frame = tk.LabelFrame(self.master, bg="white", text="Data setings")
        buttons_frame.place(relx=0.005, rely=0.76, relwidth=0.99, relheight=0.2)

        Import_data = tk.Button(buttons_frame, text="Import", command=lambda: self.data_manager.File_dialog())
        Import_data.place(relx=0.1, rely=0.1, relheight=0.6, relwidth=0.1)

        Load_data = tk.Button(buttons_frame, text="Load", command=lambda: self.data_manager.Load_data())
        Load_data.place(relx=0.3, rely=0.1, relheight=0.6, relwidth=0.1)

        Remove_data = tk.Button(buttons_frame, text="Remove", command=lambda: self.data_manager.remove_data())
        Remove_data.place(relx=0.5, rely=0.1, relheight=0.6, relwidth=0.1)

        Edit_data = tk.Button(buttons_frame, text="Jeszcze się zobaczy", command=lambda: print("jasiu"))
        Edit_data.place(relx=0.7, rely=0.1, relheight=0.6, relwidth=0.1)

    def new_window(self, _class,):
        try:
            self.new = tk.Toplevel(self.master)
            _class(self.new,self.data_manager.data) # tutaj ważne dodaję dane do funkcji która wrzuca te klasy
        except AttributeError:
            popup_window("Information", "No data have been loaded.")
            pass



root = tk.Tk()
app = StartPage(root)
root.mainloop()

