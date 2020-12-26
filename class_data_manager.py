import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import messagebox, ttk
from pandas import *
import subprocess
import os
from Window_popup_message import popup_window

class Data_manager:

    def __init__(self, master, frame_with_data):

        self.treeview_style = ttk.Treeview(frame_with_data)
        self.treeview_style.place(relheight=1, relwidth=1)
        y_scrollbar = tk.Scrollbar(frame_with_data, orient="vertical", command=self.treeview_style.yview)
        x_scrollbar = tk.Scrollbar(frame_with_data, orient="horizontal", command=self.treeview_style.xview)
        self.treeview_style.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
        x_scrollbar.pack(side="bottom", fill="x")
        y_scrollbar.pack(side="right",fill="y")

        self.path_label = tk.Label(master, bg="red", text="No File Selected.")
        self.path_label.place(relx=0.005, rely=0.95, relwidth=0.99, relheight=0.04)

    def file_dialog(self):
        try:
             self.file_path = askopenfile(mode='r', title="Select A File",
                                          filetypes=[("Excel Files", "*.xlsx"), ("Excel Files", "*.xls"),
                                                     ("CSV Files","*.csv"),])
             self.path_label["text"] = self.file_path.name
             self.path_label["bg"] = "light green"
             self.load_data(path=self.file_path.name)
             popup_window("Information","Data were imported.")
        except AttributeError:
            pass

    def load_data(self,path):
        self.path = path
        try:
            name, file_extention = os.path.splitext(self.path)
            try:
                if file_extention == '.csv':
                    self.data = read_csv(self.path)
                elif file_extention == '.xlsx':
                    self.data = read_excel(self.path)
                elif file_extention == '.xls':
                    self.data = read_excel(self.path)

            except ValueError:
                tk.messagebox.showerror("Information", "The file_path you have chosen is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file_path as {self.path}")
                return None

            self.treeview_style["column"] = list(self.data.columns)
            self.treeview_style["show"] = "headings"

            for column in self.treeview_style["columns"]:
                self.treeview_style.heading(column, text=column)  # let the column heading = column name

            data_rows = self.data.to_numpy().tolist()  # turns the dataframe into a list of lists
            for row in data_rows:
                self.treeview_style.insert("", "end", values=row)

            self.state_for_menu = 'normal'

        except AttributeError:
            pass

    def remove_data(self):
        self.path_label["text"] = "No File Selected."
        self.path_label["bg"] = "red"
        self.treeview_style.delete(*self.treeview_style.get_children())
        for column in self.treeview_style["columns"]:
            self.treeview_style.heading(column, text="")
        self.data = None














