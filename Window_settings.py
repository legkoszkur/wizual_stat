import tkinter as tk


class Settings:#todo tutuaj będzie okienko do tworzenia wykresów
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master)
        self.quit = tk.Button(self.frame, text=f"Here will be settings panel", command=self.close_window)
        self.quit.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()
