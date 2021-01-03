from tkinter.filedialog import askopenfile
from tkinter import ttk, Label, Scrollbar
from pandas import read_csv, read_excel
import os
from function_popup_message import popup_window


class DataManager:

    def __init__(self, master, frame_with_data):
        self.data = None
        self.tree_view_style = ttk.Treeview(frame_with_data)
        self.tree_view_style.place(relheight=1, relwidth=1)
        y_scrollbar = Scrollbar(frame_with_data, orient="vertical", command=self.tree_view_style.yview)
        x_scrollbar = Scrollbar(frame_with_data, orient="horizontal", command=self.tree_view_style.xview)
        self.tree_view_style.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
        x_scrollbar.pack(side="bottom", fill="x")
        y_scrollbar.pack(side="right", fill="y")

        self.__path_label = Label(master, bg="red", text="No File Selected.")
        self.__path_label.place(relx=0.005, rely=0.95, relwidth=0.99, relheight=0.04)

    def __file_dialog(self):
        file_path = askopenfile(mode='r', title="Select A File",
                                     filetypes=[("Excel Files", "*.xlsx"),
                                                  ("Excel Files", "*.xls"),
                                                  ("CSV Files", "*.csv",)])
        return file_path

    def __get_path(self, path):
        try:
            name, file_extension = os.path.splitext(path.name)
        except AttributeError:
            return None
            pass
        else:
            return [path.name, file_extension]

    def __read_data(self, path_elements_list):
        data = None
        if path_elements_list[1] == '.csv':
            data = read_csv(path_elements_list[0])
        elif path_elements_list[1] == '.xlsx' or path_elements_list[1] == '.xls':
            data = read_excel(path_elements_list[0])
        else:
            popup_window("Error","There is some unexpected error, please try another file.")
        self.data = data
        return data

    def __insert_data_into_tree_view(self, data, tree_view):
        tree_view["column"] = list(data.columns)
        tree_view["show"] = "headings"

        for column in tree_view["columns"]:
            tree_view.heading(column, text=column)

        data_rows = data.to_numpy().tolist()
        for row in data_rows:
            tree_view.insert("", "end", values=row)

    def __remove_data_from_tree_view(self, tree_view):
        tree_view.delete(*tree_view.get_children())
        for column in tree_view["columns"]:
            tree_view.heading(column, text="")
        self.data = None

    def __path_bar_color_on(self, label, path_name):
        label["text"] = path_name
        label["bg"] = "light green"

    def __path_bar_color_off(self, label):
        label["text"] = "No File Selected."
        label["bg"] = "red"

    def load_data(self):
        path = self.__file_dialog()
        parts_of_path = self.__get_path(path)
        data = self.__read_data(parts_of_path)
        self.__insert_data_into_tree_view(data, self.tree_view_style)
        self.__path_bar_color_on(self.__path_label, parts_of_path[0])
        popup_window("Information", "Data were imported.")

    def remove_data(self):
        self.__remove_data_from_tree_view(self.tree_view_style)
        self.__path_bar_color_off(self.__path_label)
