from tkinter.filedialog import askopenfile
from tkinter import ttk, Label, Scrollbar
from pandas import read_csv, read_excel
import os
from function_popup_message import popup_window


class DataManager:

    def __init__(self, master, frame_with_data):
        # creates tree view to show the data
        self.data = None
        self.tree_view_style = ttk.Treeview(frame_with_data)
        self.tree_view_style.place(relheight=1, relwidth=1)
        y_scrollbar = Scrollbar(frame_with_data, orient="vertical", command=self.tree_view_style.yview)
        x_scrollbar = Scrollbar(frame_with_data, orient="horizontal", command=self.tree_view_style.xview)
        self.tree_view_style.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
        x_scrollbar.pack(side="bottom", fill="x")
        y_scrollbar.pack(side="right", fill="y")

        # creates bar under data frame to show state of insert
        self.__path_label = Label(master, bg="red", text="No File Selected.")
        self.__path_label.place(relx=0.005, rely=0.95, relwidth=0.99, relheight=0.04)

    # opens file dialog window
    @staticmethod
    def __file_dialog():
        file_path = askopenfile(mode='r', title="Select A File",
                                     filetypes=[("Excel Files", "*.xlsx"),
                                                ("Excel Files", "*.xls"),
                                                ("CSV Files", "*.csv",)])
        return file_path

    # takes path and return his components
    @staticmethod
    def __get_path(path):
        try:
            name, file_extension = os.path.splitext(path.name)
        except AttributeError:
            return None
            pass
        else:
            return [path.name, file_extension]

    # reads data depending on its extension
    @staticmethod
    def __read_data(path_elements_list):
        data = None
        if path_elements_list[1] == '.csv':
            data = read_csv(path_elements_list[0])
        elif path_elements_list[1] == '.xlsx' or path_elements_list[1] == '.xls':
            data = read_excel(path_elements_list[0])
        else:
            popup_window("Error", "There is some unexpected error, please try another file.")
        return data

    # inserts data into the tree view
    @staticmethod
    def __insert_data_into_tree_view(data, tree_view):
        tree_view["column"] = list(data.columns)
        tree_view["show"] = "headings"

        for column in tree_view["columns"]:
            tree_view.heading(column, text=column)

        data_rows = data.to_numpy().tolist()
        for row in data_rows:
            tree_view.insert("", "end", values=row)

    # removes data from tree view
    @staticmethod
    def __remove_data_from_tree_view(tree_view):
        tree_view.delete(*tree_view.get_children())
        for column in tree_view["columns"]:
            tree_view.heading(column, text="")

    # manages the color of the status bar
    @staticmethod
    def __path_bar_color(label, text, status):

        if status == "On":
            label["text"] = text
            label["bg"] = "light green"

        elif status == "Off":
            label["text"] = text
            label["bg"] = "red"

    # loads the data with all other processes
    def load_data(self):
        path = self.__file_dialog()
        parts_of_path = self.__get_path(path)
        self.data = self.__read_data(parts_of_path)
        self.__insert_data_into_tree_view(self.data, self.tree_view_style)
        self.__path_bar_color(self.__path_label, text=parts_of_path[0], status="On")
        popup_window("Information", "Data were imported.")

    # removes data with all other processes
    def remove_data(self):
        self.__remove_data_from_tree_view(self.tree_view_style)
        self.__path_bar_color(self.__path_label, text="No File Selected.", status="Off")
        self.data = None
