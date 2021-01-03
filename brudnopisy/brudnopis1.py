from tkinter.filedialog import askopenfile
from tkinter import messagebox, ttk, Label, Scrollbar
from pandas import read_csv, read_excel
import os
from function_popup_message import popup_window


class DataManager:

    def __init__(self, master, frame_with_data):
        self.data = None
        self.file_path = None

        self.tree_view_style = ttk.Treeview(frame_with_data)
        self.tree_view_style.place(relheight=1, relwidth=1)
        y_scrollbar = Scrollbar(frame_with_data, orient="vertical", command=self.tree_view_style.yview)
        x_scrollbar = Scrollbar(frame_with_data, orient="horizontal", command=self.tree_view_style.xview)
        self.tree_view_style.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
        x_scrollbar.pack(side="bottom", fill="x")
        y_scrollbar.pack(side="right", fill="y")

        self.path_label = Label(master, bg="red", text="No File Selected.")
        self.path_label.place(relx=0.005, rely=0.95, relwidth=0.99, relheight=0.04)

    def file_dialog(self):
        try:
            self.file_path = askopenfile(mode='r', title="Select A File",
                                         filetypes=[("Excel Files", "*.xlsx"),
                                                    ("Excel Files", "*.xls"),
                                                    ("CSV Files", "*.csv"), ])

            self.load_data(path=self.file_path.name)
            self.path_bar_color()
            popup_window("Information", "Data were imported.")
        except AttributeError:
            pass

    def path_bar_color(self):
        self.path_label["text"] = self.file_path.name
        self.path_label["bg"] = "light green"

    def load_data(self, path):
        try:
            name, file_extension = os.path.splitext(path)
            try:
                if file_extension == '.csv':
                    self.data = read_csv(path)
                elif file_extension == '.xlsx' or file_extension == '.xls':
                    self.data = read_excel(path)


            except ValueError:
                messagebox.showerror("Information", "The file_path you have chosen is invalid")
                return None
            except FileNotFoundError:
                messagebox.showerror("Information", f"No such file path as {path}")
                return None

            self.tree_view_style["column"] = list(self.data.columns)
            self.tree_view_style["show"] = "headings"

            for column in self.tree_view_style["columns"]:
                self.tree_view_style.heading(column, text=column)

            data_rows = self.data.to_numpy().tolist()
            for row in data_rows:
                self.tree_view_style.insert("", "end", values=row)

        except AttributeError:
            pass

    def remove_data(self):
        self.path_label["text"] = "No File Selected."
        self.path_label["bg"] = "red"
        self.tree_view_style.delete(*self.tree_view_style.get_children())
        for column in self.tree_view_style["columns"]:
            self.tree_view_style.heading(column, text="")
        self.data = None
