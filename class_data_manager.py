import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import messagebox, ttk
from pandas import *
import os
from Function_message_window import popup_window


# todo wywalić całego labelframa z ładowaniem danych do osobnej klasy dajesz 2 mastery i na dole czerwony pasek (data loaded)/(data unavalible)

class Data_manager:

    def __init__(self,master,frame_with_data,):
        self.treeview_style = ttk.Treeview(frame_with_data)
        self.treeview_style.place(relheight=1, relwidth=1)
        y_scrollbar = tk.Scrollbar(frame_with_data, orient="vertical", command=self.treeview_style.yview)
        x_scrollbar = tk.Scrollbar(frame_with_data, orient="horizontal", command=self.treeview_style.xview)
        self.treeview_style.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
        x_scrollbar.pack(side="bottom", fill="x")
        y_scrollbar.pack(side="right",fill="y")

        self.path_label = tk.Label(master, bg="red", text="No File Selected.")
        self.path_label.place(relx=0.005, rely=0.97, relwidth=0.99, relheight=0.02)

    def File_dialog(self):
        try:
             self.file_path = askopenfile(mode='r', title="Select A File",
                                          filetypes=[("Excel Files", "*.xlsx"), ("Excel Files", "*.xls"), ("CSV Files","*.csv"),])
             self.path_label["text"] = self.file_path.name
             self.path_label["bg"] = "light green"
             popup_window("Information","Data were imported.")
        except AttributeError:
            pass


    def remove_data(self):
        self.path_label["text"] = "No File Selected."
        self.path_label["bg"] = "red"
        self.treeview_style.delete(*self.treeview_style.get_children())
        for column in self.treeview_style["columns"]:
            self.treeview_style.heading(column, text="")
        self.data = None

    def Load_data(self):
        try:
            name, file_extention = os.path.splitext(self.file_path.name)
            try:
                if file_extention == '.csv':
                    temp_data = read_csv(self.file_path.name)
                elif file_extention == '.xlsx':
                    temp_data = read_excel(self.file_path.name)
                elif file_extention == '.xls':
                    temp_data = read_excel(self.file_path.name)
                self.data = temp_data
            except ValueError:
                tk.messagebox.showerror("Information", "The file_path you have chosen is invalid")
                return None
            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file_path as {self.file_path}")
                return None

            self.treeview_style["column"] = list(self.data.columns)
            self.treeview_style["show"] = "headings"

            for column in self.treeview_style["columns"]:
                self.treeview_style.heading(column, text=column)  # let the column heading = column name

            data_rows = self.data.to_numpy().tolist()  # turns the dataframe into a list of lists
            for row in data_rows:
                self.treeview_style.insert("", "end", values=row)
            self.file_path = ""
            self.state = "normal"

        except AttributeError:
            pass







